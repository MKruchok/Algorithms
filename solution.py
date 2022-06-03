class Solution:

    def __init__(self, text, pattern):
        self.results = []
        self.pattern = pattern
        self.text = text

    def find_lps(self):
        lps = [0] * len(self.pattern)
        index = 0
        for i in range(1, len(self.pattern)):
            if self.pattern[i] == self.pattern[index]:
                lps[i] = index + 1
                index += 1
            else:
                if index != 0:
                    index = lps[index - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp(self):
        lps = self.find_lps()
        i = j = 0
        while i < len(self.text) and j < len(self.pattern):
            if self.text[i] == self.pattern[j]:
                i += 1
                j += 1
                if j == len(self.pattern):
                    self.results.append(i - j)
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return self.results
