# function to display current sales

def display_sales(sales_data):
    """ Displays current sales 
    Args: sales_data (dict) : A dictionary with sales and their product values"""
    for product, sales in sales_data.items():
        print(f"{product}: {sales} units.")
        
# function to update sales
def update_sales(sales_data, product, new_sales):
    """Updates sales for a specific product.
    Args: sales_data (dict): A dictionary with products and their sales values.
          product (str): The name of the product.
          new_sales (int): The new sales value"""
    sales_data["product"] = new_sales
    
# Main part of the program
sales_data = {
    "Laptop": 50,
    "Phone": 100,
    "Television": 30
}

# Display current sales
display_sales(sales_data)

# Update sales (simulate change)
update_sales(sales_data, "Phone", 120)

# Display updated sales
print(f"\nUpdated sales:")
display_sales(sales_data)