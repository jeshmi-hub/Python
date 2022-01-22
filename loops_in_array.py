heights = [189, 170, 189, 163, 175, 178, 173, 174, 183, 180, 170, 182, 188, 185, 191]
ages = [45, 55, 67, 45, 43, 56, 14, 56, 34, 45, 46, 56, 78, 90, 76]

cnt = 0
for height in heights:
    if height > 188:
        cnt += 1
print(cnt)


import numpy as np
heights_arr = np.array(heights)
print((heights_arr > 188).sum())
print(heights_arr.size)
print(heights_arr.shape)


heights_and_ages = heights + ages
heights_and_ages_arr =  np.array(heights_and_ages)
print(heights_and_ages_arr.reshape(3,10))
print(heights_arr.dtype)



