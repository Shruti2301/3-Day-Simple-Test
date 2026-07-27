def loop_test(nums):
    for i in range(len(nums)):
        print(f"In Outer Loop (i): Index:{i}, Value:{nums[i]}")

        for j in range(i+1, len(nums)):
            print(f"In Inner Loop (j): Index:{j}, Value:{nums[j]}")
            sum = nums[i] + nums[j]
            print(f"SUM: Value at i={i} + Value at j={j} = {sum} ")
        
    
nums = [9,5,7,5,4,8,3,2,1]
print(loop_test(nums))