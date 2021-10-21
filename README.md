# Dromcondra Craftshop - Online Store

* Supporting your local artisans.

![DC-Web-Mockup](wireframes/dc-techsini-multidevice-mockup.png)

## Contents

---

* UX
  * Project Goals
    * User Goals
    * User Stories
    * Site Owner Goals
    * User Requirements and Expectations
    * Design Choices
      * Fonts
        * Icons
        * Colours
* Technologies
* Features
  * Features that have been developed
    * Features that will be implemented in the future
* Testing
* Bugs
* Deployment
* Credit

## UX (User Experience)

---

### Project Goals

* The goal of this project is to create a digital counter part for a successful local craft business in order for them to broaden their horizons and sell products to a wider audience. 

### User Goals

* As a **site owner**, I want a functional e-business platform to complement my real-world business.
* As a **shopper**, I want to be able to view and buy this company's products on-line.
* As a ....

### User Stories

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

#### Site Administration

* As a **Site-Owner**, I want to be able to **create new products to sell in the shop** so that I can **easily expland my range of products**.
* As a **Site-Owner**, I want to be able to **create new creator/artisans for the store** so that I can **easily reduce or add extra items as needed**.

### User Requirements and Expectations

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

### Design Choices

---
In designing this site I took inspiration from...

#### Fonts

[Google fonts](https://fonts.google.com/) have been used to give typographic style.
font-family: **???** is used for most text on the site.
font-family: **???** is used for special sans-serif fonts such as the pre-header and footer where a more compact and stylish font are desired.

#### Icons

[Bootstrap Icons](https://icons.getbootstrap.com/) free icons have been used throughout this project.

#### Colors

The website colors were chosen using [coolors.co](https://coolors.co/). The justification is...
![Color-Selection](/wireframes/dc-site-colors.jpg)

## Wireframing

Wireframing was done using Balsamiq under full-functional trial provided by Code Institute.
Wireframes were developed for a [main page](wireframes/wf-home-page-rev-0-1.png), [standard section page](wireframes/wf-electrical-design-page-0-1.png) and a [contact page](wireframes/wf-contact-page-rev0-1.png).
As the design progressed however, the site diverged significantly from multipage model to a single scolling site with all content on a single page.

---

## Features

---
**Features** that have been **implemented:**

* Simple navigation on all screen sizes.
* Contact form with text entry, drop-downs and check boxes.
* Main store view with products listed on bootstrap cards.
* Individual product view with a product detailed description.
* Creator view... TBA
* Shopping basket page with a table of products added.

**Features** that will be **implemented** in the **future:**

* The

## Technologies Used

---

### Languages

* HTML
* CSS
* JavaScript
* Python

### Tools & Libraries

* [Git](https://git-scm.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Font-Awesome](https://fontawesome.com/icons?d=gallery)
* [Popper](https://popper.js.org/)
* [JQuery](https://jquery.com/)
* [Google fonts](https://fonts.google.com/)
* [Markdownlint](https://dlaa.me/markdownlint/)
* [Django](https://www.djangoproject.com/)

## Testing

---

### HTML Test


```

#### HTML Test Fixes

* Erroneous placeholder reference deleted from the form dropdown list.
* Misspelling between the label and the id fixed for the form's given name entry.
* Re-Testing after these corrections gave a **PASS**.

### CSS Test

CSS code has been tested using the [CSS validator](http://jigsaw.w3.org/css-validator/) and gave the following errors and warnings.

#### CSS Test Errors

 176 #btn-floating-home Value Error : background-color 212121 is not a background-color value : 212121

#### CSS Test Warnings

``` css
    153  -moz-transition /*is an unknown vendor extension*/
    154  -webkit-transition /*is an unknown vendor extension*/
    190  -webkit-box-shadow /*is an unknown vendor extension*/
    191  -moz-box-shadow /*is an unknown vendor extension*/
    293 .footer-list-group-item /*Same color for background-color and border-color*/
```

#### CSS Test Fixes

* TBA
* TBA
* Re-testing after these fixes gave a **PASS**.

### Responsiveness

* The site has been implemented using Bootstrap throughout and built with a mobile first philosophy.
* Responsiveness is quite good going from mobile to larger screens and navbar collapses predictably.
* Some of the propotioning on images could be improved with media queries but overall the test is a **PASS**.

<details>
  <summary>Responsiveness of the design was tested using Chrome's Developer Tools and the result overall was a **PASS**. Open the dropdown here to see screenshots of the results.</summary>

#### Summary of responsive design tests

* Full Screen 24” Browser Window – Google Chrome – No Issues - **PASS**
  * Result: ![Responsive test Fullscreen](wireframes/dc-responsive-fullscreen.jpg)
  * iPhone 6/7/8 – Slight shift in page top and bottom cut off when scrolling - **PASS**
  * Result: ![Responsive test iPhone 6/7/8](wireframes/dc-responsive-iphone678.jpg)
  * iPhone 6/7/8 Plus – Slight shift in page top and bottom cut off when scrolling - **PASS**
  * Result: ![Responsive test iPhone 6/7/8 Plus](wireframes/dc-responsive-iphone678plus.jpg)
  * iPhone X – Slight shift in page top and bottom cut off when scrolling - **PASS**
  * Result: ![Responsive test iPhone X](wireframes/dc-responsive-iphonex.jpg)
  * iPad – ~48px shift in page top and bottom cut off when scrolling - **PASS**
  * Result: ![Responsive test iPad](wireframes/dc-responsive-ipad.jpg)
  * iPad Pro – Slight shift in page top and bottom cut off when scrolling - **PASS**
  * Result: ![Responsive test iPad Pro](wireframes/dc-responsive-ipadpro.jpg)
  * Surface Duo – Slight shift in page top and bottom cut off when scrolling - **PASS**
  * Result: ![Responsive test Surface Duo](wireframes/dc-responsive-surfacepro.jpg)
  * Galaxy Fold – Slight shift in page top and bottom cut off when scrolling - **PASS**
  * Result: ![Responsive test Galaxy Fold](wireframes/dc-responsive-galaxyfold.jpg)

</details>

### Design

* The design of the site was inspired by a combination of a craftshop in my locality that sells a lot of unique, locally produced goods and the Boutique Ado tutorial project on the CI course. Simplicity of design was important throughout with a calm color palette. Accessible contact details are there also for people who feel more comfortable contacting the business directly with any queries.

### Contact form

* The contact form was provided to allow a quick way of a person contacting the store with a simple question outside of normal office hours. Typically, online shopping may be conducted in the evening time or international customers may prefer not to dial an international number.

### User Stories

<details>
  <summary>User stories were tested using Google Chrome and developer tools.</summary>

#### Summary of user tests

##### Viewing and Navigation

* Test-1.   As a **Shopper**, I want to be able to **view the site's products** so that I can **chose some to buy**.
![DC-User-Test-1](wireframes/dc-user-test-1.png)
* Test-2.   As a **Shopper**, I want to be able to **view an individual product's detailed information** so that I can **see the detailed description, manufacturer or creator, price and rating.**.
![DC-User-Test-2](wireframes/dc-user-test-2.png)
* Test-3.   As a **Shopper**, I want to be able to **see the number of items and value of my shopping basket** so that I can **be aware of how much I've committed to spend**.
![DC-User-Test-3](wireframes/dc-user-test-3.png)

##### Registration and User Accounts

* Test-4.   As a **Site User**, I want to be able to **easily sign up for an account** so that I can **have an account and view my profile**.
![DC-User-Test-4](wireframes/dc-user-test-4.png)
* Test-5.   As a **Site User**, I want to be able to **log in and logout** so that I can **access my personal information**.
![DC-User-Test-5](wireframes/dc-user-test-5.png)
* Test-6.   As a **Site User**, I want to be able to **recover my password** so that I can **regain access to my account if I forget my stored password**.
![DC-User-Test-6](wireframes/dc-user-test-6.png)
* Test-7.   As a **Site User**, I want to be able to **receive password change confirmation by email** so that I can **know my password has been changed - by me or someone else**.
![DC-User-Test-7](wireframes/dc-user-test-7.png)
* Test-8.   As a **Site User**, I want to be able to **have a personal email profile** so that I can **see order history, confirmations and personal information**.
![DC-User-Test-8](wireframes/dc-user-test-8.png)

##### Sorting and Searching

* Test-9.   As a **Shopper**, I want to be able to **see a list of available products** so that I can **I can chose some to buy**.
![DC-User-Test-9](wireframes/dc-user-test-9.png)
* Test-10.   As a **Shopper**, I want to be able to **chose a product category** so that I can **see a sub set of products of a particular type**.
![DC-User-Test-10](wireframes/dc-user-test-10.png)
* Test-11.   As a **Shopper**, I want to be able to **sort by price or rating** so that I can **so that I can see items that are well reviewed or see ones in a particular price range**.
![DC-User-Test-11](wireframes/dc-user-test-11.png)
* Test-12.   As a **Shopper**, I want to be able to **search by product name** so that I can **find a particular item I'm looking for**.
![DC-User-Test-12](wireframes/dc-user-test-12.png)
* Test-13.   As a **Shopper**, I want to be able to **see search results and number selected** so that I can **see what my search results are and know how narrow/wide my search criteria is**.
![DC-User-Test-13](wireframes/dc-user-test-13.png)
* Test-14.   As a **Shopper**, I want to be able to **see results for particular creator** so that I can **see other items made by the same person**.
![DC-User-Test-14](wireframes/dc-user-test-14.png)

##### Purchasing and Checkout

* Test-15.   As a **Shopper**, I want to be able to **see a list of items in my shopping basket** so that I can **I know exactly what I am buying**.
![DC-User-Test-15](wireframes/dc-user-test-15.png)
* Test-16.   As a **Shopper**, I want to be able to **adjust the quantity of items in my basket** so that I can **easily reduce or add extra items as needed**.
![DC-User-Test-16](wireframes/dc-user-test-16.png)
* Test-17.   As a **Shopper**, I want to be able to **return to the main shopping area from the shopping basket screen** so that I can **continue shopping after having confirmed what's in my basket**.
![DC-User-Test-17](wireframes/dc-user-test-17.png)
* Test-18.   As a **Shopper**, I want to be able to **buy items in my basket securely** so that I can **feel safe regarding my payment details**.
![DC-User-Test-18](wireframes/dc-user-test-18.png)

##### Site Administration

* Test-19.   As a **Site-Owner**, I want to be able to **create new products to sell in the shop** so that I can **easily expland my range of products**.
![DC-User-Test-19](wireframes/dc-user-test-19.png)
* Test-20.   As a **Site-Owner**, I want to be able to **create new creator/artisans for the store** so that I can **easily reduce or add extra items as needed**.
![DC-User-Test-20](wireframes/dc-user-test-20.png)
</details>

## Bugs

---

Many bugs were encountered during the development of the project - all admittedly of my own making while trying to learn Django.

### Development Bugs

* BugFix:  Issue with AllAuth password authentication found. Error found in Settings.py AUTH_PASSWORD_VALIDATORS. Important note here is to ensure the correct version of Allauth is installed. (Currently 0.43.0.)
* Bugfix:  Used the variable product_id rather than product.id in the product detail anchor. This created some very strange error messages that took a long time to figure out what I had done wrong. The fix is described in the CI Boutique Ado tutorial.
* Bugfix:  Missing 'url' term from Django template link in base.html caused a synthax error. This took quite a while to figure out what I had done.
* BugFix:  Missing single quotes around search term in views.py caused a synthax error on implementation of the search bar. This is was obvious enough from the error message and quickly fixed.
* BugFix:  Error on variable name 'categories' in products/views.py. Incorrectly named 'category' and threw error message.


### Testing Bugs

* A few bugs were thrown up by the HTML Validator and CSS Validator. The solutions are given above in the **HTML Test** and **CSS Test** Sections.

## Deployment

---

The site has been deployed on ...

## Credits

---

* Credit 1

### Special Thanks

* My Code Institute mentor, [Simen Daehlin](https://github.com/Eventyret), for a lot of great advice and direction along the way. His time, effort and experience made a huge difference to the code quality, readability and end result. It would be hard to overstate his input here.