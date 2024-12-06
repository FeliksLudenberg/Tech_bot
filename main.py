import sqlite3 
con = sqlite3.connect("auto-replies.db")

cur = con.cursor()
cur.execute('''CREATE TABLE question (id, question)''')
cur.execute('''
    INSERT INTO question VALUES
        (1, 'Как оформить заказ?'),
        (2, 'Как узнать статус моего заказа?'),
        (3, 'Как отменить заказ?'),
        (4, 'Что делать, если товар пришел поврежденным?'),
        (5, 'Как связаться с вашей технической поддержкой?'),
        (6, 'Как узнать информацию о доставке?')
''')


cur = con.cursor()
cur.execute('''CREATE TABLE answer (id, answer)''')
cur.execute('''
    INSERT INTO answer VALUES
        (1, 'Для оформления заказа, пожалуйста, выберите интересующий вас товар и нажмите кнопку "Добавить в корзину", затем перейдите в корзину и следуйте инструкциям для завершения покупки.'),
        (2, 'Вы можете узнать статус вашего заказа, войдя в свой аккаунт на нашем сайте и перейдя в раздел "Мои заказы". Там будет указан текущий статус вашего заказа.'),
        (3, 'Если вы хотите отменить заказ, пожалуйста, свяжитесь с нашей службой поддержки как можно скорее. Мы постараемся помочь вам с отменой заказа до его отправки.'),
        (4, 'При получении поврежденного товара, пожалуйста, сразу свяжитесь с нашей службой поддержки и предоставьте фотографии повреждений. Мы поможем вам с обменом или возвратом товара.'),
        (5, 'Вы можете связаться с нашей технической поддержкой через телефон на нашем сайте или написать нам в чат-бота.'),
        (6, 'Информацию о доставке вы можете найти на странице оформления заказа на нашем сайте. Там указаны доступные способы доставки и сроки.')
''')
con.commit()