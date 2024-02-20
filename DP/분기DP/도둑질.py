def solution(money):
    d1 = [0] * len(money)
    d1[0] = money[0]
    d1[1] = d1[0]
    for i in range(2, len(money) - 1):
        d1[i] = max(d1[i - 1], d1[i - 2] + money[i])
        
    d2 = [0] * len(money)
    d2[1] = money[1]
    for i in range(2, len(money)):
        d2[i] = max(d2[i - 1], d2[i - 2] + money[i])
    
    return max(d1[-2], d2[-1])