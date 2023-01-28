from pynput.keyboard import Key, Listener, Controller
import pyperclip
eng = """`1234567890-=\\][poiuytrewqasdfghjkl;'/.,mnbvcxz~!@#$%^&*()_+|}{POIUYTREWQASDFGHJKL:"?><MNBVCXZ """
thai = """_ๅ/-ภถุึคตจขชฃลบยนรีัะพำไๆฟหกดเ้่าสวงฝใมทืิอแปผ%+๑๒๓๔ู฿๕๖๗๘๙ฅ,ฐญฯณ๊ํธฑฎ"๐ฤฆฏโฌ็๋ษศซ.ฦฬฒ?์ฺฮฉ)( """

eng2thai = {k :v for k,v in zip(eng,thai)}
thai2eng = {k :v for k,v in zip(thai,eng)}

keyboard = Controller()
timer = 0
def convert(texts):
    ans = ''
    for text in texts:
        try:
            ans += eng2thai[text]
        except KeyError:
            try:
                ans += thai2eng[text]
            except KeyError:
                ans += text
        except:
            print("something went wrong") 
            return False
    return ans       

def on_press(key):
    global timer
    if key == Key.f2:
        data = pyperclip.paste()
        data = convert(data)
        if data:
            keyboard.type(data)
    if key == Key.esc:
        timer +=1
    else:
        timer =0
        
def on_release(key):
    global timer
    if key == Key.esc:
        # Stop listener
        if timer >= 3:
            return False

# Collect events until released
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()