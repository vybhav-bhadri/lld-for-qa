# practice_exercise.py
# 🎯 PRACTICE EXERCISE: Create a Product class for e-commerce testing
# This is YOUR turn to write code!

"""
INSTRUCTIONS:
-----------
Create a Product class for an e-commerce application with:

1. Properties (in __init__):
   - product_id (string)
   - name (string)
   - price (float)
   - stock (integer)

2. Methods to implement:
   - apply_discount(discount_percent): Reduce price by given percentage, return new price
   - is_available(): Return True if stock > 0, else False
   - display_details(): Print product details nicely

After completing the class, test it with the code at the bottom!
"""

class Product:
    """
    A class to represent a product in an e-commerce store
    Complete the methods below!
    """
    
    def __init__(self, product_id, name, price, stock):
        """
        Initialize a new product
        
        TODO: Store all parameters as instance variables
        Hint: self.property_name = parameter_name
        """
        # YOUR CODE HERE
        pass
    
    def apply_discount(self, discount_percent):
        """
        Apply a discount to the product price
        
        Args:
            discount_percent (float): Discount percentage (e.g., 10 for 10% off)
        
        Returns:
            float: New discounted price
        
        TODO: Calculate and return the discounted price
        Hint: new_price = self.price * (1 - discount_percent/100)
        """
        # YOUR CODE HERE
        pass
    
    def is_available(self):
        """
        Check if product is in stock
        
        Returns:
            bool: True if stock > 0, False otherwise
        
        TODO: Return True if stock is greater than 0
        """
        # YOUR CODE HERE
        pass
    
    def display_details(self):
        """
        Display product details in a nice format
        
        TODO: Print product_id, name, price, stock, and availability
        Hint: Use f-strings and self.property_name
        """
        # YOUR CODE HERE
        pass


# ============================================================
# TEST YOUR CLASS HERE (Don't modify this section)
# ============================================================

def test_product_class():
    """
    Test function to check if your Product class works correctly
    Uncomment the code below after completing the class!
    """
    
    print("="*60)
    print("🧪 TESTING YOUR PRODUCT CLASS")
    print("="*60)
    
    # Uncomment below after completing the class
    
    # # Test 1: Create products
    # print("\n✅ Test 1: Creating products")
    # phone = Product("P001", "iPhone 15", 79999, 10)
    # laptop = Product("P002", "MacBook Pro", 199999, 5)
    # headphones = Product("P003", "Sony WH-1000XM5", 29999, 0)
    # print("Products created successfully!")
    
    # # Test 2: Display details
    # print("\n✅ Test 2: Displaying product details")
    # phone.display_details()
    # laptop.display_details()
    # headphones.display_details()
    
    # # Test 3: Check availability
    # print("\n✅ Test 3: Checking availability")
    # print(f"iPhone available: {phone.is_available()}")  # Should be True
    # print(f"MacBook available: {laptop.is_available()}")  # Should be True
    # print(f"Headphones available: {headphones.is_available()}")  # Should be False
    
    # # Test 4: Apply discounts
    # print("\n✅ Test 4: Applying discounts")
    # original_price = phone.price
    # discounted_price = phone.apply_discount(10)  # 10% off
    # print(f"iPhone original price: ₹{original_price}")
    # print(f"iPhone after 10% discount: ₹{discounted_price}")
    
    # original_price = laptop.price
    # discounted_price = laptop.apply_discount(15)  # 15% off
    # print(f"MacBook original price: ₹{original_price}")
    # print(f"MacBook after 15% discount: ₹{discounted_price}")
    
    # print("\n" + "="*60)
    # print("🎉 ALL TESTS COMPLETED!")
    # print("="*60)
    
    pass


# ============================================================
# HINTS (Uncomment if you need help!)
# ============================================================

"""
HINT 1 - __init__ method:
-------------------------
def __init__(self, product_id, name, price, stock):
    self.product_id = product_id
    self.name = name
    self.price = price
    self.stock = stock

HINT 2 - apply_discount method:
-------------------------------
def apply_discount(self, discount_percent):
    discount_amount = self.price * (discount_percent / 100)
    new_price = self.price - discount_amount
    return new_price

Or shorter version:
    return self.price * (1 - discount_percent/100)

HINT 3 - is_available method:
-----------------------------
def is_available(self):
    return self.stock > 0

HINT 4 - display_details method:
--------------------------------
def display_details(self):
    print(f"\\nProduct ID: {self.product_id}")
    print(f"Name: {self.name}")
    print(f"Price: ₹{self.price}")
    print(f"Stock: {self.stock}")
    print(f"Available: {self.is_available()}")
"""

# ============================================================
# Run the tests
# ============================================================

if __name__ == "__main__":
    print("""
    📚 EXERCISE: Create a Product Class
    ===================================
    
    Your task:
    1. Complete the __init__ method
    2. Complete the apply_discount method
    3. Complete the is_available method
    4. Complete the display_details method
    
    Then uncomment the test code in test_product_class() function
    and run this file!
    
    Need help? Scroll down to see hints!
    
    Good luck! 🚀
    """)
    
    test_product_class()