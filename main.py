#!/usr/bin/env python3
"""Daily Commodity Analysis Report Generator.

Generates a Romanian-language report covering:
- XAU-USD (Gold)
- XAG-USD (Silver)
- Palladium
- Crude Oil (WTI)
- Natural Gas

Data sourced from Yahoo Finance. News from Google News RSS.
"""

import os
from datetime import datetime

from report.generator import generate_report


def main():
    print("=" * 50)
    print("  Generator Raport Zilnic Commodities")
    print("=" * 50)
    print()

    report = generate_report()

    # Write to output file
    os.makedirs("output", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    output_path = f"output/raport_{timestamp}.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nRaport generat cu succes: {output_path}")
    print()
    print(report)


if __name__ == "__main__":
    main()
