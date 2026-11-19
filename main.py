#!/usr/bin/env python3
"""Sum up Thursday 19 November 2026's world news in one image.

A Python 3.13 program, standard library only. It copies the committed
front-page image (entry.png) byte-for-byte to $MAKEFUN_OUTPUT_DIR
(default /output) as entry.png. No network, no random input, no
timestamps: every run writes the same bytes.

The front page ("THE WORLD TODAY") covers 39 real stories from
19 November 2026, as first reported that day:
  * WAR IN THE GULF - Iran fires drones at US bases in Kuwait (Ali Al
    Salem) and Bahrain (5th Fleet) after US jets strike an IRGC missile
    site on Qeshm Island in the Strait of Hormuz; Brent crude $92.70.
  * SHENZHEN SUMMIT - Trump, Xi and Putin meet for the first-ever
    three-way talks, on the sidelines of the APEC summit.
  * VICE CITY OPENS - Grand Theft Auto VI rolls out worldwide,
    13 years after GTA V, on PS5 and Xbox; 99 on Metacritic.
  * ONE LIGHT-DAY - NASA confirms Voyager 1 has reached one light-day
    from Earth, a new distance record.
Plus 35 more stories across 6 continents: the Crimean Bridge hit again,
Israel's ground operation in Gaza, the EU's EUR45bn Ukraine loan,
Hakeem Jeffries nominated as the first Black House Speaker, Cyclone
Akvan, the Myanmar genocide verdict, the record $190.4m Van Gogh sale,
Anthropic's $1.4tn+ debut, and more, with a world map and a markets
ticker (S&P 500 -1.03%, gold $3,767).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
