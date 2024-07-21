import tkinter as tt
from wordcloud import WordCloud
from matplotlib import pyplot as plt

# words & clouds
def figureCloud():
    plt.figure(figsize=(10, 10))
    plt.imshow(cloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("pics/cloud.jpg")
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