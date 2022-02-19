import time
import  pyautogui as pg
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
pg.write("\n 3...")
time.sleep(1)
pg.write("\n 2..")
time.sleep(1)
pg.write("\n 1.")
pg.write("\n Go !")
for i in range(100):
    time.sleep(0)
    pg.write("msg")
    pg.press("Enter")