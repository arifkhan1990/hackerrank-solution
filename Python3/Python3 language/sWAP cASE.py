#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: sWAP cASE
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/swap-case/problem
#

def swap_case(s):
    st = ''
    for i in s:
        if i.isupper() == True:
            st += (i.lower())
        else:
            st += (i.upper())
            
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)