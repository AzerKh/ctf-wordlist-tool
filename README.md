# 👻 GhostList --- Wordlist Generator

GhostList is a customizable **password wordlist generator** designed for
**CTFs, labs, and authorized security testing**.\
It mutates seed words using **case variations, leetspeak, numbers,
years, and special characters** to expand the password search space.

> ⚠️ **For educational purposes, CTFs, and authorized testing only.**\
> Do **NOT** use this tool against systems you do not own or have
> explicit permission to test.

------------------------------------------------------------------------

## ✨ Features

-   🔡 Case variations (lower, upper, capitalized)
-   🔢 Numeric suffixes & prefixes
-   📅 Year mutations (1990--2030)
-   💀 Leetspeak substitutions (`a → @`, `e → 3`, `s → $`, etc.)
-   🔐 Special character injection
-   🔄 Word permutations (multi-word combos)
-   ⚡ Fast generation using Python sets
-   🎯 Designed for CTFs & pentesting wordlists

------------------------------------------------------------------------

## 📦 Requirements

-   Python **3.7+**
-   No external libraries required

------------------------------------------------------------------------

## 🚀 Usage

``` bash
python3 ghostlist.py -w admin root test
python3 ghostlist.py -f words.txt
python3 ghostlist.py -w admin user --min 1 --max 3
python3 ghostlist.py -w admin -o mywordlist.txt
```

------------------------------------------------------------------------

## ⚙️ Arguments

  Option           Description
  ---------------- ----------------------
  `-w, --words`    Seed words
  `-f, --file`     Load words from file
  `-o, --output`   Output file
  `--min`          Minimum combinations
  `--max`          Maximum combinations

------------------------------------------------------------------------

## 🛡️ Disclaimer

This tool is intended **only for CTFs, labs, and authorized penetration
testing**.

Unauthorized use is illegal.

------------------------------------------------------------------------

Happy hacking 👻
