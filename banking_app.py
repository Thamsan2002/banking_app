# Customer Registration  --------------------------------------------

def Customer_Details_Get():
    
    First_Name=input("Enter Your First Name:")
    Last_Name=input("Enter Your Last Name:")
    Date_Of_Birth=input("Enter Your Date Of Birth(Eg:-Year/Month/Date):")
    Age=int(input("Enter Your Age:"))
    Gender=input("Enter Your Gender:")
    NIC_No=input("Enter Your NIC Number:")
    Address=input("Enter Your Address:")
    G_Mail=input("Enter Your Gmail Address:")
    Mobile_NO=int(input("Enter Your Mobile Number:"))
    Customer_Details=[First_Name,Last_Name,Date_Of_Birth,Age,Gender,NIC_No,Address,Mobile_NO,G_Mail]
    return(Customer_Details)

def Customer_Details_Save():
    Customer_Details=Customer_Details_Get()
    from datetime import datetime
    date_and_time=datetime.now()
    DATE_AND_TIME=date_and_time.strftime("%Y-%m-%d   %H:%M:%S")
    import os
    Customer_Personal_File="Customer_Personal_Details.txt"
    if os.path.exists(Customer_Personal_File):
        with open("Customer_Personal_Details.txt","r+") as file:
            Last_Line=file.readlines()[-1]
            Last_Used_Customer_Id=Last_Line.split("   ")[2]
            Next_Customer_Id=(f"CU{str(int(Last_Used_Customer_Id[2:])+1)}")
            file.write(f"{DATE_AND_TIME}   {Next_Customer_Id}   {Customer_Details[0]}   {Customer_Details[1]}   {Customer_Details[2]}   {Customer_Details[3]}   {Customer_Details[4]}   {Customer_Details[5]}   {Customer_Details[6]}   {Customer_Details[7]}   {Customer_Details[8]}\n")
    else:
        with open("Customer_Personal_Details.txt","w") as file:
            file.write(f"{DATE_AND_TIME}   CU100   {Customer_Details[0]}   {Customer_Details[1]}   {Customer_Details[2]}   {Customer_Details[3]}   {Customer_Details[4]}   {Customer_Details[5]}   {Customer_Details[6]}   {Customer_Details[7]}   {Customer_Details[8]}\n")
           
# Customer_Details_Save()

# --------------------------------------------------------------
# Account Creation----------------------------------------------

def Account_Creation():
    NIC_No=int(input("Enter Your NIC Number:"))
    Initial_Balance=float(input("Enter Your Deposite Amount:"))
    from datetime import datetime
    date_and_time=datetime.now()
    DATE_AND_TIME=date_and_time.strftime("%Y-%m-%d   %H:%M:%S")
    pass_code=str(NIC_No)[-5:-1]
    with open("Customer_Personal_Details.txt","r") as file:
            Lines=file.readlines()
    for Line in Lines:
        if str(NIC_No) in Line.split("   "):
            User_Name=Line.split("   ")[4]
            User_Id=Line.split("   ")[2]
    import os
    Account_file="Account_Details.txt"
    if os.path.exists(Account_file):
        with open("Account_Details.txt","r+") as file:
            Last_Line=file.readlines()[-1]
            Last_Allocated_Accont_No=Last_Line.split("   ")[3]
            New_Account_no=str(int(Last_Allocated_Accont_No)+1)
            file.write(f"{DATE_AND_TIME}   {User_Id}   {New_Account_no}   {Initial_Balance}\n")
        with open("Login_Informations.txt","r") as file:
            lines=file.readlines()
        User_Ids=[]
        User_Names=[]
        for line in lines:
            User_Ids.append(line.split("   ")[0])
            User_Names.append(line.split("   ")[1])
        if User_Id not in User_Ids:
            if User_Name in User_Names:
                while True:
                    print("...This Customer Name Already Taken To Youser Name!...")
                    New_User_Name=input("Enter a New UserName:")
                    if New_User_Name in User_Names:
                        print("...This UserName Already Taken!...\n...Try Another One...")
                    else:
                        with open("Login_Informations.txt","a") as file:
                            file.write(f"{User_Id}   {New_User_Name}   {pass_code}\n")
                            print(f"...Successfully Account Created...\n...Your Account Number Is:{New_Account_no}...\n...Your UserName Is:{User_Name}...\n...Your PassCode Is:{pass_code}...")
                            break
            else:
                with open("Login_Informations.txt","a") as file:
                    file.write(f"{User_Id}   {User_Name}   {pass_code}\n")
                print(f"...Successfully Account Created...\n...Your Account Number Is:{New_Account_no}...\n...Your UserName Is:{User_Name}...\n...Your PassCode Is:{pass_code}...")
        
    else:
        New_Account_no=10000
        with open("Account_Details.txt","a") as file:
            file.write(f"{DATE_AND_TIME}   {User_Id}   {New_Account_no}   {Initial_Balance}\n")
        with open("Login_Informations.txt","w") as file:
            file.write(f"{User_Id}   {User_Name}   {pass_code}\n")
        print(f"...Successfully Account Created...\n...Your Account Number Is:{New_Account_no}...\n...Your UserName Is:{User_Name}...\n...Your PassCode Is:{pass_code}...")
    with open("Transaction_History.txt","a") as file:
        file.write(f"{User_Id}   {DATE_AND_TIME}   {New_Account_no}   +{Initial_Balance}   {Initial_Balance}\n")
    
# Account_Creation()

# --------------------------------------------------------------
# Getting Customer Id-------------------------------------------
def Getting_Customer_Id():
    with open("Login_Informations.txt","r") as file:
        Lines=file.readlines()
    for Line in Lines:
        if User_Name in Line:
            Customer_Id=Line.split("   ")[0]
    return Customer_Id
# --------------------------------------------------------------
# Show Customer Accounts----------------------------------------
def Show_Customer_Accounts(Customer_Id):
    Accounts=[]
    with open("Account_Details.txt","r") as file:
        lines=file.readlines()
    for line in lines:
        if Customer_Id in line.split("   "):
            Accounts.append(line.split("   ")[3])
            print(f"Your Account Number is:{line.split("   ")[3]}")
    return lines,Accounts
# --------------------------------------------------------------
# Changing Username&Password------------------------------------

def Changing_Username_Password():
    Customer_Id=Getting_Customer_Id()
    Read_Lines=[]
    All_Usernames=[]
    with open("Login_Informations.txt","r") as file:
        Lines=file.readlines()
        for Line in Lines:
            All_Usernames.append(Line.split("   ")[1])
            if Customer_Id in Line.split("   "):
                Old_Username=Line.split("   ")[1]
                Old_Passcode=Line.split("   ")[2]
    while True:
        print("   1.Change Your Username\n   2.Change Your Passcode\n   3.Change UserName & PassCode\n   4.Exit")
        Choice=int(input("Enter Your Choice:"))
        if Choice==1:
            while True:
                New_Username=input("Enter Your New User Name:")
                if New_Username in All_Usernames:
                        print("This UserName Already Taken\nTry Another One")
                else:
                    while True:
                        Pass_Code=int(input("Enter Your Passcode:"))
                        if str(Pass_Code)==Datas[-1]:
                            for Line in Lines:
                                if Customer_Id in Line.split("   "):
                                    Read_Lines.append(f"{Customer_Id}   {New_Username}   {Old_Passcode}")
                                else:
                                    Read_Lines.append(Line)
                            with open("Login_Informations.txt","w")as file:
                                file.writelines(Read_Lines)
                            print(f"...Username Successfully Changed...\nYour New UserName Is:{New_Username}\n...please Login With New UserName...")
                            break
                        else:
                            print("...Your PassCode Is Wrong!...\n...Try Again..")
                    break
            break
        elif Choice==2:
            while True:
                New_Passcode1=input("Enter Your New Passcode:")
                New_Passcode2=input("Re Your New Passcode:")
                if New_Passcode1==New_Passcode2:
                    while True:
                        Pass_Code=int(input("Enter Your Old Passcode:"))
                        if str(Pass_Code)==Datas[-1]:
                            for Line in Lines:
                                if Customer_Id in Line.split("   "):
                                    Read_Lines.append(f"{Customer_Id}   {Old_Username}   {New_Passcode1}")
                                else:
                                    Read_Lines.append(Line)
                            with open("Login_Informations.txt","w")as file:
                                file.writelines(Read_Lines)
                            print(f"...PassCode Successfully Changed...\nYour New PassCode: {New_Passcode1}\n...please Login With New PassCode...")
                            break
                        else:
                            print("...Your PassCode Is Wrong!...\n...Try Again..")
                    break
                else:
                    print("...PassCode Not Matching...\n...Try Again...")
            break
        elif Choice==3:
            while True:
                New_Username=input("Enter Your New User Name:")
                if New_Username in All_Usernames:
                        print("This UserName Already Taken\nTry Another One")
                else:
                    while True:
                        New_Passcode1=input("Enter Your New Passcode:")
                        New_Passcode2=input("Re Your New Passcode:")
                        if New_Passcode1==New_Passcode2:
                            while True:
                                Pass_Code=int(input("Enter Your Old Passcode:"))
                                if str(Pass_Code)==Datas[-1]:
                                    for Line in Lines:
                                        if Customer_Id in Line.split("   "):
                                            Read_Lines.append(f"{Customer_Id}   {New_Username}   {New_Passcode1}")
                                        else:
                                            Read_Lines.append(Line)
                                    with open("Login_Informations.txt","w")as file:
                                        file.writelines(Read_Lines)
                                    print(f"...Username & PassCode Successfully Changed...\nYour New UserName Is:{New_Username}\nYour New PassCode: {New_Passcode1}\n...please Login With New UserName...")
                                    break
                                else:
                                    print("...Your PassCode Is Wrong!...\n...Try Again...")
                            break
                        else:
                            print("...PassCode Not Matching...\n...Try Again...")
                    break
            break
        elif Choice==4:
            break
# --------------------------------------------------------------
# Deposite -----------------------------------------------------

def Deposite(Datas,lines,Accounts):
    Accont_No=int(input("Enter Your Account Number:"))
    if str(Accont_No) in Accounts:
        Deposite_Money=float(input("Enter Your Deposite Ammount:"))
        if Deposite_Money>0:
            Pass_Code=int(input("Enter Your Passcode:"))
            if str(Pass_Code)==Datas[-1]:
                updated_line=[]
                for Needed_line in lines:
                    if str(Accont_No) in Needed_line:
                        Datas_in_line=Needed_line.strip().split("   ")
                        Current_balance=Datas_in_line[4]
                        New_balance=str(float(Current_balance)+Deposite_Money)
                        updated_line.append(f"{Datas_in_line[0]}   {Datas_in_line[1]}   {Datas_in_line[2]}   {Datas_in_line[3]}   {New_balance}\n")
                        from datetime import datetime
                        date_and_time=datetime.now()
                        DATE_AND_TIME=date_and_time.strftime("%Y-%m-%d   %H:%M:%S")
                        with open("Transaction_History.txt","a") as file:
                            file.write(f"{Datas_in_line[2]}   {DATE_AND_TIME}   {Datas_in_line[3]}   +{Deposite_Money}   {New_balance}\n")
                    else:
                        updated_line.append(Needed_line)
                with open("Account_Details.txt","w") as file:
                    file.writelines(updated_line)
            else:
                print("...Your PassCode Is Wrong...")
        else:
            print("...Enter a Valid Amount!...")
    else:
        print("...Account Number Is Wrong...")
# --------------------------------------------------------------
# Customer Deposite---------------------------------------------
def Customer_Deposite(Datas):
    Customer_Id=Getting_Customer_Id()
    lines,Accounts=Show_Customer_Accounts(Customer_Id)
    Deposite(Datas,lines,Accounts)
# --------------------------------------------------------------
# Getting All_Accounts For Admin--------------------------------
def Getting_All_Accounts():
    Accounts=[]
    with open("Account_Details.txt","r") as file:
        lines=file.readlines()
        for line in lines:
            Accounts.append(line.split("   ")[3])
    return lines,Accounts
# --------------------------------------------------------------
# Admin Deposite------------------------------------------------
def Admin_Deposite(Datas):
    lines,Accounts=Getting_All_Accounts()
    Deposite(Datas,lines,Accounts)
    
# --------------------------------------------------------------
# Withdrawal----------------------------------------------------

def Withdrawal(Datas,lines,Accounts):
    Accont_No=int(input("Enter Your Account Number:"))
    if str(Accont_No) in Accounts:
        Withdrawal_Money=float(input("Enter Your Withdrawal Ammount:"))
        if Withdrawal_Money>0:
            Pass_Code=int(input("Enter Your Passcode:"))
            if str(Pass_Code)==Datas[-1]:
                updated_line=[]
                for Needed_line in lines:
                    if str(Accont_No) in Needed_line:
                        Datas_in_line=Needed_line.strip().split("   ")
                        Current_balance=Datas_in_line[4]
                        if str(Withdrawal_Money)<=Current_balance:
                            New_balance=str(float(Current_balance)-Withdrawal_Money)
                            updated_line.append(f"{Datas_in_line[0]}   {Datas_in_line[1]}   {Datas_in_line[2]}   {Datas_in_line[3]}   {New_balance}\n")
                            from datetime import datetime
                            date_and_time=datetime.now()
                            DATE_AND_TIME=date_and_time.strftime("%Y-%m-%d   %H:%M:%S")
                            with open("Transaction_History.txt","a") as file:
                                file.write(f"{Datas_in_line[2]}   {DATE_AND_TIME}   {Datas_in_line[3]}   -{Withdrawal_Money}   {New_balance}\n")
                        else:
                            print("...Insiffience Balance...")
                    else:
                        updated_line.append(Needed_line)
                with open("Account_Details.txt","w") as file:
                    file.writelines(updated_line)
            else:
                print("...Your PassCode Is Wrong...")
        else:
            print("...Enter a Valid Amount!...")
    else:
        print("...Account Number Is Wrong...")
# --------------------------------------------------------------
# Customer Withdrawal-------------------------------------------
def Customer_Withdrawal(Datas):
    Customer_Id=Getting_Customer_Id()
    lines,Accounts=Show_Customer_Accounts(Customer_Id)
    Withdrawal(Datas,lines,Accounts)
# --------------------------------------------------------------
# Admin Withdrawal----------------------------------------------
def Admin_Withdrawal(Datas):
    lines,Accounts=Getting_All_Accounts()
    Withdrawal(Datas,lines,Accounts)
# --------------------------------------------------------------
# View Customer Details-----------------------------------------
def View_Customer_Detailes():
    with open("Customer_Personal_Details.txt","r") as file:
        Lines=file.readlines()
    while True:
        print("   1.Get Customer Id\n   2.View Customer Personal Details\n   3.View Customer Login Info\n   4.Back To Admin Menu")
        admin_choice=int(input("Enter Your Choice:"))
        if admin_choice==1:
            NIC_No=int(input("Enter Your NIC Number:"))
            for Line in Lines:
                if str(NIC_No) in Line.split("   "):
                    print(f"{NIC_No} Your Customer Id Is:{Line.split("   ")[2]}")
                    break
            else:
                print(f"{NIC_No} is Not Registered Customer")
        elif admin_choice==2:
            Customer_Id=(input("Enter The Customer Id:"))
            for Line in Lines:
                if str(Customer_Id) in Line.split("   "):
                    print(Line)
                    break
            else:
                print("...Incorrect Customer Id")                           
        elif admin_choice==3:
            Customer_Id=(input("Enter The Customer Id:"))
            with open("Login_Informations.txt","r") as file:
                lines=file.readlines()
            for line in lines:
                if Customer_Id in line.split("   "):
                    print(f"Id:{Customer_Id}   UserName:{line.split("   ")[1]}   PassCode:{line.split("   ")[2]}")
                    break
            else:
                print("...Incorrect Customer Id")
        elif admin_choice==4:
            break
        else:
            print("...Invalid Choice!...")        
# --------------------------------------------------------------
# Update Customer-----------------------------------------------
# --------------------------------------------------------------
# Show Account Balance------------------------------------------
def Show_Account_Balance(Customer_Id):
    with open("Account_Details.txt","r") as file:
        Lines=file.readlines()
    for Line in Lines:
        if Customer_Id in Line.split("   "):
            print(f"Your Account {Line.split("   ")[3]} Balance is:{Line.split("   ")[4]}")
        
# --------------------------------------------------------------
# Transaction History-------------------------------------------
def Transaction_HIstory(Customer_Id):
    with open("Transaction_History.txt","r") as file:
        Lines=file.readlines()
    while True:
        print("1.All Transactions\n2.Transactions By Account\n3.Back To  Menu")
        Transaction_Choice=int(input("Enter Your Choic:"))
        if Transaction_Choice==1:
            for Line in Lines:
                if Customer_Id in Line.strip().split("   "):
                    Datas_in_Line=Line.strip().split("   ")
                    print(f"{Datas_in_Line[1]}   {Datas_in_Line[2]}   {Datas_in_Line[3]}   {Datas_in_Line[4]}   {Datas_in_Line[5]}")
        elif Transaction_Choice==2:
            Show_Customer_Accounts(Customer_Id)
            Accont_No=int(input("Enter Your Account Number:"))
            for Line in Lines:
                if str(Accont_No) in Line.strip().split("   "):
                    print(f"{Datas_in_Line[1]}   {Datas_in_Line[2]}   {Datas_in_Line[3]}   {Datas_in_Line[4]}   {Datas_in_Line[5]}")
        elif Transaction_Choice==3:
            break
        else:
            print("...Invalid Input...")

# --------------------------------------------------------------
# Admin-Menu-Driven Interface-----------------------------------

def Admin_Menu():
    while True:
        print("1.Customer Registration\n2.Account Creation\n3.Deposite Money\n4.Withdraw Money\n5.View Customer Details\n6.Check Account Balance\n7.View Transaction History\n")
        Admin_Response=int(input("Enter Your Choice:"))
        if Admin_Response==1:
            Customer_Details_Save()
        elif Admin_Response==2:
            Account_Creation()
        elif Admin_Response==3:
            Admin_Deposite("1234")
        elif Admin_Response==4:
            Admin_Withdrawal("1234")
        elif Admin_Response==5:
            View_Customer_Detailes()
        elif Admin_Response==6:
            Customer_Id=input("Enter The Customer Id:")
            Show_Account_Balance(Customer_Id)
        elif admin_choice==7:
            Customer_Id=input("Enter The Customer Id:")
            Transaction_HIstory(Customer_Id)

        
# --------------------------------------------------------------
# Customer-Menu-Driven Interface--------------------------------

def Customer_Menu(Datas):
    while True:
        print("1.Change UserName Or PassCode\n2.Deposite Money\n3.Withdraw Ammount\n4.Check Balance\n5.Transaction History\n6.Exit")
        Customer_Response=int(input("Enter Your Choice:"))
        if Customer_Response==1:
            Changing_Username_Password()
            break   
        elif Customer_Response==2:
            Customer_Deposite(Datas)
        elif Customer_Response==3:
            Customer_Withdrawal(Datas)
        elif Customer_Response==4:
            Customer_Id=Getting_Customer_Id()
            Show_Account_Balance(Customer_Id)
        elif Customer_Response==5:
            Customer_Id=Getting_Customer_Id()
            Transaction_HIstory(Customer_Id)
        elif Customer_Response==6:
            break
        else:
            print("...Invalid Input...")

            
# --------------------------------------------------------------
# Main_Menu-----------------------------------------------------

while True:
    import os
    Customer_file="Customer_Personal_Details.txt"
    if os.path.exists(Customer_file):
        print("...Welcome Mini Banking...")
        User_Name=input("Enter Your Username:")
        Pass_Code=int(input("Enter Your Passcode:"))
        if User_Name=="admin" and Pass_Code==1234:
                 Admin_Menu()
        with open("Login_Informations.txt","r") as file:
            Lines=file.readlines()
            for Line in Lines:
                Datas=Line.strip().split("   ")
                if User_Name==Datas[-2] and str(Pass_Code)==Datas[-1]:
                    Customer_Menu(Datas)
                    break
            else:
                print("Incorrect UserName Or PassCode")
            
        
        
    else:
        print("...Welcome Mini Banking...")
        print("User_Name:-admin , pass code:-1234")
        User_Name=input("Enter Your Username:")
        Pass_Code=int(input("Enter Your Passcode:"))
        if User_Name=="admin" and Pass_Code==1234:
            Admin_Menu()
        else:
            print("...Incorrect User_Name! or Pass_Code!...")

# --------------------------------------------------------------