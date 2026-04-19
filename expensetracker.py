import csv
import os

if not os.path.exists("expense_details.csv"):
    with open("expense_details.csv", 'w', newline="") as f:
        w = csv.writer(f)
        w.writerow(['CATEGORY', 'AMOUNT'])


def add_expense(n):
        with open("expense_details.csv",'a',newline="") as f:
             w=csv.writer(f)
             for i in range(n):
                category=input("Enter category: ")
                amount=float(input("Enter amount: "))
                w.writerow([category.upper(),amount])
        print("All expenses are stored in CSV file")

def view_expense():
     with open("expense_details.csv",'r') as f:
          r=csv.reader(f)
          print("\n{:<15} {:<10}".format("CATEGORY", "AMOUNT"))
          print("-" * 25)
          next(r,None)
          for i in r:
            print("{:<15} {:<10}".format(i[0], i[1]))

def total_expense():
    sum_expenses=0
    with open("expense_details.csv",'r') as f:
        r=csv.reader(f)
        next(r,None)
        for rows in r:
            try:
                sum_expenses+=float(rows[1])
            except:
                continue
    print(f"TOTAL EXPENSE: {sum_expenses:.2f}")

def category_wise_sum(category):
    sum_category=0
    found=False
    with open("expense_details.csv",'r') as f:
        r=csv.reader(f)
        next(r,None)
        for amount in r:
            try:
                if(category.upper()==amount[0]):
                    sum_category+=float(amount[1])
                    found=True
            except:
                pass
        if(not found):
            print("No such category found")
        else:
            print(f"CATEGORY {category.upper()} TOTAL IS: {sum_category:.2f}")

def all_category_wise():
    details={}
    with open("expense_details.csv",'r') as f:
        r=csv.reader(f)
        next(r,None)
        for row in r:
            try:
                amount=float(row[1])
                if(row[0] not in details):
                    details[row[0]]=amount
                else:
                    details[row[0]]+=amount
            except:
                continue
    print("\nCATEGORY-WISE SPENDING:")
    print("-------------------------")
    for k, v in details.items():
        print(f"{k}: {v:.2f}")
        
#MENU UPDATING:

while(True):
    print("1.ADD EXPENSES")
    print("2.VIEW EXPENSES")
    print("3.TOTAL SUM OF EXPENSES")
    print("4.SUM OF EXPENSES CATEGORY WISE") 
    print("5.ALL CATEGORY WISE SUM")
    print("6.EXIT")
    try:
        choice=int(input("Enter your choice: ")) 
    except:
        print("Please enter valid number: ")
        continue

    if(choice==1):
        try:
            n=int(input("Enter number of expenses to add: "))
            add_expense(n)
        except:
            print("please enter valid number")
            continue

    elif(choice==2):
        print("EXPENSES ARE: ")
        view_expense()
    elif(choice==3):
        total_expense()
    elif(choice==4):
        cat=input("Enter category to find sum: ")
        category_wise_sum(cat)
    elif(choice==5):
        all_category_wise()
    elif(choice==6):
        print("Exiting")
        break
    else:
        print("Invalid choice...Try again:)")
