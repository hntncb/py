import minimodule
import threading
import time
from pynput import keyboard
isStop = False
listen = keyboard.Listener()
profiles = [minimodule.ProfileInfo('Thread1'),minimodule.ProfileInfo('Thread2')]

def showInfo(profiles,sleepTime):
    while True:
        print(profiles.Name)
        if (profiles.isStop):
            break
        time.sleep(sleepTime)
    totalRunningThread = any(x.isStop == False for x in profiles)
    print("Total: {}\n".format(totalRunningThread))
    if(totalRunningThread == False):
        listen.stop()

def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    print('vk =', vk)
    if(vk == None):
        return
    index = vk - 48
    if(index >= 0 and index < len(profiles) and profiles[index].isStop == False):
        print("Doing stop: {}".format(profiles[index].Name))
        profiles[index].isStop = True

if __name__== "__main__":
    isStop = False
    for item in profiles:
        thread = threading.Thread(target=showInfo, args=(item,1))
        thread.start()
    with keyboard.Listener(on_press=on_press) as listener:
        listen = listener
        listener.join()