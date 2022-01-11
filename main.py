from datetime import datetime
import webbrowser, time, pyautogui, keyboard, os, cv2, pytesseract
from PIL import Image, ImageGrab,ImageEnhance
from PIL import ImageOps
import numpy as nm

# positions
bc_connectwallet = (962,624)
bc_wallpass = (1616,356)
bc_sign = (1824,547)
bc_huunt = (974,441)
bc_hero = (960,719)
#farmersworld
fw_login = (962,916)
fw_wax = (967,518)
fw_stoneaxe = (626,383)
fw_encientaxe = (625,470)
fw_work = (1021,668)
fw_repair = (1203,667)
fw_map = (1069,958)
fw_mining = (749,443)
fw_plant = (746,667)
fw_chicken = (1163,440)
fw_seed1 = (627,386)
fw_seed2 = (627,475)
fw_seed3 = (627,561)
fw_seed4 = (627,647)
fw_openarea = (303,276)
fw_addenergy = (1698,148)
fw_energyinput = (970,531)
fw_exchange = (963,612)

#timer
stoneaxe_click = ""
encientaxe_click = ""
seed1_click = ""
seed2_click = ""
seed3_click = ""
seed4_click = ""
script_start = time.time()



def open_site():
    webbrowser.open_new('https://play.farmersworld.io')
    time.sleep(10)
    login()


def login():
    pyautogui.click(fw_login)
    time.sleep(5)
    pyautogui.click(fw_wax)
    time.sleep(10)
    stoneaxe_mine()


def stoneaxe_mine():
    global stoneaxe_click
    global script_start
    goto_stoneaxe()
    if stoneaxe_click == "":
        if check_timer() == "00:00:00":
            add_energy(5)
            pyautogui.click(fw_work)
            time.sleep(10)
            stoneaxe_click = time.time()
            script_start = time.time()
            pyautogui.click(fw_openarea)
            time.sleep(5)
            encientaxe_mine()
        else:
            encientaxe_mine()
    else:
        if round(((time.time() - stoneaxe_click)/3600)) >= 1:
            if check_timer() == "00:00:00":
                add_energy(5)
                pyautogui.click(fw_work)
                time.sleep(10)
                stoneaxe_click = time.time()
                script_start = time.time()
                pyautogui.click(fw_openarea)
                time.sleep(5)
                encientaxe_mine()
            else:
                encientaxe_mine()
        else:
            encientaxe_mine()


def encientaxe_mine():
    global encientaxe_click
    goto_encientaxe()
    if encientaxe_click == "":
        if check_timer() == "00:00:00":
            add_energy(5)
            pyautogui.click(fw_work)
            time.sleep(10)
            encientaxe_click = time.time()
            pyautogui.click(fw_openarea)
            time.sleep(5)
            seed1_farm()
        else:
            seed1_farm()
    else:
        if round(((time.time() - encientaxe_click)/3600)) >= 2:
            if check_timer() == "00:00:00":
                add_energy(5)
                pyautogui.click(fw_work)
                time.sleep(10)
                encientaxe_click = time.time()
                pyautogui.click(fw_openarea)
                time.sleep(5)
                seed1_farm()
            else:
                seed1_farm()
        else:
            seed1_farm()


def seed1_farm():
    global seed1_click
    goto_seed1()
    if seed1_click == "":
        if check_timer() == "00:00:00":
            add_energy(120)
            pyautogui.click(fw_work)
            time.sleep(10)
            seed1_click = time.time()
            pyautogui.click(fw_openarea)
            time.sleep(5)
            seed2_farm()
        else:
            seed2_farm()
    else:
        if round(((time.time() - seed1_click)/3600)) >= 4:
            if check_timer() == "00:00:00":
                add_energy(120)
                pyautogui.click(fw_work)
                time.sleep(10)
                seed1_click = time.time()
                pyautogui.click(fw_openarea)
                time.sleep(5)
                seed2_farm()
            else:
                seed2_farm()
        else:
            seed2_farm()


def seed2_farm():
    global seed2_click
    goto_seed1()
    if seed2_click == "":
        if check_timer() == "00:00:00":
            pyautogui.click(fw_work)
            time.sleep(10)
            seed2_click = time.time()
            pyautogui.click(fw_openarea)
            time.sleep(5)
            seed3_farm()
        else:
            seed3_farm()
    else:
        if round(((time.time() - seed2_click)/3600)) >= 4:
            if check_timer() == "00:00:00":
                pyautogui.click(fw_work)
                time.sleep(10)
                seed2_click = time.time()
                pyautogui.click(fw_openarea)
                time.sleep(5)
                seed3_farm()
            else:
                seed3_farm()
        else:
            seed3_farm()


def seed3_farm():
    global seed3_click
    goto_seed1()
    if seed3_click == "":
        if check_timer() == "00:00:00":
            pyautogui.click(fw_work)
            time.sleep(10)
            seed3_click = time.time()
            pyautogui.click(fw_openarea)
            time.sleep(5)
            seed4_farm()
        else:
            seed4_farm()
    else:
        if round(((time.time() - seed3_click)/3600)) >= 4:
            if check_timer() == "00:00:00":
                pyautogui.click(fw_work)
                time.sleep(10)
                seed3_click = time.time()
                pyautogui.click(fw_openarea)
                time.sleep(5)
                seed4_farm()
            else:
                seed4_farm()
        else:
            seed4_farm()

def seed4_farm():
    global seed4_click
    goto_seed1()
    if seed4_click == "":
        if check_timer() == "00:00:00":
            pyautogui.click(fw_work)
            time.sleep(10)
            seed4_click = time.time()
            pyautogui.click(fw_openarea)
            time.sleep(5)
            repeat_mine()
        else:
            repeat_mine()
    else:
        if round(((time.time() - seed4_click)/3600)) >= 4:
            if check_timer() == "00:00:00":
                pyautogui.click(fw_work)
                time.sleep(10)
                seed4_click = time.time()
                pyautogui.click(fw_openarea)
                time.sleep(5)
                repeat_mine()
            else:
                repeat_mine()
        else:
            repeat_mine()


def repeat_mine():
    global script_start
    while True:
        time.sleep(1800)
        difference = round((time.time() - script_start)/3600)
        if int(difference) >= 1:
            stoneaxe_mine()
            break
        else:
            print(datetime.now().strftime("%H:%M:%S"))
        

def add_energy(amt):
    pyautogui.click(fw_addenergy)
    time.sleep(5)
    pyautogui.click(fw_energyinput)
    time.sleep(5)
    keyboard.write(str(amt))
    time.sleep(5)
    pyautogui.click(fw_exchange)
    time.sleep(10)


def goto_stoneaxe():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_mining)
    time.sleep(5)
    pyautogui.click(fw_stoneaxe)
    time.sleep(5)


def goto_encientaxe():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_mining)
    time.sleep(5)
    pyautogui.click(fw_encientaxe)
    time.sleep(5)

def goto_seed1():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_plant)
    time.sleep(5)
    pyautogui.click(fw_seed1)
    time.sleep(5)

def goto_seed2():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_plant)
    time.sleep(5)
    pyautogui.click(fw_seed2)
    time.sleep(5)

def goto_seed3():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_plant)
    time.sleep(5)
    pyautogui.click(fw_seed3)
    time.sleep(5)

def goto_seed4():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_plant)
    time.sleep(5)
    pyautogui.click(fw_seed4)
    time.sleep(5)


def check_timer():
    box = (1008,582,1214,632)
    image = ImageGrab.grab(bbox=box)
    text = pytesseract.image_to_string(cv2.cvtColor(nm.array(image),cv2.COLOR_BGR2GRAY),lang='eng')
    ocr = text.replace("\n\x0c", "") 
    print(ocr)
    # print(ocr.strip() == "00:00:00")
    ocr = ocr.strip()
    return ocr



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
    # check_timer()
    # print(pyautogui.position())
    # stoneaxe_mine()
    # add_energy(200)