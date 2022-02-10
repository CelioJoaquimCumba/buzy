# About the project
The project name is 'Buzy', which is a plataform that manages projects, it was centerly designed for projects that have a client base, and products to sell. But it does not exclude other types of projects only makes it a more limited.

# Distinctiveness and Complexity
I believe that the project is different from every other that i made so far, a more difficult and complex. 
## Distinctiveness
The project has a concept that was never talked about in the course. It is focused mainly in team collaborations. Thats why we have a project that can have multiply user. That can be working alone, or with eachother.Creating differenct activitites.

## Complexity
This project has alot of information that is given by the user and that must be placed not only to that user but to oher participants as well, one of the most difficul and complex challenges is to make the assertive managment of the data and also making the web apllication user friendly.

Till The log in trough the creatino of activity on a project, this project makes it very clear how should the user interact with.

In this project i used all the concepts given in this course, in both sides(back-end and front-end) doing the good use of pyhton, javascript,jinga, css, html and databases using django's models.

# What is contained in each file
- **urls.py** - in this file i have all the urls that the buzy project will use to get to everypage created in here
- **models.py** - in this file is contained all the models used to manipulate data in this project, models such as **Project, User,Product,Client,...**
- **views.py** - in this file is where i inplemented all the back-end logic. the functions created are:
    - login 
    - logout
    - register
    - create - handles with the creation of projects, adding the _title, description, participants and starting revenue_
    - profile - shows the current user his information and also handles the operation of following and unfollwing other users
    - project - shows the project details and handles the manipulationof the project information such as _activities,clients, products_
- **admin.py** - in this files i registered the models, they would appear on the admin page in the website
- **templates\buzy** - in this file we have all the html templates used in the creation of this. I suppose that the html file names are self explanatory
- **static\buzy** - in this file we have and _'buzy.png'_ file that has the project logo, and _'style.css'_ that has all the css and finnaly a _'buzy.js'_ that all the front end logic in javascript 

# How to get started
## migrations
1. In your terminal , `cd` into the capstone directory
2. run `python manage.py makemigrations buzy` to make migrations
3. run `python manage.py migrate` to apply migrations
## set website
1. still in the terminal run `python manage.py runserver`
2. copy the given url to the browser url field

## inside the website
1. First of all it shows a login form, but in the first time is most likely that you don't have an accoun, so click in the text bellow that says 'You dont have an account?Register' and you will be send to the register page. so after the registration you will be sent to the index page.
_ps:Next time you can login with the credential you used to register_
2. If this is your first time you wont have projects in the index page, and you will not be following anyone. so first of all. Go to the profile page by clicking in the nav bar there where is _'profile'_ and by inserting a username you can get a user, so you can follow and then be able to add as a participant in future projects
3. Already having added all the users you want for ur project , you will create a project by going to the navbar and clicking the _'+ project'_ link
4. After creating you will be redirected to the project page. You can also go to the project page by going to the index, this after creating a project or by getting added by another user. In the project page at the bottom you can click in the follwing titles so you can make actions to the project : _'Create Client, View Client, Create Product, View Product, Create Activity, View Acticity '_.




