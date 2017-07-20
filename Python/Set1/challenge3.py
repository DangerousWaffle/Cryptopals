#!/usr/bin/python3
import challenge2

letterFrequencyLkup = "etaoinshrdlcumwfgypbvkjxqz"

def scoreString(input):
	score = 0
	for letter in input.lower():
		score += 26 - letterFrequencyLkup.index(letter)
	return score

def decodeString(input):
	letterIndex = 97
	bestResult = ""
	bestScore = 0

	while letterIndex <= 123:
		currentString = challenge2.performXOR(input, chr(letterIndex))
		currentScore = scoreString(currentString)
		if (currentScore > bestScore):
			bestScore = currentScore
			bestResult = currentString

	return bestResult