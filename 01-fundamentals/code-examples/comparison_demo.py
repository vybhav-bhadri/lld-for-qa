# comparison_demo.py
# Let's see the difference side by side
# WITHOUT Classes vs WITH Classes

print("="*70)
print("COMPARISON: WITHOUT CLASSES vs WITH CLASSES")
print("="*70)

print("\n" + "🔴 WITHOUT CLASSES (Old Way - Problem):")
print("-"*70)

# Scenario: Testing login for 3 users WITHOUT classes
username1 = "user1@test.com"
password1 = "pass1"
result1 = "Not Tested"

username2 = "user2@test.com"
password2 = "pass2"
result2 = "Not Tested"

username3 = "user3@test.com"
password3 = "pass3"
result3 = "Not Tested"

# Testing logic repeated 3 times!
if username1 and password1:
    result1 = "Passed"
if username2 and password2:
    result2 = "Passed"
if username3 and password3:
    result3 = "Passed"

print(f"✓ Created 3 users")
print(f"\n📊 Statistics:")
print(f"   Variables created: 9 (3 per user)")
print(f"   Lines of code: ~15")
print(f"   Logic repetition: 3 times")
print(f"\n❌ Problems:")
print(f"   • Need to add email field? Add 3 more variables")
print(f"   • Need to change test logic? Change 3 places")
print(f"   • Need 50 users? 150 variables and 200+ lines!")
print(f"   • Bug in one test? Might exist in other 2 copies")
print(f"   • Code is messy and hard to maintain")

print("\n" + "="*70)
print("🟢 WITH CLASSES (OOP Way - Solution):")
print("-"*70)

class LoginTest:
    """Blueprint for login tests"""
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.result = "Not Tested"
    
    def run_test(self):
        """Test login functionality"""
        if self.username and self.password:
            self.result = "Passed"
            print(f"✓ {self.username}: {self.result}")

# Create 3 test objects - SO EASY!
test1 = LoginTest("user1@test.com", "pass1")
test2 = LoginTest("user2@test.com", "pass2")
test3 = LoginTest("user3@test.com", "pass3")

# Run all tests with ONE loop - ELEGANT!
print(f"✓ Created 3 test objects")
print(f"\nRunning tests:")
for test in [test1, test2, test3]:
    test.run_test()

print(f"\n📊 Statistics:")
print(f"   Class defined: 1 (reusable blueprint)")
print(f"   Objects created: 3")
print(f"   Lines of code: ~8")
print(f"   Logic repetition: 0 (defined once!)")
print(f"\n✅ Benefits:")
print(f"   • Need to add email field? Add 1 line in class")
print(f"   • Need to change test logic? Change 1 place")
print(f"   • Need 50 users? Just 50 lines (not 600!)")
print(f"   • Fix a bug once, all tests benefit")
print(f"   • Code is clean and maintainable")

print("\n" + "="*70)
print("📈 SCALABILITY COMPARISON")
print("="*70)

print("\nFor 10 users:")
print("  Without Classes: ~50 variables, ~40 lines of logic")
print("  With Classes:    10 objects, same class (no extra code!)")

print("\nFor 100 users:")
print("  Without Classes: ~500 variables, ~400 lines (NIGHTMARE!)")
print("  With Classes:    100 objects, same class (EASY!)")

print("\nFor 1000 users:")
print("  Without Classes: 🤯 IMPOSSIBLE to maintain")
print("  With Classes:    1000 objects, same class (STILL EASY!)")

print("\n" + "="*70)
print("🎯 REAL-WORLD EXAMPLE: WhatsApp")
print("="*70)
print("\nWhatsApp has 2+ billion users!")
print("Without Classes: Would need 2+ billion sets of variables 😱")
print("With Classes:    One User class, 2+ billion User objects ✅")
print("\nThis is why EVERY modern app uses Object-Oriented Programming!")

print("\n" + "="*70)
print("💡 KEY TAKEAWAY")
print("="*70)
print("""
Classes and Objects are NOT about making things complicated.
They're about making things SIMPLER when dealing with:
  • Multiple similar items (users, products, tests)
  • Adding new features
  • Maintaining large codebases
  • Scaling from 3 to 3000 to 3 million items

Remember:
  CLASS = Blueprint/Template (define ONCE)
  OBJECT = Real thing from blueprint (create MANY)

It's like:
  • Cookie cutter (class) vs Cookies (objects)
  • House plan (class) vs Houses (objects)
  • Car design (class) vs Cars (objects)
""")
print("="*70)