#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Designer Door Mat
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
#

x, y = map(int, input().split())
for i in range(1, x, 2):
    print((".|."*i).center(y,'-'))
print("WELCOME".center(y,'-'))

for i in range(x-2,-1,-2):
    print((".|."*i).center(y,'-'))