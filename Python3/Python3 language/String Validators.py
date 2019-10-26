#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: String Validators
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/string-validators/problem
#

if __name__ == '__main__':
    s = input()

print(bool(len([ch for ch in s if ch.isalnum()])))
print(bool(len([ch for ch in s if ch.isalpha()])))
print(bool(len([ch for ch in s if ch.isdigit()])))
print(bool(len([ch for ch in s if ch.islower()])))
print(bool(len([ch for ch in s if ch.isupper()])))