#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Tuoles
#                      Difficulty: Medium
#                      Problem Link: https://www.hackerrank.com/challenges/python-tuples/problem
#

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup = tuple(integer_list)
    print (hash(tup))