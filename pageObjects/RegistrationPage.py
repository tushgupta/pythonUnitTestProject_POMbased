from selenium.webdriver.common.by import By

from Functions import Test_functions


class RegistrationPage:
    # locators of all the elements on Registration page.
    left_nav_panel_item1_linktext = "Personal Details"
    textbox_fname_xpath = "//*[@id='fname']"
    textbox_mname_id = "mname"
    textbox_lname_id = "lname"
    textbox_mobile_number_id = "mobile.0.number"
    button_add_another_number = "Add another number"
    textbox_email_id = "email"
    textbox_password_id = "password"
    button_login_id = "Log in"

    def __init__(self, driver):
        self.driver = driver

    def setfname(self):
        self.driver.find_element(By.ID(self.textbox_fname_xpath).send_keys(self))

    """def setmname(self):
        self.driver.find_element_by_id(self.textbox_mname_id).send_keys("mname")"""

    def setlname(self):
        self.driver.find_element_by_id(self.textbox_lname_id).send_keys(self)

    def setmobilenumber(self):
        self.driver.find_element_by_id(self.textbox_mobile_number_id).send_keys(Test_functions.phonenumber)

    def clickanothernumber(self):
        self.driver.find_element_by_id(self.button_add_another_number).click()

    def emailid(self):
        self.driver.find_element_by_id(self.textbox_email_id).click()

    def password(self):
        self.driver.find_element_by_id(self.textbox_password_id).click()

