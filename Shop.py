class Shop:

    def __init__(self, shop_name, shop_address, employee_count):
        # Private attributes
        self.__shop_name = shop_name
        self.__shop_address = shop_address
        self.__employee_count = employee_count
        self.__inventory = {}  # Dictionary with product name as key and dict of price/quantity as value
        self.__customer_origins = []  # List to track regions of each customer

    # Getters
    def get_shop_name(self):
        return self.__shop_name

    def get_shop_address(self):
        return self.__shop_address

    def get_employee_count(self):
        return self.__employee_count

    # Setters
    def set_shop_name(self, name):
        self.__shop_name = name

    def set_shop_address(self, address):
        self.__shop_address = address

    def set_employee_count(self, count):
        self.__employee_count = count

    # Calculate average rating from a list of integers (1 to 5)
    def calculate_review_stars(self, reviews):
        if len(reviews) == 0:
            return 0
        average = sum(reviews) / len(reviews)
        return format(average, '.2f')

    # Append customer's region (normalized)
    def add_customer_origin(self, customer):
        self.__customer_origins.append(customer.get_origin().strip().lower())

    def get_customer_origins(self):
        return self.__customer_origins

    # Count and display customers per region
    def display_customer_stats(self):
        origin_count = {}
        for region in self.__customer_origins:
            origin_count[region] = self.__customer_origins.count(region)

        max_count = max(origin_count.values())

        for region, count in origin_count.items():
            print(f"For region {region}, there were {count} customers.")
            if count == max_count:
                top_region = region

        print()
        print(f"The region with the most customers is {top_region} with {origin_count[top_region]} customers.")

    # Show inventory details
    def show_inventory(self):
        print()
        for idx, (name, data) in enumerate(self.__inventory.items(), start=1):
            print(f"{idx}) Name: {name} || Quantity: {data['quantity']} || Price: {data['price']}")

    # Normalize strings: remove leading/trailing spaces, replace internal spaces with "_", convert to lowercase
    def normalize_string(self, string):
        return string.strip().replace(" ", "_").lower()

    # Add a product to inventory
    def add_product(self, product_name, product_price, product_quantity):
        while True:
            if product_name.strip() == "":
                new_name = str(input("Product name is empty. Please enter a valid name: "))
                if new_name and not new_name.isdigit():
                    product_name = new_name
                else:
                    print("Invalid name. Try again.")
                    continue

            if product_price <= 0:
                price_input = float(input("Invalid price. Please enter a positive decimal (e.g. 2.0): "))
                if isinstance(price_input, float):
                    product_price = price_input

            if product_quantity <= 0:
                quantity_input = int(input("Invalid quantity. Enter a number greater than 0: "))
                if isinstance(quantity_input, int):
                    product_quantity = quantity_input

            if product_name and product_price > 0 and product_quantity > 0:
                normalized_name = self.normalize_string(product_name)
                self.__inventory[normalized_name] = {
                    "quantity": product_quantity,
                    "price": product_price
                }
                print("Product successfully added to inventory!")
                break

    # Remove a product by name
    def remove_product(self, product_name):
        if product_name:
            normalized_name = self.normalize_string(product_name)
        try:
            del self.__inventory[normalized_name]
            print(f"Product '{normalized_name}' removed successfully.")
        except KeyError:
            print(f"The product '{product_name}' does not exist in the inventory.")

    # Reduce the quantity of a product
    def reduce_quantity(self, product_name, quantity_to_reduce):
        if product_name:
            normalized_name = self.normalize_string(product_name)

        if quantity_to_reduce > 0:
            try:
                self.__inventory[normalized_name]['quantity'] -= quantity_to_reduce
                if self.__inventory[normalized_name]['quantity'] < 0:
                    self.__inventory[normalized_name]['quantity'] = 0
            except KeyError:
                print("The product does not exist in the inventory.")
        else:
            print("Quantity must be greater than 0.")

    # Calculate total value of inventory
    def calculate_inventory_total(self):
        total = 0
        for product in self.__inventory:
            total += self.__inventory[product]['quantity'] * self.__inventory[product]['price']
        print(f"Total inventory value: {total}")

    # Display per-product total (unit price * quantity)
    def calculate_unit_totals(self):
        product_totals = {}

        for product in self.__inventory:
            total_price = self.__inventory[product]['quantity'] * self.__inventory[product]['price']
            product_totals[product] = total_price

        for name, total in product_totals.items():
            print(f"Product '{name}' has a total value of {format(total, '.2f')}")
