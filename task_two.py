import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Обєкти для стемінга та лематизації
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


def preprocess_text(text):
    # 1. Токенізація
    tokens = word_tokenize(text)
    # 2. лематизація та стемінг
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    stemmed = [stemmer.stem(word) for word in lemmatized]
    # 3. Видалення стоп-слів
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in stemmed if word.lower() not in stop_words]
    # 4. Видалення пунктуації
    processed_words = [word for word in filtered_words if word.isalpha()]

    return processed_words


input_file_path = 'input_text.txt'
output_file_path = 'processed_text.txt'

try:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    processed_text = preprocess_text(text)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(' '.join(processed_text))

    print(f"Оброблений текст записан у файл {output_file_path}")

except FileNotFoundError:
    print(f"Файл {input_file_path} не знайдено!")

