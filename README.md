# Corruption Feed

Corruption Feed is an application that allow users to expose corruption cases within the country.Other users can view the cases and make comments. 
### Authors
* Albert Byrone
* John Mbugua
* Brian Major

### Features
As a user of the application, you will be able to:
> * Expose corruption cases by posting them in the application
> * View cases posted by other users
> * Comment on the cases posted by other users
> * Create an account, login and update your profile 

### BDD
| Behaviour    | input     | output     |
| -------------| :--------:| -----------|
| Home Page | Displays all cases  | All cases reported |
|Login| Click on **login**|Allows user to login into the account using the login form|
|Create an account| Click on **sign in**|Form which allows users to sign in for the first time|
|Post cases| Click on **Report Here**|Displays an input form for posting a case|
|Comment on a case| Click on **comment**|Displays a comment box to allow users to post a comment on a specific case|
|Update profile| Click on **Profile** |Takes the user to the profile page with options to edit and upload profile picture|

## Getting started
#### Prerequisites
* python 
* virtual environment
* pip

#### Cloning
Navigate into the folder you want the application to be
In your terminal, run the commands
  > $ git clone https://github.com/Albert-Byrone/corruption-feeds
  > 
  > $ cd corruption-feeds

### Running the application
* Update the DATABASE_URL in config.py 
* Modify the start.sh file with your own gmail credentials
* To run the app type the commands in your terminal
 install all the dependencies listed in the requirements.txt file
> $ chmod a+x start.sh
>
> $ ./start.sh

### Testing the application
* To run the tests for the class in your terminal
 > $ python3.6 manage.py test

 ### Technologies used
Python
Flask
Html
Bootstrap

### Known Bugs
No known bug
### License
This project is Licensed under MIT.

### Collaborate
>To collaborate, reach us at:
>>Github: 
>> [Jmos-Mbugua](https://github.com/Jmos-Mbugua)
>> [Albert-Byrone](https://github.com/Albert-Byrone)
>>[Brian Major](https://github.com/bryomajor)

