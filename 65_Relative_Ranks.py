def findRelativeRanks(score):
    n = len(score)
    
    # store (score, index)
    arr = [(score[i], i) for i in range(n)]
    print(arr)
    # sort by score descending
    arr.sort(reverse=True)
    print(arr)
    
    ans = [""] * n
    
    for rank, (s,idx) in enumerate(arr):
        if rank == 0:
            ans[idx] = "Gold Medal"
        elif rank == 1:
            ans[idx] = "Silver Medal"
        elif rank == 2:
            ans[idx] = "Bronze Medal"
        else:
            ans[idx] = str(rank + 1)
    
    return ans
print(findRelativeRanks([10, 3, 8, 9, 4]))