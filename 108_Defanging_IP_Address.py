class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".","[.]")
        
print(Solution().defangIPaddr("1.1.1.1"))