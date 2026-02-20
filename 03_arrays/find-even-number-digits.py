def find_even_number_digits(nums):
    return sum(1 for num in nums if len(str(num)) % 2 == 0)


print(find_even_number_digits([555,901,482,1771]))