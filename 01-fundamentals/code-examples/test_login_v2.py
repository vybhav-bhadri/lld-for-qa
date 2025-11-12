# test_login_v2.py - The OOP Way
# This demonstrates how CLASSES and OBJECTS solve the problem

class User:
    """
    This is a blueprint for creating users.
    It defines WHAT a user IS and WHAT a user CAN DO.
    """
    
    def __init__(self, username, password, phone, city):
        """
        This is called when you CREATE a new user object.
        It sets up the user's data.
        __init__ is called a "constructor" - it constructs/initializes the object
        """
        self.username = username
        self.password = password
        self.phone = phone
        self.city = city
        self.login_result = None
    
    def test_login(self, entered_password):
        """
        This is what a user CAN DO - test their login!
        This is called a "method" - a function inside a class
        """
        print(f"\nTesting login for {self.username}")
        
        if self.username and entered_password == self.password:
            self.login_result = "Success"
            print(f"✓ Test Passed: {self.username} logged in successfully")
            return True
        else:
            self.login_result = "Failed"
            print(f"✗ Test Passed: Login correctly failed")
            return False
    
    def display_info(self):
        """Users can display their info"""
        print(f"User: {self.username}, City: {self.city}, Phone: {self.phone}")


print("LOGIN TESTING - WITH CLASSES (OOP Way)")
print("="*60)

# Now CREATE objects (actual users) from the blueprint
# This is SO EASY now!

user1 = User("rajesh@gmail.com", "Rajesh@123", "9876543210", "Mumbai")
user2 = User("priya@gmail.com", "Priya@123", "9876543211", "Delhi")
user3 = User("amit@gmail.com", "Amit@123", "9876543212", "Pune")

# Test them all
user1.test_login("Rajesh@123")  # Correct password
user2.test_login("wrong_password")  # Wrong password
user3.test_login("")  # Empty password

print("\n" + "="*60)
print("BENEFITS OF USING CLASSES:")
print("="*60)
print(" Defined User structure ONCE in the class")
print(" Created 3 users with just 3 lines")
print(" Each user manages its own data")
print(" Want 50 users? Just 50 lines (not 600!)")
print(" Want to add OTP field? Add it ONCE in class")
print(" Test logic in ONE place, works for ALL users")
print("="*60)

# Display user info
print("\nUser Information:")
user1.display_info()
user2.display_info()
user3.display_info()