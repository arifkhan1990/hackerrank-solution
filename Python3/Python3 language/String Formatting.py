#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: String Formatting
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/python-string-formatting/problem
#

def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1,number+1):
        print(' '.join(map(lambda x: x.rjust(w), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)