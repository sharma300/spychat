from datetime import datetime



class Spy:



    def __init__(self, name, salutation, age, rating):

        self.name = name

        self.salutation = salutation

        self.age = age

        self.rating = rating

        self.is_online = True

        self.chats = []

        self.avg_word=0

        self.current_status_message = None





class ChatMessage:



    def __init__(self,message,sent_by_me):

        self.message = message

        self.time = datetime.now()

        self.sent_by_me = sent_by_me





spy = Spy('Sherlock Holmes', 'Mr.', 34, 4.1)



friend_one = Spy('Jhonny English', 'Mr.', 4.1, 26)

friend_two = Spy('Nick Fury', 'Mr.', 4.19, 29)

friend_three = Spy('Natasha', 'Ms.', 4.39, 31)





friends = [friend_one, friend_two, friend_three]