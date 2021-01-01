# **Tech Bytes!**
## **A Markdown Blogging Platform For All Things Tech**

> You can write your blog in markdown and share it with the world.

> You can also follow your favorite writers to not miss their new blogs.

| Home Page                                           | Profile Page                                          |
| :-------------------------------------------------  | :---------------------------------------------------- |
| <img src="/pics/tech_bytes_home.png" width="1000"/> | <img src="/pics/tech_bytes_profile.png" width="1000"/> |

### Features:
* Signup and Create interesting profiles, use **_Gravatar_** to make amazing profile pictures.
* Write and Edit blogs in **_Markdown_**, get a visual preview of your Markdown.
* Comment to discuss about your favourite blogs.
* View the latest blogs on the home page of the blog.
* Click on permalink to view the whole article, you can share it with friends aswell.
* Follow writers and view their latest in the **Followed** tab feed in your home page.
* User, Moderator and Admin level permissions given to appropriate users.
* Moderator has the ability to censor comments if not appropriate.
* Admin has all edit permissions.

## **Made in Python**
Using: **`import flask`**, **`SQLite3`**, **`SQL Alchemy`**, **`Jinja2`** and **`Bootstrap`**

This is heavily inspired from **Miguel Grinberg**'s book **Flask Web Development**.
* _Flask_ was used as the backend framework.
* _SQLite3_ database was used with _SQL Alchemy_ as the _ORM_.
* The front-end was written in _HTML5_ and _CSS_ with _Jinja2_ for the dynamic part which talks with Flask.
* _Bootstrap_ was used for UI elements.

Demo Video: https://www.youtube.com/watch?v=JeWJCIdw0JE&feature=youtu.be

## How to Use
1. Create a virtual environment using `virtualenv`
1. `source venv/bin/activate` : To activate virtualenvironment
1. Install packages from the dev.txt or prod.txt file in the requirements directory using: `pip install -r requirements/dev.txt`
1. Create the following environment variables:
   * `export FLASK_APP=flasky.py`
   * `export FLASK_CONFIG_TYPE=testing` : development(default if not given) or testing or production
   * `export FLASK_DEBUG=1` : If in dev mode
   * `export SECRET_KEY='097h30...anyrandom...t28uh9'` : For 
   * `export MAIL_USERNAME='_eg-username_'` : For sending mails, has to ba gmail account
   * `export MAIL_PASSWORD='_passwd_'` : password for above mail
   * `export TEST_ADMIN='_email_'` : Mail to which admin mails are sent. (not admin of website)
1. `flask run` : Runs Flask server, press Ctrl+C to stop server.
1. `deactivate` : To get outside virtual environment.
