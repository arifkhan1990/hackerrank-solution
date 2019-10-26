#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: String Split and Join
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
#

def split_and_join(line):
    line1 = "-".join(line.split())
    return line1

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)