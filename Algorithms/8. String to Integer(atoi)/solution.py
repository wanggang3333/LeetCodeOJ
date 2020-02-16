class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647; INT_MIN = -2147483648
        sums = 0
        sign = 1
        i = 0
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and str[i] == '-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            if INT_MAX/10 >= sums:
                sums = sums * 10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            if INT_MAX - digit >= sums:
                sums = sums + digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1
        return sign * sums
                