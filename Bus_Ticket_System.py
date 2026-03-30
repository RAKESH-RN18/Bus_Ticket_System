print("-------BUs Ticket Discount-------")
gender=str(input("Enter your gender >> ").capitalize())
if gender == "Female":
    print("congrats yo get a fee Ticket")
if gender == "Male":
    age=int(input("Enter your age >> "))
    is_physically_abeled=input("Are you physically abeled.Say 'Yes' or 'No'>> ").capitalize()
    if is_physically_abeled =="Yes":
        print("You will get a Free Ticket")
    else:
        if age<5:
            print("Cograts,you get a child discount (free ticket)")
        elif age >=60 :
            print("you get a senior discount.")
        else:
            print("sorry you didn't get any discounts")
print("---$$$$$$$$$$$$$$$$$$$$$---")