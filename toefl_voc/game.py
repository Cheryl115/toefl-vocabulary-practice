# -*- coding: utf-8 -*-
#!/usr/bin/env python


import tkinter as tk
import csv
import random
from random import shuffle
from PIL import Image, ImageTk
from tkmacosx import Button
import time

window = tk.Tk()
window.title('TOEFL vocabulary Practice')
window.geometry('500x500')
vocs = []

with open('voc.csv', 'r',encoding="UTF-8") as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    vocs.append(row)
    
csvfile.close

frame = tk.Frame(window)
frame.pack(pady=24)

var = tk.StringVar()    # 这时文字变量储存器
voc = tk.Label(frame, textvariable=var, font=('Noto Sans TC', 14)) # 使用 textvariable 替换 text, 因为这个可以变化
voc.grid(row=0,column=0,columnspan=2)

var1 = tk.StringVar()    # 这时文字变量储存器
pos = tk.Label(frame, textvariable=var1, font=('Noto Sans TC', 14)) # 使用 textvariable 替换 text, 因为这个可以变化
pos.grid(row=1, column=0)

var2 = tk.StringVar()    # 这时文字变量储存器
meaning = tk.Label(frame, textvariable=var2, font=('Noto Sans TC', 14)) # 使用 textvariable 替换 text, 因为这个可以变化
meaning.grid(row=1,column=1)


text = tk.StringVar()
text.set('Start')


btn1 = False
def btn1_click():
    global btn1
    #當按鈕被按下
    if btn1 == False:
        flag = True
        btn1 = True
        while(flag==True):
            voc = random.choice(vocs)
            try:
                if voc[0]!='None' and voc[1]!='None' and voc[2]!='None':
                    var.set(voc[0])
                    var1.set(voc[1])
                    var2.set(voc[2])
                    text.set('Next')
                    flag = False
                    
            except Exception:
                flag = True
    else:
        btn1 = False
        var.set('')
        var1.set('')
        var2.set('')
        

# 第5步，在視窗介面設定放置Button按鍵
b1 = Button(window, 
               textvariable=text, 
               font=('Noto Sans TC', 14), 
               padx=12, pady=4, 
               borderwidth=0,
               focuscolor='',
               fg='#0B1013',
               bg='#81C7D4',
               activebackground='#51A8DD',
               activeforeground='#0B1013',
               command=btn1_click,
               borderless=1)
b1.pack(pady=24)

canvas = tk.Canvas(window, height=500, width=500)
image_file = Image.open('tensai_girl.png')
resiged_img = image_file.resize((200,187))
img = ImageTk.PhotoImage(resiged_img)
image = canvas.create_image(250, 0, anchor='n',image=img)
canvas.pack()

window.mainloop()
