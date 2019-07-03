def depositProfit(deposit, rate, threshold):
    if threshold <= deposit:
        return 0
    deposit = deposit + (rate*0.01)*deposit
    return 1 + depositProfit(deposit, rate, threshold)


deposit = 1
rate = 100
threshold = 64

print(depositProfit(deposit, rate, threshold))