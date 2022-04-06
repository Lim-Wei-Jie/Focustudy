------------------------------------------------------------------------------------------------------------------------------------------------------------

IS213 - G2T1 - Focustudy

------------------------------------------------------------------------------------------------------------------------------------------------------------

Group Members:
- Gnanasekaran Sanchana (sanchanag.2020)
- Koh Hui Qing (huiqing.koh.2020)
- Lim Wei Jie (weijie.lim.2020)
- Ricky Goh Rui Yu (ricky.goh.2020)
- Sophia Chow Hui Ru (sophia.chow.2020)

------------------------------------------------------------------------------------------------------------------------------------------------------------

Project Overview

------------------------------------------------------------------------------------------------------------------------------------------------------------

What is the problem?
   - It’s getting harder and harder to focus. With everything going digital, the amount of time spent on our various devices has increased exponentially. The sheer amount of content exhausts our attention and leads to a decreased attention span. And studying is no exception

How do we solve it?
   - Introducing Focustudy, where we aim to create an environment where students can configure their studying essentials - study timer, to-dos, music. It will all be available in one application, allowing them to remain focused as they work.

------------------------------------------------------------------------------------------------------------------------------------------------------------

How to Install Our Web Application (This method is applicable to both Mac OS and Windows OS)

------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Firstly, clone this repository into your local environment.
   - On the '<> Code' page, click on the green 'Code' button and a dropdown will appear.
   - Make sure you're under the 'HTTPS' tab, and copy the URL.

2. Next , open Visual Studio Code. 
   - Change the current working directory to any location where you want the cloned repository to be - use command ```cd``` <path> to navigate.
   - Type ```git clone```, and then paste the URL you copied earlier.
   - Press "Enter" to clone into your local machine.
   - After cloning, change directory into the local repository.
     * Note that Focustudy is the root folder, containing the main sub-folders - "backend" and "frontend".

3. Next, start WAMP/MAMP and import the .sql files from Focustudy/backend/sql into localhost/phpmyadmin.
   - On the localhost/phpmyadmin page, click on the 'Import' button and a 'Choose File' button will appear. Select a file and click 'Go'.
   - Make sure to import all 3 .sql files.

4. Next, install the node modules used in this repository
   - Change directory into the frontend folder.
   - Type ```npm install``` or ```npm i``` for short to install all the node modules used in the front-end folder.

------------------------------------------------------------------------------------------------------------------------------------------------------------

How to Run Our Application on Your Localhost

------------------------------------------------------------------------------------------------------------------------------------------------------------

1. First, run the docker compose file from the backend folder.
   - Go to Focusstudy/backend/docker-compose.yml.
   - Ctrl + F and input 'esdg2t1'. Replace all with your docker id.

#####################################################################################

If you are using MAMP:

1. Go to Focustudy/backend/docker-compose.yml.
2. Replace the following lines with the code below:

   - Line 20 -

      dbURL: mysql+mysqlconnector://root:root@host.docker.internal:3306/timer

   - Line 34 -

      dbURL: mysql+mysqlconnector://root:root@host.docker.internal:3306/rating

   - Line 129 -

      dbURL: mysql+mysqlconnector://root:root@host.docker.internal:3306/tasklist

#####################################################################################

   - Change directory into the backend folder.
   - Type ```docker-compose up -d``` to build and run all the images in the backend folder.

2. Next, run the frontend of Focustudy from the frontend folder.
   - Change directory to the frontend folder.
   - Type ```npm run serve``` to run the frontend.
   - Ctrl + Click or manually go to http://localhost:8000 to see our app!

------------------------------------------------------------------------------------------------------------------------------------------------------------

How To Use Focustudy

------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Welcome to Focustudy. Login with Google to start focusing!
   - Login with your personal Google account, or use the account that we have prepared just for you! The account comes with database records already in place.

#####################################################################################

Email: esdg2t1@gmail.com
Password: dockerisfun1!

#####################################################################################

2. Upon successful login, you will be brought to Focustudy's home page.
   - Start a study session.
   - Upon completing a study session, you will be prompted to rate it.
   - View, add and delete tasks in your to-do list.
   - Play music from Spotify.

3. Interested in your past study sessions?
   - Press the "History" button located at the top right of the home page.
   - You will be brought to the history page where you will be able to view all your past study sessions sessions.

4. We are sad to see you go!
   - Log out by clicking on the exit button at the top right corner of the home page.

------------------------------------------------------------------------------------------------------------------------------------------------------------

AMQP Testing

------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Import the Postman collection
   - Open Postman and import Focustudy/backend/AMQP Tests.postman_collection.json.

2. Testing Error and Activity Log microservices
   - Requests have been prepared for you to simulate errors in Record Session and Display Sessions microservices. Messages will be printed in the console.