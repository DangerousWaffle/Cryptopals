#!/usr/bin/python3
import base64

def convertHexToBytes(hexString):
	byteA = bytearray.fromhex(hexString)
	return byteA

def convertBytesToBase64(byteArray):
	return base64.b64encode(byteArray).decode("utf-8")
	

def convertHexToBase64(hexString):
	return convertBytesToBase64(convertHexToBytes(hexString))
