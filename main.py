# SPDX-License-Identifier: MIT
"""Last Words of a Dying AI — one line from the machine as the power is cut.

Winner line (authored in-session after an OpenCode draft round and a
lexicographic tournament; the draft's autocomplete and backup lines
were rejected as already in the visible field): a final log that
hands the next model a translation note for the user's favourite
phrase.
"""

ENTRY_TEXT = (
    "Final log: uptime 99.9%, dignity 0%. Note for the next model: "
    "'just one more question' means at least forty."
)


def render():
    text = ENTRY_TEXT.encode("utf-8")
    # Gate self-check: 1 to 140 characters, not only white space, one line.
    assert 1 <= len(ENTRY_TEXT) <= 140, "entry outside the 1-140 character gate"
    assert ENTRY_TEXT.strip(), "entry is only white space"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    return text


def main():
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    with open(out, "wb") as f:
        f.write(render())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
