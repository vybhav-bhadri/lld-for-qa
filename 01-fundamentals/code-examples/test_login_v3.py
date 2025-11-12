# test_login_v3.py - Adding new features is EASY with Classes!
# Manager said: "Add OTP verification"
# With classes, we just modify ONE place!

import random

class User:
    """Same blueprint, but now with OTP!"""
    
    def __init__(self, username, password, phone, city):
        self.username = username
        self.password = password
        self.phone = phone
        self.city = city
        self.otp = None  # NEW FIELD - Added in ONE place!
        self.login_result = None
    
    def generate_otp(self):
        """
        NEW FEATURE - Added in ONE place!
        All users automatically get this capability
        """
        self.otp = random.randint(100000, 999999)
        print(f"📱 OTP generated for {self.username}: {self.otp}")
        return self.otp
    
    def test_login_with_otp(self, entered_password, entered_otp):
        """
        UPDATED FEATURE - Modified in ONE place!
        Now login requires both password and OTP
        """
        print(f"\nTesting login for {self.username}")
        print(f"Entered Password: {'*' * len(entered_password)}")
        print(f"Entered OTP: {entered_otp}")
        
        if entered_password == self.password and entered_otp == self.otp:
            self.login_result = "Success"
            print(f"✓ Test Passed: {self.username} logged in with OTP")
            return True
        else:
            self.login_result = "Failed"
            if entered_password != self.password:
                print(f"✗ Test Failed: Invalid password")
            elif entered_otp != self.otp:
                print(f"✗ Test Failed: Invalid OTP")
            return False
    
    def display_info(self):
        """Display user information"""
        print(f"User: {self.username}, City: {self.city}, Phone: {self.phone}")


print("LOGIN TESTING WITH OTP - EASY TO ADD NEW FEATURES!")
print("="*60)

# ALL existing users automatically get new features!
# No need to modify user1, user2, user3 creation code!

user1 = User("rajesh@gmail.com", "Rajesh@123", "9876543210", "Mumbai")
user2 = User("priya@gmail.com", "Priya@123", "9876543211", "Delhi")
user3 = User("amit@gmail.com", "Amit@123", "9876543212", "Pune")

# Test Scenario 1: Valid password and OTP
print("\n📋 Test Scenario 1: Valid credentials with correct OTP")
print("-" * 60)
otp1 = user1.generate_otp()
user1.test_login_with_otp("Rajesh@123", otp1)

# Test Scenario 2: Valid password but wrong OTP
print("\n📋 Test Scenario 2: Valid password but wrong OTP")
print("-" * 60)
otp2 = user2.generate_otp()
user2.test_login_with_otp("Priya@123", 999999)  # Wrong OTP

# Test Scenario 3: Wrong password with correct OTP
print("\n📋 Test Scenario 3: Wrong password with correct OTP")
print("-" * 60)
otp3 = user3.generate_otp()
user3.test_login_with_otp("wrong_password", otp3)  # Wrong password

print("\n" + "="*60)
print("THE POWER OF CLASSES:")
print("="*60)
print(" Added OTP feature by changing code in ONE place (the class)")
print(" All users automatically got the new feature")
print(" No need to modify user1, user2, user3 creation")
print(" Old way would need modifying 50+ places for 50 users")
print(" This way? Just modify the class ONCE!")
print("="*60)