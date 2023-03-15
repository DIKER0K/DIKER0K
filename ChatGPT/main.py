import os

print('Бот запущен!')

NUMBERS_ROWS = 6


import openai
import telebot

openai.api_key = "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"
bot = telebot.TeleBot('5747127396:AAEXYrvUMht9LJqUzxoQA-Xg4Tv8wO98tRI')

if not os.path.exists("users"):
    os.mkdir("users")


@bot.message_handler(content_types=['text'])
def msg(message):
    if f"{message.chat.id}.txt" not in os.listdir('users'):
        with open(f"users/{message.chat.id}.txt", "x") as f:
            f.write('')

    with open(f'users/{message.chat.id}.txt', 'r', encoding='utf-8') as file:
        oldmes = file.read()

    if message.text == '/clear':
        with open(f'users/{message.chat.id}.txt', 'w', encoding='utf-8') as file:
            file.write('')
        return bot.send_message(chat_id=message.chat.id, text='История очищена!')

    try:
        send_message = bot.send_message(chat_id=message.chat.id, text='Обрабатываю запрос, пожалуйста подождите!')
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[{"role": "user", "content": oldmes},
                        {"role": "user","content": f'Предыдущие сообщения: {oldmes}; Запрос: {message.text}'}], presence_penalty=0.6)

        bot.edit_message_text(text=completion.choices[0].message["content"], chat_id=message.chat.id, message_id=send_message.message_id)

        with open(f'users/{message.chat.id}.txt', 'a+', encoding='utf-8') as file:
            file.write(message.text.replace('\n', ' ') + '\n' + completion.choices[0].message["content"].replace('\n', ' ') + '\n')


        with open(f'users/{message.chat.id}.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if len(lines) >= NUMBERS_ROWS +1:
            with open(f'users/{message.chat.id}.txt', 'w', encoding='utf-8') as f:
                f.writelines(lines[2:])

    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=e)



bot.infinity_polling()
