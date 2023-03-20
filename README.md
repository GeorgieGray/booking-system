# Lettuce Eat

![devices](https://i.imgur.com/Uut5HeV.png)

[Lettuce Eat](https://ci-booking-system.herokuapp.com/) is a digital booking system for restaurants.

Restaurant owners enter data about their restuarant, the system processes it and automatically manages table availability. It makes consideration for preferences of the business including table party size min/max, stay duration, regular open hours and restuarant closure days under exceptional circumstance.

The web application frontend has four high-level views:
- Landing view
- User login
- User registration
- Table booking

In addition to this the web application boasts a REST API, exposing the following functionality:
- User registration
- User login & logout
- Create booking
- Delete booking
- View booking
- View all bookings (from the perspective of that user)
- View available times for a given day and party size

The website is hosted using Heroku, see it here:  
https://ci-booking-system.herokuapp.com/

## Table of Contents
- [Target Demographic](#target-demographic)
- [Project planning](#project-planning)
- [Project management](#project-management)
- [Features](#features)
- [Technology](#technology)
- [Project Structure](#project-structure)
- [Local Development](#local-development)
- [Deployment](#deployment)
- [Testing](#testing)
  - [Methodology](#methodology)
  - [Third-Party](#third-party)
- [Citations & Credits](#citations--credits)

## Target Demographic
- Restuarant owners looking to modernise their booking experience
- Restaurant owners who want their table booking to be self-service, and mostly self-managed
- Restuarant owners looking to improve their online advertising conversion rate, by lowering the barrier for customers to give them business
- Restuarant customers who dislike phone conversations (book online instead)
- Restuarant customers who are technology-aware

## Project planning
This section discusses my approach to thinking about and designing the system. The diagrams I created are mostly accurate to the final system, some small changes were made as I made further discoveries during development.

An example of a small change is how the booking view moved from it's originally planned place in the landing view to a private dedicated booking view.
### Mind map
![](https://i.imgur.com/zWQv8oC.jpg)

I started this project by exploring what functionality a user would be looking for in a restaurant booking system: what are the things they'll want to know about the restaurant, and how should they experience the booking journey.

During this phase I also considered which constraints would be meaningful for a restuarant owner to be able to set. For example: A restaurant owner may want to limit time spent per table.

### Data model
![](https://i.imgur.com/DOEj8hJ.jpg)

In this next phase I designed a data model to hold the information necessary to deliver on the ideas captured in the mind mapping phase. The lines represent relationships between tables.

The data model includes the following: restaurant meta data, regular opening days & hours, once-off days when the restauarant is closed (training, renovation, public holiday), the tables at the premises and their meta data, the users of the system and of course the key piece of data: the bookings themselves.

### Data operations
![](https://i.imgur.com/AOxCvJR.jpg)

From here I considered the key functionalities of the system with respect to the data model. Pictured here are each key feature and their data dependencies.

### UI/UX
![](https://i.imgur.com/QBRJLXF.jpg)

Finally I imagined how the user experience would be, and how the previously considered functionalities would be exposed to the end-user.

## Project management
- See [Github Project](https://github.com/users/GeorgieGray/projects/1)

## Features
### Landing view
![](https://i.imgur.com/85TbWcQ.png)

The welcome view. This is the start of the users journey.

Once the user has registered and is logged in, they're no longer shown the registration controls.

![](https://i.imgur.com/96uVbLe.png)

### User registration
![](https://i.imgur.com/lQpyiID.png)

A form to collect the users information and allow them to create an account. Once they've successfully submit the form they're automatically logged in and taken to the booking view.

### User login
![](https://i.imgur.com/4Fqton7.png)

A form to allow the user to log in if they already have an account. On successful login they're taken to the booking view. A logged in user is unable to see this view, they're immediately forwarded to the booking view.

### Table booking
![](https://i.imgur.com/Yyf1LlE.png)

The main functionality of the web application. This view allows users to see and manage their previous bookings, and create new ones.

![](https://i.imgur.com/RRXjBjM.png)
There is a datepicker.

![](https://i.imgur.com/cNzG4bx.png)
After choosing a date and their party size, they're presented with time slots when there is a suitable table.

![](https://i.imgur.com/2zyjWIK.png)
Finally they recieve notice that their booking was a success and they can see their new booking to the right.

## Technology

- [Python 3.10.10](https://www.python.org/downloads/release/python-3110/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask Login](https://flask-login.readthedocs.io/en/latest/)
- [Green Unicorn](https://gunicorn.org/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/)
- [Python DotEnv](https://github.com/theskumar/python-dotenv)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [PostgreSQL](https://www.postgresql.org/)

## Project structure

### app
The flask app

#### api
The REST API endpoints

#### templates
Jinja templates for Flask

#### view
The MVC application endpoints

### helpers
Helper functions

### models
SQLAlchemy data models

### operations
Data operations involving SQLAlchemy data models and the DB

### static
Static files, only the logo lives here currently

## Local Development

Install dependencies
> pip install -r requirements.txt

Run with flask
> python -m flask --app app run

## Deployment
The game is deployed to Heroku.

Here are some instructions so you can do it yourself:
1. Create an account on Heroku
2. "New" in the top right corner of dashboard > create new app
3. Install the [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
4. Authenticate with the CLI: `heroku login`
5. Follow the [Deploying with Git](https://devcenter.heroku.com/articles/git) instructions to setup your git repo correctly to speak with Heroku.
6. Set the env variables: settings > config vars (See: `env.example` in src code)
6. When you're ready to deploy: `git push heroku main`

## Testing
### Methodology

Here is my regression testing method:

1. Go to home view, see both hero buttons + signup and login links
1. Register an account `/signup`
2. Test validation for each of the inputs
3. Submit, see that you're redirected to `/booking`
4. Return to home view, see only one hero button + logout and book a table
5. Log out
6. Go to login view, login, get redirected to `/booking`
7. Change browser url to `/login`, see that you're redirectedt to `/booking` automatically.
8. Go to `/booking`
9. Choose a monday, submit, see no tables (closed on monday), see error message
10. Press start again, see form reset
10. Choose another day, choose any group size, see times suggested
11. Choose a time, see success message and booking appear to right
12. Delete booking to right, see it disappear
13. Refresh page to ensure it was deleted from DB too
14. Book many tables for the same time and date, eventually see that the tables run out for that time slot.
15. See that tables one hour before and two hours after are not available either, the restuarant has a 2 hour limit per table + expects customers to stay for the 2 hours.
16. Log out, register a new user and log back in.
17. Ensure that bookings from previous steps are scoped to the previous user only.
18. Try to book tables for the same times when the tables were exhausted previously, see that the tables are still unavailable.
19. Log out and return to previous user, delete tables where table stock is exhausted.
20. Place another booking for the same day, see that the timeslot is now available again since a booking was deleted.

### Third party
#### Lighthouse
![](https://i.imgur.com/AWyKxqo.png)

#### W3C Jigsaw
There is an error here but it belongs to Bootstrap, so is out of my control. Otherwise good.

![](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-booking-system.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

#### W3C Markup Validator
Info + minor warning, otherwise good.
https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-booking-system.herokuapp.com%2F


## Citations & Credits

### Learning resources
- Heroku documentation
  - https://devcenter.heroku.com/articles/heroku-cli
  - https://devcenter.heroku.com/articles/git

- Flask documentation
  - https://flask.palletsprojects.com/en/2.2.x/

- Flask login documentation
  - https://flask-login.readthedocs.io/en/latest/

- Digital ocean learning resources
  - This provided a good example to validate my learning against
  - https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

- SQLAlchemy documentation
  - https://docs.sqlalchemy.org/en/20/

### Free assets
- App logo source
  - https://www.creativefabrica.com/product/vector-lettuce-filled-outline-icon/