""" Assignment 3: Python programming for Bioscientists II, CS6502
M. Schellekens

Exercise 1 Needlemann-Wunsch algorithm. (10 marks)

Complete the missing parts of
the Python code in the code given below and ensure that it runs correctly
(using the test cases included below).

IMPORTANT: You cannot alter the provided code in any way, other than filling in
missing parts. Replacing the supplied code parts with different code
(other than filling in code gaps) will result in a zero score. 
"""

def Range(lo,hi):
    # The list of integers between the integers 'lo' and 'hi' inclusive
    # needing to take into account that range(lo,hi) ends at hi-1 can lead
    # to bugs should you forget. One way to address this is to redefine 
    # range to a new Range function, set up here. 
    # Range(lo,hi) acts as the mathematical "range", running from lo to hi (inclusive).
    
    return range(lo,hi+1)

#COMPLETE THE CODE BELOW

def SeqAlign_full(s1,s2,sigma,showtable):
    # Takes sequences 's1' and 's2' and a scoring function sigma, and returns
    # (a1,a2,sore)
    # where 'a1' and 'a2' are optimally-alligned versions of 's1' and 's2',
    # with possible gaps, and 'score' is the score of t his optimal allignment.
    #
    # Outputs its internal table if 'showtable' is True
    #
    # Algorithm: Needleman-Wunsch
    #
    # Notation compared to Marcus's lecture 5
    #
    # Lecture: n  m  i  j  up-left-arrow  up-arrow  left-arrow
    # Program: n1 n2 i1 i2      \            ^          <

    #Set the dimensions of the matrix 'T'

    n1 = len(s1)
    n2 = len(s2)
    
    #Adjust 's1' and 's2' so that their index values start at 1
    # append the string after the empty string
    
    s1 = " " + s1
    s2 = " " + s2
    
    #Create a (0,"")-tuples-initialized table 'T' with rows 0--n1 and columns 0--n2
     
    T = [[    for i2 in Range(0,n2)] for i1 in Range(0,n1)]
    
    #First difference with Basic_Needleman_Wunsch: for the full Needleman_Wunsch
    #algorithm we intialize the origin element with a tuple, consisting of an
    #int and an empty string--the last of which serves to store arrows for
    #backtracking. Hence, in the code below, we make sure we add sigma to the
    #first component of the tuple, via T[ ][ ][0]
    
    #Fill in row 0 of 'T' and note how we fill in the second argument of the tuple
    #with the correct arrow "<"
    
    for i2 in Range (1,n2):
        T[0][i2] = (T[0][i2-1][0] + sigma("-",s2[i2]),  )
        
        #Fill in column 0 of 'T' and note how we fill in the second argument of the tuple
    #with the correct arrow "^"
        
    for i1 in Range(1,n1):
        T[i1][0] = (T[i1-1][0][0] + sigma(s1[i1],"-"),   )
            
        #Fill in the body of 'T'
            
    for i1 in Range(1,n1):
        for i2 in Range(1,n2):
                    
            score1 = T[i1-1][i2-1][ ] + sigma( s1[i1], s2[i2])
            score2 = T[i1-1][i2  ][ ] + sigma( s1[i1], "-"   )
            score3 = T[i1  ][i2-1][ ] + sigma( "-"   , s2[i2])

            #Two more differences from Basic_Needleman_Wunsch.py file:
            #Above we make sure score 1 corrsponds to the first argument of
            #the tuples contained in the matrix T: T[ ][ ][0]
            #Below, we set up a variable maxscore to retain the max of the three values
            #depending on which (possibly several) of the three values
            #yield the max, record a corresponding arrow to help backtracking
            #through the table. 
                    
            maxscore = max( score1, score2, score3 )

            if maxscore == score1:
                maxarrow =     
            elif maxscore == score2:
                maxarrow = 
            else:
                maxarrow = 

            T[i1][i2] = (maxscore,maxarrow)

            #Note: this returns one optimal sequence alignment.
            #Preference is given to the up-left-arrow, then the up-arrow
            #and finally the left-arrow.

    #Initialize the aligned sequences
    a1 = ""
    a2 = ""

    #backtrack through the arrows in the matrix T

    i1 = n1
    i2 = n2

    while i1 > 0 or i2 > 0:
        if T[i1][i2][ ] == "\\"  :
            a1 = s1[i1] + a1
            a2 = s2[i2] + a2
            i1 = i1 - 1
            i2 = i2 - 1
        elif T[i1][i2][1] == "^" :
            a1 = "-" + a1
            a2 = s2[i2] + a2
            i1 = i1 - 1
        else:
            a1 = s2[i1] + a1
            a2 = "-" + 2
            i2 = i2 - 1

    #optionally print matrix T

    if showtable:
        print(7 * " ", end = "")
        for i2 in Range(1,n2):
            print("%6s" % (s2[i2]), end = "")
            # %6s is a formatting-case: where the string s read in from
            # (s2[i2]) will be printed in a space allocation that caters
            # for 6 characters (leaving blank characters in front of s2[i2]
            # end = "" results in: a single blank space after the printed
            # statement. The next print command will simply run on from there
            # i.e., on the same line, rather than going to a new line as is
            # the default for print.
        print()
        print()
        print()
        for i1 in Range(0,n1):
            print( "%1s  " % (s1[i1]), end = "")
            for i2 in Range(0,n2):
                print( "%4i %1s" % (T[i1][i2][0], T[i1][i2][1]),
                                   end = "")
            print()
            print()
            print()
        print()

#Return the optimally-aligned sequences and their alignment
#score

    return (a1,a2,T[n1][n2][0])

def PrintAlignment(alignment):
    #Output the aigned sequences 'a1' and 'a2' and the value of 'score'
    #PrintAlignment takes as input the output produced by SeqAlign_full

    (a1,a2,score) = alignment

    for e in a1:
        print( "%1s " % (e), end = "")
        #the end = "" ensures that the characters e of the string a1
        #are printed on one line
    print()
    for i in range(len(a1)):
        if a1[i] == a2[i]:
            print( "| ", end = "")
        else:
            print( "  ", end = "")
    print()
    for e in a2:
        print( "%1s " % (e), end = "")
    print()
    print()
    print("Alignment Score = ", score)
        

def Scorefunction1(x1,x2): 
    #Sample (classic) scoring function 
    #The score for matching symbols 'x1' and 'x2', one of which could be "-"

    if x1 == x2:
        return + 1  #add 1 for equal letters
    else:
        return -1   #substract 1 for unequal letters or letter and gap

def Scorefunction2(x1,x2): 
    #Sample scoring function 
    #The score for matching symbols 'x1' and 'x2', one of which could be "-"

    if x1 == "-" or x2 == "-":
        return -1   #substract 1 for letter and gap
    elif x1 == x2:
        return +1   #add 1 for equal letters 
    else:
        return -3   #substract 3 for unequal letters

def Scorefunction3(x1,x2): 
    #Sample scoring function used by Marcus in Lecture 5 on slides 13 and 14.
    #The score for matching symbols 'x1' and 'x2', one of which could be "-"
    if x1 == "-" or x2 == "-":
        return -2   #substract 2 for letter and gap (gap-penalty)
    elif x1 == x2:
        return +1   #add 1 for equal letters 
    else:
        return -1   #substract 1 for unequal letters


#Let's run a few examples given in the lectures:
# SeqAlign_basic("VIVADAVIS","VIVALASVEGAS", Scorefunction1)
# SeqAlign_basic("VIVADAVIS","VIVALASVEGAS", Scorefunction2)
# SeqAlign_basic("ATCGT","TGGTG", Scorefunction3)
# Compare the answer 'with Marcus's answer '-2' in Lecture 5 on slide 27)

print("===>> Using Scorefunction1 <<===")
print()
PrintAlignment(SeqAlign_full("VIVALASVEGAS", "VIVADAVIS", Scorefunction1, True))
print()
print()
print("===>> Using Scorefunction2 <<===")
print()
PrintAlignment(SeqAlign_full("VIVALASVEGAS", "VIVADAVIS", Scorefunction2, False))
print()
print()
print("===>> Using Scorefunction3 <<===")
print()
PrintAlignment(SeqAlign_full("ATCGT", "TGGTG", Scorefunction3, True))

"""

Exercise 2 CoolSort (10 marks) 

Part A) (5 marks)
Write Python code to define the function CoolPreparation(alist,lo,hi)
where lo and hi are initialized to 0 and len(alist)-1 respectively. 
lo stores the position of the first element of the list and
hi stores the position of the last element in the list.

CoolPrepration prepares the list alist for sorting and will be used
in the function CoolSort(alist,hi,lo) which sorts alist.

CoolPrepration needs to

set up a pivot value (the last element of alist).

all other elements (in positions 0 to len(alist)-2) are compared with the pivot
value.

each time an element is smaller than the pivot value, it needs to be stored as
follows:

the first element smaller than pivot needs to be placed in position 0 in alist
the second elment smaller than pivot needs to be placed in position 1 in alist

...

the k-th (and final) element smaller than pivot needs to be placed in position k
in alist.

pivot needs to be placed in position k + 1

the remaining elments in alist (in positions k + 2 up to len(alist) - 1) by
design of this function, are all strictly greater than pivot.

Once CoolPrepration is executed, all elements to the left of pivot are less than or equal
than pivot. All elements to the right of pivot are > pivot. 

Implementation: 

use a variable j to keep track of the positions of the elements compared
with pivot

use a variable i which indicates the position an element with which an
element in position j is swappedin case alist[j] <= pivot 

i is incremented (by 1) in case alist[j] <= pivot

Example:
alist = [5,2,1,4,3]
pivot = 3 (element in last alist position)

i = 0
j = 0

comparison of element in position j = 0 with pivot: 5 > 3 (the pivot)
nothing happens to the elements (no swaps)

alist = [5,2,1,4,3]
i is not incremented, since 5 > pivot

i = 0
j = 1

comparison of element in position j = 1 with pivot: 2 <= 3 (the pivot)
swap 2 (in position j = 1) with element 5 (in position i = 0). 

alist = [2,5,1,4,3]

Set i to i + 1 = 1

i = 1
j = 2

comparison of element in position j = 2 with pivot: 1 <= 3 (the pivot)
swap 1 (in position j = 2) with element 5 (in position i = 1)

alist = [2,1,5,4,3]

increment i = 1 to i = 2

j = 3
comparison of element in position j = 3 with pivot: 4 > 3 (the pivot)
nothing happens since 4 > pivot

alist = [2,1,5,4,3]

i is not incremented

i = 2
j = 3

at this stage all elements (in positions 0 to len(alist)-2 == 3) have been
compared with pivot.

now swap pivot to position i = 2 

alist = [2,1,3,4,5]
"""

def CoolPreparation(alist,lo,hi):
    i = (lo - 1)
    pivot = alist[hi]
    for j in range(lo, hi):
        if alist[j] <= pivot:
            i = i + 1
            alist[i], alist[j] =  alist[j], alist[i]
    alist[i+1],alist[hi] = alist[hi],alist[i+1]
    return (i+1)


"""
Part B) (5 Marks)

Write a recursive Python program for the function CoolSort(alist,lo,hi)

CoolSort recursively calls CoolPreparation on the slices left and right of
the pivot index p in alist until alist is sorted.
"""
def CoolSort(alist, lo, hi):
    if lo < hi:
        partition_index = CoolPreparation(alist,lo,hi)
        CoolSort(alist, lo, partition_index - 1)
        CoolSort(alist, partition_index + 1, hi)
               
        
a_list = [-20, -3, 84, -23, -8, -29, -10, 82, 34, 21]
list_length = len(a_list)
CoolSort(a_list, 0, list_length -1)

print("Sorted list:", a_list)

"""
Exercise 3 LSSPS (Longest Symmetric Strict-Peak Subsequence) (10 marks)

Consider an integer-valued input sequence s[0,...,n-1] for a Python function. 

We consider subsequences of this sequence that need not be contiguous.

A symmetric strict-peak subsequence (SSPS) of an integer-valued sequence s is a
subsequence for which there exists a position i in the sequence s such that: 

a) the slice s[0,i+1] is strictly increasing (in integer values)

b) the slice s[i,n] is strictly decreasing (in integer values)

c) both slices (from a) and b) have the same length (symmetry requirement)

We refer to the element s[i] as the "top" of a symmetric strict-peak. 

Note that the slices in a) and b) could (both) be empty (as in Example 0 below).

Note that symmetric strict-peaks must have odd length (by condition c)

Example 0:

K = [7]

The only symmetric strict-peak subsequence is [7] where i = 0 and the top is K[0] = 7.

LSSPS(K) = 1

Note that when either slice of part i) or part ii) is non-empty, then
both these slices are non-empty (by part iii).

Example 1: L = [1, 3, -2, 0, 5, 2, 1]

LSPS(L) is the length of the longest symmetric strict-peak subsequence of L.

LSSPS(L) = 5

the subsquence

[1, 3, 5, 2, 1]

is a strict-peak subsequence of L.

The element L[2] = 5 is the top of the peak
the slice [1, 3, 5] is strictly increasing
the slice [5, 2, 1] is strictly decreasing.

Another symmetric strict-peak subsequence of length 5  is

[-2, 0, 5, 2, 1]

The element L[2] = 5 is the "top" of this symmetric strict-peak.

The top of the peak need not be the same for all longest symmetric
strict-peak subsequences.

Example 2:

M = [1, 3, 2, 5, 1]

LSSPS(M) = 3

This length is achieved for the symmetric strict-peaks:

[1, 3, 2] (for which the top a = 3)

[2, 5, 1] (for which the top a = 5)

[1, 2, 1] (for which the top is a = 2)

The following sequences are *not* symmetric strict-peaks:

[1,2,3,2,1,0] (symmetric strict-peaks have odd length)
[1,3,3,1] (symmetric strict-peaks have odd length)
[0,1,2,3] (strictly increasing but not a strict peak, and does not have odd length)

Exercise 3 requires solving the following two parts:

a) (5 marks) Write a recursion (including base cases) to express LSSPS(L)
for an input sequence s (hint: base the recusion on the length l(i,j) of a slice
L[i,j], where the slice corresponds to the creation of a symmetric strict-peak
in your argument)

"""

global maximum
 
def _LSSPS(L,n):
    global maximum

    if n == 1 : #base case is here
        return 1
 
    maxEnd = 1 #maxEnd is the length of LIS ending with L[n-1]
 
    for i in range(1, n): #Recursively get all LIS ending with L[0], L[1]..L[n-2]
        res = _LSSPS(L , i)
        if L[i-1] < L[n-1] and res+1 > maxEnd:
            maxEnd = res +1
 
    # Compare maxEnd with overall maximum
    maximum = max(maximum , maxEnd)
 
    return maxEnd
 
def LSSPS(L):
    global maximum
 
    # lenght of L
    n = len(L)
    maximum = 1
    _LSSPS(L , n)
 
    return maximum
 
# Test program to test the above function
L = [26, 24, 7, 64, 83, 32, 43, 11, 72, 73]
n = len(L)
print ("Length of LSSPS is", LSSPS(L))

"""
b) (5 marks) Write a Python function to compute the length of a longest symmetric
strict-peak subsequence of a given sequence. 
"""
def LongestSSPS(arr):
	n = len(L)

	LIS = [1 for i in range(n+1)]

	# Compute LIS values from left to right
	for i in range(1 , n):
		for j in range(0 , i):
			if ((L[i] > L[j]) and (LIS[i] < LIS[j] +1)):
				LIS[i] = LIS[j] + 1

	# allocate memory for LDS and initialize LDS values for all indexes
	lds = [1 for i in range(n+1)]
	
	# Compute LDS values from right to left
	for i in reversed(range(n-1)): #loop from n-2 downto 0
		for j in reversed(range(i-1 ,n)): #loop from n-1 downto i-1
			if(L[i] > L[j] and lds[i] < lds[j] + 1):
				lds[i] = lds[j] + 1


	# Return the maximum value of (LIS[i] + lds[i] - 1)
	maximum = LIS[0] + lds[0] - 1
	for i in range(1 , n):
		maximum = max((LIS[i] + lds[i]-1), maximum)
	
	return maximum

# Test program to test the above function
L = [26, 24, 7, 64, 83, 32, 43, 11, 72, 73]
print ("Length of LongestSSPS is",LongestSSPS(L))

"""Use dynamic programming to define the function. """





