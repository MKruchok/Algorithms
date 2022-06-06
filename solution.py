class Solution:

    def __init__(self, text, pattern):
        self.results = []
        self.pattern = pattern
        self.text = text

    def find_lps(self):
        lps = [0] * len(self.pattern)
        base = 0
        for current in range(1, len(self.pattern)):
            if self.pattern[current] == self.pattern[base]:
                lps[current] = base + 1
                base += 1
            else:
                if base != 0:
                    base = lps[base - 1]
                else:
                    lps[current] = 0
                    current += 1
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
