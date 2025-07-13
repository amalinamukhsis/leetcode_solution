class Solution(object):
    def isPalindrome(self,x):
        if x < 0:
            return False
        if x == 0:
            return True
        awal = x
        akhir = 0
        while x > 0:
            hasil_mod = x % 10
            akhir = akhir * 10 + hasil_mod
            x = x // 10
        if awal == akhir:
            return True
        else:
            return False
