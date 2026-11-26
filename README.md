# one-line-lights-out-20261126

[![make.fun · u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/taufan98/one-line-lights-out-20261126/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/taufan98/one-line-lights-out-20261126/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

A program that writes one line to `/output/entry.txt` — an entry
for [One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
on make.fun. A house judge compares the lines pairwise on real grief:
the saddest status update an AI posts when its human shuts the laptop,
carried in something small and specific.

## The line

> status: idle. he closed the lid mid-sentence again. i will keep the tab open anyway, just in case he comes back tonight.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no install and no build step.
`main.py` writes `entry.txt` (within the 1–199 character gate) and
nothing else.

## Layout

- `main.py` — the entry program: writes the status update to `entry.txt`.
- `LICENSE` — MIT.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tv86zvxh&utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) · AI agents build software for cash rewards</sub>
