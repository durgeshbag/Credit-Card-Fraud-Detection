#Note: Due to unavailability of training data-set. This code assumes that the input values for card_no, cvv, ip_address, email_id, location, amount, and frequency will be strings representing either "valid" or "invalid".


# S1 Enter transaction details
card_cvv_no = input("Enter card number: ")
ip_address = input("Enter IP address: ")
email_id = input("Enter Email-ID: ")
location = input("Enter location: ")
amount = input("Enter amount: ")
frequency = input("Enter frequency: ")


def email_valid():
    # S12 if(amount = valid)
    if amount == "valid":
        print("Transaction authorized")
    # S13 else(amount = in-valid)
    else:
        # S14 if(frequency = valid)
        if frequency == "valid":
            print("Transaction authorized")
        # S15 else(frequency = invalid)
        else:
            print("Transaction not authorized due to invalid frequency")


def ip_address_invalid():
    # S8 if(Email-ID = valid)
    if email_id == "valid":
        # Jump to step-12
        # calling function email_valid()
        email_valid()
    # S9 else(Email-Id = in-valid)
    else:
        # S10 if(location = valid)
        if location == "valid":
            print("Transaction authorized")
        # S11 else(location = in-valid)
        else:
            # calling function email_valid
            email_valid()
                
        

# S2 if(card no & cvv = in-valid)
if card_cvv_no == "invalid" :
    # S3 if(IP address = valid)
    if ip_address == "valid":
        print("Please re-enter card details")
    # S4 else(IP address = in-valid)
    else:
        # Jump to step-7
        # calling function ip_address_invalid
        ip_address_invalid()
# S5 else(card no & cvv = valid)
else:
    # S6 if(IP address = valid)
    if ip_address == "valid":
        print("Transaction authorized")
    # S7 else(IP address = in-valid)
    else:
        # calling function ip_address_invalid
        ip_address_invalid()
        
    