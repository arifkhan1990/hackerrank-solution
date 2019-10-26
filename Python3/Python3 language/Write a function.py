#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Write a function
#                      Difficulty: Medium
#                      Problem Link: https://www.hackerrank.com/challenges/write-a-function/problem
#

def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap
    
year = int(input())
print(is_leap(year))