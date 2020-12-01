class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix_longest = ""
        character_current = ""
        array_shortestword = ""
        array_shortestlength = 0

        # Obtain array specifics
        array_shortestword = min(strs, key=len)
        array_shortestlength = len(array_shortestword)

        # Iterate over the characters of array_shortestword
        for index in range(array_shortestlength):
            character_current = array_shortestword[index]

            for string in strs:
                if string[index] != character_current:
                    return prefix_longest
            
            prefix_longest += character_current
        return prefix_longest
