import keyboard,webbrowser, time, pyautogui, os, cv2, pytesseract
from PIL import ImageGrab
import numpy as nm


#farmersworld positions
fw_login = (681,675)
fw_wax = (681,348)
fw_stoneaxe = (395,246)
fw_encientaxe = (395,408)
fw_fishrod = (395,319)
fw_work = (731,474)
fw_repair = (884,474)
fw_map = (772,711)
fw_mining = (506,290)
fw_plant = (506,482)
fw_chikfarm = (845,296)
fw_seed1 = (395,241)
fw_seed2 = (395,311)
fw_seed3 = (395,383)
fw_seed4 = (395,451)
fw_seed5 = (395,279)
fw_seed6 = (395,344)
fw_seed7 = (395,415)
fw_seed8 = (395,481)
fw_chicken1 = (395,244)
fw_openarea = (203,247)
fw_openarea2 = (1283,112)
fw_addenergy = (1282,54)
fw_energyinput = (709,365)
fw_exchange = (683,429)
rpc_endpoint = (734,597)
membership = (396,388)
membership_claim = (793,466)

# bombcrypto positions
login_btn = (689,543)
sign_btn = (1275,632)
trasure_hunt = (685,489)
hero = (1086,575)
all_active = (593,212)
all_rest = (656,209)
exit_hero = (734,158)
back_btn = (245,78)
metamask = (1306,85)
metamask_sign = (1151,581)

#browser positions
tab1 = (0,0)
tab2 = (0,0)

#open both fw and bombcrypto sites in firefox browser
def open_site():
    print("Opening Websites")
    webbrowser.open_new_tab('https://play.farmersworld.io')
    time.sleep(2)
    webbrowser.open_new_tab('https://app.bombcrypto.io/')
    time.sleep(20)
    pyautogui.click(metamask)
    time.sleep(2)
    keyboard.write("Agsarnab@095")
    time.sleep(2)
    pyautogui.click(metamask_sign)
    time.sleep(2)
    loginto_games()

#change tabs and log into both games
def loginto_games():
    pyautogui.hotkey("ctrl","tab") #farmmersworld tab
    time.sleep(2)
    print("Trying To Login....")
    pyautogui.click(rpc_endpoint) #change rpc endpoint
    time.sleep(2)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(fw_login) #click on login button
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(fw_wax) #click on wax button
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey("ctrl","tab") #bombcrypto tab
    time.sleep(2)
    pyautogui.click(login_btn)
    time.sleep(3)
    pyautogui.click(sign_btn)
    time.sleep(25)
    play_bombcrypto()


def play_bombcrypto():
    print("Activating Heros")
    pyautogui.moveTo(hero)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(all_active)
    time.sleep(1)
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(exit_hero)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    print("Going Traasure hunt")
    pyautogui.moveTo(trasure_hunt)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    play_fw()


global fishrod_check
fishrod_check = 0

def play_fw():
    time.sleep(2)
    print("Now Farming Food")
    
    global fishrod_check
    
    goto_mining()
    goto_fishrod()

    while check_timer() == "00:00:00":
        work_now()
        fishrod_check = int(fishrod_check) + 1
        if int(fishrod_check) > 5:
            fishrod_check = 0
            stoneaxe_mine()
            break
    else:
        stoneaxe_mine()



global stoneaxe_check
stoneaxe_check = 0

def stoneaxe_mine():
    print("Farming Wood With Stone Axe")
    global stoneaxe_check

    goto_stoneaxe()

    if check_timer() == "00:00:00":
        add_energy(10)
        time.sleep(2)
        while check_timer() == "00:00:00":
            work_now()
            stoneaxe_check = int(stoneaxe_check) + 1
            if int(stoneaxe_check) > 5:
                stoneaxe_check = 0
                membership_farm()
                break
        else:
            membership_farm()
    else:
        membership_farm()


global membership_check
membership_check = 0

def membership_farm():
    print("Getting Farmer Coins...")
    global membership_check

    goto_membership()

    while check_member_timer() == "00:00:00":
        work_now_member()
        membership_check = int(membership_check) + 1
        if int(membership_check) > 5:
            membership_check = 0
            seed1_farm()
            break
    else:
        seed1_farm()



global seed1_check
seed1_check = 0

def seed1_farm():
    print("Farming Barley From Seed1")
    global seed1_check
    
    goto_crops()
    goto_seed1()
    
    if check_timer() == "00:00:00":
        add_energy(30)
        while check_timer() == "00:00:00":
            work_now()
            seed1_check = int(seed1_check) + 1
            if int(seed1_check) > 5:
                seed1_check = 0
                seed2_farm()
                break
        else:
            seed2_farm()
    else:
        seed2_farm()


global seed2_check
seed2_check = 0

def seed2_farm():
    print("Farming Barley From Seed2")
    global seed2_check
    
    goto_seed2()
    
    if check_timer() == "00:00:00":
        add_energy(30)
        while check_timer() == "00:00:00":
            work_now()
            seed2_check = int(seed2_check) + 1
            if int(seed2_check) > 5:
                seed2_check = 0
                seed3_farm()
                break
        else:
            seed3_farm()
    else:
        seed3_farm()



global seed3_check
seed3_check = 0

def seed3_farm():
    print("Farming Barley From Seed3")
    global seed3_check
    
    goto_seed3()
    
    if check_timer() == "00:00:00":
        add_energy(30)
        while check_timer() == "00:00:00":
            work_now()
            seed3_check = int(seed3_check) + 1
            if int(seed3_check) > 5:
                seed3_check = 0
                seed4_farm()
                break
        else:
            seed4_farm()
    else:
        seed4_farm()

global seed4_check
seed4_check = 0

def seed4_farm():
    print("Farming Barley From Seed4")
    global seed4_check
    
    goto_seed4()
    
    if check_timer() == "00:00:00":
        add_energy(30)
        while check_timer() == "00:00:00":
            work_now()
            seed4_check = int(seed4_check) + 1
            if int(seed4_check) > 5:
                seed4_check = 0
                seed5_farm()
                break
        else:
            seed5_farm()
    else:
        seed5_farm()


global seed5_check
seed5_check = 0

def seed5_farm():
    print("Farming Barley From Seed5")
    global seed5_check
    
    seed_scroll()    
    goto_seed5()
    
    if check_timer() == "00:00:00":
        add_energy(30)
        while check_timer() == "00:00:00":
            work_now()
            seed5_check = int(seed5_check) + 1
            if int(seed5_check) > 5:
                seed5_check = 0
                seed6_farm()
                break
        else:
            seed6_farm()
    else:
        seed6_farm()


global seed6_check
seed6_check = 0

def seed6_farm():
    print("Farming Barley From Seed6")
    global seed6_check
    
    goto_seed6()
    
    if check_timer() == "00:00:00":
        add_energy(30)
        while check_timer() == "00:00:00":
            work_now()
            seed6_check = int(seed6_check) + 1
            if int(seed6_check) > 5:
                seed6_check = 0
                seed7_farm()
                break
        else:
            seed7_farm()
    else:
        seed7_farm()



global seed7_check
seed7_check = 0

def seed7_farm():
    print("Farming Barley From Seed7")
    global seed7_check
    
    goto_seed7()
    
    if check_timer() == "00:00:00":
        add_energy(30)
        while check_timer() == "00:00:00":
            work_now()
            seed7_check = int(seed7_check) + 1
            if int(seed7_check) > 5:
                seed7_check = 0
                seed8_farm()
                break
        else:
            seed8_farm()
    else:
        seed8_farm()


global seed8_check 
seed8_check = 0

def seed8_farm():
    print("Farming Barley From Seed8")
    global seed8_check
    
    goto_seed8()
    
    if check_timer() == "00:00:00":
        add_energy(30)
        while check_timer() == "00:00:00":
            work_now()
            seed8_check = int(seed8_check) + 1
            if int(seed8_check) > 5:
                seed8_check = 0
                chicken_eggs()
                break
        else:
            chicken_eggs()
    else:
        chicken_eggs()

global chicken_checks
chicken_checks = 0

def chicken_eggs():
    print("Getting Eggs From Chicken...")
    global chicken_checks

    goto_chickenfarm()
    goto_chicken()

    while check_timer() == "00:00:00":
        work_now()
        chicken_checks = int(chicken_checks) + 1
        if int(chicken_checks) > 5:
            chicken_checks = 0
            show_bombcrypto()
            break
    else:
        show_bombcrypto() 

global bombcrypto_count
bombcrypto_count = 0

def show_bombcrypto():
    global bombcrypto_count
    if bombcrypto_count <= 9:
        bombcrypto_count = int(bombcrypto_count) + 1
        pyautogui.hotkey("ctrl","tab")
        time.sleep(300)
        play_fw()
    elif bombcrypto_count >= 24:
        bombcrypto_count = 0
        pyautogui.hotkey("ctrl","tab")
        time.sleep(2)
        pyautogui.press("f5")
        time.sleep(20)
        pyautogui.moveTo(login_btn)
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)
        pyautogui.click(sign_btn)
        time.sleep(20)
        pyautogui.moveTo(trasure_hunt)
        time.sleep(1)
        pyautogui.click()
        time.sleep(300)
        play_fw()
    else:
        bombcrypto_count = int(bombcrypto_count) + 1
        pyautogui.hotkey("ctrl","tab")
        time.sleep(2)
        pyautogui.moveTo(back_btn)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(hero)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(all_rest)
        time.sleep(1)
        pyautogui.click()
        time.sleep(8)
        pyautogui.moveTo(exit_hero)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        play_fw()

def work_now():
    print("Clicking On Mine Button...")
    pyautogui.click(fw_work)
    time.sleep(15)
    pyautogui.click(fw_openarea2)
    time.sleep(2)

def work_now_member():
    print("Clicking On Claim  Button...")
    pyautogui.click(membership_claim)
    time.sleep(15)
    pyautogui.click(fw_openarea2)
    time.sleep(2)

def add_energy(amt):
    print(f"Adding {amt} Energy...")
    pyautogui.click(fw_addenergy)
    time.sleep(2)
    pyautogui.click(fw_energyinput)
    time.sleep(2)
    pyautogui.write(str(amt))
    time.sleep(2)
    pyautogui.click(fw_exchange)
    time.sleep(20)
    pyautogui.click(fw_openarea2)
    time.sleep(2)

def goto_mining():
    print("Going To Mining Section...")
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_mining)
    time.sleep(5)

def goto_crops():
    print("Going To Crops...")    
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_plant)
    time.sleep(5)

def goto_chickenfarm():
    print("Going To Chicken Farm...")
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_chikfarm)
    time.sleep(5)

def goto_fishrod():
    print("Going To Fishing...")
    pyautogui.click(fw_fishrod)
    time.sleep(2)

def goto_chicken():
    print("Going To Chicken...")
    pyautogui.click(fw_chicken1)
    time.sleep(2)

def goto_stoneaxe():
    print("Going To Stone Axe...")
    pyautogui.click(fw_stoneaxe)
    time.sleep(2)


def goto_encientaxe():
    print("Going To Encient Axe..")
    pyautogui.click(fw_encientaxe)
    time.sleep(2)

def goto_seed1():
    print("Going To Seed1..")
    pyautogui.moveTo(fw_seed1)
    pyautogui.click()
    time.sleep(2)

def goto_seed2():
    print("Going To Seed2..")
    pyautogui.moveTo(fw_seed2)
    pyautogui.click()
    time.sleep(2)

def goto_seed3():
    print("Going To Seed3..")
    pyautogui.moveTo(fw_seed3)
    pyautogui.click()
    time.sleep(2)

def goto_seed4():
    print("Going To Seed4..")
    pyautogui.moveTo(fw_seed4)
    pyautogui.click()
    time.sleep(2)

def goto_seed5():
    print("Going To Seed5..")
    pyautogui.moveTo(fw_seed5)
    pyautogui.click()
    time.sleep(2)

def goto_seed6():
    print("Going To Seed6..")
    pyautogui.moveTo(fw_seed6)
    pyautogui.click()
    time.sleep(2)

def goto_seed7():
    print("Going To Seed7..")
    pyautogui.moveTo(fw_seed7)
    pyautogui.click()
    time.sleep(2)

def goto_seed8():
    print("Going To Seed8")
    pyautogui.moveTo(fw_seed8)
    pyautogui.click()
    time.sleep(2)

def goto_membership():
    print("Going To Membership")
    pyautogui.moveTo(membership)
    pyautogui.click()
    time.sleep(2)

def seed_scroll():
    print("Scrolling....")
    pyautogui.moveTo(fw_seed2)
    time.sleep(2)
    pyautogui.scroll(-1000)
    time.sleep(2)

def check_timer():
    box = (726,402,889,443)
    image = ImageGrab.grab(bbox=box)
    text = pytesseract.image_to_string(cv2.cvtColor(nm.array(image),cv2.COLOR_BGR2GRAY),lang='eng')
    ocr = text.replace("\n\x0c", "") 
    print(f"Time is: {ocr}")
    ocr = ocr.strip()
    return ocr


def check_member_timer():
    box = (706,391,878,436)
    image = ImageGrab.grab(bbox=box)
    text = pytesseract.image_to_string(cv2.cvtColor(nm.array(image),cv2.COLOR_BGR2GRAY),lang='eng')
    ocr = text.replace("\n\x0c", "") 
    print(f"Time is: {ocr}")
    ocr = ocr.strip()
    return ocr



def check_energy():
    box = (1121,38,1158,66)
    image = ImageGrab.grab(bbox=box)
    text = pytesseract.image_to_string(cv2.cvtColor(nm.array(image),cv2.COLOR_BGR2GRAY),lang='eng')
    ocr = text.replace("\n\x0c", "") 
    try:
        ocr = ocr.split(")")
    except Exception as e:
        ocr = ocr.strip("/")
    finally:
        return ocr[0]


def close():
    pid = os.getpid()
    try:
        os.system(f'kill {pid}')
    except Exception as e:
        pass
    finally:
        os.system(f'taskkill /F /PID {pid}')


keyboard.add_hotkey('ctrl+q',close)

if __name__ == '__main__':
    open_site()
