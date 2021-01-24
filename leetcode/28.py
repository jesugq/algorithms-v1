class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        haystack_length = len(haystack)
        needle_length = len(needle)
        first_char = needle[0]
        chars_range = haystack_length - needle_length + 1

        for i in range(chars_range):
            if haystack[i] == first_char:
                string = haystack[i:i+needle_length]
                if needle == string:
                    return i
        return -1

class Main:
    def exec(self):
        solution = Solution()
        haystack, needle = self.e1()
        answer = solution.strStr(haystack, needle)
        print(answer)

    def e1(self):
        return "hello", "ll"

    def e2(self):
        return "aaaaa", "bba"

    def e3(self):
        return "", ""

    def e4(self):
        return "", "heyaa"

main = Main()
main.exec()