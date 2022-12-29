class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(i+1):
                l = len(s) - i
                sub_s = s[j:j + l]
                # print(sub_s)
                if sub_s == sub_s[::-1]:
                    # print(sub_s)
                    return sub_s


if __name__ == "__main__":
    s = Solution()

    s.longestPalindrome("a")  # "a"
    s.longestPalindrome("bb")  # "a"
    s.longestPalindrome("babad")  # "bab"
    s.longestPalindrome("cbbd")  # "bb"
    s.longestPalindrome("abcabcdedcbaccc")  # "cabcdedcbac"
    # s.longestPalindrome("xiqhechagdpbcdthaafmcnplenylepawbafsmxqlwhzgqmuemwolgoockcafchdsfggulwfzwwkvivnwgbelbbydzfkcfsschvbantskuosunhqihmqjmzgavfnonwhwrkfxgcbowfsebthbrhhklxxyoxiphrgxqodulrbbvdwcclpyjhljgyypztbqzkiyzbfnvnoargyyakaidkiyleurvjbadzwqjtrluayhblhdokmwrwhassruxpftwlbalfvwxtfcqibywsusrlwmbcibvgwnmmdmuhswuperbjoxarhqcpcebbtyhnrouvuwftspmzsmdhfcqovffkuikzrcweffmpnjldoalhcvqvjavllvajvqvchlaodljnpmffewcrzkiukffvoqcfhdmszmpstfwuvuornhytbbecpcqhraxojbrepuwshumdmmnwgvbicbmwlrsuswybiqcftxwvflablwtfpxurssahwrwmkodhlbhyaulrtjqwzdabjvruelyikdiakayygraonvnfbzyikzqbtzpyygjlhjyplccwdvbbrludoqxgrhpixoyxxlkhhrbhtbesfwobcgxfkrwhwnonfvagzmjqmhiqhnusoukstnabvhcssfckfzdybblebgwnvivkwwzfwluggfsdhcfackcooglowmeumqgzhwlqxmsfabwapelynelpncmfaahtdcbpdgahcehqix")
    print("done")