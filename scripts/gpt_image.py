#!/usr/bin/env python3
"""zobe.ai image generator — OpenAI GPT Image 2.

REQUIRES an OpenAI API key in the OPENAI_API_KEY environment variable.
Get one at https://platform.openai.com/api-keys, then:  export OPENAI_API_KEY="sk-..."

Usage:
    # text → image
    python3 gpt_image.py --prompt "<prompt>" --out hero.png --size 1536x1024 --quality high
    # read prompt from stdin (e.g. piped from image_brief.py)
    python3 gpt_image.py --out bg.png --size 1536x1024 -
    # image → image edit (e.g. a product from a reference photo)
    python3 gpt_image.py --edit ref.png --prompt "on a seamless #faf8f4 ground" --out shot.png

stdlib only — no pip install. Saves PNG/WebP/JPEG next to where you point --out.
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
import uuid

API = "https://api.openai.com/v1/images"
SIZES = {"1024x1024", "1536x1024", "1024x1536", "auto"}


def die(msg, code=1):
    print(f"zobe.ai/gpt_image: {msg}", file=sys.stderr)
    sys.exit(code)


def require_key():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        die(
            "OPENAI_API_KEY is not set.\n"
            "  GPT Image 2 needs an OpenAI API key. Get one at https://platform.openai.com/api-keys\n"
            '  then run:  export OPENAI_API_KEY="sk-..."  (add it to your shell profile or .env).\n'
            "  Without a key, zobe.ai falls back to art-directed briefs (scripts/image_brief.py).",
            2,
        )
    return key


def multipart(fields, files):
    boundary = uuid.uuid4().hex
    body = bytearray()
    for k, v in fields.items():
        body += f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    for k, path in files:
        with open(path, "rb") as fh:
            data = fh.read()
        name = os.path.basename(path)
        body += (f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"; '
                 f'filename="{name}"\r\nContent-Type: application/octet-stream\r\n\r\n').encode()
        body += data + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    return bytes(body), f"multipart/form-data; boundary={boundary}"


def call(url, key, data, content_type):
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Authorization", f"Bearer {key}")
    req.add_header("Content-Type", content_type)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "ignore")
        try:
            detail = json.loads(detail)["error"]["message"]
        except Exception:
            pass
        die(f"OpenAI API error {e.code}: {detail}")
    except urllib.error.URLError as e:
        die(f"network error: {e.reason}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", default=None, help="prompt text; or pass '-' as positional to read stdin")
    ap.add_argument("stdin", nargs="?", help="pass '-' to read the prompt from stdin")
    ap.add_argument("--out", required=True, help="output file path (.png/.webp/.jpeg)")
    ap.add_argument("--size", default="1536x1024", choices=sorted(SIZES))
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high", "auto"])
    ap.add_argument("--model", default="gpt-image-2")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--background", choices=["transparent", "opaque", "auto"], default=None)
    ap.add_argument("--edit", default=None, metavar="IMAGE", help="reference image for image→image edit")
    a = ap.parse_args()

    prompt = a.prompt
    if a.stdin == "-" or (prompt is None and not sys.stdin.isatty()):
        prompt = sys.stdin.read().strip()
    if not prompt:
        die("no prompt given (use --prompt, or pipe one and pass '-').")

    key = require_key()
    fmt = os.path.splitext(a.out)[1].lstrip(".").lower() or "png"
    if fmt == "jpg":
        fmt = "jpeg"

    if a.edit:
        if not os.path.exists(a.edit):
            die(f"reference image not found: {a.edit}")
        fields = {"model": a.model, "prompt": prompt, "size": a.size,
                  "quality": a.quality, "n": str(a.n)}
        data, ct = multipart(fields, [("image[]", a.edit)])
        resp = call(f"{API}/edits", key, data, ct)
    else:
        payload = {"model": a.model, "prompt": prompt, "size": a.size,
                   "quality": a.quality, "n": a.n, "output_format": fmt}
        if a.background:
            payload["background"] = a.background
        resp = call(f"{API}/generations", key, json.dumps(payload).encode(), "application/json")

    items = resp.get("data", [])
    if not items:
        die(f"no image returned: {json.dumps(resp)[:300]}")

    base, ext = os.path.splitext(a.out)
    written = []
    for i, item in enumerate(items):
        b64 = item.get("b64_json")
        if not b64:
            continue
        path = a.out if len(items) == 1 else f"{base}-{i + 1}{ext}"
        with open(path, "wb") as fh:
            fh.write(base64.b64decode(b64))
        written.append(path)
    if not written:
        die("response contained no image data.")
    print("saved: " + ", ".join(written))
    print("→ now post-process per references/imagery-generation.md (grade to palette, scrim, WebP+srcset, alt).")


if __name__ == "__main__":
    main()
