# test_login_v1.py
# Ravi's first attempt - Testing login WITHOUT using classes
# This demonstrates the problem with traditional programming approach

# User 1 - Valid login
username1 = "rajesh@gmail.com"
password1 = "Rajesh@123"
phone1 = "9876543210"
city1 = "Mumbai"
login_result1 = None

print(f"Testing login for {username1}")
if username1 and password1:
    login_result1 = "Success"
    print(f"✓ Test Passed: {username1} logged in successfully")
else:
    login_result1 = "Failed"
    print(f"✗ Test Failed")

# User 2 - Invalid password
username2 = "priya@gmail.com"
password2 = "wrong_password"
phone2 = "9876543211"
city2 = "Delhi"
login_result2 = None

print(f"\nTesting login for {username2}")
if username2 and password2 == "Priya@123":  # correct password
    login_result2 = "Success"
    print(f"✓ Test Passed: {username2} logged in successfully")
else:
    login_result2 = "Failed"
    print(f"✓ Test Passed: Login correctly failed for wrong password")

# User 3 - Empty password
username3 = "amit@gmail.com"
password3 = ""
phone3 = "9876543212"
city3 = "Pune"
login_result3 = None

print(f"\nTesting login for {username3}")
if username3 and password3:
    login_result3 = "Success"
    print(f"✓ Test Passed: {username3} logged in successfully")
else:
    login_result3 = "Failed"
    print(f"✓ Test Passed: Login correctly failed for empty password")

print("\n" + "="*60)
print("Problems with this approach:")
print("- Need 12 variables for just 3 users!")
print("- Logic is repeated 3 times")
print("- Adding new field (like OTP) means adding 3+ more variables")
print("- Imagine doing this for 50 users... nightmare!")
print("="*60)