# Ice Cream Shop Application
# Author: Candace Vogel
# Date: 1/29/2025

# Store our ice cream shop's menu items
# Added three more flavors - oreo, sherbert, and coffee
flavors = ["vanilla", "caramel", "mint", "oreo", "sherbert", "coffee"]
toppings = ["sprinkles", "nuts", "cherry"]
# Added cone list
cones =  ["cake cone", "sugar cone", "waffle cone"]
prices = {"scoop": 2.50, "topping": 0.50, "cone": 1.50}

def display_menu():
    """Shows available flavors and toppings to the customer"""
    print("\n=== Welcome to the Ice Cream Shop! ===")
    print("\nAvailable flavors:")

    # Loop through the flavor list and show each flavor, then
    # we'll loop through the toppings list and display them

    for flavor in flavors:
        print(f" - {flavor}")

    print("\nAvailable Toppings: ")
    for topping in toppings:
        print(f"- {topping}")

# Search function for ice cream flavors
# Convert input to lowercase so our program can search the list
def search_flavors():
    search = input("\nSearch for ice cream flavor: ").lower()
    if search in flavors:
        print(f"{search} is in stock!")
    else:
        print(f"Sorry, {search} is not available.")

# Display the prices to our user
print("\nPrices")
print(f"Scoops: ${prices['scoop']:.2f}")
print(f"Toppings: ${prices['topping']:.2f} each")
print(f"Cones: ${prices['cone']:.2f}")
print(f"10% off all orders over $10!")

def get_flavors():
    """Gets ice cream flavor choices from the customer"""
    chosen_flavors = []

    # Use a while loop to keep taking orders until the customer is done
    while True:
        try:
            # Prompt the user to choose their scoops of ice cream
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))
            # Validate the input
            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1 and 3 scoops.")
        except ValueError:
             #except any error that's thrown   
             print("Please enter a number.") 

    # Prompt the user to enter the ice cream flavor
    print("\nFor each scoop, enter the flavor you'd like: ")
    for i in range(num_scoops): #For loop prompts for each scoop of ice cream
        # Nested while loop handles the user's input and validation
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()
            # Check to see if the flavor is one that's in the shop's list
            if flavor in flavors:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor isn't available.")

    # Return to the calling function, the number of scoops user wants
    # and the flavors they picked
    return num_scoops, chosen_flavors

def get_toppings(): 
    """Gets topping choices from the customer"""
    chosen_toppings = []

    # Use a while loop to prompt the user for toppings until
    # they are done adding toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        #Test if the user is done ordering toppings 
        if topping == 'done': 
            break
        # Test if the topping is in the list of toppings for our shop
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")

    # Return the list of toppings that the user chose
    return chosen_toppings

def get_cones():
    chosen_cone = []
    # Gets cone choice from the user
    # Ask user for cone choice. Only one selection can be made.
    while True:
        cone = input("\nEnter cone choice (or 'done' if no cone): ").lower()
        # if user is done ordering...
        if cone == 'done':
            break
        # test if cone is available on menu
        if cone in cones:
            chosen_cone.append(cone)
            print("\nAdded cone to order!")
            return chosen_cone
        else:
            print("\nSorry, your cone selection isn't available.")

    # Return cone selection if none
    return None

def calculate_total(num_scoops, num_toppings, chosen_cone):
    """Calculates the total cost of the order"""
    scoop_cost = num_scoops * prices["scoop"]
    topping_cost = num_toppings * prices["topping"]
    cone_cost = prices["cone"] if chosen_cone else 0
    # cone cost is $0 if no cone was chosen during selection
    return scoop_cost + topping_cost + cone_cost

def print_receipt(num_scoops, chosen_flavors, chosen_toppings, chosen_cone):
    """Prints a nice formatted receipt for the customer"""
    print("\n=== Your Ice Cream Order ===")
    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}")

    if chosen_toppings:
        print("\nToppings:")
        # Loop through the list of toppings
        for topping in chosen_toppings:
            print(f" - {topping.title()}")

    if chosen_cone:
        print("\nCone:")
        # Loop through list of cones
        for cone in chosen_cone:
            print(f" - {cone.title()}")

    #Calculate the total cost before discount
    total = calculate_total(num_scoops, len(chosen_toppings), chosen_cone)

    #Check if eligible for discount
    #Using if-else to print "Total after discount:" if discount is applied,
    #else print "Total:"
    if total > 10:
        discount = total * 0.10
        total -= discount
        print(f"\n${discount:.2f} discount applied!")
        print(f"\nTotal after discount: {total:.2f}")
    else:
        # Print the total amount for customer
        print(f"\nTotal: ${total:.2f}")

    # Save order to file
    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops - ${total:.2f}")

# Main function - updated test function
def main():
    display_menu()
    search_flavors()
    # Call get flavors function, which returns the number of scoops
    # and the list of flavors
    num_scoops, chosen_flavors = get_flavors()
    # Call the get toppings functions which returns the list of toppings
    chosen_toppings = get_toppings()
    # Call the get cones function which returns the cone selected by user
    chosen_cone = get_cones()
    # Display the receipts
    print_receipt(num_scoops, chosen_flavors, chosen_toppings, chosen_cone)

# Automatically execute the main function when application runs
if __name__ == "__main__":
    main()
