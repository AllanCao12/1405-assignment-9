#Allan Cao's Assignment 9 submission
#student number is 101218998 
#Submitted to Professor Collier on 2021-11-21

import sys

ACRONYMS = [
	('BY THE WAY', "BTW"),
	('AS FAR AS I KNOW', "AFAIK"),
	('FOR YOUR INFORMATION', "FYI"),
	('BECAUSE', "B/C"),
	('OH MY GOD', "OMG"),
	('I DONT KNOW', "IDK"),
	('IN MY OPINION', "IMO"),
	('THANKS', "THX"),
	('SEE YOU', "CU"),
	('TO BE HONEST', "TBH"),
]

HOMOGLYPHS = [
	('A', '/-\\'),
	('B', '|3'),
	('H', '|-|'),
	('L', '|_'),
	('M', '|v|'),
	('N', '|\|'),
	('S', '$'),
	('U', '|_|'),
	('V', '\\/'),
	('W', '\\/\\/'),
	('X', '><'),
	('Z', '-/_'),
]

def removePunctuation(s):#Removes punctuation
	result = ''
	for ch in s:
		# treat all char other than alphabet letters, number and space as punctuations.
		if ch.isalnum() or ch.isspace(): 
			result += ch
	return result

def toUpper(s): #Makes the msg upper case
	result = ''
	for ch in s:
		if ch >= 'a' and ch <= 'z': #or ch.islower()
			ch = chr( ord('A') + ord(ch) -ord('a') )  #or ch.upper()
		result += ch
	return result

def doAcronyms(s): #Checking if need to make any part of the msg an acronym
	result = ''
	i, n = 0, len(s)
	while i < n:
		found = False
		if not s[i].isspace() and (i==0 or s[i-1].isspace()): #If the letter we are on is not a space and the character preceeding this one is a space or it's the first letter
			#start to check acronym when it's a word start.
			for v in ACRONYMS:
				acronFrom, acronTo = v
				endpos = i + len(acronFrom)
				if endpos>n or (endpos<n and not s[endpos].isspace()):#This acronym is too long, or if the character at the endpos is not a space, we skip it. (Endpos is 1 greater than the ending position since lists begin at 0)
					continue

				if s[i:endpos] == acronFrom: #compare str with acronFrom
					#found a match, append acronTo, advance index to end of this acronym.
					found = True
					result += acronTo
					i += len(acronFrom)
					break

		if not found:
			#append the char to result and increase i 
			result += s[i]
			i += 1

	return result

def doHomoglyphs(s):
	result = ''
	for ch in s:
		for v in HOMOGLYPHS:
			if v[0] == ch: #if the first part of v is the char, then v[1], its homoglyph, is equal to ch
				ch = v[1]
				break
		result += ch
	return result
#Main function
def main():
	while True:
		s = input("Enter a line to decode, or blank line to quit: ")
		if not s:
			break
		s = removePunctuation(s)
		s = toUpper(s)
		s = doAcronyms(s)
		s = doHomoglyphs(s)
		print("Encoded:", s)
	print("Bye.")

main()
