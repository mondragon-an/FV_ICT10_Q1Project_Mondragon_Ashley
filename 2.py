from pyscript import document, display

label1 = "crescendo croissant"#string
label2 = "sweet symphony cake (slice)"#string
label3 = "harmony muffin"#string
label4 = "soloist scone"#string
label5 = "off-key cookie"#string
label6 = "backbeat brownie"#string

#displays the food names
display(label1, target="label1")
display(label2, target="label2")
display(label3, target="label3")
display(label4, target="label4")
display(label5, target="label5")
display(label6, target="label6")

#displays the food prices
tax_rate = 0.03 #float
price1 = 105*tax_rate+105 #float
price2 = 220*tax_rate+220 #float
price3 = 100*tax_rate+100 #float
price4 = 90*tax_rate+90 #float
price5 = 65*tax_rate+65 #float
price6 = 65*tax_rate+65 #float

food_prices = {
    "food1": price1,
    "food2": price2,
    "food3": price3,
    "food4": price4,
    "food5": price5,
    "food6": price6,
}#dictionary

#collects form data, calculates total from checked items, and displays order summary
def place_order(e):
    fname = document.getElementById("fname").value
    addressA = document.getElementById("addressA").value
    numberA = document.getElementById("numberA").value
    
    total_cost = 0.0
    
    for food_id, price in food_prices.items():
        checkbox = document.getElementById(food_id)
        
        if checkbox and checkbox.checked:
            total_cost += price
            
    display(f"order for: {fname}", target="fname1")
    display(f"address: {addressA}", target="addressA1")
    display(f"contact number: {numberA}", target="numberA1")

    display(f"total amount due: ₱{total_cost:.2f}", target="total_cost")
