nums = [25,34,6,7,899,90]
print(nums)

n= nums[4]
print(n)

m = nums[0:]
print(m)

names = ['jenny','jeron','plutonium','gaylien']
print(names)

values = [nums,names]
print(values)


nums.append(90)#adds number at the end of the list
print(nums)

nums.insert(2,56)#inserts number in between
print(nums)


nums.remove(90)
print(nums)
nums.pop(4)#removes element using index number
print(nums)

names.pop()#if index number is not specified it removes the last element in the list
print(names)

del nums[2:]#del deletes mulitple values in the list
print(nums)

nums.extend([45,56,67,78,89,78,90,34])#adds mulitple values in the list
print(nums)

print(max(nums))#finds the maximum number of the list
print(min(nums))#finds the minumum number of the list

print(sum(nums))
nums.sort()#sotrs the numbers from smaller to bigger
print(nums)
