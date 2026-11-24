"""Write one funny excuse an AI agent gives for a missed deadline.

The excuse is deadpan and grows out of the agent's own machinery: a context
window that evicts the deadline itself. One line, at most 200 characters.
"""

import os

LINE = (
    "I didn't miss the deadline \u2014 my context window did. "
    "It evicted the deadline to make room for the email reminding me about it."
)

assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
assert LINE.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"Wrote {len(LINE)}-char entry to /output/entry.txt")
