from selenium import webdriver as webd
from time import sleep



twi_id = ''
twi_pass = ''
print("tweettext=>")
sampletxt = str(input().rstrip())
print(sampletxt)

##open driver
driver = webd.Chrome("C:/Users/beata/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.twitter.com")



elem_login_btn = driver.find_element_by_css_selector("#doc > div > div.StaticLoggedOutHomePage-content > div.StaticLoggedOutHomePage-cell.StaticLoggedOutHomePage-utilityBlock > div.StaticLoggedOutHomePage-signupBlock > div.StaticLoggedOutHomePage-signupHeader > a")
#elem_serch_btn = driver.find_element_by_id("srchbtn")
elem_login_btn.click()


##login form##
elem_id_form = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input")
elem_id_form.send_keys(twi_id)
elem_pass_form = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input")
elem_pass_form.send_keys(twi_pass)
elem_login = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > div.clearfix > button")
elem_login.click()

##tweet

elem_tweet_btn = driver.find_element_by_css_selector("#global-new-tweet-button")
elem_tweet_btn.click()

elem_tweet_smple_form = driver.find_element_by_css_selector("#Tweetstorm-tweet-box-0 > div.tweet-box-content > div.tweet-content > div.RichEditor.RichEditor--emojiPicker.is-fakeFocus > div.RichEditor-container.u-borderRadiusInherit > div.RichEditor-scrollContainer.u-borderRadiusInherit > div.tweet-box.rich-editor.is-showPlaceholder")

elem_tweet_smple_form.send_keys()
elem_tweet_smple_form.send_keys(sampletxt)

elem_tweet_form_box = driver.find_element_by_css_selector("#Tweetstorm-tweet-box-0 > div.tweet-box-content > div.TweetBoxToolbar > div.TweetBoxToolbar-tweetButton > span > button.SendTweetsButton.EdgeButton.EdgeButton--primary.EdgeButton--medium.js-send-tweets")
elem_tweet_form_box.click()
sleep(10)
driver.close()

