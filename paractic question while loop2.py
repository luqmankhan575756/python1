# Q3
n = 1
m = 3
while n <= 10 :
    p = m*n
    print(p)
    n += 1
  
  
    #Q4
    nums = [1,4,9,16,25,36,49,64,81,100]
    idx = 0
    while idx < len(nums) :
        print(nums[idx])
        idx += 1

#Q5

nums = [1,4,9,16,25,36,49,64,81,100]
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index",i)
        i += 1