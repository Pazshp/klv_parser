#!/usr/bin/env python3

import klv_parser
import pprint

if __name__ == "__main__":
	with open('./data/DynamicConstantMISMMSPacketData.bin', 'rb') as f:
		for packet in klv_parser.StreamParser(f):
			metadata=packet.MetadataList()
			pprint.pprint(metadata)
			break #Print only first packet
