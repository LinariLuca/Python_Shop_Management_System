from Person import Person

class Employee(Person):

    # Validates contract type input
    def check_contract_type(self, contract_str):
        if contract_str:
            contract_str = contract_str.strip().lower()

        if contract_str in ["permanent", "fixed-term", "internship", "training"]:
            return contract_str
        else:
            return "no_contract"

    # Validates and formats salary
    def check_salary(self, salary):
        if salary and salary > 1200.00:
            return format(float(salary), '.2f')
        else:
            # Set minimum average salary for an employee
            return format(1200, ".2f")

    def __init__(self, last_name, first_name, contract_type, salary):
        super().__init__(last_name, first_name)
        self.__contract_type = self.check_contract_type(contract_type)
        self.__salary = self.check_salary(salary)

    # Getters
    def get_contract_type(self):
        return self.__contract_type

    def get_salary(self):
        return self.__salary

    # Setters
    def set_contract_type(self, contract_type):
        self.__contract_type = contract_type

    def set_salary(self, salary):
        self.__salary = salary

    # The employee interacts with the shop and its products, not the other way around

    def print_inventory(self, shop):
        shop.show_inventory()

    def add_product(self, shop, product_name, product_price, product_quantity):
        shop.add_product(product_name, product_price, product_quantity)

    def remove_product(self, shop, product_name):
        shop.remove_product(product_name)

    def reduce_quantity(self, shop, product_name, quantity_to_reduce):
        shop.reduce_quantity(product_name, quantity_to_reduce)

    def calculate_total(self, shop):
        shop.calculate_inventory_total()

    def calculate_unit_totals(self, shop):
        shop.calculate_unit_totals()

    # Displays average rating from customer reviews
    def view_reviews(self, shop, reviews_array):
        print(f"The average review rating is: {shop.calculate_review_stars(reviews_array)}")
