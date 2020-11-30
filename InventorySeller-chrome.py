from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Initialisation
SteamID=input("Enter steam ID:  ")
SteamPassword=input("Enter steam password:  ")


#Opens browser logs-in and waits for key
browser=webdriver.Chrome(executable_path="C:\\Users\\Anuj\\Desktop\\Scripts\\chromedriver.exe")
browser.get("https://store.steampowered.com/")
Login_Button=browser.find_element_by_css_selector('a.global_action_link')
Login_Button.click()
Username=browser.find_element_by_css_selector('#input_username')
Username.send_keys(SteamID)
Password=browser.find_element_by_css_selector('#input_password')
Password.send_keys(SteamPassword)
Login_Button_2=browser.find_element_by_css_selector('button.btnv6_blue_hoverfade > span:nth-child(1)')
Login_Button_2.click()

code=input("Add steam mobile authenticator code(case-insensitive):  ")
time.sleep(15)


#key has been stored in 'Code', now filling and entering homepage
EnterKeyField=browser.find_element_by_css_selector('#twofactorcode_entry')
EnterKeyField.send_keys(code)
SubmitCodeButton=browser.find_element_by_css_selector('#login_twofactorauth_buttonset_entercode > div:nth-child(1) > div:nth-child(2)')
SubmitCodeButton.click()
time.sleep(5)

#opening inventory
UserButton=browser.find_element_by_css_selector('a.menuitem:nth-child(5)')
UserButton.click()
time.sleep(3)
InventoryButton=browser.find_element_by_css_selector('div.profile_menu_item:nth-child(7) > a:nth-child(1) > span:nth-child(2)')
InventoryButton.click()
time.sleep(3)

#selecting the game inventory
print("Kindly select the game inventory you want to sell")
time.sleep(5)


#Run a for loop the number of times there is a marketable item
FilterButton=browser.find_element_by_css_selector('#filter_tag_show > span:nth-child(1)')
FilterButton.click()
rawtext=browser.find_element_by_css_selector('#tags_76561198730525703_730_2 > div:nth-child(5) > div:nth-child(2) > label').text
rawnum=rawtext.split()[1]
MarketableItems=int(rawnum[1:len(rawnum)-1])


#Setup for the script has now been done, following code is the crux

for i in range(0,5):
        browser.get('https://steamcommunity.com/profiles/76561198730525703/inventory/')
        FilterButton=browser.find_element_by_css_selector('#filter_tag_show > span:nth-child(1)')
        FilterButton.click()
        time.sleep(3)
        MarketableOption=browser.find_element_by_css_selector('#tag_filter_730_2_misc_marketable')
        MarketableOption.click()
        time.sleep(3)
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "730_2_15636531128"))).click()
        #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[9]/div[2]/div[1]/div/div[1]/div[4]/div/a"))).click()
        time.sleep(3)
        ItemTop=browser.find_element_by_xpath('/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[9]/div[1]/div[1]/div[3]/div/div/div[2]')
        price=ItemTop.text.split()[3]
        SellButton=browser.find_element_by_css_selector('.item_market_action_button_contents')
        SellButton.click()
        time.sleep(3)
        entry=browser.find_element_by_css_selector('#market_sell_buyercurrency_input')
        entry.send_keys(price)
        CheckBox=browser.find_element_by_css_selector('#market_sell_dialog_accept_ssa')
        CheckBox.click()
        ListingButton=browser.find_element_by_css_selector('#market_sell_dialog_accept > span:nth-child(1)')
        ListingButton.click()
        time.sleep(3)
        OKButton=browser.find_element_by_css_selector('#market_sell_dialog_ok > span:nth-child(1)')
        OKButton.click()
        time.sleep(10)
        
        
        
        
        

