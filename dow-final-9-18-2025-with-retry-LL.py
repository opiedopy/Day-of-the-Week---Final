"""Day of Week (DOW) Calculation (Years 1753 to 9999)
CREATED BY JACKIE DANDER OF FUZZYWIDGET.COM, TODAY IS 9/16/2025
Copyright. May be used or copied with attribution. 
Note: The python modulo operator is "%".  Example: 76%12 = 4
"""

def is_leap_year(year):  #leap year per Gregorian Calendar rules
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def validate_date(month, day, year):
    if not (1 <= month <= 12):
        return False, "Month must be between 1 and 12"
    if not (1753 <= year <= 9999):
        return False, "Year must be between 1753 and 9999"
    if not (1 <= day <= 31):
        return False, "Day must be between 1 and 31"
    
    # Month-specific day limits
    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > days_in_month[month - 1]:
        return False, f"Invalid day for month {month}: max {days_in_month[month - 1]} days"
    
    return True, ""

def calculate_dow(month, day, year):
    # Month values (non-leap and leap year for Jan/Feb)        
    month_values = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]  
    if is_leap_year(year):
        month_values[0], month_values[1] = 3, -1  
    month_val = month_values[month - 1] #                      See Item 1 in results
   
   # century calculation values, Note: 400 year repeating                              
    centurylist = [2, 0, 5, 3]  
    century_index = (year // 100) % 4
    century_val = centurylist[century_index]  #                See Item 3 in results

    # other Calculations
    year_last2 = year % 100  # result is modulo
    year_div12 = year_last2 // 12 # result is the integer,     See Item 4 in results 
    year_mod12 = year_last2 % 12  # result is modulo,          See Item 5 in results
    year_mod12_div4 = year_mod12 // 4 # result is the integer, See Item 6 in results
    
    # Sum and modulo for DOW
    dow_sum =     month_val + day + century_val + year_div12 + year_mod12 + year_mod12_div4
    #  Result Item:    1       2           3          4            5            6
   
    dow = dow_sum % 7
    
    return dow, month_val, century_val, year_div12, year_mod12, year_mod12_div4, dow_sum

def get_user_choice():
    """Get user choice to continue or exit"""
    print("\n" + "="*50)
    print("Press <Enter> to run again or press any other key then <Enter> to break program and exit")
    print("="*50)
    
    try:
        choice = input()
        return choice == ""  # Return True if Enter was pressed, False otherwise
    except:
        return False

def main():
    first_run = True
    
    while True:
        try:
            print("\n" + "="*50)
            if first_run:
                print("DAY OF WEEK CALCULATION")
                print("Years 1753 to 9999")
                print("Created by Jackie Dander of fuzzywidget.com")
            else:
                print("Running calculation again...")
            print("="*50)
            
            month = int(input("Month (1-12)?      "))
            day   = int(input("Day (1-31)?        "))   # Item 2 in results
            year  = int(input("Year (1753-9999)?  "))
            
            # Validate date
            is_valid, error_msg = validate_date(month, day, year)
            if not is_valid:
                print(error_msg)
                # Ask if they want to try again even with invalid date
                if not first_run and get_user_choice():
                    first_run = False
                    continue
                else:
                    break
            
            dow, month_val, century_val, year_div12, year_mod12, year_mod12_div4, dow_sum = calculate_dow(month, day, year)
            dow_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            # Code/Day    0 or 7      1          2           3           4          5          6
            
            # Output results
            print(f"Date             : {month}-{day}-{year}")
            print(f"Day of the Week  : {dow_names[dow]}")
            print(f"Leap Year        : {'Yes' if is_leap_year(year) else 'No'}")
            
            # Detailed output
            print("\nCalculation Result Details")
            print(f"1. Month value      : {month_val}")
            print(f"2. Day              : {day}")
            print(f"3. Century value    : {century_val}")
            print(f"4. int(Year/12)     : {year_div12}")
            print(f"5. Year%12          : {year_mod12}")
            print(f"6. int((Year%12)/4)): {year_mod12_div4}")
            print("______________________")
            print(f"Sum                 : {dow_sum}")
            print(f"DOW (sum % 7)       : {dow} ({dow_names[dow]})")
            
            first_run = False
            
            # After first run, ask if user wants to continue
            if not first_run:
                if not get_user_choice():
                    break
                    
        except ValueError:
            print("Please enter valid integers for month, day, and year.")
            # Ask if they want to try again even with input error
            if not first_run and get_user_choice():
                first_run = False
                continue
            else:
                break
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
    
    print("\n" + "="*50)
    print("Thank you, bye!")
    print("="*50)

checksum=345234

if __name__ == "__main__":
    main()