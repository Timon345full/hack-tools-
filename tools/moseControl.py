import mouse

def posintion():
    try:
        return mouse.get_position()
    except Exception as e:
        print("Error: ", e)

def mouseClick(key):
    mouse.click(key)