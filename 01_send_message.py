# -*- encoding:utf-8 -*-
# @time: 2022/7/7 12:23
# @author: Apple
"""
运行程序之前确保飞书是退出状态
"""
import time
import pyautogui
import cv2
import pyperclip


def send_msg(info):
    with open('to_send.txt', mode='r', encoding='utf-8') as f:
        for item in f:
            # 将名字筛选出来
            name = item.split(' ')[1].split(',')[-1].replace(']', "")
            time.sleep(2)
            pyautogui.keyDown('command')
            pyautogui.press('k')
            pyautogui.keyUp('command')
            time.sleep(2)
            pyperclip.copy(name)
            pyautogui.keyDown('command')
            pyautogui.press('v')
            pyautogui.keyUp('command')
            pyautogui.press('space')
            time.sleep(2)
            state, msg = findImg("check")
            if not state:
                pyautogui.click(600, 248)
                time.sleep(2)
                pyperclip.copy(info)
                pyautogui.keyDown('command')
                pyautogui.press('v')
                pyautogui.keyUp('command')
                pyautogui.press('enter')
                print(name, msg)
            else:  # 加上容错机制
                print(f'未找到联系人{name}')
                pyautogui.keyDown('command')
                pyautogui.press('k')
                pyautogui.keyUp('command')


def findImg(filename):
    try:
        im = pyautogui.screenshot()
        im.save('screen.png')
        screen = cv2.imread('./screen.png')
        joinMeeting = cv2.imread(f'{filename}.png')
        result = cv2.matchTemplate(joinMeeting, screen, cv2.TM_CCOEFF_NORMED)
        pos_start = cv2.minMaxLoc(result)[3]  # 获取最相似点相似坐标
        x = int(pos_start[0]) + int(joinMeeting.shape[1] / 2)
        y = int(pos_start[1]) + int(joinMeeting.shape[0] / 2)
        if x > 200:
            return False, '已发送'
        return True, [x, y]
    except Exception as e:
        print(e)
        return False, '已发送'


def run():
    msg = input('请输入想要批量转发的句子:').strip()
    time.sleep(3)
    # 返回主界面
    # pyautogui.keyDown("command")  # push win
    # pyautogui.press("m")
    # pyautogui.keyUp("command")  # release win
    # state, position = findImg("feishu")
    # time.sleep(2)
    # print(state, position)
    # pyautogui.click(position[0], position[1])  # double click
    # pyautogui.click(position[0], position[1])
    # time.sleep(2)
    # send message
    send_msg(msg)


if __name__ == '__main__':
    run()
