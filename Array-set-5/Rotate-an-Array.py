
n = int(input())
Array = list(map(int, input().split()))
k = int(input())

i = n - k
while i < n:
  print(Array[i], end=" ")
  i = i + 1

j = 0
while j < n - k:
  print(Array[j], end=" ")
  j = j + 1

"""
Difficulty Level: Hard

Problem Statement: 
Write a program that takes three lines of input:
The length of the array n.
The array of n integers entered on a single line, with elements separated by spaces.
An integer k. 
The program should rotate the array k positions to the right, and print the resulting array, with elements separated by spaces.

Constraints:
Do not use a for loop, use only a while loop instead.
Do not use inbuilt functions or methods like len() or rotate()
The array will contain at least one element.

Sample Input 1: 
5 
1 2 3 4 5 
2

Sample Output 1: 
4 5 1 2 3
Explanation: After rotating 2 positions to the right, the array becomes [4, 5, 1, 2, 3].

Sample Input 2: 
4 
7 8 9 10 
3

Sample Output 2: 
8 9 10 7
Explanation: After rotating 3 positions to the right, the array becomes [8, 9, 10, 7].
"""