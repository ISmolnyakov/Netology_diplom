from database import *
from class_bot import *
from keyboard import sender


for event in vk_bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        sender(user_id, msg.lower())
        if request == 'начать поиск':
            creating_database()
            vk_bot.write_msg(user_id, f'Привет, {vk_bot.name(user_id)}')
            vk_bot.find_user(user_id)
            vk_bot.write_msg(event.user_id, f'Нашёл для тебя пару, жми на кнопку "Вперёд"')
            vk_bot.find_persons(user_id, offset)

        elif request == 'вперёд':
            for i in line:
                offset += 1
                vk_bot.find_persons(user_id, offset)
                break

        else:
            vk_bot.write_msg(event.user_id, 'Твоё сообщение непонятно')