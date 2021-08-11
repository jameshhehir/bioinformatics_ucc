# James Henry Hehir

"""Assignment 2, CS6502 (Python for BioScientists, II), M. Schellekens,
Total of 35 Marks """

"""Exercise 1 (17 marks in total), adjust the code for the brute force
computation of the max sum of a contiguous subsequence of a given sequence
(use the code seen in the labs,recalled below)"""


"""Exercise, 1, Part 1) (5 Marks)

Adjust the code so it prints not only the max sum, but also the slice that
produces a max sum.

Rename the function

BruteForce_max_sum

to

Brute_Force_max_sum_and_slice.

Adjust the print command so it not only prints the name of the functin andthe
"max sum =", m  but also add a print command, using "max_sum_slice =", ***"
in which *** is replaced by code reproducing a slice that sums to max sum. 

Test the code on: 

BruteForce_max_sum_and_slice([1,3,-1,5,-1,2]) """

def all_pairs(n):
    s = [ ]
    for i in range(n):
       for j in range(i,n):
           s.append((i,j))
    return s


def BruteForce_max_sum_and_slice(a):
    m = 0
    for p in all_pairs(len(a)):
        i = p[0]
        j = p[1]
        b = a[i:j+1]
        s = sum(b)
        m = max(m, s)
    print("BruteForce_max_sum", a," max sum =", m)
    print("max_sum_slice =", a[i:j+1]) 

BruteForce_max_sum_and_slice([1,3,-1,5,-1,2]) 

"""Exercise 1, Part 2) (12 Marks) Adjust the code further so it prints all
info printed under Part 1) (but using the newly defined function name, as given
below) and *all* slices producing the max sum.

Rename the function

Brute_Force_max_sum_and_slice

to

BruteForce_max_sum_and_all_slices

Test the code on: BruteForce_max_sum_and_all_slices([1,3,-1,5,-1,-1,2])

"""

def all_pairs(n):
    s = [ ]
    for i in range(n):
       for j in range(i,n):
           s.append((i,j))
    return s


def BruteForce_max_sum_and_all_slices(a):
    m = 0
    for p in all_pairs(len(a)):
        i = p[0]
        j = p[1]
        b = a[i:j+1]
        s = sum(b)
        m = max(m, s)
    print("BruteForce_max_sum", a," max sum =", m)
    print("max_sum_slice =", a[i:j+1])
    print("All slice are:", all_pairs(len(a)))

BruteForce_max_sum_and_all_slices([1,3,-1,5,-1,-1,2])


"""Exercise 2 (7 Marks) write a Python function MaxMatrix(A,n) that takes as
input an n x n matrix and prints the output formulated as a print command using:
"max of Matrix", matrix A, "is", m

in which A is the input matrix and m is the maximum value of the matrix.

The matrix can be assumed to contain positive values only.

Test the code on:"""

A = [[1,3,2],[2,1,5],[0,1,3]]  
def maxmatrix(A):
    m = (max(map(max, A)))
    return "Max of Matrix", A, "is", m
print(maxmatrix(A))

"""
Exercise 3 (11 marks). LPCS (Longest Palindromic Contiguous Substring)

Introduction to Exercise 3: Longest Palindromic Substring (recalled from labs)

We have seen code in the labs for a function LPS to compute the length of a
longest palyndromic substring of a given string (code recalled below).

The substring need not be contiguous. 

This code only computes the length of the longest palindromic substring
and does not return the longest palindromic subsequence. 

Consider the input string s[0,...,n-1] of length n.

Let l(i,j) = length of a largest palindromic substring of s
starting at i and ending at j.

We recall the recursion. We refer to the two characters s[i] and s[j] in a
substring s[i:j+1] = s[i]...s[j] of a string s

as "bookend-characters". The recursion is driven by considering these
bookend-characters on either end of a given string s.

Recursion:

A single character s[i] is always a palindrome (of length 1), hence:

l(i,i) = 1 (base cases of recursion)

The code for LPS sets up a matrix and fills the diagonal with the number 1.

CASE 1:

If the characters in positions i and j in the the string s are identical then:

l(i,j) = l(i + 1, j - 1) + 2

CASE 2:

If the characters in position i and j in the string s differ then:

l(i,j) = max(l(i+1,j),l(i,j-1))

 """


def LPS(s):
    n = len(s)
    print("length longest palindromic substring, n =", n)
    A = [[0] * n for i in range(n)]
#creates a n x n matrix initialized with zeros in all entries
    for i in range(n):
        A[i][i] = 1
#initalizes the diagonal with 1       
    for diff in range(1,n):
        for i in range(n - diff):
            j = i + diff
            if s[i] != s[j]:
                A[i][j] = max(A[i+1][j], A[i][j - 1])
            else:
                A[i][j] = A[i + 1][j -1] + 2
#computes the recursive calls
    print("length-longest-palindrome =", A[0][n-1])

 
LPS("BBRARBB")


 

def LPCS(st) :
    n = len(st) #get the length of the iput string
    table = [[0 for x in range(n)] for y in range(n)] 
    maxLength = 1 #all substrings of length 1 are palindrome
    i = 0
    while (i < n) :
        table[i][i] = True
        i = i + 1

    start = 0
    i = 0
    while i < n - 1 : #check if substring of length 2
        if (st[i] == st[i + 1]) :
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1
     
    k = 3
    while k <= n : #check for substrings greater than 2 
        i = 0
        while i < (n - k + 1) : 
            j = i + k - 1 #getting the end index of substring
            if (table[i + 1][j - 1] and st[i] == st[j]) :
                table[i][j] = True
                if (k > maxLength) :
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1

    print ("Longest palindrome contiguous substring is: " + st[(start) : (start + maxLength -1) + 1], flush=True)
    print ("Length is:", maxLength) 
 
LPCS("BBRARBB") 
LPCS("RABAA")





""" Exercise 3 (continued): Write a Python function LPCS (Length of Longest
Palindromic CONTINGUOUS Substring) to compute the length of the longest
contiguous palindromic substring.

I sketch two possible approaches to solve this problem, and recommend
implementing the first of these. I do not recommend the second potential
solution method for this assignment (though, see comment below on
accepting a solution following the second route if you find one). 

Solution approach 1

Adjust the code of LPS:

pair the numbers you compute for the length with truth values (True or False).

True indicates that this regards a possible contiguous solution.

False means the substring under consideration cannot yield a contiguous result.
(This happens when the bookends of the string differ.) Further extension of
this case cannot yield a contiguous result. 

Initialization: use [0, T] for every matrix entry (except on the diagonal
for which values will be overwritten by [1,T]).

On the diagonal, the function LPCS must fill in the value [1,T]
This reflects that a single character forms a contiguous palindrome.

Computing the next diagonal entry (just above the central one):

If the book-end characters are the same, replace [a,b] by [a + 2,b]
(hence the truth-value b remains the same, True if it was True before, and
False if it was False before)

The value [a + 2,b] is obtained from [a,b] located in the matrix as
follows:

  *    [a + 2, b]
  
[a,b]     *

If the book-end characters differ: then [a,b] and [c,d] yield:

[maximum of [a,c], False]

As before: the value [maximum of [a,c], False] is obtained from [a,b] and [c,d]
located in the matrix as follows:

[a,b)  [maximum of [a,c],False]
  
  *       [c,d]


We illustrate the intended computation below, where we indicate the substrings
under consideration for each matrix entry. These only illustrate the
substrings considered in the computation and do not form part of the
actual computation by LPCS of the pairs [a,b]. Also not all [0,T] entries
filled in by LPCS  are indicated.

Blank matrix entries reflect that these should be [0,T] entries, which have been
omitted as they do not play a role in the actual computation. 

      B          B          R         A          R          B          B


      B         BB         BBR       BBRA      BBRAR      BBRARB     BBRARBB
B   [1,T]      [2,T]      [2,F]     [2,F]      [3,F]      [5,F]      [7,T]



                B          BR        BRA       BRAR       BRARB      BRARBB
B   [0,T]      [1,T]      [1,F]     [1,F]      [3,F]      [5,T]      [5,F]



                            R        RA         RAR      RARB       RARBB
R              [0,T]      [1,T]     [1,F]      [3,T]     [3,F]      [3,F]



                                      A          AR       ARB       ARBB
A                         [0,T]     [1,T]      [1,F]     [1,F]      [2,F]



                                                 R        RB         RBB
R                                   [0,T]      [1,T]     [1,F]      [2,F]



                                                          B          BB
B                                               [0,T]    [1,T]      [2,T]



                                                                      B
B                                                        [0,T]       [1,T]




Write code for the function LPCS(s),which computes the length of a
Longest Palindromic Contiguous Substring of the string s. Adapt the code
for LPS(s) as described above, working over pairs of elements (implemented
as a two-element list).


The output is the pair [a,b] which has b = True and which has largest
value for a.

In the above example this is the pair: [7,T]. The longest palindromic substring
associated with this pair is:     BBRARBB   (as indicated via the string
associated with this pair in the above example) Note that BBRARBB happens
to be a palindrome. For non-palindromes, the max could be obtained for a strict
substring.

The function LPCS(s) needs to include a print command, printing the following
result (this is not Python code, merely an indication of the output-format):

"LPCS",the input string s,"length-longest-contiguous-palindrome =", 
the computed length.  

Test the code on: LPCS("BBRARBB") and LPCS("RABAA")

Solution approach 2 (not required for this assignment)

You could atempt to write new code from scratch with the aim to provide a
recursion for the longest contiguous palindromic substring (if it exists).
This is not required or recommended for the assignment. However, if you do
produce this type of solution (provided it can be done and it is correct--I have
not worked this out), it will be accepted. 

Note: there are other ways to solve this problem. Alternative solutions, if
correct, will be accepted. For instance, you could atempt a brute force approach,
producing all palindromic subsequences, and select the contiguous ones
among them, then select the longest among these. 
"""


    
