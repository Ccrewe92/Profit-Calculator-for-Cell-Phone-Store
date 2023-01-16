#Clinton Crewe
#October - 20 - 2022
#A program to calculate the daily profit for Circle Phones.


# INDEPENDENT VARIABLES #


product_table = {'apple_iphone' : 120.45,'android_phone' : 99.50,'apple_tablet' : 75.69,'android_tablet' : 65.73,'windows_tablet' : 51.49}

day_of_week = ['Monday', 'Tesuday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

daily_profit = 0

# LOOP FOR CALCULATION OF DAILY PROFITS #


print("\n Welcome to Circle Phones Profit calculator.")
print("\n 1= One Day \n 2= One Week \n 3= Week of Business Days \n 4= Weekend")

running = True
while running:
    sales_period = int(input("Enter time period for sales data [1-4]:  "))
    if sales_period == 1:
        specific_day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
        print('For:', specific_day)
        for day in range(sales_period):
            while True: 
                print("\n 1= Apple Iphone \n 2= Android Phone \n 3= Apple Tablet \n 4= Android Tablet \n 5= Windows Tablet")
                product_catagory = int(input("Enter product number 1-5, or enter 0 to stop:  "))
                if product_catagory == 0:
                    print('Total Profit in $CDN for', specific_day, 'is:', daily_profit)
                    break
                
                quantity = int(input("Enter quantity sold:"  ))
                if   product_catagory == 1:
                    daily_profit += product_table['apple_iphone'] * quantity 
                elif product_catagory == 2:
                    daily_profit += product_table['android_phone'] * quantity
                elif product_catagory == 3:
                    daily_profit += product_table['apple_tablet'] * quantity 
                elif product_catagory == 4:
                    daily_profit += product_table['android_tablet'] * quantity
                elif product_catagory == 5:
                    daily_profit += product_table['windows_tablet'] * quantity
                    
                else:
                    print("Product catagory should be 0-5, no other number")
        if daily_profit >= 10000:
            print('You did well this period! Keep up the great work!')
        else:
            print('We did not reach our goal for this period. More work is needed.')            

        running = False
    
    elif sales_period == 2:
        for day in range(len(day_of_week)):
            print(day_of_week[day])
            while True: 
                print("\n 1= Apple Iphone \n 2= Android Phone \n 3= Apple Tablet \n 4= Android Tablet \n 5= Windows Tablet")
                product_catagory = int(input("Enter product number 1-5, or enter 0 to stop:  "))
                if product_catagory == 0:
                    #print(daily_profit)
                    break
                
                quantity = int(input("Enter quantity sold:"))
                if   product_catagory == 1:
                    daily_profit += product_table['apple_iphone'] * quantity 
                elif product_catagory == 2:
                    daily_profit += product_table['android_phone'] * quantity
                elif product_catagory == 3:
                    daily_profit += product_table['apple_tablet'] * quantity 
                elif product_catagory == 4:
                    daily_profit += product_table['android_tablet'] * quantity
                elif product_catagory == 5:
                    daily_profit += product_table['windows_tablet'] * quantity
                    
                else:
                    print("Product catagory should be 0-5, no other number")
        print('Total Profit for the week is $CDN:', daily_profit )
        if daily_profit >= 10000:
            print('You did well this period! Keep up the great work!')
        else:
            print('We did not reach our goal for this period. More work is needed.')

        running = False
    
    elif sales_period == 3:
        for day in range (0,5,1):
            print(day_of_week[day])
            while True: 
                print("\n 1= Apple Iphone \n 2= Android Phone \n 3= Apple Tablet \n 4= Android Tablet \n 5= Windows Tablet")
                product_catagory = int(input("Enter product number 1-5, or enter 0 to stop:  "))
                if product_catagory == 0:
                    #print(daily_profit)
                    break
                
                quantity = int(input("Enter quantity sold:  "))
                if   product_catagory == 1:
                    daily_profit += product_table['apple_iphone'] * quantity 
                elif product_catagory == 2:
                    daily_profit += product_table['android_phone'] * quantity
                elif product_catagory == 3:
                    daily_profit += product_table['apple_tablet'] * quantity 
                elif product_catagory == 4:
                    daily_profit += product_table['android_tablet'] * quantity
                elif product_catagory == 5:
                    daily_profit += product_table['windows_tablet'] * quantity
                    
                else:
                    print("Product catagory should be 0-5, no other number")
        print('Total Profit for the business days is $CDN:', daily_profit )
        if daily_profit >= 10000:
            print('You did well this period! Keep up the great work!')
        else:
            print('We did not reach our goal for this period. More work is needed.')
        
        running = False
    
    
    elif sales_period == 4:
        for day in range(5,7,1):
            print(day_of_week[day])
            while True: 
                print("\n 1= Apple Iphone \n 2= Android Phone \n 3= Apple Tablet \n 4= Android Tablet \n 5= Windows Tablet")
                product_catagory = int(input("Enter product number 1-5, or enter 0 to stop:  "))
                if product_catagory == 0:
                    #print(daily_profit)
                    break
                
                quantity = int(input("Enter quantity sold:  "))
                if   product_catagory == 1:
                    daily_profit += product_table['apple_iphone'] * quantity 
                elif product_catagory == 2:
                    daily_profit += product_table['android_phone'] * quantity
                elif product_catagory == 3:
                    daily_profit += product_table['apple_tablet'] * quantity 
                elif product_catagory == 4:
                    daily_profit += product_table['android_tablet'] * quantity
                elif product_catagory == 5:
                    daily_profit += product_table['windows_tablet'] * quantity
                    
                else:
                    print("Product catagory should be 0-5, no other number")
        print('Total Profit for the weekend is $CDN:', daily_profit )
        if daily_profit >= 10000:
            print('You did well this period! Keep up the great work!')
        else:
            print('We did not reach our goal for this period. More work is needed.')
        
        running = False
    
    else:
        break
