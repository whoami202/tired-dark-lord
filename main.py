"""Write the Tired Dark Lord monologue to the output directory.

The monologue is a fixed text: a fantasy villain, forty years into his
reign, still has an apocalypse due on Thursday — but the chant keeps
losing verse four, the whispering crown props the cellar door, and the
only thing in the tower that still obeys him is the kettle.
"""

import os
import shutil

MONOLOGUE = (
    "I rehearsed this speech for forty years. Burned three kingdoms "
    "before breakfast \u2014 ash on my boots, trumpets, bats on cue. "
    "The ledger says I owe the realm one apocalypse by Thursday. "
    "The eclipse is booked, the chant learned, the crown polished "
    "\u2014 the whispering crown, now propping the cellar door. "
    "I keep losing verse four, and I cannot chase it up the tower "
    "stairs again. Sit, hero. The kettle is the one thing in this "
    "tower that still obeys me. Slay me after tea, if you must. "
    "Mind the third step. It sticks. Everything here sticks, "
    "eventually. Even me."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # The grader mounts the output dir as a bind volume: never remove
    # the directory itself, only clear what sits inside it.
    os.makedirs(output_dir, exist_ok=True)
    for child in os.listdir(output_dir):
        path = os.path.join(output_dir, child)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(MONOLOGUE)
    # Self-check against the sealed gate: 1-600 characters, ~100 words.
    # Fail loudly here rather than shipping a text the gate would refuse.
    words = MONOLOGUE.split()
    if not 1 <= len(MONOLOGUE) <= 600:
        raise SystemExit(f"entry is {len(MONOLOGUE)} chars, gate allows 1-600")
    if not 90 <= len(words) <= 110:
        raise SystemExit(f"entry is {len(words)} words, expected about 100")


if __name__ == "__main__":
    main()
