import climage

# Login method for admin panel
def login():
    while True:
        # Request username and password
        user = input("Username: ")
        pwd = input("Password: ")
        # If username and password are correct break else keep looping
        if user == "admin" and pwd == "1234":
            print("\033[1;34mLogin Successful!\033[0;0m")
            break
        else:
            print("\033[1;31mLogin Failed!\nTry again.\033[0;0m")


def runShop():

    # Initiate dictionaries and test data
    categoriesDict = {}
    cat1 = {"ID": "p1", "name": "plants", "disc": "Indoor & Outdoor plants"}
    cat2 = {"ID": "p2", "name": "vegetables", "disc": "Greek fresh produce"}
    cat3 = {"ID": "p3", "name": "fruit", "disc": "Local Greek fruit"}
    categoriesDict["C1"] = cat1
    categoriesDict["C2"] = cat2
    categoriesDict["C3"] = cat3
    productsDict = {}
    prod1 = {"ID": "pr1", "name": "pothos", "price": "15", "categoryID": "p1"}
    prod2 = {"ID": "pr2", "name": "eggplant", "price": "1", "categoryID": "p2"}
    prod3 = {"ID": "pr3", "name": "spider plant", "price": "12", "categoryID": "p1"}
    prod4 = {"ID": "pr4", "name": "watermelon", "price": "3", "categoryID": "p3"}
    prod5 = {"ID": "pr5", "name": "cucumber", "price": "1", "categoryID": "p2"}
    productsDict["P1"] = prod1
    productsDict["P2"] = prod2
    productsDict["P3"] = prod3
    productsDict["P4"] = prod4
    productsDict["P5"] = prod5
    customersDict = {}
    cust1 = {"ID": "c1", "email": "alex45@gmail.com", "phone": "695332042", "address": "45th Avenue Street",
             "location": "London", "country": "UK"}
    cust2 = {"ID": "c2", "email": "emily37@gmail.com", "phone": "694353055", "address": "255th St Merry",
             "location": "London", "country": "UK"}
    cust3 = {"ID": "c3", "email": "james24@gmail.com", "phone": "6943232492", "address": "Cov Square",
             "location": "Coventry", "country": "UK"}
    cust4 = {"ID": "c4", "email": "leah85@gmail.com", "phone": "69590215402", "address": "14 Fish Terrace",
             "location": "Liverpool", "country": "UK"}
    customersDict["CU1"] = cust1
    customersDict["CU2"] = cust2
    customersDict["CU3"] = cust3
    customersDict["CU4"] = cust4
    ordersDict = {}
    ord1 = {"ID": "o1", "pID": "pr2", "quantity": "3", "total": "3", "custID": "cu1", "status": "delivered"}
    ord2 = {"ID": "o2", "pID": "pr3", "quantity": "6", "total": "72", "custID": "cu4", "status": "delivered"}
    ord3 = {"ID": "o3", "pID": "pr1", "quantity": "2", "total": "30", "custID": "cu3", "status": "shipping"}
    ord4 = {"ID": "o4", "pID": "pr3", "quantity": "4", "total": "48", "custID": "cu3", "status": "delivered"}
    ordersDict["O1"] = ord1
    ordersDict["O2"] = ord2
    ordersDict["O3"] = ord3
    ordersDict["O4"] = ord4

    # Run Admin panel
    while True:
        print("\n\033[1;34mAdmin Panel\n\033[0;0m")
        print("1. Insert new Object.")
        print("2. Get Sales.")
        print("3. View Details.")
        print("4. Exit.")
        inp = int(input("Select an action: "))
        # Exit admin panel
        if inp == 4:
            break
        # Add new Object
        if inp == 1:
            print("What would you like to insert:")
            print("1. Insert new Category.")
            print("2. Insert new Product.")
            print("3. Insert new Customer.")
            print("4. Go Back.")
            inp2 = int(input("Select an action: "))
            # Add new Category
            if inp2 == 1:
                name = input("Name: ")
                disc = input("Description: ")
                categoriesCount = 0
                for x in categoriesDict:
                    categoriesCount += 1
                categoriesDict["P" + str(categoriesCount + 1)] = {"ID": "c" + str(categoriesCount + 1), "email": name,
                                                                  "disc": disc}
            # Add new Product
            elif inp2 == 2:
                name = input("Name: ")
                price = input("Price: ")
                catID = input("Category ID: ")
                catIDList = []
                for x in categoriesDict:
                    catIDList.append(categoriesDict.get(x).get("ID"))
                # Check if category provided exists
                if catID not in catIDList:
                    print("\033[1;31mCategory ID does not exist!\nTry again.\033[0;0m")
                else:
                    productCount = 0
                    for x in productsDict:
                        productCount += 1
                    productsDict["P" + str(productCount + 1)] = {"ID": "pr" + str(productCount + 1), "name": name,
                                                                 "price": price, "categoryID": catID}
            # Add new customer
            elif inp2 == 3:
                email = input("Email: ")
                phone = input("Phone: ")
                address = input("Address: ")
                location = input("Location/City: ")
                country = input("Country: ")
                customerCount = 0
                for x in customersDict:
                    customerCount += 1
                customersDict["P" + str(customerCount + 1)] = {"ID": "pr" + str(customerCount + 1), "email": email,
                                                               "phone": phone, "address": address, "location": location,
                                                               "country": country}
                print(customersDict)
            # Go back to admin panel
            elif inp2 == 4:
                pass
        # Display data for selected dictionary
        elif inp == 3:
            print("What would you like to display:")
            print("1. Display All Categories.")
            print("2. Display All Products.")
            print("3. Display All Customers.")
            print("4. Display All Orders.")
            print("5. Go Back.")
            inp2 = int(input("Select an action: "))
            # Get data for all categories
            if inp2 == 1:
                print("\033[1;36mCategories\033[0;0m")
                for x in categoriesDict:
                    print("\033[33m=========================")
                    print("ID: " + categoriesDict.get(x).get("ID"))
                    print("Name: " + categoriesDict.get(x).get("name"))
                    print("Description: " + categoriesDict.get(x).get("disc"))
                print("=========================\033[0;0m")
            # Get data for all products
            elif inp2 == 2:
                print("\033[1;36mProducts\033[0;0m")
                for x in productsDict:
                    print("\033[33m=========================")
                    print("ID: " + productsDict.get(x).get("ID"))
                    print("Name: " + productsDict.get(x).get("name"))
                    print("Price: " + productsDict.get(x).get("price"))
                    print("Category ID: " + productsDict.get(x).get("categoryID"))
                print("=========================\033[0;0m")
            # Get data for all Customers
            elif inp2 == 3:
                print("\033[1;36mCustomers\033[0;0m")
                for x in customersDict:
                    print("\033[33m====================================")
                    print("ID: " + customersDict.get(x).get("ID"))
                    print("Email: " + customersDict.get(x).get("email"))
                    print("Phone number: " + customersDict.get(x).get("phone"))
                    print("Address: " + customersDict.get(x).get("address") + ", " + customersDict.get(x).get(
                        "location") + ", " + customersDict.get(x).get("country"))
                print("====================================\033[0;0m")
            # Get data for all Orders
            elif inp2 == 4:
                print("\033[1;36mOrders\033[0;0m")
                for x in ordersDict:
                    print("\033[33m=========================")
                    print("ID: " + ordersDict.get(x).get("ID"))
                    print("Product ID: " + ordersDict.get(x).get("pID"))
                    print("Quantity: " + ordersDict.get(x).get("quantity"))
                    print("Total Price: " + "£" + ordersDict.get(x).get("total"))
                    print("Customer ID: " + ordersDict.get(x).get("custID"))
                    print("Status: " + ordersDict.get(x).get("status"))
                print("=========================\033[0;0m")
            # Go back to admin panel
            elif inp2 == 5:
                pass
        # Get sales with specific parameters
        elif inp == 2:
            print("What would your sales like to be based on:")
            print("1. Get Sales based on product ID.")
            print("2. Get Products and Sales based on category.")
            print("3. Get Products based on total revenue.")
            print("4. Get Products based on Location.")
            inp2 = int(input("Select an action: "))
            print("\033[35m=========================")
            # Loop through orders and find orders with matching product ID
            if inp2 == 1:
                pID = input("Insert the Product ID: ")
                totalOrders = 0
                for x in ordersDict:
                    if ordersDict.get(x).get("pID") == pID:
                        print("Order ID: " + ordersDict.get(x).get("ID"))
                        print("Quantity: " + ordersDict.get(x).get("quantity"))
                        print("Total Price: " + "£" + ordersDict.get(x).get("total"))
                        print("Customer ID: " + ordersDict.get(x).get("custID"))
                        print("Status: " + ordersDict.get(x).get("status"))
                        totalOrders += 1
                        print("========================")
                print(pID + " has been sold a total of " + str(totalOrders) + " times.")
            # Print orders and products with matching category
            if inp2 == 2:
                categName = input("Insert the Category Name: ")
                catID = ""
                for x in categoriesDict:
                    if categoriesDict.get(x).get("name") == categName:
                        catID = categoriesDict.get(x).get("ID")
                print("========================")
                print("Products under " + categName + " category:")
                productList = []
                # Loop through products with matching category
                for p in productsDict:
                    if productsDict.get(p).get("categoryID") == catID:
                        print("-------------------")
                        print("ID: " + productsDict.get(p).get("ID"))
                        print("Name: " + productsDict.get(p).get("name"))
                        print("Price: " + productsDict.get(p).get("price"))
                        productList.append(productsDict.get(p).get("ID"))
                print("========================")
                print("Sales under " + categName + " category:")
                # Loop through orders with matching category
                for po in ordersDict:
                    if ordersDict.get(po).get("pID") in productList:
                        print("Order ID: " + ordersDict.get(po).get("ID"))
                        print("Product ID: " + ordersDict.get(po).get("pID"))
                        print("Quantity: " + ordersDict.get(po).get("quantity"))
                        print("Total Price: " + "£" + ordersDict.get(po).get("total"))
                        print("Customer ID: " + ordersDict.get(po).get("custID"))
                        print("Status: " + ordersDict.get(po).get("status"))
                        print("-------------------")
            # Loop through orders and find total revenue per product
            if inp2 == 3:
                priceDict = {}
                ascending = int(input(
                    "Would you like in ascending order or descending of total revenue?\n1. Ascending\n2. Descending"))
                for o in ordersDict:
                    total = int(ordersDict.get(o).get("total"))
                    productId = ordersDict.get(o).get("pID")
                    if productId not in priceDict:
                        priceDict[productId] = total
                    else:
                        priceDict.update({productId: priceDict.get(productId) + total})
                # In ascending order of total revenue
                if ascending == 1:
                    priceList = sorted(priceDict.items(), key=lambda j: j[1])
                    sortPriceDict = dict(priceList)
                    for x in sortPriceDict:
                        print("Item ID: " + x + ", Total revenue: " + str(sortPriceDict.get(x)))
                # In descending order of total revenue
                if ascending == 2:
                    priceList = sorted(priceDict.items(), key=lambda j: j[1], reverse=True)
                    sortPriceDict = dict(priceList)
                    for x in sortPriceDict:
                        print("Item ID: " + x + ", Total revenue: " + str(sortPriceDict.get(x)))
            # Loop through orders and find customers with location that matches the input
            if inp2 == 4:
                pLoc = input("Insert the Location: ")
                for x in ordersDict:
                    custID = ordersDict.get(x).get("custID")
                    if customersDict.get(custID.upper()).get("location") == pLoc:
                        print("Order ID: " + ordersDict.get(x).get("ID"))
                        print("Product ID: " + ordersDict.get(x).get("pID"))
                        print("Quantity: " + ordersDict.get(x).get("quantity"))
                        print("Total Price: " + "£" + ordersDict.get(x).get("total"))
                        print("Customer ID: " + ordersDict.get(x).get("custID"))
                        print("Status: " + ordersDict.get(x).get("status"))
                        print("-------------------")

# Print welcome screen and image
print("\033[0;32m------------------------")
print("Welcome to Bessy's Garden")
print("------------------------\033[0;0m")
print(climage.convert('flower_3.png'))
# Run login function
login()
# Run admin panel
runShop()

'''
//This program runs our Garden Shop with a variety of plants, vegetables, and fruit

print "welcome the admin to the shop"
print flower.png
run the login() function that requires the user to enter their credentials(username and password) in order to move to the admin panel.
run the runShop() function that contains all the admin panel and all the test data
while True:
    print menu
        Option 1. Insert new Object.
            print Second menu
            choose to insert new category, product or customer
            request user for required info
            add new object to respective dictionary
        Option 2. Get Sales.
            print Second menu
            Option 1: Get sales with specific product ID
                Loop through Orders
                    print orders with matching product ID
            Option 2: Get sales and products with matching category 
                loop through products
                    print products with matching category name
                loop through Orders
                    print products with matching category name 
            Option 3: Get products according to sales
                Ask user if they want the result in ascending or descending order
                    Extract total revenue for each product from Orders:
                    Sort and Display data according to ascending or descending order
            Option 4: Get products with matching Location
                loop through Orders
                    extract customer info and print orders with matching location       
        Option 3. View Details.
            Display categories, products customers or orders dictionaries depending on user input
        Option 4. Exit. 
            break the loop and exit

'''
