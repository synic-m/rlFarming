from selenium import webdriver as webd
from selenium.webdriver.common.keys import Keys   
from time import sleep

login_password = "pasword"

for x in range(1,2):
    try:
        ##open driver
        driver = webd.Chrome("C:/Users/beata/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail&hl=ja&flowName=GlifWebSignIn&flowEntry=SignUp")
        
        #first page
        #gets selector
        elem_last_name_form = driver.find_element_by_css_selector("#lastName")
        elem_first_name_form = driver.find_element_by_css_selector("#firstName")
        elem_username_form = driver.find_element_by_css_selector("#username")
        elem_password_form = driver.find_element_by_css_selector("#passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
        elem_re_password_form = driver.find_element_by_css_selector("#confirm-passwd > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
        elem_next_p1_btn = driver.find_element_by_css_selector("#accountDetailsNext")

       
        
        user_id = "moziretu.1uto." + str(x)
        #doing
        elem_last_name_form.send_keys('akasa')
        elem_first_name_form.send_keys('tmoyuki')
        elem_username_form.send_keys(user_id)
        elem_password_form.send_keys('login_password')
        elem_re_password_form.send_keys('login_password')
        #next page
        elem_next_p1_btn.click()
        #second page
        sleep(2)
        #gets selector
        elem_year_form = driver.find_element_by_css_selector("#year")
        elem_month_form = driver.find_element_by_css_selector("#month")
        elem_date_form = driver.find_element_by_css_selector("#day")
        elem_sex_form = driver.find_element_by_css_selector("#gender")
        elem_next_p2_btn = driver.find_element_by_css_selector("#personalDetailsNext")

        #doing
        elem_year_form.send_keys(str(1980 + x))
        elem_month_form.send_keys(str(7))
        elem_date_form.send_keys(str(x))
        elem_sex_form.click()
        elem_sex_form.send_keys(Keys.DOWN)
        elem_sex_form.send_keys(Keys.ENTER)
        elem_next_p2_btn.click()
        
        sleep(5)
        #agreement form
        #scroll ~~~
        #agree ~~~
        elem_txt_form = driver.find_element_by_xpath("//*[@id=\"view_container\"]/form/div[2]/div/div/div/div[1]/content") 
        elem_agree_btn = driver.find_element_by_css_selector("#termsofserviceNext")
        #scroll and agree
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",elem_txt_form)
        sleep(2)
        elem_agree_btn.click()

        #driver.close()
    except Exception as e:
        print(e)
        pass


