class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[(num%10)])
"""
還蠻直覺的做法吧
算是歸納法？ 把千位數百位數十位數個位數都弄好, 然後就用mod的來做
不難, 要背熟
"""
