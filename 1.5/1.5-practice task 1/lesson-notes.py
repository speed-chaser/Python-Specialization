class Date(object):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_date(self):
        output = str(self.day) + "/" + str(self.month) + "/" +  str(self.year)
        return output

    def set_date(self):
        self.day = int(input("Enter the day of the month: "))
        self.month = int(input("Enter the month: "))
        self.year = int(input("Enter the year: "))

    def is_leap_year(self):
        return self.year % 4 == 0
    
    def is_valid_date(self):
        if not (type(self.day) == int and type(self.month) == int and type(self.year) == int):
            return False
        
        if self.year < 0:
            return False
        
        if self.month < 1 or self.month > 12:
            return False
        
        last_dates = {
            1: 31,
            2: 29 if self.is_leap_year() else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if self.day < 1 or self.day > last_dates.get(self.month):
            return False
        

        return True
    
date1 = Date(29, 2, 2000)
date2 = Date(29, 2, 2001)
date3 = Date('abc', 'def', 'ghi')

print(str(date1.get_date()) + ": " + str(date1.is_valid_date()))
print(str(date2.get_date()) + ": " + str(date2.is_valid_date()))
print(str(date3.get_date()) + ": " + str(date3.is_valid_date()))

first_moon_landing = Date(20, 7, 1969)

print(first_moon_landing.get_date())

first_moon_landing.set_date()

print(first_moon_landing.get_date())
