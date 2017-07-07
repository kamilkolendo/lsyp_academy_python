from selenium.common.exceptions import WebDriverException


def gui_interaction(func):

    def wrapper(*args, **kwargs): # <-zmienna ilosc argumentow

        print("Gui interaction starts") # <-wykonuje sie przed opakowaną funkcją

        try:
            result = func(*args, **kwargs) # <-miejsce wykonania faktycznej funkcji

            print("Gui interaction done") # <-wykonuje sie po opakowanej funkcji

            return result

        except WebDriverException as e:
            raise

    return wrapper

@gui_interaction
def click_some_element():
    print("I try to click element")

click_some_element()