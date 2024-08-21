import tkinter as tk
from tkinter import messagebox
from tkinter import font
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from gtts import gTTS
from playsound import playsound
import time as t

from functions import *

# Lastest Edited | 2024 aug 21st wed pm 05:00 utc+09:00
# X(Twitter) @shininggrail | Discord nerdmecha#1806 | GameJolt @nerdmecha

# figureCloud() # active words & clouds
# inputSpeaker() # active langs & speech

def entryShow():
    entry = tk.Entry(window, width=30)
    entry.pack(pady=10)

    buttonSubmit = tk.Button(window, text="submit", command=lambda: submit(entry))
    buttonSubmit.pack(pady=5)

def submit(entry):
    userInput = entry.get()
    tts = gTTS(text=userInput, lang='en')
    tts.save("auds/speechTwo.mp3")
    t.sleep(5)
    playsound("auds/speechTwo.mp3")


def activeButton(buttonNumber):
    if buttonNumber == 1:
       figureCloud()
    if buttonNumber == 2:
        entryShow()

window = tk.Tk()

x = 400
y = 300

width = str(x)
height = str(y)

window.title("Python Github")
window.geometry(width +"x"+ height)

fontPath = font.Font(font="fonts/HancomMalangMalang-Bold.ttf")

label = tk.Label(window, text="Choose Your Button", font=fontPath)
label.place(relx=0.5, rely=0.5, anchor="center")

button01 = tk.Button(window, text="Press 01", command=lambda: activeButton(1))
button01.place(x=100, y=180, width=200, height=50)

button02 = tk.Button(window, text="Press 02", command=lambda: activeButton(2))
button02.place(x=100, y=90, width=200, height=50)

window.mainloop()