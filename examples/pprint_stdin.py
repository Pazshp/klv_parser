#!/usr/bin/env python3

import sys, klv_parser;
for packet in klv_parser.StreamParser(sys.stdin.buffer.read()): packet.structure()

# python -c "import sys; import klv_parser; for packet in klv_parser.StreamParser(sys.stdin.buffer.read()): packet.structure()"
