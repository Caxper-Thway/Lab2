def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    bmi = str(calculate_bmi(weight=57, height=1.73))
    print("BMI =" + bmi)

    if float(bmi) < 18.5:
        print("Under Weight") 
    elif 18.5 <= float(bmi) <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")
    
    display_main_menu()
    num_list = get_user_input()

    average = calc_average_temperature(num_list)
    print("Average " + str(average))
 

    max_min_list = calc_min_max_temperature(num_list)

    print ("Max is " + str(int(max_min_list[0])))
    print ("Min is " + str(int(max_min_list[1])))


def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    bmi = weight/(height * height)
    return round(bmi,2)
#Add code here to display calculate BMI
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average():
    print("calc_average")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    float_list = [];
    for num_str in string_list:
        float_list.append(float(num_str))
    return float_list

def calc_average_temperature(list):

    average = 0

    for num_str in list:
        average = average + num_str

    return average/5

def calc_min_max_temperature(list):
    max = 0
    min = 100
    for num_str in list:
        if(num_str > max):
            max = num_str
        if(num_str < min):
            min = num_str

    max_min_list = [max, min];

    return max_min_list

   



if __name__ == "__main__":
    main()