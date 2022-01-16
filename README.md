* Note to CodeInstitute corrector: I can only apologise for the final state of the project here. I ran out of time to implement the user access control and stripe payments. The user stories, responsiveness, manual and automatic tests have not been completed because I was unable to get the code to the finish line. I'm really sorry for wasting your time here having to look at this poor submission. Django has defeated me.

# Dromcondra Craftshop - Online Store

* Supporting your local artisans.

## Project Goals

* The goal of this project is to create a digital counterpart for a successful local craft business in order for them to broaden their horizons and sell products to a wider audience. 

<a></a>

## Table of Contents <a name="contents"></a>

---

* [UX](#ux)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
  * [Site Owner Goals](#site-owner-goals)
  * [User Requirements and Expectations](#user-requirements)
  * [Design Choices](#design-choices)
    * [Fonts](#fonts)
    * [Icons](#icons)
    * [Colors](#colors)
    * [Structure](#structure)
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)
  * [Wireframes](#wireframes)
  * [Flowcharts](#flowcharts)
  * [Database Structure](#database-structure)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Libraries and Frameworks](#libraries-frameworks)
  * [Tools](#tools)
* [Features](#features)
  * [Features that have been developed](#features-done)
  * [Features that will be implemented in the future](#features-future)
* [Testing](#testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
  * [Local Deployment](#local-deployment)
  * [Heroku/AWS Deployment](#remote-deployment)
* [Credit](#credit)

## UX (User Experience) <a name="ux"></a>

---

### User Goals <a name="user-goals"></a>

* As a **site owner**, I want a functional e-business platform to complement my real-world business.
* As a **shopper**, I want to be able to view and buy this company's products on-line.
* As a ....

### User Stories <a name="user-stories"></a>

#### Viewing and Navigation 

* As a **Shopper**, I want to be able to **view the site's products** so that I can **chose some to buy**.
* As a **Shopper**, I want to be able to **view an individual product's detailed information** so that I can **see the detailed description, manufacturer or creator, price and rating.**.
* As a **Shopper**, I want to be able to **see the number of items and value of my shopping basket** so that I can **be aware of how much I've committed to spend**.

#### Registration and User Accounts

* As a **Site User**, I want to be able to **easily sign up for an account** so that I can **have an account and view my profile**.
* As a **Site User**, I want to be able to **log in and logout** so that I can **access my personal information**.
* As a **Site User**, I want to be able to **recover my password** so that I can **regain access to my account if I forget my stored password**.
* As a **Site User**, I want to be able to **receive password change confirmation by email** so that I can **know my password has been changed - by me or someone else**.
* As a **Site User**, I want to be able to **have a personal email profile** so that I can **see order history, confirmations and personal information**.

#### Sorting and Searching

* As a **Shopper**, I want to be able to **see a list of available products** so that I can **I can chose some to buy**.
* As a **Shopper**, I want to be able to **chose a product category** so that I can **see a sub set of products of a particular type**.
* As a **Shopper**, I want to be able to **sort by price or rating** so that I can **so that I can see items that are well reviewed or see ones in a particular price range**.
* As a **Shopper**, I want to be able to **search by product name** so that I can **find a particular item I'm looking for**.
* As a **Shopper**, I want to be able to **see search results and number selected** so that I can **see what my search results are and know how narrow/wide my search criteria is**.
* As a **Shopper**, I want to be able to **see results for particular creator** so that I can **see other items made by the same person**.

#### Purchasing and Checkout

* As a **Shopper**, I want to be able to **see a list of items in my shopping basket** so that I can **I know exactly what I am buying**.
* As a **Shopper**, I want to be able to **adjust the quantity of items in my basket** so that I can **easily reduce or add extra items as needed**.
* As a **Shopper**, I want to be able to **return to the main shopping area from the shopping basket screen** so that I can **continue shopping after having confirmed what's in my basket**.
* As a **Shopper**, I want to be able to **buy items in my basket securely** so that I can **feel safe regarding my payment details**.

### Site Owner Goals <a name="site-owner-goals"></a>

#### Site Administration

* As a **Site-Owner**, I want to be able to **create new products to sell in the shop** so that I can **easily expland my range of products**.
* As a **Site-Owner**, I want to be able to **create new creator/artisans for the store** so that I can **easily reduce or add extra items as needed**.

### User Requirements and Expectations <a name="user-requirements"></a>

#### Requirements

* Easily navigate with a **navbar**.
* Provide a simple overview on the main page and a little more detail in sub sections.
* Fast **loading-times**.
* **Contact form** for users to send a project information request.
* Company **contact** details readily accessible on the **header and footer** of every page.

#### Expectations

* Content is **visually satisfying** and **informative**.
* **Navigation** takes **user** to specific **parts** of the **website**.
* Working **Read More** buttons to **avoid** big **lumps** of clustered **text**.

### Design Choices <a name="design-choices"></a>

---
In designing this site I took inspiration from...

#### Fonts <a name="fonts"></a>

[Google fonts](https://fonts.google.com/) have been used to give typographic style.
font-family: **???** is used for most text on the site.
font-family: **???** is used for special sans-serif fonts such as the pre-header and footer where a more compact and stylish font are desired.

#### Icons <a name="icons"></a>

[Bootstrap Icons](https://icons.getbootstrap.com/) free icons have been used throughout this project.

#### Colors <a name="colors"></a>

The website colors were chosen using [coolors.co](https://coolors.co/).
![Color-Selection](/wireframes/dc-colors.png)

#### Structure <a name="structure"></a>

The website is structured with a main entry page with an enter store button and subsequent product view pages.

###### [Back to Top](#contents)

## Wireframes and Flowcharts <a name="wireframes-and-flowcharts"></a>

### Wireframes <a name="wireframes"></a>

Wireframing was done using Balsamiq under full-functional trial provided by Code Institute.
Wireframes were developed for a ![main page](wireframes/wf-home-page-rev-0-1.png), ![main product view page](wireframes/wf-product-page-0-1.png).


### Flowcharts <a name="flowcharts"></a>

Flow chart for this project is not complete.

#### Database Structure <a name="database-structure"></a>

Insert database structure for this project is as follows:
![database structure](wireframes/dc-database-schema.png)

---

###### [Back to Top](#contents)

## Technologies Used <a name="technologies"></a>

---

### Languages <a name="languages"></a>

* HTML
* CSS
* JavaScript
* Python

### Libraries and Frameworks <a name="libraries-frameworks"></a>

* [Bootstrap](https://getbootstrap.com/)
* [Popper](https://popper.js.org/)
* [JQuery](https://jquery.com/)
* [Django](https://www.djangoproject.com/)

### Tools <a name="tools"></a>

* [Git](https://git-scm.com/)
* [Markdownlint](https://dlaa.me/markdownlint/)

---

###### [Back to Top](#contents)

## Features <a name="features"></a>

---
**Features** that have been **implemented:** <a name="features-done"></a>

* Simple navigation on all screen sizes.
* Main store view with products listed on bootstrap cards.
* Individual product view with a product detailed description.
* Shopping basket page with a table of products added.
* Search functionality for products.
* Category and Creator filtering and filter display.

**Features** that will be **implemented** in the **future:** <a name="features-future"></a>

* Stripe payments and checkout is not working.
* Heroku deployment has failed due to database and program errors that I have not been able to fix.

###### [Back to Top](#contents)

## Testing <a name="testing"></a>

---

### HTML Test

---

#### HTML Test Fixes

* Site testing incomplete.

### CSS Test

* Site testing incomplete.

#### CSS Test Errors

* Site testing incomplete.

#### CSS Test Warnings

``` css
* Site testing incomplete. css test code errors to be entered here when completed.

```

#### CSS Test Fixes

* Site testing incomplete.

### Responsiveness

* The site has been implemented using Bootstrap throughout and built with a mobile first philosophy.
* Responsiveness is quite good going from mobile to larger screens and navbar collapses predictably.
* Site testing incomplete.


### Design

* The design of the site was inspired by a combination of a craftshop in my locality that sells a lot of unique, locally produced goods and the Boutique Ado tutorial project on the CI course. Simplicity of design was important throughout with a calm color palette. Accessible contact details are there also for people who feel more comfortable contacting the business directly with any queries.

### Contact form

* Site testing incomplete and contact form was not created.

### User Story Tests

<details>
  <summary>User stories were tested using Google Chrome and developer tools.</summary>

#### Summary of user tests

##### Viewing and Navigation

* Test-1.   As a **Shopper**, I want to be able to **view the site's products** so that I can **chose some to buy**. Test incomplete - FAIL.
![DC-User-Test-1](wireframes/dc-user-test-1.png)
* Test-2.   As a **Shopper**, I want to be able to **view an individual product's detailed information** so that I can **see the detailed description, manufacturer or creator, price and rating.**. Test incomplete - FAIL.
![DC-User-Test-2](wireframes/dc-user-test-2.png)
* Test-3.   As a **Shopper**, I want to be able to **see the number of items and value of my shopping basket** so that I can **be aware of how much I've committed to spend**. Test incomplete - FAIL.
![DC-User-Test-3](wireframes/dc-user-test-3.png)

##### Registration and User Accounts

* Test-4.   As a **Site User**, I want to be able to **easily sign up for an account** so that I can **have an account and view my profile**. Test incomplete - FAIL.
![DC-User-Test-4](wireframes/dc-user-test-4.png)
* Test-5.   As a **Site User**, I want to be able to **log in and logout** so that I can **access my personal information**. Test incomplete - FAIL.
![DC-User-Test-5](wireframes/dc-user-test-5.png)
* Test-6.   As a **Site User**, I want to be able to **recover my password** so that I can **regain access to my account if I forget my stored password**. Test incomplete - FAIL.
![DC-User-Test-6](wireframes/dc-user-test-6.png)
* Test-7.   As a **Site User**, I want to be able to **receive password change confirmation by email** so that I can **know my password has been changed - by me or someone else**. Test incomplete - FAIL.
![DC-User-Test-7](wireframes/dc-user-test-7.png)
* Test-8.   As a **Site User**, I want to be able to **have a personal email profile** so that I can **see order history, confirmations and personal information**. Test incomplete - FAIL.
![DC-User-Test-8](wireframes/dc-user-test-8.png)

##### Sorting and Searching

* Test-9.   As a **Shopper**, I want to be able to **see a list of available products** so that I can **I can chose some to buy**. Test incomplete - FAIL.
![DC-User-Test-9](wireframes/dc-user-test-9.png)
* Test-10.   As a **Shopper**, I want to be able to **chose a product category** so that I can **see a sub set of products of a particular type**. Test incomplete - FAIL.
![DC-User-Test-10](wireframes/dc-user-test-10.png)
* Test-11.   As a **Shopper**, I want to be able to **sort by price or rating** so that I can **so that I can see items that are well reviewed or see ones in a particular price range**. Test incomplete - FAIL.
![DC-User-Test-11](wireframes/dc-user-test-11.png)
* Test-12.   As a **Shopper**, I want to be able to **search by product name** so that I can **find a particular item I'm looking for**. Test incomplete - FAIL.
![DC-User-Test-12](wireframes/dc-user-test-12.png)
* Test-13.   As a **Shopper**, I want to be able to **see search results and number selected** so that I can **see what my search results are and know how narrow/wide my search criteria is**. Test incomplete - FAIL.
![DC-User-Test-13](wireframes/dc-user-test-13.png)
* Test-14.   As a **Shopper**, I want to be able to **see results for particular creator** so that I can **see other items made by the same person**. Test incomplete - FAIL.
![DC-User-Test-14](wireframes/dc-user-test-14.png)

##### Purchasing and Checkout

* Test-15.   As a **Shopper**, I want to be able to **see a list of items in my shopping basket** so that I can **I know exactly what I am buying**. Test incomplete - FAIL.
![DC-User-Test-15](wireframes/dc-user-test-15.png)
* Test-16.   As a **Shopper**, I want to be able to **adjust the quantity of items in my basket** so that I can **easily reduce or add extra items as needed**. Test incomplete - FAIL.
![DC-User-Test-16](wireframes/dc-user-test-16.png)
* Test-17.   As a **Shopper**, I want to be able to **return to the main shopping area from the shopping basket screen** so that I can **continue shopping after having confirmed what's in my basket**. Test incomplete - FAIL.
![DC-User-Test-17](wireframes/dc-user-test-17.png)
* Test-18.   As a **Shopper**, I want to be able to **buy items in my basket securely** so that I can **feel safe regarding my payment details**. Test incomplete - FAIL.
![DC-User-Test-18](wireframes/dc-user-test-18.png)

##### Site Administration

* Test-19.   As a **Site-Owner**, I want to be able to **create new products to sell in the shop** so that I can **easily expland my range of products**. Test incomplete - FAIL.
![DC-User-Test-19](wireframes/dc-user-test-19.png)
* Test-20.   As a **Site-Owner**, I want to be able to **create new creator/artisans for the store** so that I can **easily reduce or add extra items as needed**. Test incomplete - FAIL.
![DC-User-Test-20](wireframes/dc-user-test-20.png)
</details>

###### [Back to Top](#contents)

## Bugs <a name="bugs"></a>

---

Many bugs were encountered during the development of the project - all admittedly of my own making while trying to learn Django.

### Development Bugs

* BugFix:  Issue with AllAuth password authentication found. Error found in Settings.py AUTH_PASSWORD_VALIDATORS. Important note here is to ensure the correct version of Allauth is installed. (Currently 0.43.0.)
* Bugfix:  Used the variable product_id rather than product.id in the product detail anchor. This created some very strange error messages that took a long time to figure out what I had done wrong. The fix is described in the CI Boutique Ado tutorial.
* Bugfix:  Missing 'url' term from Django template link in base.html caused a synthax error. This took quite a while to figure out what I had done.
* BugFix:  Missing single quotes around search term in views.py caused a synthax error on implementation of the search bar. This is was obvious enough from the error message and quickly fixed.
* BugFix:  Error on variable name 'categories' in products/views.py. Incorrectly named 'category' and threw error message.
* BugFix:  Serious issues encountered trying to connect Heroku with AWS's S3 bucket. Many setting configurations were attempted. Solution was found to be an incorrectly assigned BASE_DIR in settings.py. Once this was corrected, static files were transferred to AWS and the deployed site loaded the correct css styles.


### Testing Bugs

* Site testing incomplete.

###### [Back to Top](#contents)

## Deployment <a name="deployment"></a>

---

### Local Deployment <a name="local-deployment"></a>

This project has been created, stored and built using GitHub and GitPod as the repository and development environments respectively.
Code changes throughout the project were committed to GitHub, followed by the 'git push' CLI command to store changes permanently.
The development version of the project used for testing runs in GitPod and the deployed version runs on Heroku.

To run the full site, you will need to create a Stripe account for the Checkout functionality to run.
An AWS (Amazon Web Services) account is required to store static and media files.

This project runs locally using the following steps in Gitpod:

1. Clone the project: From GitHub repository, click the 'Code' button and download the zip of the repository.
    Alternatively, the respository can be cloned using the following CLI command in GitPod.
    ```
    git clone https://github.com/STarrant/drumcondra-craftshop.git
    ```

1. Open the copied repository and install the required packages using the following CLI command.
    ```
    pip3 install -r requirements.txt
    ```

1. In GitPod create an env.py file to contain the required enviroment variables at root level.
    **IMPORTANT** Ensure env.py is added to the .gitignore in your repository to prevent these sensitive data points being made public.
    ```
    import os

    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEVELOPMENT"] = "True"

    os.environ["DEFAULT_FROM_EMAIL"] = 'DEFAULT_FROM_EMAIL'

    os.environ["STRIPE_PUBLIC_KEY"] = "insert your stripe public key here"
    os.environ["STRIPE_SECRET_KEY"] = "insert your stripe secret key here"
    os.environ["STRIPE_WH_SECRET"] = "insert your stripe webhook hey here"
    os.environ["STRIPE_CURRENCY"] = "EUR"
    ```
    Please refer to Stripe's documentation to get the exact details of how to ascertain the three required data points above that need to be manually inserted.

    An alternative option to using an env.py file in GitPod is to use GitPod's own [Variables](https://gitpod.io/variables) to store your project specific environment variables in a secure and convenient manner.

1. Migrate the database models with the following commands.
    ```
    python3 manage.py makemigrations --dry-run
    python3 manage.py makemigrations
    python3 manage.py migrate --planned
    python3 manage.py migrate
    ```
1. Create a superuser account for database access with the following command.
    ```
    python3 manage.py createsuperuser
    ```
1. The application can be started with the following command.
    ```
    python manage.py runserver
    ```
    The local application's webserver address will be displayed in the terminal and there is usually a dialog box to open in a new browser window.
1. To access the site administration page, add '/admin' to the application's url and login in with the superuser credentials created above.

### Remote Deployment <a name="remote-deployment"></a>

The site has been deployed and tested remotely using Heroku and AWS S3 services.
Heroku Site is available on [drumcondra-craftshop-heroku-app](https://drumcondra-craftshop.herokuapp.com/).

The remote deployment is setup as follows:
1. A Heroku account is required for this application. Create a new account if you do not already have one, create a new app and choose the most appropriate region.
1. In order to run the database end of the application the Heroku Postgres Add-on needs to be included. This can be found under Add-Ons and select the 'Hobby Dev - Free' plan and click 'Submit order form' to create a new database and attach it to the app.
1. In the Heroku main settings, scroll to the Config Vars and click Reveal Config Vars. A set of variables, similar to the env.py file in local deployment, need to be setup to hold sensitive or project specific datapoints that cannot be hard-coded into the application's software.
    ```
    AWS_ACCESS_KEY_ID = "Your AWS access key ID"
    AWS_SECRET_ACCESS_KEY = "Your AWS secret access key"
    AWS_STORAGE_BUCKET_NAME = "Your AWS bucket name"
    USE_AWS = True
    
    DATABASE_URL = "This is the URI for your Heroku Postgres Database. (Should be automatically populated by Heroku at DB creation.)"

    SECRET_KEY = "SECRET_KEY"

    STRIPE_PUBLIC_KEY = "Your Stripe public key"
    STRIPE_SECRET_KEY = "Your Stripe secret key"
    STRIPE_WH_SECRET = "Your Stripe webhook secret key"

    DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL"  **testhigh delete**
    EMAIL_HOST = "smtp.gmail.com"  **testhigh delete**
    EMAIL_HOST_PASSWORD = "Your email host password"
    EMAIL_HOST_USER = "Your email host username"
    EMAIL_PORT = 587  **testhigh delete**
    EMAIL_USE_TLS = True   **testhigh delete**
    ```
1. From this screen in Heroku, take note of the DATABASE_URL setting and navigate to settings.py in Gitpod in the Drumcondra_Craftshop folder.
    Comment out the default database configuration and add the following code with the previously noted DATABASE_URL setting inserted:
    ```
    DATABASES = {
        'default': dj_database_url.parse('postgres://.....'))
    }
    ```
1. Migrate again with the following commands in Gitpod.
    ```
    heroku login -i
    (Enter heroku login credential for Heroku site.)
    heroku run python3 manage.py makemigrations --dry-run
    heroku run python3 manage.py makemigrations
    heroku run python3 manage.py migrate --planned
    heroku run python3 manage.py migrate
    ```

1. Still in the Gitpod Terminal, enter the following command to create a new Heroku Postgres superuser account.
    ```
    heroku run python3 manage.py createsuperuser
    ```
1. Load data from the development database into the production databases with the following commands.

    ```
    python3 manage.py loaddata <name of file containing the data *>
    ``` 
    * products_datadump.json

1. After migrations are complete, change database configurations in settings.py to:
    ```
    if 'DEVELOPMENT' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    else:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
```
This set up will allow your site to use Postgres in the Heroku production deployment and sqlite3 in Gitpod development environment.


1. Make sure you have your requirements.txt file and your Procfile. In case you don't, follow the below steps:
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
1. The Procfile should contain the following line:
    ```
    web: gunicorn drumcondra_craftshop.wsgi:application

    ```

1. Add your files and commit them to GITHUB by running the following commands:
    ```
    git add . 
    git commit -m "Your commit message"
    git push
    ```

1. Add your Heroku app URL to ALLOWED_HOSTS in your settings.py file
1. Disable collect static so that Heroku doesn't try to collect static files when you deploy by typing the following command in the terminal
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1
    ```
1. Go back to HEROKU and click "Deploy" in the navigation. 
1. Scroll down to Deployment method and Select Github. 
1. Look for your repository and click connect. 
1. Under automatic deploys, click 'Enable automatic deploys'

1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 


1. Store your static files and media files on AWS. You can find more information about this on [Amazon S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).
    If you would like to follow a tutorial instead, visit [this tutorial on Youtube from Amazon Web Services](https://youtube.com/watch?v=e6w9LwZJFIA)

1. Set up email service to send confirmation email and user verification email to the users. You can do this by following the next steps (Gmail only)

(Be aware that this migth be different for other providers or the process might have changed over time)

* Go to your email account and go to your account settings
* Under Security, scroll down to Signing in to Google and make sure 2 step verification is turned on
* Under the same heading (Signing in to Google) you will see the 'App passwords' option.
* Click on the option, select mail for the app and under device type select other and fill in 'Django'
* You will now get a password which you should copy and set it as a config variable in Heroku:

```
    EMAIL_HOST_PASS = 'Password you just copied'
    EMAIL_HOST_USER = 'Your gmail account
```
* Go to your settings.py in casa_pedra_nobre directory and add the following:

```
    if "DEVELOPMENT" in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```


###### [Back to Top](#contents)

## Credits <a name="credit"></a>

---
### Photo Credits

* Main home page [photo](https://unsplash.com/photos/KT4dOfvtZSg) by (Gregory Dalleau)[https://unsplash.com/@gregda] from [Unsplash](https://unsplash.com/).
* Photograph of [potter](https://unsplash.com/photos/5z6a2OlqhrY) by (Iraj Beheshti)[https://unsplash.com/@setarehshab] from [Unsplash](https://unsplash.com/).

### Special Thanks

* My Code Institute mentor, [Simen Daehlin](https://github.com/Eventyret), for a lot of great advice and direction along the way. His time, effort and experience made a huge difference to the code quality, readability and end result. It would be hard to overstate his input here. 
* [Chris Z](https://github.com/ckz8780) whose excellent Boutique Ado project walk-through was used as the basis for the structural code in this project.
* [Sean_CI](https://github.com/nazarja) for helping me fix a database error that stumped me for over two weeks.
* Last and most certainly not least, I owe a huge debt to my patient wife, kids and dogs who have tolerated my untold hours on evenings, nights and weekends, squirrelled away on front of a screen while I've been doing this project. There is a lot of time to be made up for.

###### [Back to Top](#contents)