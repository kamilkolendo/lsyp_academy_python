from selenium.webdriver import Firefox

driver = Firefox()

driver.get("https://www.igame.com/eye-test/")

driver.switch_to.frame(driver.find_element_by_tag_name("Iframe"))

for x in range(1000):
    el = driver.find_element_by_class_name("thechosenone")
    el.click()


# driver.close()