# Dynamic_Programming

We want to devise a dynamic programming algorithm for the following problem:

There is a string of characters which might have been a sequence of words with all the spaces removed, and we want to find a way, if any, in which to insert spaces that separate valid English words. For example, theyouthevent could be from “the you the vent”, “the youth event” or “they out he vent”. If the input is theeaglehaslande, then there’s no such way. Your task is to implement a dynamic programming solution in the following ways:

• iterative bottom-up version

• recursive memoized version

Assume that the original sequence of words had no other punctuation (such as periods), no capital letters, and no proper nameThe program will read a text file from standard input. The name of the dictionary file should be hardwired in the code. We will be testing your program on a file named “diction10k.txt”, and your program will be tested in a directory containing that file.

SAMPLE INPUT:

The first line of input is an integer C. This is followed by C lines, each containing a single string, representing a phrase to be tested.

3

theyouthevent

theeaglehaslande

lukelucklikeslakeslukeducklikeslakeslukelucklickslakesluckducklickslakes

SAMPLE OUTPUT:

phrase number: 1

theyouthevent

iterative attempt: YES, can be split

the you the vent

memoized attempt: YES, can be split

the you the vent

phrase number: 2

theeaglehaslande

iterative attempt: NO, cannot be split

memoized attempt: NO, cannot be split

phrase number: 3

lukelucklikeslakeslukeducklikeslakeslukelucklickslakesluckducklickslakes

iterative attempt: YES, can be split

luke luck likes lakes luke duck likes lakes luke luck licks lakes luck duck licks lakes

memoized attempt: YES, can be split

luke luck likes lakes luke duck likes lakes luke luck licks lakes luck duck licks lakes
