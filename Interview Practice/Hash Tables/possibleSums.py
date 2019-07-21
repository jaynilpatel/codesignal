def possibleSums(coins, quantity):
    poss_sums = {0}
    
    for coin, quant in zip(coins, quantity):
        d = {}
        for i in range(1, quant+1):
            for sum in poss_sums:
                temp = sum + i * coin
                if temp not in poss_sums:
                    d[temp] = temp
        poss_sums.update(d)
    
    return len(poss_sums) - 1

coins = [10, 50, 100] 
quantity = [1, 2, 1]




print(possibleSums(coins, quantity))