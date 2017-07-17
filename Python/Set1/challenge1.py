#!/usr/bin/python3
import base64

def convertHexToBytes(hexString):
	byteA = bytearray.fromhex(hexString)
	return byteA

def convertBytesToHex(byteArray):
	#Starting with the empty string, add each element in the byteArray
	#02x pads the string when needed
	return ''.join(format(x, '02x') for x in byteArray)

def convertBytesToBase64(byteArray):
	return base64.b64encode(byteArray).decode("utf-8")
	
def convertBase64ToBytes(b64String):
	return base64.b64decode(b64String)

def convertHexToBase64(hexString):
	return convertBytesToBase64(convertHexToBytes(hexString))

def convertBase64ToHex(b64String):
	return convertBytesToHex(convertBase64ToBytes(b64String))
