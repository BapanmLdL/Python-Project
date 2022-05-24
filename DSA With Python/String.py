import sys
s = "listen"
l = [e for e in s]
# print(l)

def permutation(S1, S2):
    if len(S1) != len(S2):
        return False

    freq = [0]*256
    for i in range(len(S1)):
        freq[ord(S1[i])] += 1
        freq[ord(S2[i])] -= 1
    for x in freq:
        if x != 0:
            return False
    return True
# s = input()
# t = input()
# out = permutation(s, t)
# print(out)

def Remove_Consecutive_Duplicates(String):
    n = len(String)
    if n == 0 :
        return String
    Si = 0
    ans = ""

    while Si < n :
        uC = String[Si]
        NuCi = Si + 1

        while (NuCi < n) and (String[NuCi] == uC):
            NuCi += 1
        ans += uC
        Si = NuCi
    return ans
# s = input()
# out = Remove_Consecutive_Duplicates(s)
# print(out)

def Reverse_Each_Word(s):
    l = s.split()
    # rev = ""

    for W in l:
        rev = ""
        for e in W:
            rev = e + rev
        print(rev, end = " ")
    # return rev
# s = input()
# Reverse_Each_Word(s)
# # print(out)

def Remove_Character(s, X):
    temp = ""

    for e in s:
        if e != X:
            temp = temp + e
    return temp
s = input()
X = input()
out = Remove_Character(s, X)
print(out)