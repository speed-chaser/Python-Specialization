class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inch"
    
    def __sub__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        # subtracting
        total_height_inches = height_A_inches - height_B_inches

        # output in feet
        output_feet = total_height_inches // 12

        # output in inches
        output_inches = total_height_inches % 12

        return Height(output_feet, output_inches)
    
    def __gt__(self, other):
        return (self.feet * 12 + self.inches) > (other.feet * 12 + other.inches)

    def __ge__(self, other):
        return (self.feet * 12 + self.inches) >= (other.feet * 12 + other.inches)
    
    def __ne__(self, other):
        return(self.feet * 12 + self.inches) != (other.feet * 12 + other.inches)
    
    
person_A_height = Height(5, 10)
person_B_height = Height(3, 9)
height_difference = person_A_height - person_B_height

print("Total height:", height_difference)
print(Height(4, 6) > Height(4, 5))   
print(Height(4, 5) >= Height(4, 5))  
print(Height(5, 9) != Height(5, 10)) 