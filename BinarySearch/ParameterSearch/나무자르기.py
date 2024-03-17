n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
start, end = 0, trees[-1] + 1

def find_lowest_cut_idx(trees, target):
    low, high = 0, len(trees) - 1

    while low <= high:
        mid = (low + high) // 2
        current = trees[mid]
        if current <= target:
            low = mid + 1
        else:
            high = mid - 1
    return low

while start <= end:
    mid = (start + end) // 2

    idx = find_lowest_cut_idx(trees, mid)
    remainder = sum(trees[idx:]) - mid * (len(trees) - idx)
    if remainder >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
    
# 다른사람의 풀이
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) 

while start <= end: 
    mid = (start+end) // 2
    
    log = 0 
    for i in tree:
        if i >= mid:
            log += i - mid
    
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)