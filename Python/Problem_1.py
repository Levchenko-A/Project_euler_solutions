def sum_of_3_5_muliples_upto_num(num):
    ''' Takes integer num and returns sum of all the multiples of 3 or 5 below that integer'''
    multiples = [n for n in range(num) if ((n % 3 == 0) or (n % 5 == 0))]
    return sum(multiples)

print(sum_of_3_5_muliples_upto_num(1000))
