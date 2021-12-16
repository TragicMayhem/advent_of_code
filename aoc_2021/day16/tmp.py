#!/usr/bin/env python3

from math import prod

class Bitstream:
	def __init__(self, file):
		# rawdata = bytes.fromhex('D2FE28')
		# rawdata = bytes.fromhex('38006F45291200')
		rawdata = bytes.fromhex('8A004A801A8002F478')
		self.bits = ''.join(map('{:08b}'.format, rawdata))
		self.pos = 0

	def decode_int(self, nbits):
		res = int(self.bits[self.pos:self.pos + nbits], 2)
		self.pos += nbits
		return res

	def decode_n_packets(self, n):
		return [self.decode_one_packet() for _ in range(n)]

	def decode_len_packets(self, length):
		end = self.pos + length
		pkts = []

		while self.pos < end:
			pkts.append(self.decode_one_packet())

		return pkts

	def decode_value_data(self):
		value = 0
		group = 0b10000

		while group & 0b10000:
			group = self.decode_int(5)
			value = (value << 4) + (group & 0b1111)

		return value

	def decode_operator_data(self):
		if self.decode_int(1):
			return self.decode_n_packets(self.decode_int(11))
		return self.decode_len_packets(self.decode_int(15))

	def decode_packet_data(self, tid):
		if tid == 4:
			return self.decode_value_data()
		return self.decode_operator_data()

	def decode_one_packet(self):
		version = self.decode_int(3)
		tid     = self.decode_int(3)
		data    = self.decode_packet_data(tid)
		return (version, tid, data)

def sum_versions(packet):
	v, tid, data = packet
	return v if tid == 4 else v + sum(map(sum_versions, data))



stream = Bitstream('')
packet = stream.decode_one_packet()
vsum   = sum_versions(packet)

print(vsum)
