n = int(input())
m = list(map(int, input().split()))

i = 0
while i < n:
  j = 0
  while j < (n - 1):
    if m[j] > m[j + 1]:
      a = m[j]
      m[j] = m[j + 1]
      m[j + 1] = a
    j = j + 1
  i = i + 1

i = 0
while i < n:
  print(m[i], end=" ")
  i = i + 1
  
"""
Problem Statement: 
Write a program that takes two lines of input:
The length of the array n.
The array of n integers entered on a single line, with elements separated by spaces. 
The program should sort the array in ascending order by swapping elements and print the sorted array on a single line.

Constraints:
Do not use a for loop, use only a while loop instead.
Do not use inbuilt functions or methods like len(), or sort().
The array will contain at least one element.

Sample Input 1: 
6 
5 2 9 1 5 6

Sample Output 1: 
1 2 5 5 6 9

Explanation: The sorted array is [1, 2, 5, 5, 6, 9].

Sample Input 2: 
5 
3 7 2 8 4

Sample Output 2: 
2 3 4 7 8
Explanation: The sorted array is [2, 3, 4, 7, 8]. """
