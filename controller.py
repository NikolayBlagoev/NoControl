import vgamepad as vg
from pynput.keyboard import Key, Listener, Controller
gamepad = vg.VX360Gamepad()
st_dict = {}
r_vect = [0,0]
l_vect = [0,0]
listener=None
btn_display = None
vkKodeToKey = {
   49 : "1",
    50 : " 2 ",
    51 : " 3 ",
    52 : " 4 ",
    53 : " 5 ",
    54 : " 6 ",
    55 : " 7 ",
    56 : " 8 ",
    57 : " 9 ",
    48 : " 0 ",
    189 : " - ",
    187 : " = ",
    81 : " q ",
    87 : " w ",
    69 : " e ",
    82 : " r ",
    84 : " t ",
    89 : " y ",
    85 : " u ",
    73 : " i ",
    79 : " o ",
    80 : " p ",
    221 : " ] ",
    65 : " a ",
    83 : " s ",
    68 : " d ",
    70 : " f ",
    71 : " g ",
    72 : " h ",
    74 : " j ",
    75 : " k ",
    76 : " l ",
    186 : " ; ",
    90 : " z ",
    86 : " v ",
    66 : " b ",
    78 : " n ",
    77 : " m ",
    67 : " c ",
    188 : " , ",
    190 : " . ",
    191 : " / ",
    97 : " <97> ",
    98 : " <98> ",
    99 : " <99> ",
    102 : " <102> ",
    101 : " <101> ",
    100 : " <100> ",
    103 : " <103> ",
    105 : " <105> ",
    104 : " <104> ",
    144 : " Key.num_lock ",
    36 : " Key.home ",
    38 : " Key.up ",
    33 : " Key.page_up ",
    39 : " Key.right ",
    12 : " <12> ",
    37 : " Key.left ",
    35 : " Key.end ",
    40 : " Key.down ",
    34 : " Key.page_down ",
    38 : " Key.up ",
    40 : " Key.down ",
    37 : " Key.left ",
    39 : " Key.right ",
}
msgprv = 0
keyw = ""
def on_press(key):
    global keyw
    if key == Key.f6:
        st_dict["running"] = not st_dict["running"]
        if st_dict["running"]:
            btn_display.setText("STOP (F6)")
        else:
            btn_display.setText("START (F6)")
        return
    if not st_dict["running"]:
        return
    key = str(key).strip("\'")
    if(st_dict.get(key) is None):
        # print("a",key, "a")
        
        return
    if(st_dict[key] == "LUP"):
        l_vect[1] += 1
    elif(st_dict[key] == "LDOWN"):
        l_vect[1] -= 1
    elif(st_dict[key] == "LRIGHT"):
        l_vect[0] += 1
    elif(st_dict[key] == "LLEFT"):
        l_vect[0] -= 1
    elif(st_dict[key] == "RUP"):
        r_vect[1] += 1
    elif(st_dict[key] == "RDOWN"):
        r_vect[1] -= 1
    elif(st_dict[key] == "RRIGHT"):
        r_vect[0] += 1
    elif(st_dict[key] == "RLEFT"):
        r_vect[0] -= 1
    else:
        print("pressing ", st_dict[key])
        gamepad.press_button(button = st_dict[key])
    
    l_vect[0] = min(max(l_vect[0],-1),1)
    r_vect[0] = min(max(r_vect[0],-1),1)
    l_vect[1] = min(max(l_vect[1],-1),1)
    r_vect[1] = min(max(r_vect[1],-1),1)
    print("prs", l_vect)
    gamepad.left_joystick_float(x_value_float=l_vect[0], y_value_float=l_vect[1])
    gamepad.right_joystick_float(x_value_float=r_vect[0], y_value_float=r_vect[1])
    gamepad.update()
  
def on_release(key):
    if not st_dict["running"]:
        return
    key = str(key).strip("\'")
    if(st_dict.get(key) is None):
        # print("a",key, "a")
        
        return
    if(st_dict[key] == "LUP"):
        l_vect[1] -= 1
    elif(st_dict[key] == "LDOWN"):
        l_vect[1] += 1
    elif(st_dict[key] == "LRIGHT"):
        l_vect[0] -= 1
    elif(st_dict[key] == "LLEFT"):
        l_vect[0] += 1
    elif(st_dict[key] == "RUP"):
        r_vect[1] -= 1
    elif(st_dict[key] == "RDOWN"):
        r_vect[1] += 1
    elif(st_dict[key] == "RRIGHT"):
        r_vect[0] -= 1
    elif(st_dict[key] == "RLEFT"):
        r_vect[0] += 1
    else:
        print("releasing ", st_dict[key])
        gamepad.release_button(button = st_dict[key])
    
    l_vect[0] = min(max(l_vect[0],-1),1)
    r_vect[0] = min(max(r_vect[0],-1),1)
    l_vect[1] = min(max(l_vect[1],-1),1)
    r_vect[1] = min(max(r_vect[1],-1),1)
    print("rls",l_vect)
    gamepad.left_joystick_float(x_value_float=l_vect[0], y_value_float=l_vect[1])
    gamepad.right_joystick_float(x_value_float=r_vect[0], y_value_float=r_vect[1])
    gamepad.update()
    


def win32_event_filter(msg, data):
    # global msgprv
    # if(msgprv != data.vkCode):
    #     msgprv = data.vkCode
    # else:
    #     print(data.vkCode, ": \"", keyw,"\"")
    # print(data.vkCode)
    if not st_dict["running"]:
        listener._suppress = False
        return
    code = data.vkCode
    if vkKodeToKey.get(code) is None:
        listener._suppress = False
        return
    if st_dict.get(vkKodeToKey[code].strip()) is None:
        print(",",vkKodeToKey[code].strip(),".")
        listener._suppress = False
    else:
        print("suppress")
        listener._suppress = True
    return

def controller(key_dict = {}, btn = None):
    global st_dict
    global listener
    global btn_display
    btn_display = btn
    st_dict = key_dict
    listener = Listener(
        on_press=on_press,
        on_release=on_release, win32_event_filter=win32_event_filter)
    listener.start()
