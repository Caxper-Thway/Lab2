

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    bmi = weight/(height * height)
    return round(bmi,2)
#Add code here to display calculate BMI
bmi = str(calculate_bmi(weight=57, height=1.73))
print("BMI =" + bmi)

if float(bmi) < 18.5:
        print("Under Weight") 
elif 18.5 <= float(bmi) <= 25.0:
    print("Normal Weight")
else:
    print("Over Weight")


