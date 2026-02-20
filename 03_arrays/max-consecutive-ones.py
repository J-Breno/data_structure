def max_consecutive_ones(nums):
    maior = 0
    contador = 0

    for num in nums:
        if num == 1:
            contador += 1
            maior = max(maior, contador)
        else:
            contador = 0

    return maior


print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(max_consecutive_ones([1, 0, 1, 1, 0, 1]))