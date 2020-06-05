from selenium import webdriver
import tkinter as tk
from tkinter import Text

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
f = open('words.txt', 'r')
dic = f.read().split(',')


#word = driver.find_element_by_id('currentWord')
def launchURL():
    skrURL = url.get()
    driver.get(skrURL)


def checkLength(x, y):
    if len(x) == len(y):
        return True
    else:
        return False


def checkChar(x, y):
    chars = []
    for char in enumerate(x):
        if char[1] != '_':
            chars.append(char)
    for val in chars:
        if y[val[0]] != val[1]:
            return False
    return True


def checkDic():
    lb1.delete(0, tk.END)

    word = driver.find_element_by_id('currentWord').text
    
    results = []
    for x in dic:
        if checkLength(word, x) and checkChar(word, x):
            
            results.append(x)
    
    for x in results:
        lb1.insert(tk.END, x)



def main(toggle=False):
    global tracking_var
    if toggle:
        if tracking_var:
            tracking_var = False
        else:
            tracking_var = True

    if tracking_var:
        checkDic()
        root.after(5000, main)


root = tk.Tk()

scrollbar = tk.Scrollbar(root)
tracking_var = False
url = tk.Entry(root, width=100, bg="white")
url.grid(column=0, padx=10)

joinGame = tk.Button(root, text='Join Game', padx=10, pady=5, fg="white", bg='#bdbdbd', command=launchURL)
joinGame.grid(column=1, row=0, padx=10)

start = tk.Button(root, text='Start', padx=10, pady=5, fg="white", bg='#bdbdbd', command=lambda: main(True))
start.grid(column=2, row=0, padx=10)

lb1 = tk.Listbox(root, height=50, width=100, bg='#bdbdbd', yscrollcommand = scrollbar.set)
lb1.grid(columnspan=4, row=1, padx=10, pady=10)

scrollbar.grid(column=3, rowspan=2)


root.mainloop()