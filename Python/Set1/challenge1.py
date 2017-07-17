#!/usr/bin/python3
import base64

def convertHexToBase64(hexString):
	#Convert to byte array
	byteA = bytearray.fromhex(hexString)
	return base64.b64encode(byteA).decode("utf-8")

