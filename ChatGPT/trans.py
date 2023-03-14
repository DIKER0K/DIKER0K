from googletrans import Translator 

# Открыть файл с английским текстом
with open('example.txt', 'r') as file:
    text = file.read() 

# Создать экземпляр класса Translator
translator = Translator()  

# Перевести текст на русский язык
translated_text = translator.translate(text, dest='ru').text 

# Записать оригинальный и переведенный текст в файл result.py
with open('result.txt', 'w') as file:
    file.write(f'Оригинал:\n{text}\n\nПеревод:\n{translated_text}')

if file.closed == False:
    print("Файл успешно создан!")