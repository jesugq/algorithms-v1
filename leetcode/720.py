from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        sorted_words = sorted(words)

        longest_word = ''
        longest_length = 0
        for word in sorted_words:
            length = len(word)
            if length > longest_length:
                for pivot in reversed(range(0, length)):
                    if pivot == 0:
                        longest_word = word
                        longest_length = length
                        break
                    if word[0:pivot] not in sorted_words:
                        break
        return longest_word

class Main:
    def execute(self):
        solution = Solution()
        tests = self.tests()
        for test in tests:
            answer = solution.longestWord(test[1])
            print(test[0] == answer, test[0], answer)

    def tests(self):
        return [
            ['world', ['w', 'wo', 'wor', 'worl', 'world']],
            ['apple', ['a', 'banana', 'app', 'appl', 'ap', 'apply', 'apple']],
            ['yodn', ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]],
            ['latte', ["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]],
            ['e', ["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]]
        
        ]

main = Main()
main.execute()