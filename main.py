from Shop import Shop
from Employee import Employee
from Customer import Customer

def main():
    # Create shop instance
    shop = Shop("Tech Store", "123 Market Street", 10)

    # Create employee
    employee = Employee("Smith", "Alice", "permanent", 2500)

    # Add products via employee
    print("\n--- Adding products to inventory ---")
    employee.add_product(shop, "Wireless Mouse", 25.99, 15)
    employee.add_product(shop, "Laptop Stand", 39.99, 10)
    employee.add_product(shop, "Keyboard", 49.99, 5)
    employee.add_product(shop, "USB-C Cable", 9.99, 25)
    employee.add_product(shop, "Monitor 27 inch", 199.99, 7)

    print("\n--- Current Inventory ---")
    employee.print_inventory(shop)

    # Show unit totals and total inventory value
    print("\n--- Unit Totals & Total Inventory Value ---")
    employee.calculate_unit_totals(shop)
    employee.calculate_total(shop)

    # Reduce quantity of a product
    print("\n--- Reducing Quantity ---")
    employee.reduce_quantity(shop, "keyboard", 2)
    employee.reduce_quantity(shop, "usb-c cable", 5)

    print("\n--- Inventory After Reduction ---")
    employee.print_inventory(shop)

    # Remove a product
    print("\n--- Removing a Product ---")
    employee.remove_product(shop, "monitor 27 inch")
    employee.print_inventory(shop)

    # Create customers
    customer1 = Customer("Miller", "John", "California")
    customer2 = Customer("Davis", "Emma", "Texas")
    customer3 = Customer("Lopez", "Carlos", "California")
    customer4 = Customer("Lee", "Sophia", "New York")
    customer5 = Customer("Wilson", "Olivia", "Florida")


    print("\n--- Customers Writing Reviews ---")
    for customer in [customer1, customer2, customer3, customer4, customer5]:
        customer.write_review()

    # Employee views average review
    print("\n--- Viewing Average Review ---")
    all_reviews = (
        customer1.get_reviews() + customer2.get_reviews() +
        customer3.get_reviews() + customer4.get_reviews() +
        customer5.get_reviews()
    )

    employee.view_reviews(shop, all_reviews)

    # Append customer origins
    print("\n--- Collecting Customer Origins ---")
    for customer in [customer1, customer2, customer3, customer4, customer5]:
        shop.add_customer_origin(customer)

    shop.display_customer_stats()


if __name__ == "__main__":
    main()
