def dig_pow(n, p):
    nums = [int(i) for i in str(n)]
    result = 0
    for i in range(len(nums)):
        result += pow(nums[i], p+i)
    result /= n
    if (result % 1 == 0):
        return result
    else:
        return -1


print(dig_pow(89, 1) == 1)
print(dig_pow(92, 1) == -1)
print(dig_pow(46288, 3) == 51)
