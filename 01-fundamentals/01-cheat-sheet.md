# Quick Reference: Classes and Objects

## 🎯 Core Concepts

| Concept | Simple Explanation | Real-World Analogy |
|---------|-------------------|-------------------|
| **Class** | Blueprint/Template | Cookie cutter, House plan, Form template |
| **Object** | Real instance from class | Cookie, House, Filled form |
| **`__init__`** | Constructor - runs when object created | Birth certificate for the object |
| **`self`** | Reference to current object | "My" (my name, my age) |
| **Instance Variable** | Data unique to each object | Each person's own name |
| **Method** | Function inside a class | What an object can DO |
| **Class Variable** | Data shared by all objects | School name (same for all students) |

## 📝 Basic Syntax

### Creating a Class

```python
class ClassName:
    """Documentation string"""
    
    def __init__(self, param1, param2):
        """Constructor - initializes the object"""
        self.property1 = param1
        self.property2 = param2
    
    def method_name(self):
        """A method - what object can do"""
        # Use self to access properties
        return self.property1
```

### Creating Objects

```python
# Create objects from the class
object1 = ClassName("value1", "value2")
object2 = ClassName("value3", "value4")

# Call methods
result = object1.method_name()
```

## 🔥 Quick Examples

### Example 1: Simple User Class

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display(self):
        print(f"{self.name} - {self.email}")

# Create users
user1 = User("Ravi", "ravi@test.com")
user2 = User("Priya", "priya@test.com")

# Use them
user1.display()  # Output: Ravi - ravi@test.com
```

### Example 2: Product with Methods

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self, percent):
        self.price = self.price * (1 - percent/100)
        return self.price

# Create and use
phone = Product("iPhone", 80000)
new_price = phone.apply_discount(10)  # 10% off
print(new_price)  # Output: 72000.0
```

### Example 3: Class Variables

```python
class Student:
    school = "DPS"  # Class variable - same for all
    
    def __init__(self, name, roll):
        self.name = name  # Instance variable - unique to each
        self.roll = roll

# All students share same school
s1 = Student("Amit", 101)
s2 = Student("Priya", 102)
print(s1.school)  # DPS
print(s2.school)  # DPS
```

## 🎓 Common Patterns

### Pattern 1: Counter in Class

```python
class TestCase:
    total_tests = 0  # Class variable
    
    def __init__(self, name):
        self.name = name
        TestCase.total_tests += 1  # Increment on creation

test1 = TestCase("Login Test")
test2 = TestCase("Logout Test")
print(TestCase.total_tests)  # Output: 2
```

### Pattern 2: Validation Method

```python
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def is_valid(self):
        return len(self.password) >= 8 and "@" in self.email

user = User("test@mail.com", "pass123")
print(user.is_valid())  # Output: True
```

### Pattern 3: Calculation Methods

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print(rect.area())       # 50
print(rect.perimeter())  # 30
```

## ⚠️ Common Mistakes

### Mistake 1: Forgetting `self`

```python
# ❌ WRONG
class User:
    def __init__(self, name):
        name = name  # Missing self!

# ✅ CORRECT
class User:
    def __init__(self, name):
        self.name = name  # Use self
```

### Mistake 2: Forgetting `self` in Method Parameters

```python
# ❌ WRONG
class User:
    def display():  # Missing self!
        print(self.name)

# ✅ CORRECT
class User:
    def display(self):  # Include self
        print(self.name)
```

### Mistake 3: Modifying Class Variable with `self`

```python
# ❌ WRONG (creates instance variable instead)
class Counter:
    count = 0
    def increment(self):
        self.count += 1  # Creates new instance variable!

# ✅ CORRECT
class Counter:
    count = 0
    def increment(self):
        Counter.count += 1  # Modifies class variable
```

## 💡 When to Use Classes?

✅ **Use Classes When:**
- You have multiple similar items (users, products, tests)
- You need to add features that apply to all items
- You want organized, maintainable code
- You're building reusable components

❌ **Don't Need Classes When:**
- Writing simple one-time scripts
- Working with just one or two items
- Simple data storage (use dictionaries)

## 🎯 Real-World Use Cases for QA

### Test Case Management
```python
class TestCase:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.status = "Not Run"
    
    def execute(self, actual, expected):
        self.status = "Passed" if actual == expected else "Failed"
```

### API Testing
```python
class APITest:
    def __init__(self, endpoint, method):
        self.endpoint = endpoint
        self.method = method
    
    def send_request(self, data):
        # Make API call
        pass
```

### Test Data Management
```python
class TestData:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def is_valid(self):
        return self.username and self.password
```

## 🔍 Debugging Tips

1. **Print object properties:**
   ```python
   print(f"{user.name}, {user.email}")
   ```

2. **Check object type:**
   ```python
   print(type(user))  # <class '__main__.User'>
   ```

3. **List all properties:**
   ```python
   print(vars(user))  # {'name': 'Ravi', 'email': 'ravi@test.com'}
   ```

4. **Check if object has property:**
   ```python
   if hasattr(user, 'name'):
       print(user.name)
   ```

## 📚 Key Takeaways

1. **Class** = Blueprint (define ONCE)
2. **Object** = Real thing (create MANY)
3. **`self`** = Refers to current object
4. **`__init__`** = Runs when object is created
5. **Methods** = What objects can DO
6. **Instance variables** = Unique to each object
7. **Class variables** = Shared by all objects

## 🚀 Next Steps

After mastering Classes and Objects:
1. Learn about **Inheritance** (reusing classes)
2. Understand **Polymorphism** (same method, different behavior)
3. Study **Encapsulation** (hiding internal details)
4. Practice **Design Patterns** (proven solutions)

---

**Pro Tip:** The best way to learn is by doing. Create your own classes for things you work with daily - test cases, users, products, etc.

**Remember:** Classes make complex things simple by organizing code the way we organize thoughts!