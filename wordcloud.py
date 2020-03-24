from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import platform

def word_cloud(text):
    tokens = tokenizer.nouns(text)
    stopwords = [] # 불용어
    tokens = [t for t in tokens if t not in stopwords]

    words = tokens.vocab().most_common(150)

    wordcloud = WordCloud(font_path = 'C:/Windows/Fonts/malgun.ttf',
                         relative_scaling = 0.2,
                         background_color = 'white',
                         ).generate_from_frequencies(dict(words))
    plt.figure(figsize=(12,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show