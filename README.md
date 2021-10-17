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

* The goal of this project is to create a digital launchpad for a small electrical engineering company. 
The main services on offer need to be clearly demonstrated on the landing section through simple bullet-points. 
Links to sections provide further information on each of these services. A simple contact page allows 
users to send a business request.

### User Goals

* Find information about **electrical design services**.
* Find information about **motor and drive services**.
* Find information about **automation services**.
* Find information about **machine safety services**.
* **Send an email** to the site owner.

### User Stories

* As a **user**, I want to see all the main services this company can offer at a glance so that in a single scroll of the homepage, I know exactly what this company has to offer.
* As a **user**, I want **fast loading-times** for pages.
* As a **user**, I want a **simple and well laid-out** website that gives the impression of these complex topics being made simple.
* As a **user**, I want to see **modern design** to show that the site owner is au fait with the latest developments in technology.
* As a **user**, I want to see some **examples of previous projects** done by this company.
* As a **user**, I want to see references to **industry standards** to be sure the deliverables will meet my company's specifications.
* As a **user**, I want to be able to **contact** the site owner and give a simple description of a potential project.

### Site Owner Goals

* As a **site-owner**, I want to clearly **communicate my company's services**.
* As a **site-owner**, I want to convey **technical expertise in the subject matter** to site visitors.
* As a **site-owner**, I want contact **telephone and email readily available** because building connections is the key to business.
* As a **site-owner**, I want **no social media affiliations** on this site becuase some projects will be undertaken with stict NDA and security requirements.
* As a **site-owner**, I want a **simple and concise contact form** that gathers important project data from potential customers.

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
* Pre-header 

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

* Removed redundant id #btn-floating-home from code.
* Set border: none; in .footer-list-group-item class.
* Errors for "-moz-transition", "-webkit-transition", "-webkit-box-shadow" and "-moz-box-shadow" are ignored.
* Re-testing after these fixes gave a **PASS**.

### Responsiveness

* The site has been implemented using Bootstrap throughout and built with a mobile first philosophy.
* Responsiveness is quite good going from mobile to larger screens and navbar collapses predictably.
* The back to top button suggested by my mentor makes returning to the top of the screen straight-forward and intuitive.
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

* The design of the site was inspired by...

### Contact form

* The contact form

### User Stories

<details>
  <summary>User stories were tested using Google Chrome and developer tools. The only item of note which could be described as noteable sub-par would be the loading speed which needs improvement. Click dropdown to see individual tests.</summary>
  
#### Summary of user tests

* Test: As a **user**, I want to 

</details>

## Bugs

---

Many bugs were encountered during the development of the project - all admittedly of my own making.

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