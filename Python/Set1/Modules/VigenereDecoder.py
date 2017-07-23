#!/usr/bin/python3
import XOR

freqLkupDict = {
	"a":8.167,
	"b":1.492,
	"c":2.782,
	"d":4.253,
	"e":12.702,
	"f":2.228,
	"g":2.015,
	"h":6.094,
	"i":6.966,
	"j":0.153,
	"k":0.772,
	"l":4.025,
	"m":2.406,
	"n":6.749,
	"o":7.507,
	"p":1.929,
	"q":0.095,
	"r":5.987,
	"s":6.327,
	"t":9.056,
	"u":2.758,
	"v":0.978,
	"w":2.360,
	"x":0.150,
	"y":1.974,
	"z":0.074
}

def scoreString(input):
	letterIndex = 97
	score = 0
	stringLen = len(input)

	while letterIndex < 123:
		percent = input.count(letterIndex) * 100 / stringLen
		score = score + abs(percent - freqLkupDict[chr(letterIndex)]) 
		letterIndex = letterIndex + 1

	return score

def decodeString(input):
	letterIndex = 97
	bestResult = ""
	bestScore = 0

	while letterIndex <= 123:
		currentString = XOR.performXOR(input, [letterIndex])
		currentScore = scoreString(currentString)
		print(currentString)
		print(currentScore)
		if (currentScore > bestScore):
			bestScore = currentScore
			bestResult = currentString
		letterIndex = letterIndex + 1
	return bestResult
