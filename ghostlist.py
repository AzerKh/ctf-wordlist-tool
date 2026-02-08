import argparse
import itertools
import sys
import time

BANNER = r"""
   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗██╗     ██╗███████╗████████╗
  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██║     ██║██╔════╝╚══██╔══╝
  ██║  ███╗███████║██║   ██║███████╗   ██║   ██║     ██║███████╗   ██║   
  ██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██║     ██║╚════██║   ██║   
  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ███████╗██║███████║   ██║   
   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝╚══════╝   ╚═╝   

            [ G H O S T L I S T ] — Wordlist Generator
              >> CTF & Authorized Testing Only <<
"""



LEET_MAP = {
    "a": ["a", "@"],
    "e": ["e", "3"],
    "i": ["i", "1"],
    "o": ["o", "0"],
    "s": ["s", "$"],
    "t": ["t", "7"],
}

SPECIALS = ["", "!", "@", "#", "$", "_"]
NUMBERS = ["", "1", "12", "123"]
YEARS = [str(y) for y in range(1990, 2031)]


def slow_print(msg, delay=0.02):
    for c in msg:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def leetspeak(word):
    combos = [""]
    for c in word.lower():
        new = []
        for base in combos:
            if c in LEET_MAP:
                for r in LEET_MAP[c]:
                    new.append(base + r)
            else:
                new.append(base + c)
        combos = new
    return combos


def case_variations(word):
    return {
        word,
        word.lower(),
        word.upper(),
        word.capitalize(),
    }


def load_words(path):
    with open(path) as f:
        return [w.strip() for w in f if w.strip()]


def main():
    print(BANNER)

    parser = argparse.ArgumentParser(description="ShadowCrack – Offensive Wordlist Generator")
    parser.add_argument("-w", "--words", nargs="+", help="Seed words")
    parser.add_argument("-f", "--file", help="Load seed words from file")
    parser.add_argument("-o", "--output", default="passwords.txt", help="Output file")
    parser.add_argument("--min", type=int, default=1, help="Min word combo")
    parser.add_argument("--max", type=int, default=2, help="Max word combo")

    args = parser.parse_args()

    base_words = []

    if args.words:
        base_words.extend(args.words)

    if args.file:
        base_words.extend(load_words(args.file))

    if not base_words:
        slow_print("[!] No payload seeds supplied. Abort.")
        return

    slow_print(f"[+] {len(base_words)} seed words loaded...")
    slow_print("[*] Launching mutation engine...")
    time.sleep(1)

    results = set()

    for r in range(args.min, args.max + 1):
        for combo in itertools.permutations(base_words, r):
            joined = "".join(combo)

            for c in case_variations(joined):
                for l in leetspeak(c):
                    results.add(l)

                    for n in NUMBERS + YEARS:
                        results.add(l + n)
                        results.add(n + l)

                    for s in SPECIALS:
                        results.add(l + s)
                        results.add(s + l)

    slow_print("[*] Encryption layers bypassed...")
    slow_print("[*] Password space expanded...")
    time.sleep(0.8)

    with open(args.output, "w") as f:
        for p in sorted(results):
            f.write(p + "\n")

    slow_print(f"[✔] Operation complete.")
    slow_print(f"[✔] {len(results)} candidate passwords dumped into → {args.output}")
    slow_print("[☠] Happy hunting, operative.\n")


if __name__ == "__main__":
    main()