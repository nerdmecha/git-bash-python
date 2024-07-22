import tkinter as tt
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from gtts import gTTS
from playsound import playsound
import time as t

# words & clouds
def figureCloud():
    plt.figure(figsize=(10, 10))
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("imgs/cloud.jpg")
    plt.show()

words = {
    'Tokusatsu': 15,
    'Video Games': 14,
    'Fanfics': 13,
    'Anime & Manga': 12,
    'Money': 12,
    'Friends': 12,
    'Foods': 11,
    'Pixelarts': 10
}

cloud = WordCloud(
    font_path="fonts/HancomMalangMalang-Bold.ttf",
    width=1000,
    height=1000,
    colormap='rainbow'
).generate_from_frequencies(words)

# langs & speech
def inputSpeaker():
    tts.save("auds/speech.mp3")
    t.sleep(5)
    playsound("auds/speech.mp3")


lang = input("Select Your Language - English or Korean : ")

while "English" not in lang and "Korean" not in lang:
    lang = input("PLZ Input Again - English or Korean : ")

if "English" in lang:
    text = input("Input Eng Lines : ")
    tts = gTTS(text=text, lang='en')
elif "Korean" in lang:
    text = input("한국어로 문장을 입력하세요 : ")
    tts = gTTS(text=text, lang='ko')
else:
    tts = gTTS(text="Good Bye", lang='en')