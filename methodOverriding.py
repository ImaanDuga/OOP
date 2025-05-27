# Base class
class Shipping:
    def __init__(self, weight):
        self.weight = weight  # weight in kilograms

    def calculate_cost(self):
        cost = self.weight * 5  # $5 per kg
        print(f"Standard Shipping Cost: ${cost}")
        return cost

# Subclass with overridden method
class ExpressShipping(Shipping):
    def calculate_cost(self):
        cost = self.weight * 10  # $10 per kg for express
        print(f"Express Shipping Cost: ${cost}")
        return cost

# Create objects
standard = Shipping(3)
express = ExpressShipping(3)

# Demonstration
print("--- Standard Shipping ---")
standard.calculate_cost()

print("\n--- Express Shipping ---")
express.calculate_cost()
