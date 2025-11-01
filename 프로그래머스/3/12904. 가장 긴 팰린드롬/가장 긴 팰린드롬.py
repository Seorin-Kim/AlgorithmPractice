def solution(s):
    def is_palindrome(x):
        return x == x[::-1]
    
    for length in range(len(s), -1, -1):
        for i in range(len(s)-length+1):
            if is_palindrome(s[i:i+length]):
                return length
