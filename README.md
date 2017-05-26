# Music Theraphy with Google Music

Музикотерапія - це процес міжособистісного спілкування, у якому кваліфікований музикотерапевт застосовує музику та всі сторони її впливу - фізичну, емоційну, інтелектуальну, соціальну, естетичну і духовну - з метою покращення чи збереження здоров’я клієтна. Ця програма допоможе вам відчути вплив музики на ваше здоров'я.

У даній програмі користувач вибирає клас до якого належить його хвороба. І на основі вибраного класу згенерується плейлист пісень на його Google Music аккаунт.

Для виконання даного проекту було використано Google Music API. Будування запиту обчислення отриманої інформації відбувається на Python.

# Вхідні та вихідні дані

Вхідними даними є лише вибір класу хвороби та назва хвороби, щоб дізнатись, який плейлист генерувати та як його назвати. Отримана інформація зберігається в Playlist, де спершу всім елементам плейлисту задано значення None. 

Кожен елемент даного Playlist, після його генерації містить лише id пісні, яка згодом записується у створений плейлист на Google Music аккаунті користувача.

# Структура

Структура проекту:
  -doc/ - модулі з детальними описами усіх етапів виконання проекту
  -modules/ -основна частина програми
    - Brain.py - реалізація класу для розумової активності
    - Breath.py - реалізація класу для дихальної системи
    - Cardiovascular.py  - реалізація класу для серцево-судинної системи
    - HeartRate.py - реалізація класу для ритму серця
    - Mental.py - реалізація класу для психічного здоров'я
    - Playlist.py - реалізація ADT
    - arrays.py - реалізація Array
    - index.py - запуск програми
  
  
# Інструкція

Щоб інсталювати цей проект, потрібно клонувати його:

git clone https://MaxVoloskiy/Coursework.git

Після клонування запустити modules/index.py
