from datetime import datetime
from glob import glob
from random import seed
import webbrowser, time, pyautogui, os, cv2, pytesseract, json
from PIL import Image, ImageGrab,ImageEnhance
from PIL import ImageOps
import numpy as nm

# positions

#farmersworld
fw_login = (682,692)
fw_wax = (688,442)
fw_stoneaxe = (466,351)
fw_encientaxe = (468,408)
fw_fishrod = (467,462)
fw_work = (725,536)
fw_repair = (857,534)
fw_map = (751,718)
fw_mining = (542,394)
fw_plant = (541,533)
fw_chikfarm = (816,380)
fw_seed1 = (466,348)
fw_seed2 = (466,408)
fw_seed3 = (466,465)
fw_seed4 = (466,524)
fw_seed5 = (466,544)
fw_chicken1 = (465,344)
fw_openarea = (203,247)
fw_addenergy = (1162,195)
fw_energyinput = (706,439)
fw_exchange = (686,501)


script_start = ""

# clicks
stoneaxe = 0
encientaxe = 0
fishrod = 0
chicken = 0
seed5 = 0
seed4 = 0
seed3 = 0
seed2 = 0
seed1 = 0

def setclick_vals():
    global stoneaxe
    global encientaxe
    global fishrod
    global chicken
    global seed5
    global seed4
    global seed3
    global seed2
    global seed1

    print(seed1)
    print(seed2)
    print(seed3)
    print(seed4)
    print(seed5)
    print(stoneaxe)
    print(encientaxe)
    print(fishrod)
    print(chicken)

    with open('/home/kali/Desktop/farmersworldauto/click.json', 'r') as openfile:
        json_object = json.load(openfile)

    stoneaxe = json_object['stoneaxe']
    encientaxe = json_object['encientaxe']
    fishrod = json_object['fishrod']
    chicken = json_object['chicken']
    seed5 = json_object['seed5']
    seed4 = json_object['seed4']
    seed3 = json_object['seed3']
    seed2 = json_object['seed2']
    seed1 = json_object['seed1']


    print(seed1)
    print(seed2)
    print(seed3)
    print(seed4)
    print(seed5)
    print(stoneaxe)
    print(encientaxe)
    print(fishrod)
    print(chicken)


    open_site()


def open_site():
    webbrowser.open_new('https://play.farmersworld.io')
    time.sleep(25)
    login()


def login():
    pyautogui.click(fw_login)
    time.sleep(10)
    pyautogui.click(fw_wax)
    time.sleep(10)
    fishrod_mine()

global fishrod_check
fishrod_check = 0

def fishrod_mine():
    global fishrod
    global fishrod_check
    global script_start
    
    goto_fishrod()

    if check_timer() == "00:00:00":
        if int(fishrod) < 24:
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            if check_timer() == "00:00:00":
                fishrod_check = int(fishrod_check) + 1
                if int(fishrod_check) > 5:
                    fishrod_check = 0
                    stoneaxe_mine()
                else:
                    fishrod_mine()
            else:
                fishrod = int(fishrod) + 1
                script_start = time.time()
                addclick('fishrod',fishrod)
                stoneaxe_mine()
        else:
            stoneaxe_mine()
    else:
        stoneaxe_mine()


global stoneaxe_check
stoneaxe_check = 0

def stoneaxe_mine():
    global stoneaxe_click
    global stoneaxe
    global stoneaxe_check

    goto_stoneaxe()

    if check_timer() == "00:00:00":
        if int(stoneaxe) < 24:
            add_energy(5)
            
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            
            if check_timer() == "00:00:00":
                stoneaxe_check = int(stoneaxe_check) + 1
                if int(stoneaxe_check) > 5:
                    stoneaxe_check = 0
                    encientaxe_mine()
                else:
                    stoneaxe_mine()
            else: 
                stoneaxe = int(stoneaxe) + 1
                addclick('stoneaxe',stoneaxe)
                stoneaxe_click = time.time()
                encientaxe_mine()
        else:
            addclick('stoneaxe',0)
            encientaxe_mine()
    else:
        encientaxe_mine()


global encient_check
encient_check = 0


def encientaxe_mine():
    global encient_check
    global encientaxe_click
    global encientaxe
    goto_encientaxe()

    if check_timer() == "00:00:00":
        if int(encientaxe) < 12:
            add_energy(4)
            
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            
            if check_timer() == "00:00:00":
                encient_check = int(encient_check) + 1
                if int(encient_check) > 5:
                    encient_check = 0
                    seed1_farm()
                else:
                    encientaxe_mine()
            else:
                encientaxe = int(encientaxe) + 1
                addclick('encientaxe',encientaxe)
                encientaxe_click = time.time()
                seed1_farm()
        else:
            addclick('encientaxe',0)
            seed1_farm()
    else:
        seed1_farm()


global seed1_check
seed1_check = 0

def seed1_farm():
    global seed1_click
    global seed1
    global seed1_check
    goto_seed1()
    if check_timer() == "00:00:00":
        if int(seed1) < 6:
            add_energy(150)
            
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            if check_timer() == "00:00:00":
                seed1_check = int(seed1_check) + 1
                if int(seed1_check) > 5:
                    seed1_check = 0
                    seed2_farm()
                else:
                    seed1_farm()
            else:
                seed1 = int(seed1) + 1
                addclick('seed1',seed1)
                seed1_click = time.time()
                seed2_farm()
        else:
            addclick('seed1',0)
            seed2_farm()
    else:
        seed2_farm()
    
global seed2_check
seed2_check = 0

def seed2_farm():
    global seed2_click
    global seed2
    global seed2_check

    goto_seed2()

    if check_timer() == "00:00:00":
        if int(seed2) < 6:
            
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            
            if check_timer() == "00:00:00":
                seed2_check = int(seed2_check) + 1
                if int(seed2_check) > 5:
                    seed2_check = 0
                    seed3_farm()
                else:
                    seed2_farm()                        
            else:
                seed2 = int(seed2) + 1
                addclick('seed2',seed2)
                seed2_click = time.time()
                seed3_farm()
        else:
            addclick('seed2',0)
            seed3_farm()
    else:
        seed3_farm()


global seed3_check
seed3_check = 0


def seed3_farm():
    global seed3_click
    global seed3
    global seed3_check

    goto_seed3()
    if check_timer() == "00:00:00":
        if int(seed3) < 6:
            
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            if check_timer() == "00:00:00":
                seed3_check = int(seed3_check) + 1
                if int(seed3_check) > 5:
                    seed3_check = 0
                    seed4_farm()
                else:
                    seed3_farm()
            else:    
                seed3 = int(seed3) + 1
                addclick('seed3',seed3)
                seed3_click = time.time()
                seed4_farm()
        else:
            addclick('seed3',0)
            seed4_farm()
    else:
        seed4_farm()



global seed4_check
seed4_check = 0

def seed4_farm():
    global seed4_click
    global seed4
    global seed4_check

    goto_seed4()

    if check_timer() == "00:00:00":
        if int(seed4)< 6:
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            if check_timer() == "00:00:00":
                seed4_check = int(seed4_check) + 1
                if int(seed4_check) > 5:
                    seed4_check = 0
                    seed5_farm()
                else:
                    seed4_farm()
            else:
                seed4 = int(seed4) + 1
                addclick('seed4',seed4)
                seed4_click = time.time()
                seed5_farm()
        else:
            addclick('seed4',0)
            
    else:
        seed5_farm()


global seed5_check
seed5_check = 0

def seed5_farm():
    global seed5_check
    global seed5_click
    global seed5

    goto_seed5()

    if check_timer() == "00:00:00":
        if int(seed5)< 6:
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            if check_timer() == "00:00:00":
                seed5_check = int(seed5_check) + 1
                if int(seed5_check) > 5:
                    seed5_check = 0
                    chicken_eggs()
                else:
                    seed5_farm()
            else:
                seed5 = int(seed5) + 1
                addclick('seed5',seed5)
                seed5_click = time.time()
                chicken_eggs()
        else:
            addclick('seed5',0)
                
    else:
            chicken_eggs()


global chicken_checks
chicken_checks = 0

def chicken_eggs():
    global chicken_click
    global chicken
    global chicken_checks

    goto_chicken()

    if check_timer() == "00:00:00":
        if int(chicken) < 4:
            pyautogui.click(fw_work)
            time.sleep(10)
            pyautogui.click(fw_openarea)
            time.sleep(5)
            if check_timer() == "00:00:00":
                chicken_checks = int(chicken_checks) + 1
                if int(chicken_checks) > 5:
                    chicken_checks = 0
                    repeat_mine()          
                else:
                    chicken_eggs()               
            else:
                chicken = int(chicken) + 1
                addclick('chicken',chicken)
                chicken_click = time.time()
                repeat_mine()
        else:
            addclick('chicken',0)
            close()
    else:
        repeat_mine()


def repeat_mine():
    global script_start
    while True:
        time.sleep(1800)
        difference = round((time.time() - script_start)/3600)
        if int(difference) >= 1:
            fishrod_mine()
            break
        else:
            print(datetime.now().strftime("%H:%M:%S"))
        

def addclick(name,val):
    with open('/home/kali/Desktop/farmersworldauto/click.json', 'r') as openfile:
        json_object = json.load(openfile)

    json_object[name] = val

    with open('/home/kali/Desktop/farmersworldauto/click.json', 'w') as openfile:
        json.dump(json_object,openfile)


def add_energy(amt):
    pyautogui.click(fw_addenergy)
    time.sleep(5)
    pyautogui.click(fw_energyinput)
    time.sleep(5)
    pyautogui.write(str(amt))
    time.sleep(5)
    pyautogui.click(fw_exchange)
    time.sleep(20)
    pyautogui.click(fw_openarea)
    time.sleep(5)

def goto_fishrod():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_mining)
    time.sleep(5)
    pyautogui.click(fw_fishrod)
    time.sleep(5)

def goto_chicken():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_chikfarm)
    time.sleep(5)
    pyautogui.click(fw_chicken1)
    time.sleep(5)

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

def goto_seed5():
    pyautogui.click(fw_map)
    time.sleep(5)
    pyautogui.click(fw_plant)
    time.sleep(5)
    pyautogui.moveTo(fw_seed2)
    pyautogui.scroll(-500)
    time.sleep(5)
    pyautogui.click(fw_seed5)
    time.sleep(5)

def check_timer():
    box = (708,463,850,513)
    image = ImageGrab.grab(bbox=box)
    text = pytesseract.image_to_string(cv2.cvtColor(nm.array(image),cv2.COLOR_BGR2GRAY),lang='eng')
    ocr = text.replace("\n\x0c", "") 
    print(ocr)
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

#keyboard.add_hotkey('ctrl+q',close)


def printvals():
    print(stoneaxe)
    print(encientaxe)
    print(seed1)
    print(seed2)

if __name__ == '__main__':
    # open_site()
    #check_timer()
    #print(pyautogui.position())
    # stoneaxe_mine()
    # add_energy(200)
    setclick_vals()
    #pyautogui.moveTo(fw_login)
