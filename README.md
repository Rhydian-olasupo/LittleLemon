# LittleLemon
![Coursera](https://img.shields.io/badge/Coursera-%230056D2.svg?style=for-the-badge&logo=Coursera&logoColor=white)
![Meta](https://img.shields.io/badge/Meta-0668E1?style=flat&logo=meta&logoColor=white)
![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)


A restful API that exposes a restaurant menu items with ability to add and update dishes along displaying the menu list also it provides booking tables 
to authenticated  users, you can register and login as a user through token based authentication.

## Urls Available
- **POST REQUEST**: auth/users/ : An api endpoint for user registration

- **POST REQUEST**: auth/token/login: Generate user's access-token {username and password}

- restaurant/menu:
    - **GET**: returns all the menu items

- restaurant/menu/<int:pk>:

  - **GET**: return item with the specified id
  
  - **PUT**: update item with the specified id
  
  - **DELETE**: delete item with the specified id
  
 - restaurant/booking/booking:
 
   - **GET**:return a list of booked tables
  
   - **POST**: book a table


## Installation and Running The Project:
- Installing Python if it's not already setup used Version is 3.10.11
-  Setting up the virtual environment using venv using the window's cmd:

```jsx
python -m venv myenv 
```
- the required packages : django, djangorestframework, mysqlclient, djoser

- Running pipenv Virtual Environment:

```jsx
myenv\Scripts\activate
```

- Configuration of mysql database
    - Set the database engine - django.db.backends.mysql
    - set the Host,user,password,port variables according to your setup

- Running the Server:
```jsx
python manage runserver
```
