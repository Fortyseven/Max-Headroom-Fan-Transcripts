#!/usr/bin/env python3
'''
Takes a standard .srt subtitle file and dumps to stdout
a ready-to-format Fountain script with all the dialogue.

The resulting file will take significant modification to
resemble a real script.

Currently every line of dialog ON SCREEN is separated into
a distinct character "LINE". Often a full set of dialogue
will be spread across several lines.

e.g.
    LINE
    I feel

    LINE
    fine, Jim.

Don't forget, not all subtitles are accurate. And often
they will be abbreviated compared to the actual dialog,
so you'll have to run through and verify.

Or do whatever your workflow is. I'm not your mother.
'''


import os
import argparse
import srt

parser = argparse.ArgumentParser()
parser.add_argument(dest="input_srt", nargs=1,
                    help="Source srt subtitle file")

args = parser.parse_args()

args.input_srt = args.input_srt[0]

if not os.path.exists(args.input_srt):
    raise FileNotFoundError(f"Could not open source file: `{args.input_srt}`")
    exit(-1)

srt_contents = ""
with open(args.input_srt) as srt_data:
    srt_contents = srt_data.read()

for sub in srt.parse(srt_contents):
    print(f"LINE\n{sub.content}\n")
