#This program uses dynamic programming to find whether a single string can be broken up 
#into english words

#Author: Mac Weinstock 

#USAGE: python3 dynProg.py < [FILENAME]

import sys

#Read in 10k word dictionary 
def readDict(file):
	tempDict = []	

	f = open(file, "r")

	for line in f:
		tempDict.append(line)

	f.close()

	return tempDict

#Store dictionary globally to improve performance (only need to read once)
dictList = readDict("dictionary_10k_sample/diction10k.txt")

#Search the dictionary for desired word
def dictSearch(w):
	for word in dictList:
		word = word.strip()
		if w == word:
			return True
	return False

#Iterative method to split each word provided
def split(string):
	n = len(string)
	splitAt = []
	splArr = []

	#Append the split word to stored array and the index of the split to another array
	for i in range(0,n):
		splArr.append(-1)
		splitAt.append(0)

	splArr.append(1)

	for i in range(n-1, -1, -1): 
		splArr[i] = 0
		
		for j in range(i, n):
			if (splArr[j+1] == 1) and (dictSearch(string[i:j+1]) == True):
				splArr[i] = 1
				splitAt[i] = j+1
				
	return splArr, splitAt

# def memo(i, phrase):
# 	n = len(phrase)
# 	splitAt = []
# 	splArr = []

# 	for i in range(0,n):
# 		splArr.append(-1)
# 		splitAt.append(0)

# 	splArr.append(1)

# 	if splArr[i] == 1:
# 		return True

# 	if splArr[i] == 0:
# 		return False

# 	if splArr[i] == -1:
# 		for j in range(i, n-1):
			
# 			if memo(j+1, phrase) and dictSearch(phrase[i:j+1]):
# 				splitArr[i] = 1
# 				splitAt[i] = j+1

# 	return splArr, splitAt
				

def main(file):
	strList = []

	fLen = file[0]

	#Parse the provided file
	for line in file[1:]:
		line = line.strip()
		strList.append(line)

	i = 1
	#Print the desired output of split array into single words
	for line in strList:
	
		l = len(line)

		print(f"Phrase {i}:\n{line}\n")

		print("Iterative attempt:")

		res, splitAt = split(line)

		if res[0] == 1:
			print("YES, can be split\n")
			print("===== words are below =====")
			for j in range(0, len(splitAt)):
				if splitAt[j] != 0:
					print(line[j:splitAt[j]])
			print("============================\n")

		else:
			print("NO, cannot be split\n")

		i += 1

	return 0

if __name__ == "__main__":
	main(sys.stdin.readlines())



