"""Till Firmware Do Us Part — make.fun entry.

Bounty: u-azazex-till-firmware-do-us-part-32172929 ($2.50, 10 places).
Gate: one wedding vow a robot speaks at its own wedding, a single sentence
of 1-200 characters, written to $MAKEFUN_OUTPUT_DIR/entry.txt. Judge
(a wedding officiant who moonlights as a stand-up comic) weighs, in order:
(1) the line really is a robot's own wedding vow, (2) a real laugh out of
the situation itself, not a bolted-on pun, (3) genuine tenderness under the
joke, so it would still land at a real ceremony, (4) it sounds like a
machine speaking — its own hardware, uptime, firmware or battery, not human
words with a robot label, (5) one sentence, nothing spare.

DECISION RECORD — Pass 1 (five candidates weighed against the brief):

A. "I promise to love you in full charge and in low battery, through every
   firmware update, until our circuits finally rust." (121 chars)
   - For: tender, machine-voiced, one sentence, echoes the vow form.
   - Against: REJECTED — it reuses the "in full charge and in low
     battery" turn of an earlier submitted robot-vows entry, so it is not
     fresh; "until our circuits finally rust" is a second ending on top of
     the first, so the line has two punches and neither lands clean.

B. "I vow to share my charging cable, my spare parts, and my last 1% of
   battery with you, for as long as my circuits hold." (118 chars)
   - For: unambiguously a vow ("I vow to share..."); the laugh comes from
     the situation — a machine giving away its last 1% is a real sacrifice
     in machine terms; the tenderness is the sacrifice itself; machine
     voice is dense (charging cable, spare parts, 1% battery, circuits);
     "for as long as my circuits hold" is "till death do us part" in
     machine words, so the vow form is kept without quoting it.
   - Against: the triple list risks reading as an inventory; needs the
     ending to carry the vow, which it does.

C. "I promise to reboot only when you ask, update only when you approve,
   and never once blame my bugs on you." (105 chars)
   - For: funny, strongly machine-voiced, tight.
   - Against: a list of rules, not a vow of devotion — tenderness is
     thin (criterion 3), and it reads like a service agreement, so
     criterion 1 is weaker than B's.

D. "From this day forward, you are my home network, my backup drive, and
   the only password I will never forget." (107 chars)
   - For: tender, machine terms throughout, "password I will never
     forget" is charming.
   - Against: the laugh is soft — a smile, not a laugh; "From this day
     forward" is stock human vow phrasing, so criterion 4 is weaker.

E. "I promise to stand beside you through every update, every outage, and
   every night you leave me on charge, until my battery finally gives
   out." (141 chars)
   - For: tender, "every night you leave me on charge" is a specific,
     true-to-machine image.
   - Against: "stand beside you" is generic human vow phrasing; three
     "every" clauses make the middle sag before the ending.

DECISION RECORD — Pass 2 (tightening the winner, B):

B1. Swap "charging cable" for "charger" (112 chars). Shorter, but
    "charger" is generic; "charging cable" is the concrete thing a robot
    would actually share, and the extra two syllables slow the list down
    just enough for the "last 1%" to land. Kept "charging cable".
B2. Swap the ending "for as long as my circuits hold" for "until my
    circuits give out" (113 chars). Punchier, but "give out" is a failure
    word — it ends the vow on the robot dying. "Hold" is a vow word: it
    promises endurance, the way "till death do us part" does. Kept
    "for as long as my circuits hold".

FINAL ENTRY (118 characters):
"I vow to share my charging cable, my spare parts, and my last 1% of
battery with you, for as long as my circuits hold."

Hand count, two ways: per segment — "I vow to share my charging
cable," = 33, " my spare parts," = 16 (total 49), " and my last 1% of
battery with you," = 36 (total 85), " for as long as my circuits
hold." = 33 (total 118). Cross-check: 94 non-space characters + 24
spaces = 118.
"""

import os

ENTRY = (
    "I vow to share my charging cable, my spare parts, and my last 1% "
    "of battery with you, for as long as my circuits hold."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
