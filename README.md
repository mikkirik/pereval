<h1 align="center">
RestAPI для базы перевалов Федерации Спортивного Туризма России (ФСТР)
</h1>
Данные проект выполнен в рамках виртуальной стажировки от Skillfactory для программы подготовки 
backend python разработчиков.

По сценарию ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило 
бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в 
приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от 
пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с 
объектами, внесёнными другими.

Опубликованный в репозитории проект реализует Rest API для общения мобильного приложения с базой
данных. Проект выполнен на фреймворке Django с использованием библиотеки Django Rest Framework. 

По заданию реализованы следующие методы API:
- POST restapi/submitData для добавления туристом информации о новом перевале;
- GET restapi/submitData/<id> — получение одной записи о перевале по её id;
- PATCH restapi/submitData/<id> — редактирование существующей записи;
- GET restapi/submitData/?user__email=<email> — список данных обо всех объектах, которые пользователь с почтой 
email отправил на сервер.

<h5>
Сгенерированная с помощью Swagger документация доступна по url: http://127.0.0.1:8000/api/schema/swagger-ui/
</h5>
<h5>
Документация redoc: http://127.0.0.1:8000/api/schema/redoc/
</h5>

<h2> Описание методов API </h2>
<h3>метод POST restapi/submitData</h3>
Когда турист поднимется на перевал, он сфотографирует его и внесёт нужную информацию с помощью мобильного приложения:

- координаты объекта и его высоту;
- название объекта;
- несколько фотографий;
- информацию о пользователе, который передал данные о перевале:
  - имя пользователя (ФИО строкой); 
  - почта;
  - телефон.
После этого турист нажмёт кнопку «Отправить» в мобильном приложении. Мобильное приложение вызовет метод submitData твоего REST API.

Метод submitData принимает JSON в теле запроса с информацией о перевале. Ниже находится пример такого JSON-а:
````
{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "", // что соединяет, текстовое поле
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
		 "name": "Василий",
		 "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную категорию трудности
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
}
````

<h3>метод GET restapi/submitData/<id></h3>
Позволяет получить одну запись (перевал) по её id.
Выводит всю информацию об объекте, в том числе статус модерации.

<h3>метод PATCH restapi/submitData/<id></h3>
Позволяет отредактировать существующую запись (замена), если она в статусе new.
Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона. 
Метод принимает тот же самый json, что был описан ранее.

В качестве результата возвращает два значения:
- state:
  - 1 — если успешно удалось отредактировать запись в базе данных.
  - 0 — в противном случае.
- message — если обновить запись не удалось, сообщает причину.
 
<h3>метод GET restapi/submitData/?user__email=<email></h3>
Возвращает список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.