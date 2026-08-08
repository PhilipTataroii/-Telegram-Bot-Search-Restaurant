import os
from peewee import SqliteDatabase, Model, CharField, IntegerField, DateTimeField
from datetime import datetime
from Token_and_Database.config import DB_PATH

# ⚡ удаляем старый файл базы при старте
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print("⚡ database.db удалён автоматически")

# создаём новое подключение
db = SqliteDatabase(DB_PATH)

class Restaurant(Model):
    name = CharField()
    cuisine = CharField()
    address = CharField()
    image_url = CharField(null=True)
    website = CharField(null=True)
    phone = CharField(null=True)
    email = CharField(null=True)

    class Meta:
        database = db

class History(Model):
    user_id = IntegerField()
    query = CharField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db

# подключаемся и пересоздаём таблицы
db.connect()
db.create_tables([Restaurant, History])
print("⚡ Таблицы Restaurant и History пересозданы")

# добавляем рестораны с сушами
Restaurant.create(
    name="Sushi House",
    cuisine="суши",
    address="ул. Пушкина, 12",
    image_url="https://franch-region.ru/upload/iblock/fa7/fc554bsp3fornvnsociiy37j3jimm6ht.jpg",
    website="https://www.sushihouse.md/",
    phone="+373 682 48 686",
    email="info@sushihouse.md"
)

Restaurant.create(
    name="Tokyo Roll",
    cuisine="суши",
    address="ул. Штефан чел Маре, 45",
    image_url="https://avatars.mds.yandex.net/get-altay/14811824/2a0000019504e334a31871b74c2fa0e0c376/orig",
    website="https://hatiko-sushi.md/ro/rolly/tokio-roll",
    phone="+373 785 48 048",
    email="No Email"
)

Restaurant.create(
    name="Samurai",
    cuisine="суши",
    address="ул. Армянская, 8",
    image_url="https://images.pexels.com/photos/34313405/pexels-photo-34313405.jpeg",
    website="https://samurai.md/",
    phone="+373 228 00 805",
    email="No Email"
)

#добавляем рестораны с пиццами
Restaurant.create(
    name="Pizza Andy's",
    cuisine="пицца",
    address='бул. Штефан чел Маре, 77',
    image_url="https://avatars.mds.yandex.net/get-altay/14811824/2a00000196ed296c8a5bb9c01e58fd9227a7/XXL_height",
    website="https://andys.md/",
    phone="+373 222 10 210",
    email="office@andys.md"

)

Restaurant.create(
    name="Casa Della Pizza",
    cuisine="пицца",
    address='ул.Михаил Когалнычяну 62',
    image_url="https://avatars.mds.yandex.net/get-altay/18166435/2a0000019c44161a7449b42a389f851c28a3/XXL_height",
    website="https://casadellapizza.md/",
    phone="+373 688 40 830",
    email="dmgpizza@gmail.com"
)

Restaurant.create(
    name="Pizzart",
    cuisine="пицца",
    address='бул. Штефан чел Маре, 67',
    image_url="https://avatars.mds.yandex.net/get-altay/9828935/2a000001896e7809fe2b84d97199c1f70406/XXL_height",
    website="https://pizzart.md/",
    phone="+373 683 56 554",
    email="info@pizzart.md"
)


print("⚡ Тестовые рестораны добавлены")




