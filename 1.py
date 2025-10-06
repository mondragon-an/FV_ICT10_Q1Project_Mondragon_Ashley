from pyscript import document, display

store_name = "Dough-Re-Mi ♪♫♪" #string
owner = 'ashley mondragon' #string
year_founded = 2025 #int

display(store_name, target="storeName")
display(f"by {owner}",target="ownerName" )
display(f"est: {year_founded}", target="yearFounded")

b1 = "crescendo croissant" #string
b2 = "sweet symphony cake (slice)" #string
b3 = "harmony muffin" #string
b4 = "soloist scone" #string
b5 = "off-key cookie" #string
b6 = "backbeat brownie" #string

display(b1, target="b1")
display(b2, target="b2")
display(b3, target="b3")
display(b4, target="b4")
display(b5, target="b5")
display(b6, target="b6")

tax_rate = 0.03 #float
p1 = 105*tax_rate+105 #float
p2 = 220*tax_rate+220 #float
p3 = 100*tax_rate+100 #float
p4 = 90*tax_rate+90 #float
p5 = 65*tax_rate+65 #float
p6 = 65*tax_rate+65 #float

display(p1, target="p1")
display(p2, target="p2")
display(p3, target="p3")
display(p4, target="p4")
display(p5, target="p5")
display(p6, target="p6")

business_hours = "10:00 am - 8:00 pm" #string
display(f"open: {business_hours}", target="business_hours")

allergens = "gluten, eggs, milk, soy" #string
display(f"common allergens: {allergens}", target="allergens")

delivery = True
display(f"delivery available: {delivery}", target="delivery")
