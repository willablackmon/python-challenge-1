

#  Interactive Food Ordering System

This Script Presents an Interactive Food Ordering System from a food truck menu.

The menu includes simple nested dictionaries.  Take inputs from the user and:
+ store the customer order
+ print the receipt at the end, with each line item orderd and total price of all items ordered. 


## Process
1. Present the top level menus to the user (with prices).
2. Prompt the customer to enter the Menu.
3. Validate inputs (entry type, presence of the item on the menu).
4. Using Menu input, show sub-menu items and allow selection.
5. Prompt for quantity of the item
   1. Validate entry or 
   2. Set to default of 1 with a warning (if incorrect entry)
6. Store entry: 
   1. append customer's order to the list in dictionary format
   2. include "Item name" "Price" and "Quantity".
7. Ask the user if they wish to continue
      1. Y/y: begin again at top level menus and repeat the above steps.
      2. N/n: exit the ordering loops and display the final receipt.
8. Final receipt will contain:
   1. Each line item ordered (adding extended price for each line)
   2. Total price of order


## Development Notes 
### Storing Customer Order

1.  This list will store the customer's order in dictionary format: 

>      [
>        {
>         "Item name": "string",
>         "Price": float,
>         "Quantity": int
>       },
>       {
>         "Item name": "string",
>         "Price": float,
>         "Quantity": int
>       },
>     ]