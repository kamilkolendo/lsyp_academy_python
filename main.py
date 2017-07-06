from utils import webutils

def main_func():
    # print("Do Stuff")
    my_str = "Hello Academy"
    str2 = "Hi!"

    output = my_str + str2 + " " + str2 #gorsza praktyka
    output2 = "Siema {}. Co tam {}"
    output3 = output2.format(my_str, str2) #dobra praktyka
    print(output3)

    output4 = "Siema {0}. Co tam? {1} To wlasnie {0}."
    output5 = output4.format(my_str, str2)
    print(output5)

    my_str = my_str.replace("Academy", "Kamcio")

    output6 = f"Siema {my_str}. Co tam? {str2}"
    print(output6)

if __name__ == "__main__":
    main_func()