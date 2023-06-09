#Note: Due to unavailability of training data-set. This code assumes that the input values for transaction_type, pin, ip_address, amount, and frequency will be strings representing either "valid" or "invalid".


# S1 Enter transaction details
transaction_type = input("Enter transaction type (TouchPay/SwipePay): ")
pin = input("Enter PIN: ")
ip_address = input("Enter IP address: ")
amount = input("Enter amount: ")
frequency = input("Enter frequency: ")

def valid_pin():
    # S4 if(ip-address = valid)
        if ip_address == "valid":
            print("Transaction authorized")
        # S5 else(ip-address = in-valid)
        else:
            # S6 if(amount = valid)
            if amount == "valid":
                # S7 if(frequency = valid)
                if frequency == "valid":
                    print("Transaction authorized")
                # S8 else(frequency = in-valid)
                else:
                    print("Transaction not authorized due to invalid frequency")
            # S9 else(amount = in-valid)
            else:
                print("Transaction not authorized due to amount exceeded alert")



def swipe_pay():
    # S3 if(pin = valid)
    if pin == "valid":
        # calling function valid_pin
        valid_pin()
    # S10 else(pin = in-valid)
    else:
        # S11 if(ip-address = in-valid)
        if ip_address == "in-valid":
            print("Transaction not authorized due to fraud")
        # S12 else(ip-address = valid)
        else:
            #S13 if(re-entered pin = valid)
            reentered_pin = input("Re-enter PIN: ")
            if reentered_pin == "valid":
                # Jump to step -S3
                # calling function valid_pin
                valid_pin()
            # S14 else(re-entered pin = in-valid)
            else:
                print("Transaction not authorized due to fraud")





# S2 if(transactionType = swipePay)
if transaction_type == "SwipePay":
   # calling function swipe_pay
   swipe_pay()
# S15 else(transactionType = touchPay)
else:
    # Jump to step-4
    valid_pin()


