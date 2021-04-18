# Django-Blog-App

### Main Features
* User Authentication
* User Registration
* Password Change
* Profile Page
* User can Post
* can delete a post

#
![Screenshot from 2021-04-18 21-09-18](https://user-images.githubusercontent.com/65526550/115151478-accd5180-a08a-11eb-9209-56fd12f25bc0.png)

## Technologies Used
* Python - Django
* crispy_forms
* Html
* CSS

# How to start with the project 

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/dev2404/Django-Blog-App.git
    $ cd into the repository
    
Activate the virtualenv for your project.
    
    $ For Windows 
    $ virtualenv\scripts\activate
    
    $ For mac and linux 
    $  virtualenv\bin\activate
    
Install project dependencies:

    $ pip install -r requirements/local.txt  
    
Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver

And That It!! Happy Coding!
