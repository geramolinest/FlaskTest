# Moscow Ring Road

![Project Image](https://github.com/geramolinest/FlaskTest/blob/main/static/assets/back-ground2.jpg)

> Calculating distance from the Moscow Ring Road area

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [Author Info](#author-info)

---

## Description

Finding the distance from the Moscow Ring Road to the specified address. The address is passed to the application in an HTTP request, 
                          if the specified address is located inside the MKAD, the distance does not need to be calculated.

#### Technologies

- Flask
- HTML
- CSS
- Yandex Geocode API


[Back To The Top](#read-me-template)

---

## How To Use

#### Installation
To install the application you need to have the python packages called Flask and geopy. You can install them through the following commands:
- pip install geopy - [GeoPy installation documentation](https://geopy.readthedocs.io/en/stable/#installation)
- pip install Flask - [Flask installation documentation](https://flask.palletsprojects.com/en/2.0.x/installation/)

After the installation of the packages you can get the code through this repository and clone it to your computer with the following command:
- git clone https://github.com/geramolinest/FlaskTest.git

After getting the code, to run the application, just run the Flask run command, or simply run the app.py file

Once the application has run, the main window will open, showing a brief description of the project and how it works, 
next to the description there is a button, which takes you to the following url where you can enter an address to geocode it and calculate its distance 
between the points of the Moscow Ring Road area.

Once a valid address has been entered, a table will be calculated for each point on the Moscow Ring Road, displaying the address, 
its coordinates and the distance between the Moscow Ring Road point in turn.(At the top of each table indicates the MKAD point in turn, displaying its address and coordinates)

If the address is invalid, you will be forwarded to a new window where you will be notified that it is not a valid address with a 
button to return to the form where you can try again.

In case you want to redirect the application to an invalid url, it will also display a window indicating that it is not a valid url, 
with a button to go to the start of the application.

---

## Author Info

- LinkedIn - [Gerardo Molina](https://www.linkedin.com/in/geramolest)
- Instagram - [@geramolina](https://www.instagram.com/geramolina)

[Back To The Top](#read-me-template)
