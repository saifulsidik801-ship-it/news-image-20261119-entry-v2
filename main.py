#!/usr/bin/env python3
"""Sum up Thursday 19 November 2026's world news in one image.

A Python 3.13 program, standard library only. It copies the committed
front-page image (entry.png) byte-for-byte to $MAKEFUN_OUTPUT_DIR
(default /output) as entry.png. No network, no random input, no
timestamps: every run writes the same bytes.

The front page ("THE WORLD IN ONE PICTURE") covers 36 real stories from
19 November 2026, as first reported that day:
  * Three illustrated leads: the Trump-Xi-Putin trilateral in Shenzhen,
    the UN court's genocide verdict for Myanmar's Rohingya, and the
    worldwide GTA VI rollout (Vice City opens).
  * Twelve illustrated cards: Iran's drones hit US bases in Kuwait and
    Bahrain, Cyclone Akvan, Voyager 1's one-light-day record, Hakeem
    Jeffries nominated as the first Black House Speaker, Pew's Islam-2035
    projection, Nvidia's $115.8bn quarter, the EU's EUR45bn Ukraine loan,
    Australia's settler sanctions, Peltola's Alaska win (56-44), the Fed
    minutes, Duckett's 133, and Modi with the Prince and Princess of Wales.
  * A "WHERE IT HAPPENED" world map with 15 numbered pins, an "ALSO ON
    THURSDAY 19 NOVEMBER" list (stories 16-36), a "THE DAY IN UTC"
    timeline, and a "DATE CHECK" box for stories that broke before today.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
