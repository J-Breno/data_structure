def dot_product_two_arrays(nums1, nums2):
    return sum(a * b for a, b in zip(nums1, nums2))


print(dot_product_two_arrays([0,1,0,0,2,0,0], [1,0,0,0,3,0,4]))