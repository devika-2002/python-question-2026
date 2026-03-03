
n = int(input())
m = list(map(int, input().split()))

i = 0
while i < n:
  j = 0
  duplicate = 0
  while j < i:
    if m[i] == m[j]:
      duplicate = 1
    j = j + 1
  if duplicate == 0:
    count = 0
    k = 0
    while k < n:
      if m[i] == m[k]:
        count += 1
      k = k + 1
    print(str(m[i]) + ": " + str(count))
i = i + 1

"""
Difficulty Level: Medium

Problem Statement: 
Write a program that takes two lines of input:
The length of the array n.The array of n integers entered on a single line, with elements separated by spaces. 
The program should calculate and print the frequency of each element in the array. Each element should be printed 
only once, in the order of their first appearance, along with its frequency.

Constraints:
Do not use a for loop, use only a while loop instead.
Do not use inbuilt functions or methods for calculating frequency like len(), count(), or collections.
The array will contain at least one element.

Sample Input 1: 
7 
1 2 2 3 3 3 4

Sample Output 1: 
1: 1 
2: 2 
3: 3 
4: 1
Explanation: Element 1 appears once, 2 appears twice, 3 appears three times, and 4 appears once.

Sample Input 2: 
6 
5 5 5 1 1 2

Sample Output 2: 
5: 3 
1: 2 
2: 1
Explanation: Element 5 appears three times, 1 appears twice, and 2 appears once.
"""