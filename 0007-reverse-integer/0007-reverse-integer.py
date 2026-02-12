class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        if str_x[0] == '-':
            reversed_str = '-' + str_x[:0:-1]
        else:
            reversed_str = str_x[::-1]
    
        reversed_num = int(reversed_str)
    
    # 32-bit integer check
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
    
        return reversed_num