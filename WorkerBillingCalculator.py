print("Welcome to our application!")
print("This program calculates the total area and price for construction workers billing.\n")

 # أخذ اسم المستخدم
user_name = input("What is your name? \n")
print("Nice to meet you, " + user_name)

while True:  
   # إدخال القيم
    str_length = input("Please type length (in meters): \n")
    str_width = input("Please type width (in meters): \n")
    str_price = input("How much for 1 square meter? :\n")

    # تحويل المدخلات لأرقام
    length = float(str_length)
    width = float(str_width)
    price = float(str_price)

    # العمليات الحسابية
    area = length * width
    total_price = price * area

    # طباعة النتائج
    print("\nThe total area is: " + str(area) + " m²")
    print("Total price to pay: $" + str(total_price))

    # سؤال إذا كان يريد عملية أخرى
    again = input("\nDo you want to calculate another job? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for using the app. Goodbye!")
        break
