Task-1 
You are the lead developer for a new clothing store. The manager wants a way 
to quickly calculate the final price of items when a customer has a discount 
coupon. 
Your Task: Write a Python program that does the following: 
1. Define a function named apply_discount. 
2. Give it two parameters: original_price and coupon_val. 
3. Inside the function, calculate the final price by subtracting the coupon 
from the original price. 
4. Use the return keyword to send that final price back. 
5. Call your function twice with different numbers (e.g., a 50/- shirt with a 
10/- coupon) and print the results to the console. 
Task-2 
Analyze a raw server log list containing strings, integers, and errors (e.g., 
["200", 404, "error"]) by using filter, map, set, and sum to extract only the 
numeric codes, find the most severe (maximum) error, and calculate the average 
status value—all without using a single for loop. 
Log_data = ["200", "404", 500, "200", "timeout", "301", 500, "error", "200", 
404] 


# ===== TASK 1: Clothing Store Discount =====

def apply_discount(original_price, coupon_val):
    final_price = original_price - coupon_val
    return final_price

print("=== Clothing Store ===")
print(f"Shirt  500/- - 10/- coupon  = {apply_discount(500, 10)}/-")
print(f"Jeans 1200/- - 250/- coupon = {apply_discount(1200, 250)}/-")


# ===== TASK 2: Server Log Analysis =====

log_data = ["200", "404", 500, "200", "timeout", "301", 500, "error", "200", 404]

print("\n=== Server Log Analysis ===")

# Step 1: Filter only numeric values (both int and numeric strings)
numeric_logs = list(filter(lambda x: str(x).isdigit(), log_data))
print(f"Numeric entries only : {numeric_logs}")

# Step 2: Map all to integers
int_logs = list(map(int, numeric_logs))
print(f"Converted to int     : {int_logs}")

# Step 3: Unique codes using set
unique_codes = set(int_logs)
print(f"Unique status codes  : {unique_codes}")

# Step 4: Most severe (maximum) error code
max_code = max(int_logs)
print(f"Most severe code     : {max_code}")

# Step 5: Average status value
average = sum(int_logs) / len(int_logs)
print(f"Average status value : {average:.2f}")
