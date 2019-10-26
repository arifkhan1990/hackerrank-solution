#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Nested Lists
#                      Difficulty: Medium
#                      Problem Link: https://www.hackerrank.com/challenges/nested-list/problem
#

if __name__ == '__main__':
    n = int(input())
    record = [[str(input()), float(input())] for _ in range(n)]
    result = sorted(set([b for a,b in record]))[1]
    
    print('\n'.join(sorted([a for a,b in record if b == result])))