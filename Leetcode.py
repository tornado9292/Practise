# """
#     print the most often appearance words in an article
# """
#
# # word_count = {}
# # line_num = 0
# # with (open("D:/Dev/Python/learn/pythonProject1/random_text.txt") as fin):
# #     for line in fin:
# #         line = line[:-1]
# #         words = line.split(" ")
# #         for word in words:
# #             if word not in word_count:
# #                 word_count[word] = 1
# #             else:
# #                 word_count[word] += 1
# # sort_by_key = dict(sorted(word_count.items(), reverse=True)[:10])
# # print(sort_by_key)
# #
# # sort_by_value = dict(sorted(word_count.items(), key=lambda itme:itme[1], reverse=True)[:10])
# # print(sort_by_value)
# #
#
# """
#     print 9 * 9 cheng fa biao
# """
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i} * {j} = {i*j}\t", end="")
#     print("")
#
# """
#     guess the number which is a random number of 3 digits, and print
#     numaAnumbB A stands for right guess digit, and B stands for wrong
#     guess digit, and numa is how many guess right
# """
#
# import random
#
# num = random.randint(100,999)
# num_str = str(num)
#
# def check_numbers(num):
#     num_guess_str = str(num)
#     numA = 0
#     flag = True
#     for i in range(len(num_str)):
#         if num_str[i] == num_guess_str[i]:
#             numA += 1
#     if numA ==3:
#         flag = False
#     print(f"{numA}A{3 - numA}B")
#     return flag
# flag = True
# total_guess = 0
# while flag:
#     num_guess = int(input("Guess the number:"))
#     if num_guess<100 or num_guess>999:
#         continue
#     flag = check_numbers(num_guess)
#     total_guess += 1
#
# print(f"You guessed {total_guess}, and random number is {num}")
"""
Yang hui triangle
"""
# from attr.validators import max_len
# from pyspark.sql.connect.functions import length
# from scipy.signal import square

# a = []
# n = int(input("please enter the how many lines:"))
# for i in range(n):
#     a.append([])
#
#     for j in range(i+1):
#         if j == 0 or j == i:
#             a[i].append(1)
#         else:
#             a[i].append(a[i-1][j]+a[i-1][j-1])
#
#
# for i in a:
#     for j in i:
#          print(f"{j}\t", end="")
#     print()
#
# s1 = 'abcdeftlkdsfk'
# s2 = 'z'
# print(s1.find(s2))
#
#
# """
# Medium: Write a function that takes a list of integers and returns a new list with all duplicate elements removed, while maintaining the original order.
# """
#
# def remove_duplicate(li):
#     new_li = []
#     for i in li:
#         if i not in new_li:
#             new_li.append(i)
#     return new_li
#
# print(remove_duplicate([1,2,2,1,5,1,78,9,'z']))

"""
Hard: Implement a function that takes a string containing only parentheses '(' and ')' and determines if the parentheses are balanced. Return True if balanced, False otherwise.
"""
#
# def check_parentheses(str):
#     stack = []
#     for char in str:
#         if char == '(':
#             stack.append(char)
#         else:
#             if len(stack) == 0:
#                 return False;
#             else:
#                 stack.pop()
#     return len(stack)==0
# def check_parentheses(str):
#     open = 0
#     close = 0
#     for char in str:
#         if char == '(':
#             open += 1
#         else:
#             close+=1
#     return open==close
# print(check_parentheses("()()"))  # True
# print(check_parentheses("(())"))  # True
# print(check_parentheses("(()"))   # False
# print(check_parentheses("())"))   # False
# #
# def find_pairs_with_sum(nums, target):
#     pairs = []
#     unique_pairs = set()
#     seen = set()
#
#     for num in nums:
#         complement = target - num
#         if complement in seen:
#             pair = tuple(sorted((num, complement)))
#             if pair not in unique_pairs:
#                 unique_pairs.add(pair)
#                 pairs.append(pair)
#         seen.add(num)
#     return pairs
# #nums = [2, 4, 3, 5, 7, 8, 9, -2]
# nums = [1,2,1,5,-2,10,3,4,6]
# target = 7
# result = find_pairs_with_sum(nums, target)
# print(result)  # Output: [(2, 5), (3, 4), (-2, 9)]
# """
# spiral print
# """
# matrix = []
#
# for i in range(4):
#     matrix.append([])
#     for j in range(4):
#         matrix[i].append(i*4+j)
# print(matrix)
#
# left = 0
# right = 4
# top = 0
# bottom = 4
# result = []
# while left<right and top<bottom:
#     for i in range(left,right):
#         result.append(matrix[top][i])
#     top += 1
#     for j in range(top,bottom):
#         result.append(matrix[j][right-1])
#     right-=1
#
#     for i in range(right-1,left-1,-1):
#
#         result.append(matrix[bottom-1][i])
#     bottom -=1
#
#     for i in range(bottom-1,top-1,-1):
#         result.append(matrix[i][left])
#
#     left+=1
# print(result)

"""
Longest Substring Without Repeating Characters:
Implement a function that takes a string and returns the length of the longest substring without repeating characters.
"""

"""
Write a function that takes a list of numbers and returns the sum of all elements at even indices using enumerate().
Create a function that takes a string and returns a new string where the characters at even indices are uppercase and odd indices are lowercase. Use enumerate() in your solution.
Write a function that takes a list and returns a new list containing only the elements whose indices are prime numbers. Use enumerate() and a helper function to check for prime numbers.
# """
# l = ['a', 'b','c','d','e','f']
# for i, element in enumerate(l,start=0):
#     if i%2==0:
#         print(i, element)
# def even_U_odd_L(s):
#     for i, char in enumerate(s):
#         if i%2==0:
#             print(char.upper(), end="")
#         else:
#             print(char, end="")
# even_U_odd_L("abcdefgh")
# import math
# def isPrime(num):
#     is_prime=False
#     if num == 0 or num==1:
#         return is_prime
#     for i in range(2,int(square(num)+1)):
#         if num%i==0:
# #             return is_prime
# #     return True
# # def print_prime_index_element(nums):
# #     l = []
# #     for i, element in enumerate(nums):
# #         if isPrime(i):
# #             l.append(nums[i])
# #     return l
# # print(print_prime_index_element(['a', 'b','c','d']))
# # #
# # l = ['a', 'b','c','d']
# # for i, j in enumerate(l):
# #     print(i, j, sep=" ")
# def length_of_longest_substring(s):
#     # Dictionary to store the last position of each character.
#     char_index = {}
#     # Initialize the starting point of the current substring.
#     start = 0
#     # Initialize the maximum length of substring found.
#     max_length = 0
#
#     for i, char in enumerate(s):
#         # If the character is found in the dictionary and is within the current substring.
#         print(f" char-index is {char_index}, i is {i}, char is {char}, star is {start}")
#         if char in char_index and char_index[char] >= start:
#             # Move the start to the right of the last occurrence of the character.
#             start = char_index[char] + 1
#             print(f"differnt now, start is {start}")
#         # Update the character's last position.
#         char_index[char] = i
#         # Update the maximum length.
#
#         max_length = max(max_length, i - start + 1)
#
#     return max_length
# s = "abcabcbb"
# print(length_of_longest_substring(s))
#
# """
# Write a function rotate_array(arr, k) that rotates an array arr by k positions to the right using slicing. For example:
# """
#
# def rotate_array(l, k):
#     new_l =[]
#     slicing_index = len(l) - k
#     new_l.extend(l[slicing_index:])
#     new_l.extend(l[:slicing_index])
#     return new_l
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# print(rotate_array(arr, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
# """
# Write a function reverse_words(sentence) that reverses the order of words in a given sentence using slicing. For example:
# """
# sentence = "The quick brown fox"
#
#
# def reverse_sentence(sentence):
#     new = sentence.split(" ")
#     return " ".join(new[::-1])
# print(reverse_sentence(sentence))
#
# """
# Write a function find_all_substrings(s) that returns a list of all possible substrings of a string s using slicing. For example:
# s = "abc"
# find_all_substrings(s)  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
# """
#
# def find_all_substrings(s):
#     # sub=[]
#     n = len(s.strip())
#     # for i in range(n):
#     #     for j in range(i,n):
#     #         sub.append(s[i:j+1])
#     # return sub
#     return [s[i:j+1] for i in range(n) for j in range(i,n)]
# s = "abc "
# print(find_all_substrings(s))  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
#
# """
# Write a function split_and_reverse(s, n) that splits a string s into n equal parts and then reverses each part using slicing. If s cannot be evenly divided, the last part should contain the remaining characters. For example:
# """
# def split_and_reverse(s, n):
#     new_s= []
#     for i in range(len(s)//n):
#         start = i*n
#         end = (i+1)*n
#         element = s[start:end]
#         new_s.append(element[::-1])
#     reminder = len(s)%n
#     if reminder!=0:
#         new_s.append(s[-reminder:][::-1])
#
#     return new_s
# s = "abcdefghijklmnop5"
# n = 4
# print(split_and_reverse(s, n))
#
# """
# Write a function extract_every_nth_element(lst, n) that returns a list containing every n-th element from the original list lst using slicing. For example:
# """
# def extract_every_nth_element(lst, n):
#     new_list = []
#     for i in range(len(lst)):
#         if (i+1) % n == 0:
#             new_list.append(lst[i])
#     return new_list
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 3
# print(extract_every_nth_element(lst, n) ) # Output: [3, 6, 9]
#
# """
# Problem: Longest Palindromic Subsequence in a Stream
# Implement a class StreamPalindrome that processes a stream of characters and maintains the length of the longest palindromic subsequence seen so far. The class should have the following methods:
# __init__(self): Initialize any necessary data structures.
# add_character(self, char: str) -> int: Add a new character to the stream and return the length of the longest palindromic subsequence in the entire stream seen so far.
# Constraints:
# The stream can contain up to 10^5 characters.
# All characters are lowercase English letters.
# The solution should be optimized for both time and space complexity.
# Example:
# python
# sp = StreamPalindrome()
# print(sp.add_character('a'))  # Output: 1
# print(sp.add_character('b'))  # Output: 1
# print(sp.add_character('a'))  # Output: 3
#
# """
# class StreamPalindrome:
#
#     def __init__(self):
#         self.max_len = 0
#         self.init_string = 'abcdefghig'
#
#     def check_palindromic(self,s:str)->bool:
#         return s==s[::-1]
#
#     def add_character(self,s:str)->int:
#         self.init_string+=s
#         l = len(self.init_string)
#         for i in range(l):
#             for j in range(i,l):
#                 if self.check_palindromic(self.init_string[i:j+1]) and len(self.init_string[i:j+1])>self.max_len:
#                     self.max_len = len(self.init_string[i:j+1])
#
#         return self.max_len
#
# sp = StreamPalindrome()
# print(sp.add_character("abcde"))

"""
Example Problem: Find the maximum sum of any contiguous subarray of size k in an array.
"""


# def max_sum_subarray(arr: list, k: int) -> int:
#     n = len(arr)
#     max_sum = sum(arr[:k])
#     window_sum = max_sum
#
#     for i in range(n - k):
#         window_sum = window_sum - arr[i] + arr[i + k]
#
#         if window_sum > max_sum:
#             max_sum = window_sum
#     return max_sum
#
#
# # Test the function
# arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
# k = 4
# print(f"the final is {max_sum_subarray(arr, k)}")  # Output: 39
# """
# Problem: Longest Substring with At Most K Distinct Characters
# Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.
# """
# from collections import Counter
#
#
# def most_frequent_char(s):
#     count = Counter(s)
#
#     most_common_char, frequency = count.most_common(1)[0]
#     return most_common_char, frequency
#
#
# def longest_substring_with_most_k(s: str, num: int) -> int:
#     most_common_char, frequency = most_frequent_char(s)
#     start = 0
#     end = 0
#     for i in range(len(s)):
#         if s[i] == most_common_char:
#             start = i
#             break
#     for i in range(len(s) - 1, -1, -1):
#         if s[i] == most_common_char:
#             end = i
#             break
#     return end - start
#
#
# s, k = "aabacbebebe", 3
# print(f"the longest is {longest_substring_with_most_k(s,k)}")
# """
# Problem: Longest Consecutive Sequence
# Given an unsorted list of integers, write a function that finds the length of the longest consecutive elements sequence.
# """
# if __name__ == "__main__":
#     pass
#
#
# def longest_consecutive_sequence(lst: list) -> int:
#     if not lst:
#         return 0
#     lst.sort()
#     longest = 1
#     lenth = 1
#     for i in range(1, len(lst)):
#
#         if lst[i] == lst[i - 1]:
#             lenth = 1
#             continue
#         elif lst[i] - lst[i - 1] == 1:
#             lenth += 1
#         else:
#             lenth = 1
#
#         if lenth > longest:
#             longest = lenth
#     return longest
#
#
# print(longest_consecutive_sequence([1, 2, 2, 3, 4]))
#
# """
# Problem: Find Maximum Average Subarray
# Given an array of integers and an integer k, find the contiguous subarray of length k that has the maximum average value. Return the maximum average value.
# Function Signature:
# """
#
#
# def find_max_average(nums: list, k: int) -> float:
#     l = len(nums)
#     max_sum = sum(nums[:k])
#     window_sum = max_sum
#     for i in range(k, l):
#         window_sum = window_sum - nums[i - k] + nums[i]
#         if window_sum > max_sum:
#             max_sum = window_sum
#     return max_sum / k
#
#
# nums, k = [1, 12, -5, -6, 50, 3], 4
# print(find_max_average(nums, k))  # dsf
#
#
# def add_item(item, items=[]):
#     items.append(item)
#     return items
#
#
# print(add_item(1))
# print(add_item(2))
# print(add_item(3))
#
#
# def add_item(item, items=None):
#     if items is None:
#         items = []
#     items.append(item)
#     return items
#
#
# print(add_item(1))
# print(add_item(2))
# print(add_item(3))
#
#
# items = [i for i in range(5)]
# print(items)
#
# v = 4
# if type(v) is int:
#     print("yes")
#
# if isinstance(v, int):
#     print("hell, yes")
#
#
# def max_sum_subarray(arr: list, k: int) -> int:
#     # Your code here
#     l = len(arr)
#     max_size = sum(arr[:k])
#     this_size = max_size
#     for i in range(l - k):
#         this_size = max_size - arr[i] + arr[i + k]
#         if this_size > max_size:
#             max_size = this_size
#     return max_size
#
#
# arr, k = [1, 4, 2, 10, 23, 3, 1, 0, 20], 4
# print(max_sum_subarray(arr, k))
#
#
# """"
# Problem: Minimum Window Substring
# Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# Function Signature:
# """
#
#
# def min_window(s: str, t: str) -> str:
#     # Your code here
#     len_s = len(s)
#     len_t = len(t)
#
#     def check(s, t) -> bool:
#         for k in t:
#             if k not in s:
#                 return False
#         return True
#
#     span = len_t
#     for i in range(len_s):
#         tem_str = s[i:span]
#         for k in range(len_s):
#             if check(tem_str, t):
#                 print(tem_str)
#                 return len(tem_str)
#
#     span += 1
#
#
# s, t = "ADOBECODEBANC", "ABC"
# print(min_window(s, t))
#

#
#
# """
# Problem: Implement a TimeMap class
# Implement a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# The TimeMap class should support two operations:
# set(string key, string value, int timestamp)
# Stores the key, value pair in the data structure with the given timestamp.
# get(string key, int timestamp)
# Returns a value such that set was called previously, with key and timestamp_prev <= timestamp.
# If there are multiple values, it should return the value associated with the largest timestamp_prev.
# If there are no values, it should return an empty string ("").
# Here's the class structure to start with:
# """
#
#
# class TimeMap:
#     def __init__(self):
#         # Initialize your data structure here
#         self.time_dict = {}
#
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         # Set the key-value pair at the given timestamp
#         if key not in self.time_dict:
#             self.time_dict[key] = {}
#         self.time_dict[key][timestamp] = value
#
#     def get(self, key: str, timestamp: int) -> str:
#         # Get the value associated with the key at the given timestamp
#         if key not in self.time_dict:
#             return ""
#         timestamps = sorted(self.time_dict[key].keys(), reverse=True)
#         for ts in timestamps:
#             if ts <= timestamp:
#                 return self.time_dict[key][ts]
#         return ""
#
#
# timeMap = TimeMap()
# timeMap.set("foo", "bar", 1)
# timeMap.set("foo", "bar2", 4)
# print(timeMap.get("foo", 1))  # Output: "bar"
#
# print(timeMap.get("foo", 3))  # Output: "bar"
#
# print(timeMap.get("foo", 4))  # Output: "bar2"
# print(timeMap.get("foo", 5))  # Output: "bar2"
# print(timeMap.get("foo", 0))  # Output: ""
# """
# Problem: Implement a Word Frequency Counter
# Create a function that takes a string of text and returns a dictionary where the keys are unique words in the text,
# and the values are the frequency of each word. The function should ignore punctuation and treat words case-insensitively.
# Here's a template to get you started:
# """
# import re
#
# def word_frequency(text):
#     text = re.sub(r'[^\w\s]', '', text.lower())
#     words = text.split()
#     words_dict = {}
#     for word in words:
#         words_dict[word] = words_dict.get(word,0)+1
#
#     return words_dict
# # Test the function
# sample_text = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."
# result = word_frequency(sample_text)
# print(result)
#
# class Employee:
#     def __init__(self):
#         self.employees={}
#     def __set__(self, name:str, dept:str, salary:int, level:int) -> None:
#         self.employees[name]=[dept,salary,level]
#
#     def __get__(self, name:str)->list:
#
#         return self.employees[name]
#     def raise_level(self) -> None:
#         for name in  self.employees:
#             if self.employees[name][2] == 1:
#                 salery = self.employees[name][1] +1000
#                 level = self.employees[name][2] + 1
#                 self.employees[name]=[self.employees[name][0],salery,level]
#         print(self.employees)

#
# employee.raise_level()










# employee = Employee()
# employee.__set__("Want Lihong","tech",3000,1)
# employee.__set__("Zhou Jielun","marketing",5000,2)
# employee.__set__("Lin Junjie","Marketing",6000,3)
# employee.__set__("Zhang Xueyou","tech",4000,1)
# employee.__set__("Liu Dehua","marketing",6000,2)
#
# class Employee:
#     def __init__(self):
#         self.employee={}
#     def __set__(self, name:str, department:str, salary:int, status:int) -> None:
#         self.employee[name]=[department,salary,status]
#     def __get__(self, name: str) -> list:
#         return self.employees[name]
#     def promotion(self) -> None:
#         for i in self.employees:
#             if self.employees[i][2]==1:
#                 salary = self.employees[i][1]+1000
#                 status = self.employees[i][2]+1
#                 self.employees[i]=[self.employees[i][0],salary,status]
#         print(self.employees)


"""
Here's the challenge:
Write a function called is_valid_parentheses that takes a string containing just the characters '(', ')', '{', '}', '[' and ']', and determines if the input string is valid. The function should return True if the string is valid, and False if it's not.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Here are some examples:

"()" -> True
"()[]{}" -> True
"(]" -> False
"([)]" -> False
"{[]}" -> True
"" -> True (empty string is considered valid)

Your function should be able to handle these and other similar cases efficiently.
Here's a function signature to get you started:
"""

str="([)]"
str = "{([]}"
open=["(", "{", "["]
close=[")", "}", "]"]

# arr=[]
# for i in str:
#     if i in open:
#         arr.append(i)
#     elif i in close:
#         if arr and open.index(str[str.index(i)-1])==close.index(i):
#             arr=[]
# if len(arr)==0:
#     print(True)
# else:
#     print(False)

def is_valid_parentheses(s: str) -> bool:
    # Your code here

    open_close = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for char in s:
        if char in open_close:
            stack.append(char)
        elif char in open_close.values():
            if not stack or open_close[stack[-1]] != char:
                return False
            else:
                stack.pop()
        else:
            return False
    return len(stack) == 0


print(is_valid_parentheses("([)]"))  # False

#class StreamPalindrome():

# def longest_palindromic_subsequence(s: str) -> int:
#     if not s:
#         return 0
#
#     length = len(s)
#
#     def expand_around_center(s,left,right):
#         while left>=0 and right<len(s) and s[left]==s[right]:
#             left-=1
#             right+=1
#
#         return right-left-1
#
#     max_len = 0
#     for i in range(length):
#         len1 = expand_around_center(s,i,i)
#         len2 = expand_around_center(s,i,i+1)
#         max_len = max(max_len,len1,len2)
#     return max_len
#
# def longest_palindromic_subsequence(s:str) ->int:
#     if not s:
#         return 0
#     def expand_around_center(s:str, left:int, right:int)->int:
#         while left>=0 and right<len(s) and s[left]==s[right]:
#             left-=1
#             right+=1
#         return right-left-1
#     max_len=0
#     length=len(s)
#     for i in range(length):
#         len1=expand_around_center(s,i,i)
#         len2=expand_around_center(s,i,i+1)
#         max_len=max(max_len,len2,len1)
#     return max_len
# print(longest_palindromic_subsequence('aabaa'))

"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""
import math

def gcdOfStrings(s1,s2):
    if s1+s2==s2+s1:
        return s1[:math.gcd(len(s1),len(s2))]

str1,str2 = "LEET",  "ABAB"

print(gcdOfStrings(str1,str2))

"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:
"""


def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
    l_bool=[]
    max=max(candies)
    for i in candies:
        if i+extraCandies>=max:
            l_bool.append(True)
        else:
            l_bool.append(False)


"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 
 """


def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count=0
    if flowerbed[0]==flowerbed[1]:
        count+=1
    if flowerbed[-1] == flowerbed[-2]:
        count += 1
    i=1
    while i < len(flowerbed)-1:
        if flowerbed[i]==flowerbed[i-1] and flowerbed[i]==flowerbed[i+1]:
            count+=1
            if flowerbed[i-1] ==1:
                flowerbed[i]=0
            else:
                flowerbed[i]=1
            i=1
        i+=1

    print(count)
    return count>=n

flowerbed,n = [1,0,0,0,1,0,0], 2
print(canPlaceFlowers(flowerbed,n))
