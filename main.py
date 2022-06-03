# all imports
import os,pathlib
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import platform

plt = platform.platform()

user = os.getlogin()

option = webdriver.ChromeOptions()
option.add_argument('--log-level=3')

# file location
base_dir = pathlib.Path(__file__).parent


# initialize webdrive of browser window and all settings
if "windows" in plt.lower():
    print("We are using windows platform")
    option.add_argument(f"user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data")
    driver = webdriver.Chrome(options=option,executable_path=os.path.join(base_dir,'chromedriver.exe'))
elif 'linux' in plt.lower():
    option.add_argument(f"user-data-dir=/home/{user}/.config/google-chrome")
    driver = webdriver.Chrome(options=option,executable_path=os.path.join(base_dir,'chromedriver'))


# tlm iterations
tlm_i = 0

def run_game():
    print(f"Program Directory: {base_dir}")
    global sidemenu_items
    global fw_tab
    global aw_tab

    print("Opening Farmersworld Site")
    # open farmersworld
    driver.get("https://play.farmersworld.io/")

    # wait for screen load
    sleep(5)

    # open alenworlds
    print("Opening Alenworlds Site")
    driver.execute_script("window.open('about:blank','secondtab');")
    sleep(2)
    driver.switch_to.window('secondtab')
    sleep(2)
    driver.get("https://play.alienworlds.io/")

    # tabs saved
    fw_tab  = driver.window_handles[0]
    aw_tab  = driver.window_handles[1]

    # # login to fw
    print("Login To Farmersworld")
    driver.switch_to.window(fw_tab)
    driver.find_element(by=By.XPATH, value='//button[normalize-space()="Login"]').click()
    driver.find_element(by=By.XPATH, value='//button[normalize-space()="Wax Wallet Account"]').click()

    sleep(15)

    # # get the side items
    print("Getting Tools")
    sidemenu = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(by=By.CLASS_NAME,value='vertical-carousel-container'))
    sidemenu = driver.find_element(by=By.CLASS_NAME,value='vertical-carousel-container')
    sidemenu_items = sidemenu.find_elements(by=By.TAG_NAME,value='img')

    for item in sidemenu_items:
        item.click()
        sleep(2)
        item_name = driver.find_element(by=By.CLASS_NAME,value='info-title-name').text
        print(item_name)

    sleep(5)

    check_cpu()

def check_cpu():
    print("Checking CPU Usage")
    driver.switch_to.window(aw_tab)
    sleep(2)
    driver.refresh()
    sleep(5)
    allres = driver.find_element(by=By.CLASS_NAME,value='css-11yb1z3')
    cpu = allres.find_elements(by=By.CLASS_NAME,value='css-1eg3rbc')[0]
    cpu_val = cpu.find_element(by=By.CLASS_NAME,value='css-1rza94z').text.strip("%")

    print(f"Available CPU: {cpu_val}")

    if int(cpu_val) < 85:
        print("CPU Ok Start Mining")
        start_mining()
    else:
        print("CPU More Then 85% Wait 5 Min To Cool Down...")
        i = 0
        while i <= 300:
            print(i)
            sleep(1)
            i+=1
        check_cpu()

def start_mining():
    print("Switch To Farmersworld Tab")
    driver.switch_to.window(fw_tab)
    sleep(3)
    # click on the first item excavator
    for item in sidemenu_items:
        print("Clicking On Tool")
        # get item details on screen
        item.click()
        
        sleep(5)

        # get name
        item_name = driver.find_element(by=By.CLASS_NAME,value='info-title-name').text

        # get countdown timer value
        get_time = driver.find_element(by=By.CLASS_NAME,value='card-container--time').text.rstrip(" ")

        # get available energy to use for tools
        header = driver.find_element(by=By.CLASS_NAME,value='container__header')
        contents = header.find_elements(by=By.CLASS_NAME,value='resource__group')
        energy = contents[-1].find_element(by=By.CLASS_NAME,value='resource-number').text.split("/")
        available_e = int(energy[0])
        total_e = int(energy[1])

        print(f"Time Is {get_time}")
        print(f"Energy Is {available_e}")
        

        if get_time == "00:00:00":
            print("Mining Available")
            if available_e < 300:
                print("Energy Low We are Adding Energy")
                driver.find_element(by=By.CLASS_NAME,value='resource-energy--plus').click()
                sleep(2)
                driver.find_element(by=By.CLASS_NAME,value='modal-input').send_keys(str(total_e-available_e))
                sleep(5)
                driver.find_element(by=By.XPATH, value='//button[normalize-space()="Exchange"]').click()
                sleep(15)
                try:
                    driver.find_element(by=By.CLASS_NAME,value='close-modal').click()
                except NoSuchElementException:
                    pass
            
            if item_name.lower() == 'bronze member':
                print("Farming From Membership")
                driver.find_element(by=By.XPATH, value='//button[normalize-space()="Claim"]').click()
                sleep(15)
                try:
                    driver.find_element(by=By.XPATH, value='//button[normalize-space()="OK"]').click()
                except NoSuchElementException:
                    driver.find_element(by=By.CLASS_NAME,value='close-modal').click()
                sleep(5)
            else:
                # check durability of the item
                get_durability = driver.find_element(by=By.CLASS_NAME,value='content').text.rstrip(" ")
                available_d = get_durability.split("/")[0].rstrip()
                total_d = get_durability.split("/")[1].rstrip()

                print(f"Durability Is {available_d}")

                if (int(total_d) - int(available_d)) == 0:
                    print("Low Durability Need To Repair Tool")
                    driver.find_element(by=By.XPATH, value='//button[normalize-space()="Repair"]').click()
                    sleep(15)
                    try:
                        driver.find_element(by=By.CLASS_NAME,value='close-modal').click()
                    except NoSuchElementException:
                        pass

                print("Now Mining")
                driver.find_element(by=By.XPATH, value='//button[normalize-space()="Mine"]').click()
                sleep(15)
                try:
                    driver.find_element(by=By.XPATH, value='//button[normalize-space()="OK"]').click()
                except NoSuchElementException:
                    driver.find_element(by=By.CLASS_NAME,value='close-modal').click()
                sleep(5)    
        
    go_tlm()


def go_tlm():
    print("Change Screen To Alenworlds")
    global tlm_i
    # switch to aw window
    driver.switch_to.window(aw_tab)
    # wait for screen to show
    sleep(5)
    # find our mining dive
    status = driver.find_element(by=By.CLASS_NAME,value='css-2s09f0')
    # check for timer
    status  = status.find_elements(by=By.CLASS_NAME,value='chakra-text')
    # if no timer then length 0 and we can click on mine
    if len(status) == 0:
        print("Mining Available Now Mining")
        # click on mine button
        driver.find_element(by=By.CLASS_NAME,value='css-2s09f0').click()
        sleep(5)
        # click on claim button
        driver.find_element(by=By.CLASS_NAME,value='css-2s09f0').click()
        sleep(5)
        # approve claim
        driver.switch_to.window(driver.window_handles[2])
        sleep(10)
        print("Approved Action")
        driver.find_element(by=By.XPATH, value='//button[normalize-space()="Approve"]').click()

        tlm_i += 1
        
        sleep(300)

        # rerun script after 5 hours
        if tlm_i == 1:
            print("5 Hours Up Resetting Program")
            driver.quit()
            sleep(2)
            rerun()
        # start form beginning after 1 hr
        elif tlm_i >= 12:
            print('1 Hour Up Going To Mine Farmersworld')
            check_cpu()
        # play tlm
        else:
            print("5 Min Up Remine TLM")
            go_tlm()
    else:
        print("Mining Not Available Go Farmersworld")
        check_cpu()


def rerun():
    print("Running Bat File To Reset Program")
    os.system(f"{os.path.join(base_dir,'rerun.bat')} {base_dir}")


if __name__ == "__main__":
    run_game()
