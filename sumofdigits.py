# Given a non-negative integer n, return the sum of all its individual digits
# Goal : Extract and sum every digit in O(d) time ( where d is the number of digits in d) without needing high memory operation

# Mathematical Approach 
# 1. Last Digit can be extracted using n%10
# 2. Remaining Digit can be isolated by removing the last digit using integer division (n//10)
# 3. Repeat this process until n becomes 0 

def sum_of_digit_math(num:int) -> int:
    # Special Case : 0 has a sum of 0
    if num == 0:
        return 0
    
    total_sum = 0
    # while number is positive
    while num > 0: 
        # Extract the rightmost digit using modulo parameter
        digit = num % 10 
        total_sum = total_sum + digit
        
        # Rename the rightmost digit using integer division
        num //= 10
        
    # Return Total sum
    return total_sum
        
print(sum_of_digit_math(4820))