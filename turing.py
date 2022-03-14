def find_max(nums):
       max_num = float("-inf") # smaller than all other numbers
       print("max: ",max_num)
       print("nums: ",nums)
       for num in nums:
              if num > max_num:
                     max_num=nums
               # (Fill in the missing line here)
       return max_num

a=find_max(float(5))

print(a)
