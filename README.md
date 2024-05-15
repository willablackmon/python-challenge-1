

### Heading
# H1
## H2
### H3

###  design interactive ordering system from a food truck menu

starter code menu.py includes the code for printing the menu for the customer.

adapt this menu to allow customers to place an order, which includes: 
+ storing the customer's order and 
+ printing the receipt with the total price of all items ordered. 
    
The starter code includes comments, which you may use as a guide for the steps you need to add.

## Store Customer Order

1.  Create an empty list.  This list will store the customer's order in dictionary format: 

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

2.  after sub-menu (?) is printed, prompt customer to enter their selection from the menu, and saving it as a variable __menu_selection__"

3. Use input validation to check if the customer input __menu_selection__ is a number. If it isn't, print an error message. If it is a number, convert the input to an integer and use it to check if it is in the keys of __menu_items__.
   
4. If user input is not in the __menu_items__, print error. Otherwise:
   1. get item name from __menu_items__ dictionary and store it as a variable.
   2. ask customer for QTY, using the name of th eitem, otherwise let them now it will default to (1) if their input is invalid.  Save answer as variable 'quantity'.
   3. check customer input is a number, otherwise set qty to 1.  
   4. append customer's order to the list in dictionary format with "Item name" "Price" and "Quantity".  Price will be found in __menu_items__ dictionary.

5. Inside continuous __while__ loop , keep prompting user to order, write a __match:case__ statement to check for __y__ or __n__ (upper or lowercase) and includes default if neither letter is entered by customer.
   1. __y__ set __place_order__ to _True_ and break from continuous loop
   2. __n__ : set __place_order__ to _False_ and print "Thank you for your order" and break from continuous loop.
   3. Default: tell customer to try again b/c they didn't type valid input.




















Basic Syntax
### Heading
# H1
## H2
### H3

### Bold
**bold text**

### Italic
*italicized text*

### Blockquote
> blockquote

### Ordered List
1. First item
2. Second item
3. Third item

### Unordered List
- First item
- Second item
- Third item

### Code
`code`

### Horizontal Rule
---

### Link
[Markdown Guide](https://www.markdownguide.org)

### Image
![alt text](https://www.markdownguide.org/assets/images/tux.png)

## Extended Syntax

### Table
| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

### Fenced Code Block
```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

### Footnote
Here's a sentence with a footnote. [^1]
[^1]: This is the footnote.

### Heading ID

### My Great Heading {#custom-id}

### Definition List
term
: definition

### Strikethrough
~~The world is flat.~~

### Task List
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

### Emoji
That is so funny! :joy:
(See also [Copying and Pasting Emoji](https://www.markdownguide.org/extended-syntax/#copying-and-pasting-emoji))

### Highlight
I need to highlight these ==very important words==.

### Subscript
H~2~O

### Superscript
X^2^