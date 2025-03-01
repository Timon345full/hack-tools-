import keyboard

class keyloger:
    try:
        def Start():
            pass 
    except Exception as e:
        print("Error: ", e)

def click(key):
    try:
        keyboard.on_press(key)
        keyboard.on_release(key)

    except Exception as e:
        print("Error:", e)

def combinationClick(combination, key, key2, key3):
    try:
        if combination == 1:
            keyboard.on_press(key)
            keyboard.on_release(key)

        if combination == 2:
            keyboard.on_press(key, key2)
            keyboard.on_release(key, key2)
                
        if combination == 3:
            keyboard.on_press(key, key2, key3)
            keyboard.on_release(key, key2, key3)
            
    except Exception as e:
        print("Error:", e)