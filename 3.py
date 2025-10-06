from pyscript import document, display

message = "we would love to hear from you ♥︎♡♥︎" #string
location = "⚲ our location ⚲"#string
locdetails = """Unit 104, The Quarter Note Arcade
1776 Conductor St.,
Barangay Crescendo,
Metro Manila 1550""" #multiline string
phone = "☎ phone number ☎" #string
phondetails = "(555) 789 - CAKE" #string
email = "✉ email address ✉" #string
emaildetails = "orders@doughremicafe.com" #string

display(message, target="message")#displays the message
display(location, target="location")#displays the heading
display(locdetails, target="locdetails")#displays the location
display(phone, target="phone")#displays the heading
display(phondetails, target="phondetails")#displays the phone number
display(email, target="email")#displays the heading
display(emaildetails, target="emaildetails")#displays the email

business_hours = "10:00 am - 8:00 pm" #string
display(f"open: {business_hours}", target="business_hours")#shows the buisness hours