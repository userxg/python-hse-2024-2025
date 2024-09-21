'''
leetcode.com/problem-list/string/
https://leetcode.com/problems/string-to-integer-atoi/description/
'''


class Solution:
    def myAtoi(self, s: str) -> int:
        num = '0123456789'
        res = ''
        for x in s:
            if x == ' ' and len(res) == 0:
                continue
            if len(res) == 0 and x != ' ' and (x in '-+' or x in num):
                res += x
            elif x in num:  res += x
            else:  break
        if res == '' or res in '-+':
            return 0
        else:
            if int(res) >= 2**31:  return (2**31 - 1)
            elif int(res) < -(2**31):  return -2**31
            else:  return int(res)