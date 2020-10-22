
This is an  quiz organizing website project, developed using Python's web framework Django.<br>
Inspired by (https://github.com/akashgiricse/lets-quiz/network) Akashgakashgiricse and Vitor Freitas



[![GitHub stars](https://img.shields.io/github/stars/akashgiricse/lets-quiz.svg)](https://github.com/Myneequaye/django-examination/stargazers)

In this Django app, teachers can create quizzes and student account in the admin panel and students can login and take quizzes related to their subjects.



### 1. Clone this repository
```bash
git clone https://github.com/akashgiricse/lets-quiz.git

```

### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

### 3. Create the virtualenv

### 4. Install python packages
```bash
## Activate the virtualenv which you created on the last step


### 5. Setup the database
*TODO - Add instructions for this when I start using MySQL database.*

### 6. Run database migrations
```bash
cd lets_quiz
python manage.py migrate
```

### 7. Create superuser
```bash
python manage.py createsuperuser
```

### 8. Run development server
```bash
python manage.py runserver
```

## License
MIT License

Copyright (c) 2018 Akash Giri.
