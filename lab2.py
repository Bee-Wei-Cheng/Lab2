def display_main_menu():
    print("display_main_menu")

def get_user_input():
    list = []
    str=input("Enter value")
    list=str.split(",")
    list=[int(i) for i in list]
    return list

def calc_average_temperature(list):
    calc_average_temperature=sum(list)/len(list)
    return calc_average_temperature

def calc_min_max_temperature(list):
    value = []
    value.append(min(list))
    value.append(max(list))
    return value

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    list=get_user_input()
    print ("Average is ", calc_average_temperature(list))
    print ("Maximum is value ", calc_min_max_temperature(list)[1])
    print ("Minimum is value ", calc_min_max_temperature(list)[0])

if __name__ == "__main__":
    main()
