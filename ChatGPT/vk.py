import vk_api
import openai
import random

# Авторизация бота в ВКонтакте
vk_session = vk_api.VkApi(token='vk1.a.ptCAnpWkPlWaIDHMPhGbOCO5Tu8c7QWkvD4vBjMJWctjnIw0AfFLQK9AZpcikfGhdADophisqRMT8VapSj9zd0Be1rlFGVRsuiKcMBG-DQl-t1v6ykw4lLoxmVcQ3Q68Ok8yF6JtwdGU66xdBQpr_t--BgkICYvere3GuUjUXBR15_7ILR3sLgLjHv8KA0UDwF2LUR7VI1xkQgoTSuvVKQ')
vk = vk_session.get_api()

# Авторизация OpenAI API
openai.api_key = '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'

# Функция для генерации ответа при получении нового сообщения  
def generate_response(message):     
    model_engine = "text-davinci-003"     
    prompt = message['text']     
    completions = openai.Completion.create(         
        engine=model_engine,         
        prompt=prompt,         
        max_tokens=1024     
    )     
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
                vk.messages.send(user_id=from_id, message=response_text, random_id=random.randint(1, 1000))
