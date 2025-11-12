# complete_test_framework.py
# A mini test automation framework using Classes!
# This shows how QA engineers can build professional frameworks with OOP

class TestCase:
    """
    Blueprint for creating test cases
    This is how real test frameworks like pytest and unittest work!
    """
    
    # Class variables - shared by ALL test cases
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    def __init__(self, test_id, description, test_type):
        """
        Initialize a new test case
        test_type can be: "smoke", "regression", "sanity", "integration"
        """
        self.test_id = test_id
        self.description = description
        self.test_type = test_type
        self.status = "Not Run"
        self.actual_result = None
        self.expected_result = None
        
        # Every time a test is created, increment the total count
        TestCase.total_tests += 1
    
    def execute(self, actual, expected):
        """
        Execute the test case
        Compare actual result with expected result
        """
        self.actual_result = actual
        self.expected_result = expected
        
        print(f"\n{'='*60}")
        print(f"🧪 Executing: {self.test_id}")
        print(f"📝 Description: {self.description}")
        print(f"🏷️  Type: {self.test_type}")
        print(f"✓ Expected: {expected}")
        print(f"⚡ Actual: {actual}")
        
        if actual == expected:
            self.status = "PASSED ✓"
            TestCase.passed_tests += 1
            print(f"📊 Status: {self.status}")
        else:
            self.status = "FAILED ✗"
            TestCase.failed_tests += 1
            print(f"📊 Status: {self.status}")
    
    def get_report(self):
        """Get individual test report"""
        return f"{self.test_id}: {self.status}"
    
    @classmethod
    def print_summary(cls):
        """
        Print summary of ALL tests
        @classmethod means this method works on the class itself, not individual objects
        """
        print(f"\n{'='*60}")
        print("📋 TEST EXECUTION SUMMARY")
        print(f"{'='*60}")
        print(f"Total Tests: {cls.total_tests}")
        print(f"Passed: {cls.passed_tests} ✓")
        print(f"Failed: {cls.failed_tests} ✗")
        
        if cls.total_tests > 0:
            pass_rate = (cls.passed_tests / cls.total_tests) * 100
            print(f"Pass Rate: {pass_rate:.2f}%")
            
            if pass_rate == 100:
                print("🎉 All tests passed! Excellent work!")
            elif pass_rate >= 80:
                print("👍 Good pass rate, but check failed tests")
            else:
                print("⚠️  Many tests failed, needs attention!")
        
        print(f"{'='*60}")
    
    @classmethod
    def reset_counters(cls):
        """Reset all counters - useful when running multiple test suites"""
        cls.total_tests = 0
        cls.passed_tests = 0
        cls.failed_tests = 0


# ============================================================
# DEMO: Using our Test Framework
# ============================================================

print("🚀 QA TEST AUTOMATION FRAMEWORK - POWERED BY CLASSES!")
print("="*60)

# ============================================================
# Login Module Tests
# ============================================================
print("\n📦 MODULE: Login Tests")
print("-"*60)

test1 = TestCase("TC001", "Login with valid credentials", "smoke")
test2 = TestCase("TC002", "Login with invalid password", "regression")
test3 = TestCase("TC003", "Login with empty username", "regression")

# Execute login tests
test1.execute(actual="Login Success", expected="Login Success")
test2.execute(actual="Login Failed", expected="Login Failed")
test3.execute(actual="Login Failed", expected="Login Failed")

# ============================================================
# Cart Module Tests
# ============================================================
print("\n📦 MODULE: Shopping Cart Tests")
print("-"*60)

test4 = TestCase("TC004", "Add item to cart", "smoke")
test5 = TestCase("TC005", "Remove item from cart", "regression")
test6 = TestCase("TC006", "Update item quantity", "regression")

test4.execute(actual="Item Added", expected="Item Added")
test5.execute(actual="Item Not Removed", expected="Item Removed")  # This will FAIL
test6.execute(actual="Quantity Updated", expected="Quantity Updated")

# ============================================================
# Payment Module Tests
# ============================================================
print("\n📦 MODULE: Payment Tests")
print("-"*60)

test7 = TestCase("TC007", "Payment with credit card", "smoke")
test8 = TestCase("TC008", "Payment with insufficient balance", "regression")

test7.execute(actual="Payment Success", expected="Payment Success")
test8.execute(actual="Payment Failed", expected="Payment Failed")

# ============================================================
# Print Summary and Individual Reports
# ============================================================

# Print overall summary
TestCase.print_summary()

# Print individual test reports
print(f"\n📝 Individual Test Reports:")
print("-"*60)
all_tests = [test1, test2, test3, test4, test5, test6, test7, test8]
for test in all_tests:
    print(test.get_report())

print("\n" + "="*60)
print("💡 KEY LEARNINGS:")
print("="*60)
print("✅ Created a TestCase CLASS - the blueprint")
print("✅ Created 8 test OBJECTS from that blueprint")
print("✅ Each test manages its own data independently")
print("✅ Class variables track overall statistics")
print("✅ Easy to add new tests - just create new objects!")
print("✅ Easy to add new features - modify class once!")
print("="*60)
print("\n🎯 This is how real frameworks like pytest work!")
print("   You just learned the foundation of test automation! 🚀")