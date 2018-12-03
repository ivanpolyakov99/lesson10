# DOCS
1. https://ru.wikipedia.org/wiki/HTTP
2. https://ru.wikipedia.org/wiki/WSGI
3. https://ru.wikipedia.org/wiki/Django


# HOW TO START
1. python manage.py makemigrations  - для создания миграций
2. python manage.py startapp <name> - создания приложение в проекте
3. python manage.py migrate - применение миграций
4. python manage.py shell - интерактивный режим python с подключенной базой данных


# HOMEWORK
1. "Поиграться" с моделями
2. https://docs.djangoproject.com/en/2.1/intro/tutorial01/ - читать
3. в файле scripts.sql лежат скрипты для работы с базой напрямую

# HOMEWORK 2
1. Создать отдельное приложение для тестирующей системы.
- описать модели для тестов, вопросов, вариантов ответа, пользователей, 
ответов пользователей, придумать филды у каждой модели. Пользователь не может отвечать на один и тот же вопрос.

# HOMEWORK 3
почитать про админку https://docs.djangoproject.com/en/2.1/ref/contrib/admin/

# HOMEWORK 4
1. Описать форму для вопросов. 

easy - форма содержит текстовое поле для ввода, куда вводится номер ответа,
добавить валидацию на проверку номера ответа, чтобы такой существовал.

easy* - форма содержит checkbox/radiobutton с вариантами ответов, добавить валидацию
что выбранный вариант существует.

Попытаться отрендерить на страницами с деталями теста вопросы и формы к ним. Вопросы получать с базы.
Выводить ошибку, если пользователь отвечает на вопрос еще раз.

# HOMEWORK 5
1. Создать view,form,template для регистрации пользователя. Добавить валидацию.

# HOMEWORK 6
1. Добавить статику к проекту
https://getbootstrap.com/docs/4.1/getting-started/download/
2. Исходя из добавленной статики - сделать "красивыми" странички с тестами, логином и реистрацией


# HOMEWORK 7
1. Покрыть тестами оставшиеся forms & view в приложении testing
2. Создать middleware, которая будет писать в базу 500 ошибки приложения(Если такие будут). PS. Покрыть тестами.
3. Добавить список ошибок в админку.

## DOCS
 - https://docs.djangoproject.com/en/2.1/topics/testing/overview/
 - https://docs.djangoproject.com/en/2.1/topics/http/middleware/
 
 
 # HOMEWORK 8
 1. Доделать покрытие тестами + покрыть мидлвару из приложения logger
 
 ## DOCS
 - https://docs.djangoproject.com/en/2.1/topics/i18n/translation/
 - https://ru.wikipedia.org/wiki/Gettext
 
 # HOMEWORK 9
 1. Почитать! про heroku https://devcenter.heroku.com/categories/working-with-django
 2. Придумать тему для диплома!.
 
 # HOMEWORK 10
 1. Отправка файлов https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/
 2. Отправка писем https://docs.djangoproject.com/en/2.1/topics/email/

# HOMEWORK 11
1. https://restfulapi.net/
2. https://www.django-rest-framework.org/

# HOMEWORK 12
1. Создать Viewset для списка вопросов
2. Добавить API для Ответа на вопрос

url должен быть вида - /en/api/tests/3/questions/4/add_answer/

3. Прочитать про celery
http://docs.celeryproject.org/en/latest/index.html