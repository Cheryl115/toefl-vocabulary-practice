# -*- coding: utf-8 -*-
#!/usr/bin/env python


import tkinter as tk
import csv
import random
from random import shuffle

window = tk.Tk()
window.title('Practice')
window.geometry('500x500')
vocs = []

with open('voc.csv', 'r',encoding="UTF-8") as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    vocs.append(row)
    
csvfile.close

var = tk.StringVar()    # 这时文字变量储存器
vocabulary = tk.Label(window, textvariable=var, font=('Arial', 12)) # 使用 textvariable 替换 text, 因为这个可以变化
vocabulary.pack()

var1 = tk.StringVar()    # 这时文字变量储存器
pos = tk.Label(window, textvariable=var1, font=('Arial', 12)) # 使用 textvariable 替换 text, 因为这个可以变化
pos.pack()


var2 = tk.StringVar()    # 这时文字变量储存器
meaning = tk.Label(window, textvariable=var2, font=('Arial', 12)) # 使用 textvariable 替换 text, 因为这个可以变化
meaning.pack()


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
                var.set(voc[0])
                var1.set(voc[1])
                var2.set(voc[2])
                flag = False
            except Exception:
                flag = True
    else:
        btn1 = False
        var.set('')
        var1.set('')
        var2.set('')
        

# 第5步，在視窗介面設定放置Button按鍵
b1 = tk.Button(window, text='Next', font=('Arial', 12), width=10, height=1, command=btn1_click)
b1.pack()

canvas = tk.Canvas(window, height=500, width=500)
image_file = tk.PhotoImage(file='tensai_girl.png')
image = canvas.create_image(250, 0, anchor='n',image=image_file)
canvas.pack()

window.mainloop()
