def calc_sum(n):
    if(n == 0):
        return
    return calc_sum(n-1)+n
    sum = calc_sum(10)
    print(sum)