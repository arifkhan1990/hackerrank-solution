#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Find the Runner-Up Score!
#                      Difficulty: Medium
#                      Problem Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result = sorted(list(set(arr)))
    print(result[-2])