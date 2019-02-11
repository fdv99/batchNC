import pyautogui, sys, time

files_to_convert = int(input("How many files need to be converted: "))
delay = float(input("Task delay? 1 for small nests, 6 for full sheet, in seconds: "))
y_modifier = 0
pyautogui.click(x=1300, y=110)
for x in range(1, files_to_convert + 1):
    try:
        # Open windows explorer
        pyautogui.hotkey('ctrl', 'd')
        x_loc = 270 
        y_loc = 180 + y_modifier
        time.sleep(0.7)
        print(x_loc, y_loc)
        # Click the next file
        pyautogui.doubleClick(x_loc,y_loc)
        time.sleep(1)
        
        # Click the generate icon
        generate_cut_path = pyautogui.locateCenterOnScreen('generate.png', grayscale=True)
        pyautogui.click(generate_cut_path)
        time.sleep(delay)
        
        # Keyboard hotkey for save
        pyautogui.hotkey('ctrl', 's') # Control + S to save nc
        y_modifier += 21  #could change depending on computer, 21 pixels on Forrest Desktop between files
        time.sleep(0.25)
        
        # Press enter to save
        pyautogui.press('enter') # Press enter to save the file with current name in current folder.
        print("File " + str(x) + " is done.")
        time.sleep(delay)

    except:
        resume = input("Do you want to continue? y/n")
        if resume == y:
            continue
        else:
            break

print("All files are converted to nc code.")
x = input("Close the program. ")