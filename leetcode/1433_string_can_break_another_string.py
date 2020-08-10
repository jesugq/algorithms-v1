class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # Length of the strings (Assume both are of the same size)
        string_length = len(s1)

        # Create the sorted permutation
        sorted_list1 = sorted(s1)
        sorted_list2 = sorted(s2)

        sorted_string1 = ''.join(sorted_list1)
        sorted_string2 = ''.join(sorted_list2)

        # Obtain the breaker (highest lexicographical ordering) and the target
        string_breaker = sorted_string1
        string_target = sorted_string2

        if string_breaker < string_target:
            string_breaker, string_target = string_target, string_breaker

        # Check that the lexicographical ordering of breaker stays constantly
        # higher than the target's
        for index in range(string_length):
            if (ord(string_breaker[index]) < ord(string_target[index])):
                return False
        return True