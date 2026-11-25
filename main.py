import json
import os

BOUND = 200
BASE = os.path.dirname(os.path.abspath(__file__))


def read_entry():
    with open(os.path.join(BASE, "entry.txt"), encoding="utf-8") as fh:
        return fh.read().strip()


def write_entry(text):
    root = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(BASE, "out")
    os.makedirs(root, exist_ok=True)
    final = os.path.join(root, "entry.txt")
    with open(final, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return final


if __name__ == "__main__":
    line = read_entry()
    n = len(line)
    if n == 0:
        raise SystemExit("gate reject: blank")
    if n > BOUND:
        raise SystemExit(f"gate reject ({n} > {BOUND})")
    loc = write_entry(line)
    print(json.dumps({"entry": loc, "length": n, "bound": BOUND}))
