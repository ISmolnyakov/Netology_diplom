import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
import requests
import datetime
from config import user_token, group_token


class VKBot:

    def __int__(self):
        self.vk_group = vk_api.VkApi(token=group_token)
        self.longpoll = VkLongPoll(self.vk_group)

    def write_msg(self, user_id):
        self.vk_group.method('messages.send', {'user_id': user_id,
                                               'message': message,
                                               'random_id': randrange(10 ** 7)})

    def find_city(self, user_id):
        params = {'access_token': group_token,
                  'v': '5.131',
                  'user_ids': user_id,
                  'fields': 'city'}
        response = self.vk_group.method("users.get", params)
        try:
            for town in response:
                if 'city' in town:
                    city = town.get('city')
                    id = str(city.get('id'))
                    return id
                elif 'city' not in town:
                    self.write_msg(user_id, 'Введите название вашего города: ')
                    for event in self.longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                            city_name = event.text
                            id_city = self.cities(user_id, city_name)
                            if id_city != '' or id_city != None:
                                return str(id_city)
                            else:
                                break
        except KeyError:
            self.write_msg(user_id, 'Ошибка получения токена')
        return city

    def get_sex(self, user_id):
        params = {'access_token': group_token,
                  'v': '5.131',
                  'user_ids': user_id,
                  'fields': 'sex'}
        req = self.vk_group.method("users.get", params)
        try:
            for i in req:
                if i.get('sex') == 2:
                    opposite_sex = 1
                    return opposite_sex
                elif i.get('sex') == 1:
                    opposite_sex = 2
                    return opposite_sex
        except KeyError:
            self.vk_group.method(user_id, 'Ошибка получения токена, введите токен в переменную - user_token')

    def check_low_age(self, user_id):
        return low_age

    def check_high_age(self, user_id):
        return high_age

    def find_person(self, user_id):
        return

    def get_photo(self, user_id):
        return top_three_photos


vk_bot = VKBot()
