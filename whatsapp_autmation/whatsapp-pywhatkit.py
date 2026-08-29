import pywhatkit


phone_number = input("enter phone number = ")

# Add '+' if missing
if not phone_number.startswith("+"):
    phone_number = "+91" + phone_number
pywhatkit.sendwhatmsg(phone_number,"Test" , 21 , 58 ,wait_time=20, tab_close=True , close_time=3)

group_id = input("enter group id = ")
pywhatkit.sendwhatmsg_to_group(group_id , "hoii" , 22 , 7)