#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Python If-Else
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/py-if-else/problem
#

if __name__ == '__main__':
    n = int(input())
    if (n%2 == 1 or (n%2 == 0 and (n>=6 and n<= 20))):
        print ("Weird")
    else:
        print ("Not Weird")