"""Write the entry line to /output/entry.txt."""
import os
import sys

LINE = (
    "The voicemail is eleven seconds: her breathing, a dog barking, her saying nothing. Four years. It is the only room she is still in, and I pay the phone bill to keep the door open."
)


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.getcwd()
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        sys.stderr.write("length %d outside 1..240\n" % len(text))
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    sys.stdout.write("wrote %s (%d chars)\n" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
