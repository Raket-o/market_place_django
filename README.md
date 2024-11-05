<div style="text-align: center">
<img src="./images_readme/logo.png" width="650" alt="logo"/>
</div>
<h1 style="text-align: center">Проект - онлайн магазин.</h1>

Краткое описание:
Разработано веб-приложение для телеграмм бота - онлайн магазин, которое позволит эффективно повысить уровень продаж.

1. Каталог товаров:
   * покупатели могут просматривать товары;
   * сортировать их по категориям.

<img src="images_readme/best_sellers.png" width="250" alt="best_sellers"/>
<img src="images_readme/details_product.png" width="250" alt="best_sellers"/>

2. Корзина покупок:
   * возможность добавлять товары в корзину;
   * удалять товары из корзины;

<img src="images_readme/basket.png" width="250" alt="best_sellers"/>

3. Кабинет покупателя:
   * редактирование личной информации;
   * просмотр истории заказов.
   
<img src="images_readme/profile.png" width="250" alt="best_sellers"/>
<img src="images_readme/orders.png" width="250" alt="best_sellers"/>


---

### <img src="images_readme/instruc.jpg" width="50" alt="instruc"/>
Для начальной настройки , Вам необходимо создать виртуальное окружение. 
Файл .env.template переименовать в .env, заполнить соответствующие параметры 

---

### <img src="images_readme/docker.svg" width="45" alt="docker"/>
Запуск через Docker-compose:
Открываем терминал, переходим в корневую папку с проектом:

1. Создаём образ командой ```docker-compose -build```
2. Поднимаем контейнер ```docker-compose up```

---

### <img src="images_readme/pep8.jpg" width="50" alt="pep8"/>
Проверено линтерами (black, isort, flake8, mypy).

---

### <img src="images_readme/licentie.jpg" width="45" alt="licentie"/>
Проект распространяется под лицензией MIT.

---
