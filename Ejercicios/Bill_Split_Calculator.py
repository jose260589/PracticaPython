print("Bill Split Calculator")

friend = int(input("How many friends are there? "))
bill = int(input("How much was the bill?")) 
tax = bill * 0.18 
tip = bill * 0.10

facture_Total = bill + tax + tip

friend_Total = facture_Total / friend

print(f"Total to pay with tax is {friend_Total} to friend")