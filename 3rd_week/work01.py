shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    result=0
    prices_len = len(prices)
    coupons_len = len(coupons)
    for x in range(coupons_len - 1):
        for y in range(coupons_len - x - 1):
            if coupons[y] < coupons[y+1]:
                coupons[y], coupons[y+1] = coupons[y+1], coupons[y]
    for x in range(prices_len - 1):
        for y in range(prices_len - x - 1):
            if prices[y] < prices[y+1]:
                prices[y], prices[y+1] = prices[y+1], prices[y]
    if coupons_len<=prices_len:
        endpoint=0
        for x in range(coupons_len):
            result+=prices[x]*(100-coupons[x])/100
            endpoint+=1
        for x in range(endpoint,prices_len,1):
            result+=prices[x]
    elif coupons_len>prices_len:
        for x in range(prices_len):
            result+=prices[x]*(100-coupons[x])/100

    return result


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
