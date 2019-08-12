import pythoncom
import PyHook3

def onMouseEvent(event):
    # 监听鼠标事件
    print("MessageName:", event.MessageName)
    return True


def onKeyboardEvent(event):
    # 监听键盘事件
    print("MessageName:", event.MessageName)
    print("Key:", event.Key)
    print("KeyID:", event.KeyID)
    return True

def main():
    # 创建一个“钩子”管理对象
    hm = PyHook3.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 监听所有鼠标事件
    # hm.MouseAll = onMouseEvent
    # 设置鼠标“钩子”
    # hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main()




