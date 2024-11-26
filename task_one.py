import nltk
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import gutenberg, stopwords

nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

def show_most_used_words(text, title):
    cnt = Counter(text)
    cort = cnt.most_common(10)
    x = [cort[el][0] for el in range(len(cort))]
    y = [cort[el][1] for el in range(len(cort))]
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel("Слова")
    plt.ylabel("Частота")
    plt.show()

def filter_text(text):
    words = [word for word in text if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

text = gutenberg.words('chesterton-thursday.txt')
show_most_used_words(text, title = "10 найбільш популярних слів у тексті")

cleaned_text = filter_text(text)
show_most_used_words(cleaned_text, title="10 найбільш популярних слів у тексті без стоп-слів та пунктуації")
