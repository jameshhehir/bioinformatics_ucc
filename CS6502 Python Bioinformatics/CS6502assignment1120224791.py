# James Henry Hehir

#Exercise 1
def is_descendings2(s):
    return s != sorted(s) #Similar to is ascending, however it just changes the operator to say not equal to sorted(s).
"""
*TESTS*
s = [1,2,3]
print (is_descendings2(s))
"""

#Exercise 2
def peakboolean(peak_list):
    i = 0
    while i < len(peak_list): #while i is less than the lenght of the list peak_list
        if peak_list[i] >= peak_list[i-1] and peak_list[i] >= peak_list[i+1]: #if the ith position is greater or equal to i-1 and i+1 returns True
            return True
        else: # else it is false
            return False
"""
*TESTS*
print (peakboolean([1,1,1,4,1,1,1]))
"""

#Exercise 3:
def partition(lst, p):
    lst1 = [i for i in lst if i < p ] #checks if ints in lst are less than the stated p vaule
    lst2 = [i for i in lst if i == p ] #checks if ints in lst are equal to the stated p value
    lst3 = [i for i in lst if i > p ] #checks if ints in lst are equal to the stated p value
    print ("lst1=",lst1 )
    print ("lst2=",lst2 )
    print ("lst3=",lst3)
"""
*TESTS*

partition([1,2,3,42,2,3,41], 3)
"""

#Exercise 4:
def recursive_sum(lst):
    if  1 >=len(lst): # if the length of the list is less than or equal to 1
        return lst[0] #return index 0 of list 1
    else:
        return recursive_sum(lst[1:]) + lst[0] #add elements of list together

def recursive_product(lst):
    if 1 >= len(lst): # if the length of the list is less than or equal to 1
        return lst[0]
    else:
        return recursive_product(lst[1:])*lst[0] #multiply elements of list

def sum_of_product(lst):
    sum_of_lst = recursive_sum(lst)
    prod_of_lst = recursive_product(lst)

    return sum_of_lst,prod_of_lst
"""
*TESTS*

print("The results are: " ,sum_of_product([1]))
"""

#Exercise 2:
def ispalindrome(word):
    return word == word[::-1] # this line basically checks if the reverse of the string word is equal to word. Returns true if they match and false if they don't
"""
*TESTS*

print (ispalindrome('racecar'))
print (ispalindrome('racecars'))
"""

#Exercise 5:
def MergeSortBCP(aSubList1, aSubList2):
    aList=[] #empty list for storted overall list
    binaryList=[] #empty list for BCP
    c1 = 0
    c2 = 0
    total = len(aSubList1) + len(aSubList2)
    while len(aList) != total:
        if c1 == len(aSubList1): #If sublist 1 is exhausted add from sublist 2
            aList += aSubList2[c2:]
            break
        elif c2 == len(aSubList2): #If sublist 2 is exhausted add from sublist 1
            aList += aSubList1[c1:]
            break
        elif aSubList1[c1] < aSubList2[c2]: #If next list 1 item < next list 2 item, add next
            aList.append(aSubList1[c1]) #list 1 item
            binaryList.append(1) #for binaryList, add the 1 to list if list 1 item < list 2 item
            c1 += 1
        else: #Else add next item from list 2
            aList.append(aSubList2[c2])
            binaryList.append(0) #for binaryList, add the 0 to list if list 2 item < list 1 item
            c2 += 1
    print("The sort list is:", aList) 
    print("The BCP list is:", binaryList) 

"""
*TESTS*

a=[1,5,9,10]
b=[2,3,6,11]
MergeSortBCP(a,b)
"""
