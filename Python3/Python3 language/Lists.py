#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Lists
#                      Difficulty: Medium
#                      Problem Link: https://www.hackerrank.com/challenges/python-lists/problem
#

if __name__ == '__main__':
    arr = []
    N = int(input())
    for i in range(0,N):
            data1 = input().split()
            data = data1[0]
            ar = data1[1:]
            if data != "print":
                data += "("+ ",".join(ar) +")"
                eval("arr."+data)
            else :
                print(arr)