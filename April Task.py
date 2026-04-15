You are the lead developer for a new clothing store. The manager wants a way to quickly 
calculate the final price of items when a customer has a discount coupon. 
Your Task: Write a Python program that does the following: 
1. Define a function named apply_discount. 
2. Give it two parameters: original_price and coupon_val. 
3. Inside the function, calculate the final price by subtracting the coupon from the 
original price. 
4. Use the return keyword to send that final price back. 
5. Call your function twice with different numbers (e.g., a 50/- shirt with a 10/- 
coupon) and print the results to the console.


def apply_discount(original_price, coupon_val):
    final_price = original_price - coupon_val
    return final_price

print(apply_discount(50, 10))   # Shirt: 50/- with 10/- coupon
print(apply_discount(120, 25))  # Jeans: 120/- with 25/- coupon
