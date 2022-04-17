# **Moto Style**

## **Fourth Milestone Project - Full Stack Frameworks With Django - Code Institute**

![Moto Style](/docs/design/logos.png)

![Responsive Design](/docs/responsive_design/responsive_design.jpg)

# Table of Contents

- **[Project Overview](#project-overview)**
- **[User Experience](#user-experience)**
- **[Strategy](#strategy)**
  * **[Project Goals](#project-goals)**
  * **[User Goals](#user-goals)**
- **[Scope](#scope)**
  * **[User Stories](#user-stories)**
- **[Structure](#structure)**
  * **[Code Structure](#code-structure)**
  * **[Database Structure](#database-structure)**
    + **[Conceptual Database Model](#conceptual-database-model)**
    + **[Physical Database Model](#physical-database-model)**
  * **[Feature requirements](#feature-requirements)**
- **[Skeleton](#skeleton)**
  * **[Wireframes](#wireframes)**
  * **[App Routes](#app-routes)**
- **[Surface](#surface)**
  * **[Design](#design)**
- * **[Features](#features)**
    + **[Landing Page](#landing-page)**
    + **[Registration Page](#registration-page)**
    + **[Login Page](#login-page)**
    + **[My Shelf - User Collection Page](#my-shelf---user-collection-page)**
    + **[Add to Shelf Page](#add-to-shelf-page)**
    + **[Change Stock Page](#change-stock-page)**
    + **[Profile Page](#profile-page)**
    + **[Superuser Management Page Page](#superuser-management-page-page)**
    + **[Navbar](#navbar)**
    + **[Footer](#footer)**
    + **[Floating Action Button](#floating-action-button)**
    + **[Custom Error Pages](#custom-error-pages)**
  * **[Technologies Used](#technologies-used)**
  * **[Testing](#testing)**
  * **[Bugs](#bugs)**
  * **[Deployment](#deployment)**
  * **[Credits](#credits)**
  * **[Acknowledgements](#acknowledgements)**
  * **[Disclaimer](#disclaimer)**

## **You can find the deployed website** [**HERE**]()

# **Project Overview**

MotoStyle is a Full Stack e-commerce project developed as the final Milestone for Code Institute. It was created with Django Framework, using python as back-end and PostgreSQL as it's database while media is stored using AWS S3 services.
Purpose of the site is to enable a store to build a database of goods, showcase them and sell them online using stripe as the payment processor. 
The store owner has access to full CRUD functionality over the database and users of the site have access to CRUD functionality in the blog app over the content they add to the site.


**Registration on the website is open so feel free to take advantage of it. Regardless, for testing purposes I have set up the following account:**
* _Standard user:_ **testuser**  _password:_ **Password1**

# **User Experience**

This feature-rich e-commerce portal gives users access everything they need to make their shopping experience as complete as possible. Users are able to browse the products using a variety of sorting methods and search options. Once a product catches their eye, users have the options to add it to their wishlist or to their cart and purchase them using a safe payment processor - stripe. 
The reviews system allows them to post a review and a rating for each product as well as read other user's reviews. Once their shopping is complete, users have the option visit the blog section where they can post or read articles related to the motorcycle industry and community, as well as interact with each other in the comment sections.

# **Strategy**

##  **Project Goals**

* Use PostgreSQL to store data,
* Use Python and Django Framework to manipulate and present the data to the end-user,
* Use AWS to host and deliver media.
* Offer full CRUD functionality over the database to the store owners,
* Offer a responsive and mobile-friendly experience to users,

## **User Goals**

* Create an account on the site,
* Add products to the shopping cart,
* Purchase the items stored in the shopping cart,
* View reviews and articles related to the store's products,
* Interact with other users via the comments section,

# **Scope**

## **User Stories**

**New Users:** 

1. As a new user, I want to be able to create and register an account.
2. As a new user, I want to be able to login and access my account.
3. As a new user, I want to be able to logout.
4. As a new user, I want to browse the store's merchandise.
5. As a new user, I want to be able to search for specific products.
6. As a new user, I want to be able to browse by categories.
7. As a new user, I want to be able to order product lists by price, rating, category or name.
8. As a new user, I want to view individual product details.
10. As a new user, I want to select the different quantities and sizes for a product.
11. As a new user, I want to be able to add products to my shopping cart.
12. As a new user, I want to be able to add products to a list of interests(wishlist).
13. As a new user, I want to be able to view the total cost of my shopping cart while I browse.
14. As a new user, I want to access and view my shopping cart.
15. As a new user, I want to adjust and manage the products in my shopping cart.
16. As a new user, I want to be able to purchase the selected products by entering my payment information in a secure way.
17. As a new user, I want to view an order confirmation.
18. As a new user, I want to receive the order confirmation via e-mail also.

**Regular Users:**

19. As a regular user, I want to store my delivery information on my profile page.
20. As a regular user, I want to view a record of my past orders.
21. As a regular user, I want to view and manage my wishlist.
22. As a regular user, I want to review, rate and read other user's reviews for the products on the site.
23. As a regular user, I want the ability to recover my password.
24. As a regular user, I want to view articles related to the store products and the community it caters to.
25. As a regular user I want to be able to post, edit or remove articles from the blog section.
26. As a regular user, I want to be able to comment on articles.

**Super Users:**

27. As a super user, I want to add products to the store.
28. As a super user, I want to edit existing products.
29. As a super user, I want to delete existing products.
30. As a super user, I want to access the administration portal.

**Site Owner:**

31. As a site owner, I want the site to be responsive.
32. As a site owner, I want to showcase my social media.
33. As a site owner, I want to provide feedback to the user based on their interactions with the site.
34. As a site owner, I want forms to be validated on the front-end for better user experience.
35. As a site owner, I want forms to be validated on the back-end in case front-end is bypassed or fails.


[Back to Top](#top-shelf)


# **Structure**

## **Code Structure**

Project is structured in separate apps, each app hosting the required files to run:

* moto_style :
    - asgi.py - It exposes the ASGI callable as a module-level variable named ``application``.
    - settings.py - Global settings for the project
    - urls.py - The `urlpatterns` list routes URLs to views. Connects all app routes to main project.
    - wsgi.py - It exposes the WSGI callable as a module-level variable named ``application``

* home:
    - static/home folder:
        - js folder hosts the script for the image slider on the landing page
    - templates/home folder:
        - index.html - Template for the landing page. Extends base template
    - apps.py - Default Django generated app config file
    - urls.py - Routes used by the views for the home app
    - views.py - Defines all the views in the home app
    - test_views.py - unit tests for the views in the home app

* products:
    - fixtures folder - contains json format fixtures for the products that need to be loaded in the database
    - static/products folder:
        - js folder - hosts the scripts for form validation, image notification, select element and quantity buttons used by the templates in the products app
    - templates/products folder:
        - custom widget template
        - includes for the product sizes
        - add_product.html - Page for adding a product to the store
        - edit_product.html - Page for editing a product from the store
        - product_detail.html - Page for displaying individual products
        - products.html - Page for displaying multiple products based on query params
    - admin.py - Defines the models from the products app in the admin panel
    - apps.py - Default Django generated app config file
    - forms.py - Defines the forms used by the products app
    - models.py - Defines the models used by the products app
    - urls.py - Routes used by the views in the products app
    - views.py - Defines all the views in the products app
    - widgets.py - Modifies the default Django CustomClearableFileInput widget
    - test_forms.py - unit tests for the forms in the products app
    - test_models.py - unit tests for the models in the products app
    - test_views.py - unit tests for the views in the products app

* profiles:
    - templates/profiles folder:
        - profile.html - Page for displaying user profile page with delivery information and order history
    - apps.py - Default Django generated app config file
    - forms.py - Defines the forms used by the profiles app
    - models.py - Defines the models used by the profiles app
    - urls.py - Routes used by the views in the profiles app
    - views.py - Defines all the views in the profiles app
    - test_forms.py - unit tests for the forms in the profiles app
    - test_models.py - unit tests for the models in the profiles app
    - test_views.py - unit tests for the views in the profiles app 

## **Database Structure**



### **Conceptual Database Model**


<details>
  <summary> (Expand) Conceptual Structure.</summary>

![Conceptual Database](/docs/database/conceptual_database_model.png)
</details>

### **Physical Database Model**

<details>
  <summary> (Expand) items Collection.</summary>

![items Collection](/docs/database/items_collection.png)
</details>

<details>
  <summary> (Expand) regions Collection.</summary>

![regions Collection](/docs/database/regions_collection.png)
</details>

<details>
  <summary> (Expand) users Collection.</summary>

![users Collection](/docs/database/users_collection.png)
</details>

## **Feature requirements**




[Back to Top](#top-shelf)


# **Skeleton**

## **Wireframes**

<details>
  <summary> (Expand) Landing Page Wireframes.</summary>

![Landing Page Wireframes](docs/wireframes/landing_page.png)
</details>

<details>
  <summary> (Expand) Registration Page Wireframes.</summary>

![Registration Page Wireframes](docs/wireframes/registration_page.png)
</details>

<details>
  <summary> (Expand) Login Page Wireframes.</summary>

![Login Page Wireframes](docs/wireframes/login_page.png)
</details>

<details>
  <summary> (Expand) User Collection Page Wireframes.</summary>

![User Collection Page Wireframes](docs/wireframes/user_collection_page.png)
</details>

<details>
  <summary> (Expand) Profile Page Wireframes.</summary>

![Profile Page Wireframes](docs/wireframes/profile_page.png)
</details>

<details>
  <summary> (Expand) Add item to Database Page Wireframes.</summary>

![Add item to Database Page Wireframes](docs/wireframes/add_item_page.png)
</details>


## **App Routes**

**Landing Page**



[Back to Top](#top-shelf)

# **Surface**

## **Design**



![Design](/docs/design/layout.png)

**UI**



**Typography**




**Color Palette**

![Color Pallette](/docs/design/colors.png)

Colors for this app were inspired by the colors a user would find when looking at a bottle of Scotch.

[Back to Top](#top-shelf)

# **Features**

### **Landing Page**



*User stories solved by this feature:*

*

<details>
  <summary> (Expand) Landing Page on mobile, tablet, 1080p and 1440p.</summary>

![Landing Page on mobile](/docs/features/landing_mobile.jpg)

![Landing Page on tablet](/docs/features/landing_tablet.jpg)

![Landing Page on 1080p](/docs/features/landing_1080.jpg)

![Landing Page on 1440p](/docs/features/landing_1440.jpg)
</details>


### **Registration Page**




*User stories solved by this feature:*

* 

<details>
  <summary> (Expand) Registration Page on mobile, tablet, 1080p and 1440p.</summary>

![Registration Page on mobile](/docs/features/register_mobile.jpg)

![Registration Page on tablet](/docs/features/register_tablet.jpg)

![Registration Page on 1080p](/docs/features/register_1080.jpg)

![Registration Page on 1440p](/docs/features/register_1440.jpg)
</details>


### **Login Page**



*User stories solved by this feature:*

* 

<details>
  <summary> (Expand) Login Page on mobile, tablet, 1080p and 1440p.</summary>

![Login Page mobile](/docs/features/login_mobile.jpg)

![Login Page tablet](/docs/features/login_tablet.jpg)

![Login Page 1080p](/docs/features/login_1080.jpg)

![Login Page 1440p](/docs/features/login_1440.jpg)
</details>


### **Profile Page**


*User stories solved by this feature:*

* 

<details>
  <summary> (Expand) Profile Page on mobile, tablet, 1080p and 1440p.</summary>

![Profile Page mobile](/docs/features/profile_mobile.jpg)

![Profile Page tablet](/docs/features/profile_tablet.jpg)

![Profile Page 1080p](/docs/features/profile_1080.jpg)

![Profile Page 1440p](/docs/features/profile_1440.jpg)
</details>



[Back to Top](#top-shelf)

### **Navbar**

The navigation bar houses the app's Logo and the main navigation links.
The links accessible will change based on wether the user is logged in or logged out.
It is collapsible on small devices and the side navigation is accessible from the burger menu on the right hand side.
Messages being flashed to the user as feedback for their interactions with the app are displayed in the section right under the navbar.

*User stories solved by this feature:*

* 15 - As a site owner, I want the app to be responsive.
* 18 - As a site owner, I want to provide feedback to the user when errors occur.

<details>
  <summary> (Expand) Navbar </summary>

![Collapsed Navbar on mobile devices](/docs/features/navbar_collapse.jpg)

![Collapsed Navbar on mobile devices with sidenav](/docs/features/navbar_collapse_sidenav.jpg)

![Expanded Navbar](/docs/features/navbar_expand.jpg)
</details>


### **Footer**

In the footer, the user can find links the owner's social media.

*User stories solved by this feature:*

* 17 - As a site owner, I want to showcase my social media.

<details>
  <summary> (Expand) Footer </summary>

![Footer](/docs/features/footer.jpg)

</details>

### **Floating Action Button**

The floating action button at the bottom right hand side corner of the page extends to provide extra functionality to the user. It can be used to go back to the top of the page or to logout.

While on their profile page, Superusers will find the regular floating action button replaced with a different one that links to the Superuser Administration Page.

*User stories solved by this feature:*

* 3 - As a new user, I want to be able to logout.

<details>
  <summary> (Expand) Floating Action Button </summary>

![Floating Action Button](/docs/features/fab.jpg)

![Floating Action Button Superuser](/docs/features/fab_superuser.jpg)

</details>

### **Custom Error Pages**

The Error Pages are displayed in case an error occurs on client, server or database side. It provides the user with the ability to go back to one of the webapp pages and maintains user engagement.
Each error page displays it's specific error in the title. The user can still use the app's navbar to navigate or click the big button in the middle of the page to return to the Landing Page.
The errors that have specific routes on backend are:

* 400 Bad Request,
* 401 Unauthorized (RFC 7235),
* 404 Not Found,
* 405 Method Not Allowed,
* 500 Internal Server Error

*User stories solved by this feature:*

*

<details>
  <summary> (expand) Error Page</summary>

![Error Page](/docs/features/error.jpg)
</details>

[Back to Top](#top-shelf)

## **Technologies Used**

* **[HTML5](https://html.spec.whatwg.org)**
* **[CSS 3](https://www.w3.org/Style/CSS/Overview.en.html)**
* **[JavaScript](https://www.javascript.com)**
* **[Python 3.9.6](https://www.python.org)**
* **[JQuery 3.6.0](https://jquery.com)** Was used for dom manipulation.
* **[Flask](https://flask.palletsprojects.com/en/2.0.x/)** Was used as the framework for the app.
* **[Jinja](https://jinja.palletsprojects.com/en/3.0.x/)** As the template engine for Flask.
* **[MaterializeCSS](https://materializecss.com)** The app's main front-end framework.
* **[Github](https://github.com)** For storing my repository.
* **[Github Desktop](https://desktop.github.com)** For managing synchronizations between local and cloud-stored repositories.
* **[Git](https://git-scm.com)** For version control.
* **[VSCode](https://code.visualstudio.com)** IDE for writing code.
* **[Balsamiq](https://balsamiq.com) For designing the wireframes.
* **[Font Awesome](https://fontawesome.com)** Provided the icons for social media links.
* **[Google Fonts](https://fonts.google.com)** Ubuntu, Oxygen and Fira Sans font families were used as default fonts for the web application.
* **[Optimizilla](https://imagecompressor.com)** To optimize images for web applications.
* **[Favicon.io](https://favicon.io)** For creating the favicon.
* **[AmIResponsive](http://ami.responsivedesign.is)** For the multi-device mockup.
* **[Markdown ToC](https://ecotrust-canada.github.io/markdown-toc/)** Used to generate the table of contents for Readme.md

## **Testing**

Documentation on all tests carried out is available in [TESTING.md](/TESTING.md)

## **Bugs**

Documentation on all bugs and solutions is available in [TESTING.md](/TESTING.md)

## **Deployment**

The website is hosted [Github](https://github.com), deployed on [Heroku](https://id.heroku.com/login) and uses [MongoDB](https://www.mongodb.com) as it's database. To be able to deploy accounts need to be created on all 3 sites.

**Hosting Repository on Github:** 

1. Login into Github account,
2. Select the button marked "New" and create a new repository,
3. Open repository with favorite IDE.

**Creating MongoDB Database:**

1. Login into MongoDB,
2. Create a new project,
3. Under "Security" click "Database Access" and set up a user with read/write permissions,
4. Create a database cluster,
5. Click on the "Collections" tab and create the necessary collections,
6. Under "Security" click "Network Access" and add the specific IP of the application you are connecting to the database or use 0.0.0.0/0 to allow global access.
7. Under "Deployment" select "Databases" and click "Connect",
8. Click "Connect your application" and select Python v3.6 or later,
9. Copy the connection string generated (MONGO_URI) and replace <password> with the password for the root user. Replace myFirstDatabase with the name of the database that connections will use by default,

![Connect app to MongoDB](/docs/deployment/mongo.png)

**Connecting app to the database:**

1. Create a env.py file in the root directory,
2. Set the environment variables:
```python
import os

os.environ.setdefault("IP", Enter IP here)
os.environ.setdefault("PORT", Enter PORT here)
os.environ.setdefault("SECRET_KEY", Enter your SECRET KEY)
os.environ.setdefault("MONGO_URI", Enter MONGO_URI received at step 9 when creating MongoDB)
os.environ.setdefault("MONGO_DBNAME", Enter name of the collection in the database)
```

**Deployment to Heroku:**

1. Create a Procfile in the root directory with contents `web:python app.py`,
2. Run `pip freeze > requirements.txt` in terminal,
3. Login into Heroku,
4. Click "Create new app",
5. As Deployment method select GitHub,
6. Select the relevant repository with the help of the search field and click Connect,
7. Click "Settings" and select "Reveal Config Vars",
8. Add the config vars used in env.py,
9. Select "Deploy Brach",
10. After deployment is successful enable automatic deploys. 

![Deploy with Heroku](/docs/deployment/heroku.png)

**Steps to follow to clone this repository:**

1. Log into your [Github](https://github.com) account,
2. Select the [Repository](https://github.com/CristianBuca/MS3_TopShelf),
3. Click on the drop-down menu title **Code** on the top right of the repository file tree,
4. Copy the HTTPS address,
5. In your Git Bash Terminal type *"git clone"* then paste the address.
6. Install all python dependencies by running this command in the terminal: `pip install -r requirements.txt`

*Alternatively you can download the repository as ZIP or use [Github Desktop](https://desktop.github.com) to get the repository on you local machine*

[Back to Top](#top-shelf)

## **Credits**

This Project was created based on the Code Institute - Flask Task Manager Project Lessons by Tim Nelson and Python Flask Tutorial - by [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g). 
There are inevitable similarities between this project and the project from these 2 tutorials, more specifically:

**From Tim Nelson's lessons I used:**

* The app initialization method,
* Overall approach on building the app using Flask and Jinja,
* Structure of the routes.

**From Corey Schafer's tutorial I used:**

* The approach of form validation using [wtForms](https://wtforms.readthedocs.io/en/3.0.x/) in python.

**JQuery component initialization** is from [MaterializeCSS](https://materializecss.com).

**JQuery form validation** was done using the [Jquery Validation Plugin](https://jqueryvalidation.org/documentation/).

**Ajax method to replace broken links** solution is from [Sitepoint](https://www.sitepoint.com/jquery-replace-broken-images/).

**Media**

* Hero Image, Error page background image, default avatar and default item images from [Pexels](https://www.pexels.com/search/cryptocurrency/).
* Individual bottle images and information sourced from [Whisky Shop](https://www.whiskyshop.com) and [Whisky Hunter](https://whiskyhunter.net)

### **Code Institute colleagues who's work I followed for guidance:**

[Carla Buongiorno](https://github.com/CarlaBuongiorno/The-Collector).

[Paul Meeneghan](https://github.com/pmeeny/CI-MS3-FootballMemories).

[Irina Pozdeeva](https://github.com/irinatu17/MyCookBook).


## **Acknowledgements**

* Special thanks to my mentor Mo Shami for his suggestions and guidance.
* Special thanks to my brother for his feedback and suggestions.
* My family for their encouragement and support.
* The Code Institute tutors that helped me when I was hitting walls.
* The Code Institute team for all the effort and energy they put into creating and curating the content for this programme.

## Disclaimer

_This project is for educational use only and was created as a Milestone Project for the Code Institute Module of Interactive Frontend Development_

Developed by Cristian Buca

[Back to Top](#top-shelf)

