import design as s 
# calculation part
class account:
    balance=0

    def __init__(self):
        pass

    def add_money(self,add):
        self.balance += add
        print(f"\n\tYou successfully Cash In : {add} Tk in your account✅\n\tNow,Your total balance is:{self.balance} Tk AND")
        time=show_date_time()
        store_CashIN_trans(add,time)
    
    def withdraw_money(self,draw):
        
        if self.balance<=0:
            print(f"\tYou don't have enough balance\n\tYou have just {self.balance} Taka left")
        else:
            self.balance -= draw    
            print(f"\n\tYou successfully Cash Out : {draw} Tk from your account✅\n\tNow,Your total balance is:{self.balance} Tk AND")
            time=show_date_time()
            store_CashOUT_trans(draw,time)

    def check_money(self):
         print("\n\tYour total Balance is:",self.balance,"Taka")


# Show date and time
def show_date_time():
    from datetime import datetime
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print("\tTransaction date and time is :",formatted)
    return formatted

# Storing the Transaction information 
def store_CashIN_trans(money,time):
    f=open("Data.txt","a")
    f.write(f"Dear Sir,You just Cash IN: {money} Tk in you account on [{time}]\n")
    f.close()


def store_CashOUT_trans(money,time):
    f=open("Data.txt","a")
    f.write(f"Dear Sir,You jus Cash OUT: {money} Tk from your account on [{time}]\n")
    f.close()

    

#storing User and Password info
def store(all):
  f=open("Data.txt","a")
  f.write(f"Account ID -->1\n")
  for i in all:
   f.write(f"{i}\n")
  f.write("\n")
  f.close()


# matching part
def auto_call():
    s.inner_info()
    num=int(input("\t-->"))
    match num:
            case 1:
                add=int(input("\n\tEnter ammount:"))
                per1.add_money(add)
                s.back_to_menu()
                c=int(input("\t----->"))
                if c==1:
                    auto_call()
                else:
                    print("\tsuccessfully Logout ✅")
                    take_back()
            case 2:
                draw=int(input("\n\tEnter ammount:"))
                per1.withdraw_money(draw)
                s.back_to_menu()
                c=int(input("\t----->"))
                if c==1:
                   auto_call()
                else:
                   print("\tsuccessfully Logout ✅")
                   take_back()
            case 3:
                per1.check_money()
                s.back_to_menu()
                c=int(input("\t----->"))
                if c==1:
                   auto_call()
                else:
                   print("\tsuccessfully Logout ✅")
                   take_back()
            case 4:
                print("\tsuccessfully Logout ✅")
                take_back()
                
            case _:
                print("\n\tInvalid choice plz try again ")
                auto_call()
    


# object of an class
per1=account()

# Index style---
s.welcome()
ans=input("\tWrite down your choice here :").lower()

#if want to creat an account---

if ans=="yes":
    s.intro()
    user_name="Username: "+input("\tEnter your Username :").strip()
    password="Password: "+input("\tSet the Password:").strip()
    all=[user_name,password]
    store(all)
    s.after_creat()
    #USING this function to back to the login interface after logout.
    def take_back():
        print("\tDo you want to login your account?\n\n\tYes / No")
        take_input=input("\n\t--->").lower()

        # if want to login-----

        if take_input=="yes":
            take_name="Username: "+input("\n\tEnter your username :").strip()
            take_password="Password: "+input("\tGive your password:").strip()

            while (take_name!=user_name or take_password!=password):
                print("\nUsername or password is invalid plz try again \n")
                take_name="Username: "+input("\tEnter your username :").strip()
                take_password="Password: "+input("\tGive your password:").strip()
            
            print("\n\tlogin Succesfully ✅ \n")  
            print("\tSelect the category :") 
            auto_call()
        # if don't want to login--
        else:
            print("\t----Thank you----")
    take_back()
# if don't want to creat an account 
else:
    print("\n\t-----OOPS!! Hope for the next time-----\nThank you for visiting our Bank")
    

