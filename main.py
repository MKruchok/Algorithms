from solution import Solution

if __name__ == '__main__':
    text = "abcxabcdababcdabcefabcdabcdabce"
    pattern = "abcdabce"
    print(Solution(text, pattern).kmp())
