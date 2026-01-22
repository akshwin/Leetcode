def firstUniqChar(s: str) -> int:
    freq = [0] * 26   # frequency array for 26 lowercase letters

    # Step 1: Count character frequencies
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    # Step 2: Find the first unique character
    for i, ch in enumerate(s):
        if freq[ord(ch) - ord('a')] == 1:
            return i

    return -1

print(firstUniqChar("leetcode"))  # Output: 0