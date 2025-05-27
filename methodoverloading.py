class Invoice:
    def generate(self, *args):
        if len(args) == 0:
            print("Generating a general invoice...")
        elif len(args) == 1:
            product = args[0]
            print(f"Invoice for one product: {product}")
        elif len(args) == 2:
            product, quantity = args
            print(f"Invoice: {quantity} x {product}")
        else:
            print("Too many arguments!")

# Demonstration
invoice = Invoice()
invoice.generate()
invoice.generate("Laptop")
invoice.generate("Phone", 2)
invoice.generate("Phone", 2, 1000)  # Too many args
