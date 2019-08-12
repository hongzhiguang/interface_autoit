
from util.MouseControl import *
from config.ProjVar import *
import time

def selectGetMethod():
    MouseControl.click(select_method_locate)
    MouseControl.move(method_get_locate)
    time.sleep(0.2)
    MouseControl.click(method_get_locate)

def selectPostMethod():
    MouseControl.click(select_method_locate)
    MouseControl.move(method_post_locate)
    time.sleep(0.2)
    MouseControl.click(method_post_locate)

def moveToUrl():
    MouseControl.move(url_locate)
    MouseControl.click(url_locate)

def moveToInputParam():
    MouseControl.move(input_param_locate)
    MouseControl.click(input_param_locate)

def moveTosignButton():
    MouseControl.move(sign_button_locate)
    time.sleep(0.5)
    MouseControl.click(sign_button_locate)

def moveToSendButton():
    MouseControl.move(send_button_locate)
    MouseControl.click(send_button_locate)

def moveToResponse():
    MouseControl.move(response_data_locate)
    MouseControl.click(response_data_locate)


