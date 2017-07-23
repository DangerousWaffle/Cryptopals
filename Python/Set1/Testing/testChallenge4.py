#!/usr/bin/python3
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Modules'))
import ConvertEncoding
import VigenereDecoder

def test4(testFilePath):

	with open(testFilePath) as f:
		highestScore = 0
		highestOrigString = ""
		highestDecodedString = ""
		lineNo = 0

		for line in f:
			print(str(lineNo) + ": " + line)
			testString = VigenereDecoder.decodeString(ConvertEncoding.convertHexToBytes(line)).decode("utf-8")
			stringScore = VigenereDecoder.scoreString(testString)
			if (stringScore > highestScore):
				highestScore = stringScore
				highestOrigString = line
				highestDecodedString = testString

	print(highestOrigString + " decodes to " + highestDecodedString)

if __name__ == "__main__":
	filePath = sys.argv[1]
	test4(filePath)