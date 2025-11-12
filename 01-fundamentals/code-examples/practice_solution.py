# practice_solution.py
# 🎯 SOLUTION: Product class for e-commerce testing
# This is the complete solution - try the exercise first before looking!

class Product:
    """
    A class to represent a product in an e-commerce store
    """
    
    def __init__(self, product_id, name, price, stock):
        """
        Initialize a new product
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            price (float): Price of the product
            stock (int): Number of items in stock
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def apply_discount(self, discount_percent):
        """
        Apply a discount to the product price
        
        Args:
            discount_percent (float): Discount percentage (e.g., 10 for 10% off)
        
        Returns:
            float: New discounted price
        """
        # Calculate the discount amount
        discount_amount = self.price * (discount_percent / 100)
        
        # Calculate new price
        new_price = self.price - discount_amount
        
        # Alternative shorter way:
        # new_price = self.price * (1 - discount_percent/100)
        
        # Update the price
        self.price = new_price
        
        return new_price
    
    def is_available(self):
        """
        Check if product is in stock
        
        Returns:
            bool: True if stock > 0, False otherwise
        """
        return self.stock > 0
    
    def display_details(self):
        """
        Display product details in a nice format
        """
        print(f"\n{'='*50}")
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price:.2f}")
        print(f"Stock: {self.stock} units")
        print(f"Available: {'Yes ✓' if self.is_available() else 'No ✗'}")
        print(f"{'='*50}")


# ============================================================
# TESTING THE SOLUTION
# ============================================================

def test_product_class():
    """Test function to demonstrate the Product class"""
    
    print("="*60)
    print("🧪 TESTING THE PRODUCT CLASS")
    print("="*60)
    
    # Test 1: Create products
    print("\n✅ Test 1: Creating products")
    print("-"*60)
    phone = Product("P001", "iPhone 15", 79999, 10)
    laptop = Product("P002", "MacBook Pro", 199999, 5)
    headphones = Product("P003", "Sony WH-1000XM5", 29999, 0)
    shoes = Product("P004", "Nike Air Max", 8999, 25)
    print("✓ 4 products created successfully!")
    
    # Test 2: Display details
    print("\n✅ Test 2: Displaying product details")
    print("-"*60)
    phone.display_details()
    laptop.display_details()
    headphones.display_details()
    shoes.display_details()
    
    # Test 3: Check availability
    print("\n✅ Test 3: Checking availability")
    print("-"*60)
    print(f"iPhone available: {phone.is_available()} (Stock: {phone.stock})")
    print(f"MacBook available: {laptop.is_available()} (Stock: {laptop.stock})")
    print(f"Headphones available: {headphones.is_available()} (Stock: {headphones.stock})")
    print(f"Shoes available: {shoes.is_available()} (Stock: {shoes.stock})")
    
    # Test 4: Apply discounts
    print("\n✅ Test 4: Applying discounts")
    print("-"*60)
    
    print(f"\nApplying 10% discount on iPhone:")
    original_price = phone.price
    discounted_price = phone.apply_discount(10)
    print(f"  Original price: ₹{original_price:.2f}")
    print(f"  After discount: ₹{discounted_price:.2f}")
    print(f"  You saved: ₹{original_price - discounted_price:.2f}")
    
    print(f"\nApplying 15% discount on MacBook:")
    original_price = laptop.price
    discounted_price = laptop.apply_discount(15)
    print(f"  Original price: ₹{original_price:.2f}")
    print(f"  After discount: ₹{discounted_price:.2f}")
    print(f"  You saved: ₹{original_price - discounted_price:.2f}")
    
    print(f"\nApplying 20% discount on Shoes:")
    original_price = shoes.price
    discounted_price = shoes.apply_discount(20)
    print(f"  Original price: ₹{original_price:.2f}")
    print(f"  After discount: ₹{discounted_price:.2f}")
    print(f"  You saved: ₹{original_price - discounted_price:.2f}")
    
    # Test 5: Complex scenario - Shopping cart
    print("\n✅ Test 5: Building a shopping cart")
    print("-"*60)
    
    cart = [phone, laptop, shoes]
    cart_total = sum(product.price for product in cart)
    
    print("\n🛒 Your Shopping Cart:")
    for i, product in enumerate(cart, 1):
        print(f"{i}. {product.name} - ₹{product.price:.2f}")
    
    print(f"\n💰 Cart Total: ₹{cart_total:.2f}")
    
    # Test 6: Stock management
    print("\n✅ Test 6: Stock management")
    print("-"*60)
    
    print(f"\nBefore purchase:")
    print(f"  iPhone stock: {phone.stock}")
    
    # Simulate a purchase
    if phone.is_available():
        phone.stock -= 1
        print(f"\nAfter purchasing 1 iPhone:")
        print(f"  iPhone stock: {phone.stock}")
        print(f"  Still available: {phone.is_available()}")
    
    print("\n" + "="*60)
    print("🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
    print("="*60)
    
    # Key learnings
    print("\n💡 KEY LEARNINGS:")
    print("-"*60)
    print("✅ Created a Product CLASS (blueprint)")
    print("✅ Created multiple product OBJECTS (real products)")
    print("✅ Each object has its own independent data")
    print("✅ Methods work on each object independently")
    print("✅ Easy to manage multiple products")
    print("✅ Adding new products? Just create new objects!")
    print("✅ Need new feature? Add method to class once!")


# ============================================================
# BONUS: Enhanced version with additional features
# ============================================================

class EnhancedProduct(Product):
    """
    Enhanced version of Product with more features
    This demonstrates how you can extend a class
    """
    
    def __init__(self, product_id, name, price, stock, category, brand):
        # Call the parent class constructor
        super().__init__(product_id, name, price, stock)
        self.category = category
        self.brand = brand
        self.ratings = []
    
    def add_rating(self, rating):
        """Add a customer rating (1-5 stars)"""
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            print(f"✓ Rating added: {rating} stars")
        else:
            print("✗ Rating must be between 1 and 5")
    
    def get_average_rating(self):
        """Calculate average rating"""
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
    
    def display_details(self):
        """Enhanced display with category, brand, and ratings"""
        super().display_details()
        print(f"Category: {self.category}")
        print(f"Brand: {self.brand}")
        if self.ratings:
            avg_rating = self.get_average_rating()
            print(f"Average Rating: {avg_rating:.1f} ⭐ ({len(self.ratings)} reviews)")
        else:
            print("Average Rating: No ratings yet")
        print(f"{'='*50}")


def demo_enhanced_product():
    """Demonstrate the enhanced product class"""
    print("\n\n" + "="*60)
    print("🌟 BONUS: ENHANCED PRODUCT CLASS")
    print("="*60)
    
    # Create enhanced products
    phone = EnhancedProduct("P001", "iPhone 15", 79999, 10, "Electronics", "Apple")
    
    # Add some ratings
    print("\nAdding customer ratings:")
    phone.add_rating(5)
    phone.add_rating(4)
    phone.add_rating(5)
    phone.add_rating(3)
    
    # Display details
    print("\nProduct with ratings:")
    phone.display_details()


# ============================================================
# Run everything
# ============================================================

if __name__ == "__main__":
    test_product_class()
    demo_enhanced_product()
    
    print("\n" + "="*60)
    print("🎓 Congratulations! You now understand:")
    print("="*60)
    print("✅ How to create a class")
    print("✅ How to define properties (__init__)")
    print("✅ How to create methods")
    print("✅ How to create and use objects")
    print("✅ Why OOP makes code better!")
    print("\n🚀 You're ready for the next topic!")
    print("="*60)