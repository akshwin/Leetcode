class Solution(object):
    def findRestaurant(self, list1, list2):
        small = float('inf')
        ans = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if (i+j) < small:
                        small = (i+j)
                        ans = [list1[i]]
                    elif (i+j) == small : 
                        ans.append(list1[i]) 
        return ans
        
print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))