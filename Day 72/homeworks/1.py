def longest_palindrome(s: str) -> int:
    if len(s) == 0:
        return 0
    
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    max_length = 1  
    
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_length = max(max_length, len1, len2)
    
    return max_length