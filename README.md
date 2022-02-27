# Keneasy.io

``Introduction``
```
The modern world provides a huge variety of different products, goods and services. This is especially noticeable when we go to shopping centers or online stores. Every year, the number of different stores and brands is expanding in almost all areas, and clothing and footwear are no exception.
In the rhythm of modern society, many people practically do not have time to visit clothing stores and select an image. Fortunately, online shopping is very developed today. Wildberries, lamoda, online stores of individual brands, stores in social networks and much more give us a huge choice. Finding the right image can take a very long time due to the enormous variety. Finding a T-shirt or sweater that matches sneakers is not an easy task for everyone. But you still want to dress uniquely and stylishly. In this regard, we decided to create a site where clothing stores will create their own sets and share them with users who will be able to purchase clothes immediately on the site.
```

``The purpose and objectives of the project``
```
Purpose: to create a website that will provide functionality for filtering sets and searching for clothes by parameters.
Tasks:
⦁ Learn the Python programming language and its Django framework.
⦁ Implement simple interface, user-friendly.
⦁ Add functionality
⦁ Make the project public
```

``Hypothesis``
```
Finding the right look can take a very long time due to the huge variety of clothes and shoes. It is getting more and more difficult to make a choice, but you still want to dress uniquely and stylishly. Ready-made sets with various filtering by clothing selection parameters simplify the search problem and save a lot of time.
```

``Hardware and software (resources) ``
```
⦁ Laptop 
⦁ Python programming language, Django, layout tools 
⦁ PyCharm development environment
```

```
Description of work ⦁ The main components of any website are content and design. The main task of design is to create a convenient and intuitive interface, which we will talk about first. The main page contains basic information with main links (Fig. 1.). Header - top of the page with possible links:
```

```
Home - go to the main page;
About - a link to a page with a brief description of the project;
Filter - page with the main functionality of the project;
Profile - link to the user profile;
Logout / Sign in / Sign up - logout / login / registration.
```

![home](https://user-images.githubusercontent.com/66637696/153063419-dcbe464d-960a-422d-a7df-16fa38868b79.png)

```
⦁ User profile (Fig. 2.).
  On the user profile page, his nickname and mail are shown at the top (the username is also indicated in the site header). Below is a link to a page to create a post. At the very bottom, all notes-posts of the user are shown.
Next, the user's cart, comments and likes will be implemented
```

![profile](https://user-images.githubusercontent.com/66637696/153063501-6188378e-fcee-492b-8505-1041a370d734.png)

```
⦁ Page with all products (Fig. 3.).
This page with all the products on the site, which can be filtered by three parameters: season, size, price. You can set only 3 optional search parameters
The product card is very simple. It contains basic information about the product.
```

![filtering](https://user-images.githubusercontent.com/66637696/153063593-d9618d29-c29a-4bc5-8d45-e83f1b5a98ec.png)

```
⦁ A page displaying all the sets on the site.
Not only users, but also shops will be registered on the site. This page displays all sets of all stores in order. Further comments and likes will be attached to the sets to promote the best sets. All images show template pictures of clothes (Fig. 4.). This was done for convenience.
```

![2022-02-26_2](https://user-images.githubusercontent.com/66637696/155880711-0cfcb1b7-2c4c-4e5b-851b-ddb1752ab8de.png)


```
5. Description of site development.
From the very beginning, I created a skeleton site in Django. After that I created a user model for registration, login and profile.
The photo shows the user model in the project
```

![2022-02-26_1](https://user-images.githubusercontent.com/66637696/155880758-abfa1f1f-730f-41ed-8282-c303ad8f45f3.png)


```
After that I created a base.html file which is templated. I used his framework in all other files.
  {% block content%}{% endblock %} - this construction is used to pass other data there
The photo shows the base.html file code
```
![2022-02-26_3](https://user-images.githubusercontent.com/66637696/155880771-4fe7d06f-9cba-4257-9bb6-25dd6865918b.png)


```
I set up all the html files and made login/registration for the user.
I started to display all the data using the views file, where I indicated the directory of my pages.
The most important thing is to do the filtering. To do this, you need to create the product model, specify the url for the tab with filtering, and create a views file to pass the filtered products to the template.
```
![2022-02-26_4](https://user-images.githubusercontent.com/66637696/155880784-ab21dbb5-15c0-452a-8fde-3c53663549af.png)


```
After that, you need to include a code block to display all elements (filtered)
Using a normal loop, we loop through all the filtered elements and display them on the page. We use the same algorithm to filter clothing sets (Figure 4).
![2022-02-26_5](https://user-images.githubusercontent.com/66637696/155880792-7dd69e10-c19f-417e-8df2-7fa6317d06bd.png)
```


``Output``

```
Finding the right image takes a very long time due to the enormous variety of clothes and shoes. Picking up any thing that fits the wardrobe is not an easy task for everyone. In this regard, we have created a website that helps people search for clothes by parameters in a convenient form (sets), in order to understand whether one or another item of clothing fits another.
This site will allow buyers to purchase goods from sets according to the parameters and filters of interest.
```

``Bibliography:``
```
1. Programming. Python. C++. Part 3: textbook / K. Yu. Polyakov. — M. : BINOM. Knowledge Laboratory, 2019.
2. Programming. Python. C++. Part 4: textbook / K. Yu. Polyakov. — M. : BINOM. Knowledge Laboratory, 2019.
3. Programming in Python 3 A detailed guide. / Summerfield M. - Per. from English. - St. Petersburg: Symbol Plus, 2009 - 608 p.
4. Learning Python, 3rd edition / Lutz M. - Per. from English. - St. Petersburg: Symbol
Plus, 2009
5. HTML and CSS. Development and design of websites / John Duckett - Per. from English. - St. Petersburg: Symbol Plus, 2013 - 514 p.
6.https://itproger.com/practice/javascript
7. Learning JavaScript Programming / Eric Freeman, Robson
Elizabeth, 2018 - 640 p.
8. Django - The Easy Way (3rd Edition): How to build and deploy web applications with Python and Django/ Samuli Natri - 2020 - 349 pp.
```




>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Keneasy.io

``Project relevance``

```
Nowadays, the problem of finding clothes is not something difficult.
It is much more difficult to find what suits you personally.
And it is not always convenient to run from one page to another to select everything separately.
Therefore, we decided to create a website that can simplify the choice and show everything you need in sets.
```
Create a simple filter site to search for clothes by parameters. An analogue of an online store, only without unnecessary functionality and assortment.

``Tasks``
1) Learn the Python programming language and its Django framework.
2) Implement a simple user-friendly interface.
3) Add functionality
4) Make the project public

``Methodology for performing work``

Equipment and programs (resources)
1. Laptop
2. Python programming language.
3. PyCharm development environment

-------------------------------------

``Description``

```
Now I’ll tell you a little about the interface of my mini-project.
The first photo is the main page. She acts as the cover of the project.
Header - top of the page with possible links. We have 5 of them.
1) Home - go to the main page
2) About - a link to a page with a brief description of the project
3) Filter - page with the main functionality of the project.
4) Profile - link to user profile
5) Logout / Sign in / Sign up - logout / login / registration
```

![home](https://user-images.githubusercontent.com/66637696/153063419-dcbe464d-960a-422d-a7df-16fa38868b79.png)

------------------------------

``Profile``

```
  On the user profile page, his nickname and mail are shown at the top
  (the username is also indicated in the site header).
  Below is a link to a page to create a post. At the very bottom,
  all notes-posts of the user are shown.
```

![profile](https://user-images.githubusercontent.com/66637696/153063501-6188378e-fcee-492b-8505-1041a370d734.png)

--------------------------------

``Filter``

```
This page with all the products on the site,
which can be filtered by three parameters:
season, size, price. You can set only 3 optional search parameters
The product card is very simple.
It contains basic information about the product.
```

![filtering](https://user-images.githubusercontent.com/66637696/153063593-d9618d29-c29a-4bc5-8d45-e83f1b5a98ec.png)
