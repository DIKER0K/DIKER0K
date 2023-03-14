import vk_api 
import openai  
# Авторизация бота в ВКонтакте 
vk_session = vk_api.VkApi(token='ваш токен') 
vk = vk_session.get_api()  
# Авторизация OpenAI API 
openai.api_key = 'ваш API ключ'  
# Функция для генерации ответа при получении нового сообщения 
def generate_response(message):
     model_engine = "completions"
     prompt = message['text']
     completions = openai.Completion.create(
     engine=model_engine, prompt=prompt, max_tokens=1024     )
     
     return completions.choices[0].text.strip()  
# Бесконечный цикл чтения и ответа на новые сообщения 
while True:
     # Получение новых сообщений от пользователей
     response = vk.messages.getConversations(filter='unanswered', count=20)
     
     if response['count'] >= 1:
        items = response['items']
        for item in items:
        last_message = item['last_message']   
        from_id = last_message['from_id']  
        if from_id != vk_session.token['access_token']: 
        # Генерация ответа                 
        response_text = generate_response(last_message)                                  
        # Отправка ответа пользователю                 
        vk.messages.send(user_id=from_id, message=response_text)