class Solution(object):
    def reverseOnlyLetters(self, s):
        arr = list(s)
        start = 0
        end = len(arr) - 1
        
        while start < end:
            if not arr[start].isalpha():
                start += 1
            elif not arr[end].isalpha():
                end -= 1
            else:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
                
        return "".join(arr)

print(Solution().reverseOnlyLetters("ab-cd"))