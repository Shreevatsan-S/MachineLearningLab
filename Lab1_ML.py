#!/usr/bin/env python
# coding: utf-8

# In[26]:


def pairs(lst1):
    res = []
    while lst1:
        num = lst1.pop()
        diff = 10 - num
        if diff in lst1:
            res.append((diff, num))
            lst1.remove(diff)
    return res

def Rangee(lst2):
    if len(lst2) < 3:
        return "Range determination not possible!"
    else:
        max1 = max(lst2)
        min1 = min(lst2)
        return max1 - min1
    
def squareMatrix():
    rank = int(input("Enter the rank of the matrix: "))
    sqMat = []
    for i in range(rank):
        inner = []
        for j in range(rank):
            element = int(input(f"Element [{i+1}][{j+1}]: "))
            inner.append(element)
        sqMat.append(inner)
    m = int(input("Enter the exponent: "))
    
    result = [[1 if i == j else 0 for j in range(rank)] for i in range(rank)]
    
    for _ in range(m):
        temp = [[0 for _ in range(rank)] for _ in range(rank)]
        for i in range(rank):
            for j in range(rank):
                for k in range(rank):
                    temp[i][j] += result[i][k] * sqMat[k][j]
        result = temp
    return result

def highestChar(input_string):
    char_count = {}
    
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    highest_char = None
    highest_count = 0
    
    for char, count in char_count.items():
        if count > highest_count:
            highest_count = count
            highest_char = char
            
    return highest_char, highest_count

lst1 = [2, 7, 4, 1, 3, 6]
result = pairs(lst1)
print("Pairs with sum 10 are: ", result)
print("Number of pairs are: ", len(result))

lst2 = [5, 3, 8, 1, 0, 4]
print("Range is: ", Rangee(lst2))

print("Matrix is: ", squareMatrix())
char, count = highest_occurring_char(input_string)
print(f"The highest occurring character is '{char}' with a count of {count}.")


# In[ ]:




