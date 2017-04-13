#Andrew Tan, 4/12, Section 010, Part 2

#Product lists
product_names = ["hamburger", "cheeseburger", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_stock = [10, 5, 20]

#Main program
while True:
    #Ask user to select mode and check validity
    option = str.lower(input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: "))

    #Search mode
    if option == "s":
        pdt = str.lower(input("Enter a product name: "))
        if pdt in product_names:
            index = product_names.index(pdt)
            print("We sell \"%s\" at %.2f per unit" %(pdt, product_costs[index]))
            print("We currently have %d in stock\n" %(product_stock[index]))
        else:
            print("Sorry, we don't sell \"%s\"\n"%(pdt))
        continue

    #List mode
    elif option == "l":
        print("{:25s}{:7s}{:8s}".format("Product", "Price", "Quantity"))
        for i in range(len(product_names)):
            print("{:25.23s}{:<7.2f}{:<8d}".format(product_names[i], product_costs[i], product_stock[i]))
        print()
        continue

    #Add mode
    elif option == "a":
        while True:
            pdt = str.lower(input("Enter a new product name: "))
            if pdt in product_names:
                print("Sorry, we already sell that product. Try again.")
                continue
            else:
                break
        while True:
            cost = float(input("Enter a product cost: "))
            if cost <= 0:
                print("Invalid cost. Try again.")
                continue
            else:
                break
        while True:
            qty = int(input("How many of these products do we have? "))
            if qty <= 0:
                print("Invalid quantity. Try again.")
                continue
            else:
                break
        product_names.append(pdt)
        product_costs.append(cost)
        product_stock.append(qty)
        print("Product added!\n")
        continue

    #Remove mode
    elif option == "r":
        pdt = str.lower(input("Enter a product name: "))
        if pdt not in product_names:
            print("Product doesn't exist. Can't remove.\n")
        else:
            index = product_names.index(pdt)
            del product_names[index]
            del product_costs[index]
            del product_stock[index]
            print("Product removed!\n")
        continue

    #Update mode
    elif option == "u":
        pdt = str.lower(input("Enter a product name: "))
        if pdt not in product_names:
            print("Product doesn't exist. Can't update.\n")
        else:
            index = product_names.index(pdt)
            print("What would you like to update?")
            item = str.lower(input("(n)ame, (c)ost or (q)uantity: "))

            #Update name
            if item == "n":
                while True:
                    newname = str.lower(input("Enter a new name: "))
                    if newname in product_names:
                        print("Duplicate name!")
                        continue
                    else:
                        product_names[index] = newname
                        print("Product name has been updated\n")
                        break

            #Update cost
            elif item == "c":
                while True:
                    newcost = float(input("Enter a new cost: "))
                    if newcost <= 0:
                        print("Invalid cost!")
                        continue
                    else:
                        product_costs[index] = newcost
                        print("Product cost has been updated\n")
                        break

            #Update quantity
            elif item == "q":
                while True:
                    newqty = float(input("Enter a new quantity: "))
                    if newqty <= 0:
                        print("Invalid quantity!")
                        continue
                    else:
                        product_stock[index] = newqty
                        print("Product quantity has been updated\n")
                        break

            #Invalid option
            else:
                print("Invalid option\n")
        continue

    #Report mode
    elif option == "e":
        totalcost = 0
        for cost, qty in zip(product_costs, product_stock):
            totalcost += cost*qty
        print("{:29s}{:.2f} ({})".format("Most expensive product:", max(product_costs), product_names[product_costs.index(max(product_costs))]))
        print("{:29s}{:.2f} ({})".format("Least expensive product:", min(product_costs), product_names[product_costs.index(min(product_costs))]))
        print("{:29s}{:.2f}\n".format("Total value of all products:", totalcost))
        continue

    #Quit program
    elif option == "q":
        print("See  you soon!")
        break

    #Invalid mode
    else:
        print("Invalid option, try again\n")
        continue
