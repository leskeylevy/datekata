# DateKata

## Contributors

+ [Kellen Njoroge](https://github.com/KellenNjoroge)
+ [Leskey Levy](https://github.com/leskeylevy)
+ [Nicholas Muchiri](https://github.com/Nicholas-muchiri)
+ [Feysal Ibrahim](https://github.com/feysal-Ibrahim)
## Technologies Used

    - Python 3.6
    - Flask Framework
    - HTML, CSS and Bootstrap
    - JavaScript
    - SQL

## Description
A personal blog

It has the following features

    + User has to login using github account
    +  User can create own profile and update it
    + Access chatroom to communicate with matched users
    + The user should receive notification of matched users
    + They should also view other user profile
    + The user block other users
    + search other users by name




## Demo
This app was deployed in Heroku

[Demo](https://datekata.herokuapp.com/)

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`


### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog'
export SECRET_KEY='Your secret key'
export DATABASE_URL_TEST='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog_test'
export MAIL_SERVER='smtp.googlemail.com'
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-email>
export MAIL_PASSWORD=<your-password>
```

## Set up and installation

    1. Clone or download the Repository
    2. Create a virtual environment
    3. Read the specs and requirements files and Install all the requirements.
    4. Edit the start.sh file with your api key from the news.org website
    6. Run chmod a+x start.sh
    7. Run ./start.sh
    8. Access the application through `localhost:5000

### Run Database Migrations
```bash
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```
### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs



## Contact details


## License

This project is licensed. under the MIT License - [License](LICENSE)
