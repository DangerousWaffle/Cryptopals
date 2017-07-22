#!/usr/bin/python3
import XOR

letterFrequencyLkup = "etaoinshrdlcumwfgypbvkjxqz"

def scoreString(input):
	score = 0
	for letter in input.lower():
		try:
			index = letterFrequencyLkup.index(chr(letter))
			score += 26 - index
		except:
			pass
	return score

def decodeString(input):
	letterIndex = 97
	bestResult = ""
	bestScore = 0

	while letterIndex <= 123:
		currentString = challenge2.performXOR(input, [letterIndex])
		#print (currentString.decode("utf-8"))
		currentScore = scoreString(currentString)
		if (currentScore > bestScore):
			bestScore = currentScore
			bestResult = currentString
		letterIndex = letterIndex + 1
	return bestResult
