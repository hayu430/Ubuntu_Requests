# 🏗️ Assignment 1: Design Your Own Class!

# Let's create a Smartphone class 📱
class Smartphone:
    def __init__(self, brand, model, storage):
        # Constructor initializes attributes
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")
    
    def info(self):
        print(f"{self.brand} {self.model} with {self.storage}GB storage")

# Inheritance Example: SuperSmartphone
class SuperSmartphone(Smartphone):
    def __init__(self, brand, model, storage, ai_assistant):
        # Call parent constructor
        super().__init__(brand, model, storage)
        self.ai_assistant = ai_assistant

    # Extra method unique to SuperSmartphone
    def use_ai(self):
        print(f"🤖 {self.ai_assistant} is helping you with smart tasks!")

# Test objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256)
phone1.info()
phone1.call("123-456-789")

super_phone = SuperSmartphone("Apple", "iPhone 15 Pro", 512, "Siri")
super_phone.info()
super_phone.use_ai()


# 🎭 Activity 2: Polymorphism Challenge!

class Vehicle:
    def move(self):
        print("This vehicle moves in some way 🚙")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water")

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
