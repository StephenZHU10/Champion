# cv2.cvtColor takes a numpy ndarray as an argument 
import numpy as nm 
import pytesseract 
import string
# importing OpenCV 
import cv2 
import time 
import win32api,win32gui,win32con
import win32com.client

from PIL import ImageGrab 
from PIL import Image, ImageDraw, ImageFilter


def imToString(): 

    # Path of tesseract executable 
    pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\97158\\Tesseract-OCR\\tesseract.exe"  #此处为你安装Tesseract.exe的位置
    # ImageGrab-To capture the screen image in a loop. 
    # Bbox used to capture a specific area. 
    
    img = Image.new('RGB', (120, 70), color = (22, 20, 17))
    cap = ImageGrab.grab(bbox =(240, 272, 335, 320)) #(520L, 275L,  585L, 330L) (230, 270, 350, 340)
    img.paste(cap, (20, 20))
    
    # Converted the image to monochrome for it to be easily 
    # read by the OCR and obtained the output String. 
    
    #cap2 = cv2.adaptiveThreshold(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #        cv2.THRESH_BINARY,11,2)
    tesstr = pytesseract.image_to_string(cv2.cvtColor(nm.array(img), cv2.COLOR_BGR2GRAY), lang ='eng', config = 'digits') 
    return tesstr 

def test():
    time.sleep(5)
    msg = imToString()
    for c in string.punctuation:  
        msg = msg.replace(c,"")
    print(msg)
    
#test()

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)

fo4 = [(hwnd, title) for hwnd, title in winlist if 'FIFA' in title.upper()]
# just grab the hwnd for first window matching FIFA
fo4 = fo4[0]
hwnd = fo4[0]

self='FIFA ONLINE 4'

def show(self):  
    win32gui.ShowWindow(hwnd,1) 
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)  

def main(int dest)：                                                   # dest为目标分数
	while(1):
	    time.sleep(5)
	    #hwnd = 395100
	    shell = win32com.client.Dispatch("WScript.Shell")
	    shell.SendKeys('%')
	    win32gui.SetForegroundWindow(hwnd)
	    
	    msg = imToString()
	    for c in string.punctuation:  
	        msg = msg.replace(c,"")    
	    score = int(msg)
	    print("Your current score is: ", score, ". Haven't reached the desired score yet.")
	    
	    if (score >= dest or score <= 1800):
	    	print("Your current score is: ", score, ". Congratulations! Mission accomplished.")
	        break
	    else:
	        show(self)
	        win32api.keybd_event(120,0,0,0)                              # 此处按下F9（0x78 = 120），为ifuzhu默认启动热键，有需要更改的请自行修改此处值
	        win32api.keybd_event(120,0,win32con.KEYEVENTF_KEYUP,0) 
	    time.sleep(900)

main(2550)


##   FOR TEST PURPOSE ONLY   ##
#from pymouse import PyMouse

## instantiate an mouse object
#m = PyMouse()
#time.sleep(5)
#m.move(240L, 272L)
#time.sleep(5)
#m.move(330L, 320L)

## instantiate an mouse object
#m = PyMouse()
#time.sleep(5)
#print(m.position())
#time.sleep(5)
#m.position()

#def get_pixel_colour(i_x, i_y):
#	i_desktop_window_id = win32gui.GetDesktopWindow()
#	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
#	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
#	i_colour = int(long_colour)
#	win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
#	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

#time.sleep(5)
#print (get_pixel_colour(335, 320))

