import sys, keyboard, time
menu=[]
unter={'Leiste':{'Datei':{
                        'p1':{"Name":"Neu","short":"ctrl+n"},
                        'p2':{"Name":"Neues Fenster","short":"Strg+shift+N"},
                        'p3':{'Name':'Öffnen','short':'ctrl+o'}
                        },
                'Bearbeiten':{
                        'p1':{'Name':'Undo','short':'ctrl+z'},
                        'p2':{'Name':'Redo','short':'ctrl+y'}
                },
                'Format':{
                        'p1':{'Name':'format','short':'ctrl+f'},
                        'p2':{'Name':'Redo','short':'ctrl+g'}
                },
                'Ansicht':{
                        'p1':{'Name':'ansicht','short':'ctrl+a'},
                        'p2':{'Name':'Redo','short':''}
                        },
                'Hilfe':{
                        'p1':{'Name':'Hilfe','short':'ctrl+h'},
                        'p2':{'Name':'Redo','short':''}
                        }
                        }
                        }

fg = {
    'Black': 30,
    'Red': 31,
    'Green': 32,
    'Yellow': 33,
    'Blue': 34,
    'Magenta': 35,
    'Cyan': 36,
    'White': 37,
    'Reset': 0
}



def set_fg_color(color: str):
    funk = f'\u001b[{fg[color]}m'
    return funk

def set_bg_color(color: str):
    farb = fg[color]+10
    funk = f'\u001b[{farb}m'
    return funk





for i in unter['Leiste'].keys():
        menu.append(i)

SET_ANSI_CTRL_SEQUENCE = '\u001b['
Anzeige = ''



def show_menu():
    z = 1
    for i in menu:
        if z == 1:
            print('┌'+'─'*len(i), end = '')
            z+=1
        elif z == len(menu):
            print('┬'+'─'*(len(i)+30)+'┐')
        else:
            print('┬'+'─'*len(i), end = '')
            z+=1
    z=1
    for i in menu:

        if i == Anzeige and z!=len(menu):
            co = set_fg_color("Green")
            print('│'+ co+ i, end = '')
            print(set_fg_color("Reset"), end = "")
            z+=1
        elif z == len(menu):
            if i == Anzeige :
                co = set_fg_color("Green")
                re = set_fg_color("Reset")
                print('│'+co+i+re +' '*30+'│' )

            else:
                print('│'+i+' '*30+'│', )

        else:
            print('│'+i, end = '')
            z+=1



    z=1
    for i in menu:
        if z == 1:
            print('└'+'─'*len(i), end = '')
            z+=1
        elif z == len(menu):
            print('┴'+'─'*(len(i)+30)+'┘')
        #elif z == 4 :
        #    print('┴'+'─'*(len(i)-1) +'┬', end = '')
        #    z+=1
        else:
            print('┴'+'─'*len(i), end = '')
            z+=1



def sub_menu_pos():
    summe = 0
    for i in menu :
        if i == Anzeige :
            break
        else:
            summe = len(i)+summe+1

    return summe+1


def clear_screen():
    sys.stdout.write(SET_ANSI_CTRL_SEQUENCE + '2J')

def move_cursor_to(x: int, y: int):
    sys.stdout.write(SET_ANSI_CTRL_SEQUENCE + '{};{}H'.format(y,x))
def sub_menu_si():
    pos = sub_menu_pos()
    move_cursor_to(pos,3)
    if pos == 1:
        print('├')
    else:
        print('┼')
    max_len = 0
    for i in unter['Leiste'][Anzeige].values():
        a = len(i['short'])
        b = len(i['Name'])
        c = a + b
        if c > max_len:
            max_len = c
    endpos = pos + max_len+10
    move_cursor_to(endpos,3)
    print('┬')





def show_sub_menu():
    pos = sub_menu_pos( )
    move_cursor_to(pos,4)
    max_len = 0
    for i in unter['Leiste'][Anzeige].values():
        a = len(i['short'])
        b = len(i['Name'])
        c = a + b
        if c > max_len:
            max_len = c
    k=1
    y = 4
    for b in unter['Leiste'][Anzeige].values() :
        if k == len(unter['Leiste'][Anzeige].keys()):
            move_cursor_to(pos,y)
            print('│'+' '*2+b['Name']+" "* (max_len+5 - len(b['Name'])-len(b['short'])) +b['short']+' '*2 +'│')
            move_cursor_to(pos,y+1)
            print('└'+'─'*(max_len+9)+'┘')
            y+=2
        else:
            move_cursor_to(pos,y)
            print('│'+' '*2+b['Name']+" "* (max_len+5 - len(b['Name'])-len(b['short'])) +b['short']+' '*2+'│')
            move_cursor_to(pos,y+1)
            print('├'+'─'*(max_len+9) +'┤')
            k  +=1
            y+=2
shortcuts=[]
for i in menu:
    shortcuts.append('alt+'+i[0].lower())
short_menu= dict(zip(shortcuts,menu))
#print(short_menu)
def runner(m):
    global Anzeige
    Anzeige = m
    clear_screen()
    move_cursor_to(0,0)
    show_menu()
    sub_menu_si()
    show_sub_menu()

show_menu()

for i in short_menu:
    keyboard.add_hotkey(i,runner ,args= [short_menu[i]] , suppress=True)



keyboard.wait('strg+q', suppress=True)
clear_screen()
move_cursor_to(0,0)
sys.exit()










while True :
    g = keyboard.read_hotkey()
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP :
        if g == "q":
            clear_screen()
            move_cursor_to(0,0)
            sys.exit()
        for i in shortcuts:
            if g==i:
                runner(short_menu[i])
        g= ''
        event = False








    if keyboard.is_pressed('b'):
        Anzeige='Bearbeiten'
        clear_screen()
        move_cursor_to(0,0)
        show_menu()
        sub_menu_si()
        show_sub_menu()
    if keyboard.is_pressed('d'):
        Anzeige='Datei'
        clear_screen()
        move_cursor_to(0,0)
        show_menu()
        sub_menu_si()
        show_sub_menu()
    if keyboard.is_pressed('F'):
        Anzeige='Format'
        clear_screen()
        move_cursor_to(0,0)
        show_menu()
        sub_menu_si()
        show_sub_menu()
    if keyboard.is_pressed('a'):
        Anzeige='Ansicht'
        clear_screen()
        move_cursor_to(0,0)
        show_menu()
        sub_menu_si()
        show_sub_menu()
    if keyboard.is_pressed('H'):
        Anzeige='Hilfe'
        clear_screen()
        move_cursor_to(0,0)
        show_menu()
        sub_menu_si()
        show_sub_menu()

