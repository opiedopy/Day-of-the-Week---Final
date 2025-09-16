"""Day of Week (DOW) Calculation (Years 1753 to 9999)
CREATED BY JACKIE DANDER OF FUZZYWIDGET.COM, TODAY IS 9/15/2025
"""

def is_leap_year(year):
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
    # Month adjustment values (non-leap and leap year for Jan/Feb)
    month_values = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]  
    if is_leap_year(year):
        month_values[0], month_values[1] = 3, -1  
    
    centurylist = [2, 0, 5, 3]  
    century_index = (year // 100) % 4
    century_val = centurylist[century_index] 

    # Calculations
    year_last2 = year % 100  # result is modulo
    month_val = month_values[month - 1]
    year_div12 = year_last2 // 12 # result is the integer
    year_mod12 = year_last2 % 12  # result is modulo
    year_mod12_div4 = year_mod12 // 4 # result is the integer 
    
    # Sum and modulo for DOW
    dow_sum = month_val + day + century_val + year_div12 + year_mod12 + year_mod12_div4
    dow = dow_sum % 7
    
    return dow, month_val, century_val, year_div12, year_mod12, year_mod12_div4, dow_sum

def main():

    try:
        month = int(input("Month (1-12)?      "))
        day = int(input("Day (1-31)?        "))
        year = int(input("Year (1753-9999)?  "))
        
        # Validate date
        is_valid, error_msg = validate_date(month, day, year)
        if not is_valid:
            print(error_msg)
            return
        
        dow, month_val, century_val, year_div12, year_mod12, year_mod12_div4, dow_sum = calculate_dow(month, day, year)
        dow_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        # Output results
        print(f"Date             : {month}-{day}-{year}")
        print(f"Day of the Week  : {dow_names[dow]}")
        print(f"Leap Year        : {'Yes' if is_leap_year(year) else 'No'}")
        
        # Detailed output
        print("\nCalculation Details")
        print(f"1. Month value      : {month_val}")
        print(f"2. Day              : {day}")
        print(f"3. Century value    : {century_val}")
        print(f"4. int(Year/12)     : {year_div12}")
        print(f"5. Year%12          : {year_mod12}")
        print(f"6. int((Year%12)/4)): {year_mod12_div4}")
        print("______________________")
        print(f"Sum                 : {dow_sum}")
        print(f"DOW (sum % 7)       : {dow} ({dow_names[dow]})")
        
    except ValueError:
        print("Please enter valid integers for month, day, and year.")

if __name__ == "__main__":
    main()
