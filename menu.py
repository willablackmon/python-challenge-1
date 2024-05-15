# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1.  Create an empty list.  This list will store the customer's order in dictionary format: 

# >      [
# >        {
# >         "Item name": "string",
# >         "Price": float,
# >         "Quantity": int
# >       },
# >       {
# >         "Item name": "string",
# >         "Price": float,
# >         "Quantity": int
# >       },
# >     ]


# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = [] 
# order_index = 0

print("\nWelcome to the Variety Food Truck!")
menu_categories = {} # make a simple list of Menu Categories


# Create a continuous loop (to allow cust to order multiple items).
place_order = True
while place_order:
    print("From which Menu would you like to order? ")

# Print the main menus for user to select, looping thru the Data.
    i = 1
    for key in menu.keys():
        print(f"\t{i}: {key}")
        menu_categories[i] = key 
        i += 1  

# Ask user to input Menu #
# Verify input is a number, verify Menu # is valid
# Save selected menu category, and reflect menu category to user
    menu_category = input("(Please enter the Menu #)  >> ")
    if menu_category.isdigit():                       
        if int(menu_category) in menu_categories.keys():   
            menu_category_name = menu_categories[int(menu_category)]
            print(f"You selected the '{menu_category_name}' menu.")  


# Prompt user to input the menu item they want to order.
# Loop through and list all Items in the selected Menu (menu_category_name)
            print(f"What Item would you like to order from the {menu_category_name} menu?")
            i = 1
            menu_items = {}    # intialize dictionary menu_items

# Format table of Items,  / Prices and display to user
# build new library of Items for this Menu and put in menu_items
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

# Looping through values of dictionary 'menu' based on the user selection
# Combining any sub-dictionary values
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

# Ask user to input Item #, verify input is a number, verify Item # is valid
# Save selected Item, and reflect menu category to user
            menu_item_number = input("(Please enter the Item #)  >> ")

            if menu_item_number.isdigit():                       
                if int(menu_item_number) in menu_items.keys():   
                    menu_item = menu_items[int(menu_item_number)]         
                    item_name = menu_items[int(menu_item_number)]['Item name']
                    item_price = menu_items[int(menu_item_number)]['Price']      

# Ask the customer for Qty of menu item; Check if quantity is a number, 
# Tell the customer that their input isn't valid and default to 1                      
            print(f'You selected {item_name} (${item_price}/each)')                 
            menu_item_qty = input("(Please enter quantity you wish to order)  >> ")

            if not menu_item_qty.isdigit():
                print(f'{menu_item_qty} was not a valid quantity. Defaulting to quantity of 1')   
                menu_item_qty = 1

# Add the item name, price, and quantity to the order list     
# Order list will store a list of dictionaries for menu item name, item price, and quantity ordered.

            print(f'Adding qty {menu_item_qty} - {item_name}(s) to your order.')
            order = {"Item name": item_name, "Price": item_price, "Quantity": menu_item_qty}
            order_list.append(order);

            # order_list.append({  
            #             "Item name": item_name,
            #             "Price": menu_items[menu_selection]["Price"],
            #             "Quantity": quantity
            #         })
            # item_price = menu_items[int(menu_item_number)]['Price']  

# If the number doesn't correlate to an Item, tell user they didn't select a valid menu option
        else:
            print(f"{menu_category} was not a menu option.")

 # Tell the customer they didn't select a number
    else:
        print("You didn't select a number.")

# Ask the customer if they would like to order anything else
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

# Check the customer's input, If Y/y, keep ordering. 
        if keep_ordering.upper() == "Y":  # Keep ordering
            print("continue ordering")
            break

# If N/n, complete order, thank for order, exit this question loop, tell customer to try/come again?
        if keep_ordering.upper() == "N":  # Exit the keep ordering question loop
            place_order = False
            break

# Print out the customer's order
print("\nThis is what we are preparing for you:")
print("Item name                 | Price  | Quantity  | Extended Price")
print("--------------------------|--------|-----------|-----------------")


line_item_total = 0;
total_order_cost = 0;

# Loop through items in customer's order; Store the dictionary items as variables
for i in range(len(order_list)):
    item_name = order_list[i]["Item name"]
    price = order_list[i]["Price"]
    quantity = order_list[i]["Quantity"]
    # total_order_cost += line_item_total
# Adding the extended price for each item (qty * price for each item)
    ext_price = round(int(quantity)*float(price), 2)

# Calculate the number of spaces for formatted printing; create space strings
# Print the item name, price, and quantity of each line item
    print(f'{item_name:<28}${price:^6}x{quantity:^16}${ext_price:^8}')

   

# Multiply the price by quantity for each item in the order list,  
# then sum() and print the prices.
# Calculate the cost of the order using list comprehension

total_order_cost = sum([float(item["Price"]) * int(item["Quantity"]) for item in order_list])
# cost_of_order = {k*3:v*2 for ("Price","Quantity") in order_list()}

print("--------------------------|--------|-----------|-----------------")
print(f'The total cost of your order is:{" " * 18}  ${total_order_cost: .2f}')
print(f'\nThank you! Please Come Again!')
print("-----------------------------------------------------------------")