# :wave: IS213 - G2T1 - Focustudy

<br>

## :man_student: Group Members

| Name                  | Email ID         |
| --------------------- | ---------------- |
| Gnanasekaran Sanchana | sanchanag.2020   |
| Koh Hui Qing          | huiqing.koh.2020 |
| Lim Wei Jie           | weijie.lim.2020  |
| Ricky Goh Rui Yu      | ricky.goh.2020   |
| Sophia Chow Hui Ru    | sophia.chow.2020 |

<br>

## 🤓 Project Overview ##

**What is the problem?**

It’s getting harder and harder to focus. With everything going digital, the amount of time spent on our various devices has increased exponentially. The sheer amount of content exhausts our attention and leads to a decreased attention span. And studying is no exception

<br>

**How do we solve it?**

Introducing Focustudy, where we aim to create an environment where students can configure their studying essentials - study timer, to-dos, music. It will all be available in one application, allowing them to remain focused as they work.

<br>
<hr>
<br>

## :computer: How to Install Our Web Application ##
* This method is applicable to both Mac OS and Windows OS

<br>

### Firstly, clone this repository into your local environment.

1. On the '<> Code' page, click on the green 'Code' button and a dropdown will appear.
2. Make sure you're under the 'HTTPS' tab, and copy the URL.

![image](https://user-images.githubusercontent.com/89062463/161909869-f189cfa5-78f4-41d3-bf8a-0bf446320fb0.png)

<br>

### Next , open Visual Studio Code. 

1. Change the current working directory to any location where you want the cloned repository to be - use command ```cd``` <path> to navigate.
2. Type ```git clone```, and then paste the URL you copied earlier.

![image](https://user-images.githubusercontent.com/89062463/161921586-99ed9312-4a70-4f6f-b5c9-e15ce18f36db.png)

3. Press **Enter** to clone into your local machine.
  
4. After cloning, change directory into the local repository.

![image](https://user-images.githubusercontent.com/89062463/161921933-ac1b8639-8945-4229-bb20-cb9c779fd647.png)

* Note that Focustudy is the **root** folder, containing the main sub-folders - **backend** and **frontend**.

<br>

### Next, start WAMP/MAMP and import the .sql files from Focustudy/backend/sql into localhost/phpmyadmin.

* The files are located here:

![image](https://user-images.githubusercontent.com/89060200/161988130-a9117a40-be67-47fb-bff0-8ea00cf30b8a.png)

1. On the localhost/phpmyadmin page, click on the 'Import' button and a 'Choose File' button will appear. Select a file and click 'Go'.
  
2. Make sure to import all **3** .sql files.

![image](https://user-images.githubusercontent.com/89062463/161923068-2a996e15-43d6-424b-932a-eb7c072bb9e1.png)

3. Upon successful import, you should see an output similar to the one as seen in the picture below.

![image](https://user-images.githubusercontent.com/89062463/161901577-de4b947e-d212-4e83-b42d-0436e270215a.png)

<br>

### Next, install the node modules used in this repository

* Note that the screens below may defer from yours.
  
1. Change directory into the frontend folder.
2. Type ```npm install``` or ```npm i``` for short to install all the node modules used in the front-end folder.

![image](https://user-images.githubusercontent.com/89062463/161926166-26749e88-00fe-4297-b52d-072d828bf697.png)

<br>
<hr>
<br>

## :runner: You are done with the set-up! Now lets run our application on your localhost. ##

- Note that the screens below may defer from yours.

<br>

### First, run the docker compose file from the backend folder.
  
1. Go to Focusstudy/backend/docker-compose.yml.
  
![image](https://user-images.githubusercontent.com/89060200/162009534-bda6cc2e-48b8-4435-b503-b12ea9453444.png)
  
2. Ctrl + F and input 'esdg2t1'. Replace all with your docker id.

##### If you are using MAMP:

1. Go to Focustudy/backend/docker-compose.yml.
2. Replace the following lines with the code below:

- Line 20

```
      dbURL: mysql+mysqlconnector://root:root@host.docker.internal:3306/timer
```

- Line 34

```
      dbURL: mysql+mysqlconnector://root:root@host.docker.internal:3306/rating
```

- Line 129

```
      dbURL: mysql+mysqlconnector://root:root@host.docker.internal:3306/tasklist
```

<br>

3. Change directory into the backend folder.
4. Type ```docker-compose up -d``` to build and run all the images in the backend folder.

![image](https://user-images.githubusercontent.com/89062463/161928446-ef7fc181-baff-4c2c-b1c9-c24dda09af67.png)

- You should see the following output in the Visual Studio Code terminal:

![](https://user-images.githubusercontent.com/89062463/161928947-4482ab14-3e51-45ba-a702-200a512d681d.png)

<br>

### Next, run the frontend of Focustudy from the frontend folder.

* Note that the screens below may defer from yours.

1. Change directory to the frontend folder.
2. Type ```npm run serve``` to run the frontend.
3. Ctrl + Click or manually go to http://localhost:8000 to see our app!

![image](https://user-images.githubusercontent.com/89062463/161932600-d6d1f1a7-6252-411b-a190-3072c56289c6.png)

<br>

<hr>
<br>

## :book: How To Use Focustudy ##

### Welcome to Focustudy. Login with Google to start focusing!
  
- Use the following account that we have prepared just for you! The account comes with database records already in place.

  | Email    | esdg2t1@gmail.com |
  | -------- | ----------------- |
  | Password | dockerisfun1!     |
  
![image](https://user-images.githubusercontent.com/89060200/162009269-85a33387-0f9b-4e31-8857-d2ed42209366.png)

<br>

### Upon successful login, you will be brought to Focustudy's home page.
  
![image](https://user-images.githubusercontent.com/89060200/162004551-0d9aef41-cdb7-41a1-a6f6-763c8afefe9a.png)

1. Start a study session.
  
![image](https://user-images.githubusercontent.com/89060200/162004743-fb8ae57a-1606-4026-88ae-6eda2958672f.png)

2. Upon completing a study session, you will be prompted to rate it.
  
![image](https://user-images.githubusercontent.com/89060200/162004833-428bf5d9-7dee-463d-af02-b8aab72bf93e.png)

![image](https://user-images.githubusercontent.com/89060200/162004886-4f9fd0a2-2078-46d0-bbd5-3a4004372abf.png)

3. View, add and delete tasks in your to-do list.

![image](https://user-images.githubusercontent.com/89060200/162005043-3fb2a6d7-db9f-4264-b6c6-8466851197c6.png)

4. Play music from Spotify.
  
![image](https://user-images.githubusercontent.com/89060200/162005131-0e515f20-49d4-4c7a-8414-6233c01b51af.png)

<br>

### Interested in your past study sessions?

- Press the "History" button located at the top right of the home page.
  
![image](https://user-images.githubusercontent.com/89060200/162005340-be9c067d-4fdc-4fe5-b56b-c8c319864998.png)
  
- You will be brought to the history page where you will be able to view all your past study sessions sessions.
  
![image](https://user-images.githubusercontent.com/89060200/162005506-5ee10603-3ada-411d-a370-58d9d68c1910.png)

<br>

### We are sad to see you go!

- Log out by clicking on the exit button at the top right corner of the home page.
  
![image](https://user-images.githubusercontent.com/89060200/162005404-5e984811-25d9-4e6f-9f50-f7466db66023.png)

<br>
<hr>
<br>

## :rabbit: AMQP Testing ##

### Import the Postman collection

- Open Postman and import Focustudy/backend/AMQP Tests.postman_collection.json.

![image](https://user-images.githubusercontent.com/89060200/161989167-c102d86d-6468-4023-bb17-f02d41661fce.png)
  
![image](https://user-images.githubusercontent.com/89060200/161990384-c72f685b-70e4-4286-a661-270ccd23d437.png)

<br>

### Testing Error and Activity Log microservices

- Requests have been prepared for you to simulate errors and activity in Record Session and Display Sessions microservices. Messages will be printed in the console.

![image](https://user-images.githubusercontent.com/89060200/161990508-a642c3f0-918a-4d03-934d-e328233402c7.png)