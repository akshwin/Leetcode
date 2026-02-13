class Solution(object):
    def capitalizeTitle(self, title):
        words = title.split(" ")
        result = []

        for w in words:
            w = w.lower()  
            if len(w) <= 2:
                result.append(w)
            else:
                result.append(w[0].upper() + w[1:])

        return " ".join(result)

print(Solution().capitalizeTitle("capiTalIze tHe titLe"))