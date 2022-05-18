import unittest
import HtmlTestRunner
import names
import sys
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Functions import Test_functions

sys.path.append("C://Users//tusharg//PycharmProjects//pythonUnitTestProject_POMbased")

from pageObjects.RegistrationPage import RegistrationPage
from Functions.Test_functions import registration_functions

class RegistrationTest(unittest.TestCase, RegistrationPage):
    baseURL = "http://40.71.253.227:5034"
    driver = webdriver.Chrome(executable_path=ChromeDriverManager(path="D:/chromedriver_win32").install())

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    @unittest.TestCase
    def test_login(self):
        registration_functions.email("")
        registration_functions.passKey("")

    @unittest.TestCase
    def test_registration(self):
        rp = RegistrationPage(self.driver)

        Test_functions.firstname()
        """def firstname():
            f_name = names.get_first_name()
            rp.setfname(fname=f_name)"""

        """Test_functions.middlename()"""
        """def middlename():
            m_name = names.get_first_name()
            rp.setmname(mname=m_name)"""

        Test_functions.lastname()

        """ def lastname():
            l_name = names.get_last_name()
            rp.setlname(lname=l_name)"""

        Test_functions.phonenumber()
        """def phonennumber(ph_no):
            ph_no = 0
            for i in range(14):
                ph_no = i
            rp.setmobilenumber(ph_no)"""

    print("Registration Page Test successfully executed.")

    time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:\\Users\\tusharg\\PycharmProjects\\pythonUnitTestProject_POMbased\\reports'))
