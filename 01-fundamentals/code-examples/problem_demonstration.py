# problem_demonstration.py
# Demonstrating what happens with raw programming
# Managing e-commerce cart without using classes

print("E-COMMERCE CART - WITHOUT USING CLASSES")
print("="*60)

# Testing 5 products in e-commerce cart
product1_name = "Samsung TV"
product1_price = 45000
product1_quantity = 1

product2_name = "Sony Headphones"
product2_price = 3500
product2_quantity = 2

product3_name = "Dell Laptop"
product3_price = 65000
product3_quantity = 1

product4_name = "iPhone"
product4_price = 85000
product4_quantity = 1

product5_name = "Nike Shoes"
product5_price = 5000
product5_quantity = 2

# Calculate total - repeating same logic!
total1 = product1_price * product1_quantity
total2 = product2_price * product2_quantity
total3 = product3_price * product3_quantity
total4 = product4_price * product4_quantity
total5 = product5_price * product5_quantity

cart_total = total1 + total2 + total3 + total4 + total5

print("\nCart Items:")
print(f"1. {product1_name}: ₹{product1_price} x {product1_quantity} = ₹{total1}")
print(f"2. {product2_name}: ₹{product2_price} x {product2_quantity} = ₹{total2}")
print(f"3. {product3_name}: ₹{product3_price} x {product3_quantity} = ₹{total3}")
print(f"4. {product4_name}: ₹{product4_price} x {product4_quantity} = ₹{total4}")
print(f"5. {product5_name}: ₹{product5_price} x {product5_quantity} = ₹{total5}")
print(f"\nCart Total: ₹{cart_total}")

print("\n" + "="*60)
print("PROBLEMS WITH THIS APPROACH:")
print("="*60)
print(" 5 products = 15 variables (name, price, quantity each)")
print(" Calculate total: Logic repeated 5 times")
print(" Print statement: Repeated 5 times")
print(" Want to add 'discount' feature? Modify 5 places!")
print(" Want to add 'GST' calculation? Modify 5 places!")
print(" Want to add 'stock' checking? Add 5 more variables!")
print(" Have 100 products? 300 variables and nightmare!")
print("="*60)

# Now manager says: "Add discount feature!"
# Oh no! We need to modify 5 places... again!

# Now manager says: "Add GST calculation!"
# Oh no! We need to modify 5 places... again!

# Now manager says: "Add stock checking!"
# Oh no! We need to add product1_stock, product2_stock... 5 more variables!

print("\nSolution: Use CLASSES and OBJECTS!")
print("   Define product structure ONCE, create as many as needed")
print("   Add features ONCE, all products get it automatically")