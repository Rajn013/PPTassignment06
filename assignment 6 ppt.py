#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Answer01


def reconstruct(s):
    n = len(s)
    perm = []
    start, end = 0, n
    
    for ch in s:
        if ch == 'I':
            perm.append(start)
            start += 1
        elif ch == 'D':
            perm.append(end)
            end -= 1
            
    perm.append(start)
    
    return perm


# In[4]:


s = "IDID"
print(reconstruct(s))


# In[31]:


#Answer02


#to solve this problem in o(log(m*n)) time complexity.we can a modified binary search algorithm.


def search_matrix(matrix, target):
    m = len(matrix)  
    n = len(matrix[0])  

    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            right = mid - 1
        else:
            left = mid + 1

    return False

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3

found = search_matrix(matrix, target)
print(found)


# In[29]:


#Answer 3


def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    left = 0
    right = n - 1

    while left < right:
        if arr[left] >= arr[left + 1] or arr[right] >= arr[right - 1]:
            return False
        left += 1
        right -= 1

    return True


# In[30]:


arr = [2, 1]
is_valid_mountain = valid_mountain_array(arr)
print(is_valid_mountain)


# In[37]:


#answe04


def findMaxLenght(nums):
    count_dict = {0: -1}
    count = 0
    max_lenght = 1

    for i, num in enumerate(nums):
        if num == 1:
            count += 1
        else:
            count -= 1

        if count in count_dict:
            max_length = max(1, i - count_dict[count])
        else:
            count_dict[count] = i

    return max_length


# In[38]:


nums = [0, 1]
max_lenght = findMaxLenght(nums)
print(max_lenght)


# In[39]:


#Answer05

def minProductSum(nums1, nums2):
    nums1.sort()  
    nums2.sort(reverse=True)  
    min_product_sum = 0

    for i in range(len(nums1)):
        min_product_sum += nums1[i] * nums2[i]

    return min_product_sum


# In[43]:


nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
min_product = minProductSum(nums1, nums2)
print(min_product)


# In[61]:


#Answer 6



from collections import defaultdict


# In[62]:


def findOriginalArray(changed):
    count = {}
    original = []
    
    
    for num in changed:
        count[num] = count.get(num, 0) + 1
        
        
    
    for num in sorted(changed):
        if count.get(num, 0) > 0 and count.get(num * 2, 0) > 0:
            original.append(num)
            count[num] -= 1
            count[num * 2] -= 1

    return original if len(original) == len(changed) // 2 else []   
        


# In[63]:


changed = [ 1, 3, 4, 2, 6, 8 ]
original = findOriginalArray(changed)
print(original)


# In[64]:


#answer07


def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1

    while row_start <= row_end and col_start <= col_end:

        for j in range(col_start, col_end + 1):
            matrix[row_start][j] = num
            num += 1
        row_start += 1


        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1


        if row_start <= row_end:
            for j in range(col_end, col_start - 1, -1):
                matrix[row_end][j] = num
                num += 1
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_start] = num
                num += 1
            col_start += 1

    return matrix


n = 3
result = generateMatrix(n)
print(result)


# In[65]:


#Answer08


def multiplySparseMatrices(mat1, mat2):
    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])

    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for x in range(k):
                result[i][j] += mat1[i][x] * mat2[x][j]

    return result


# In[66]:


mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]

result = multiplySparseMatrices(mat1, mat2)
print(result)


# In[ ]:




