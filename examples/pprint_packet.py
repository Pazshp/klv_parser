#!/usr/bin/env python3

import klv_parser

if __name__ == "__main__":
	with open('./data/DynamicConstantMISMMSPacketData.bin', 'rb') as f:
		for packet in klv_parser.StreamParser(f):
			packet.structure()
