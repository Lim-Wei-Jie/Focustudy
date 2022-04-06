# :wave: IS213-project

## 🤓 IS213 - G2 - Focustudy
* Group members:
* Gnanasekaran Sanchana (sanchanag.2020)
* Koh Hui Qing (huiqing.koh.2020)
* Lim Wei Jie (weijie.lim.2020)
* Ricky Goh Rui Yu (ricky.goh.2020)
* Sophia Chow Hui Ru (sophia.chow.2020)

<br>

## 🤓 Project Overview ##

**What is the problem?**

It’s getting harder and harder to focus. With everything going digital, the amount of time spent on our various devices has increased exponentially. The sheer amount of content exhausts our attention and leads to a decreased attention span. And studying is no exception

<br>

**How do we solve it?**

Introducing, FOCUSTUDY, we aim to create an environment where students can configure their studying essentials - study timer, to-dos, music. It will all be available in one application, allowing them to remain focused as they work.


<br>
<hr>
<br>



## 🤓 How to Install Our Web Application ##
* This method is applicable to both Mac OS and Windows OS


### Firstly, clone this repository into your local environment

1. On the '<> Code' page, click on the green 'code' button and a dropdown will appear.
2. Make sure you're under the 'HTTPS' tab, and copy the URL.

![image](https://user-images.githubusercontent.com/89062463/161909869-f189cfa5-78f4-41d3-bf8a-0bf446320fb0.png)


### Next , Open visual studio code. 

1. Change the current working directory to any location where you want the cloned repository to be - use command ```cd``` <path> to navigate
2. Type ```git clone```, and then paste the URL you copied earlier.

It should look something like this:

![image](https://user-images.githubusercontent.com/89062463/161921586-99ed9312-4a70-4f6f-b5c9-e15ce18f36db.png)

Press **Enter** to clone into your local machine
  
After cloning, change directory into the local repository
  
![image](https://user-images.githubusercontent.com/89062463/161921933-ac1b8639-8945-4229-bb20-cb9c779fd647.png)


* Note that Focustudy is the **root** folder, containing the main sub-folders - **backend** and **frontend**
  
  


### Next, import the following SQL files located in the link below into localhost/phpmyadmin

file: [focustudy_sql_files.zip](https://github.com/Lim-Wei-Jie/Focustudy/files/8423838/focustudy_sql_files.zip)

1. On the localhost/phpmyadmin page, click on the 'import' button and a 'choose file' button will appear.Select a file and click 'go'
  
2. Make sure to import each file into the sql database(there should be 3 sql files to import in total)

![image](https://user-images.githubusercontent.com/89062463/161923068-2a996e15-43d6-424b-932a-eb7c072bb9e1.png)

3. Upon successful import, one should see an output similar to the one as seen in the picture below

![image](https://user-images.githubusercontent.com/89062463/161901577-de4b947e-d212-4e83-b42d-0436e270215a.png)
  
  

### Next, install the node modules used in this repository
  
* Note that the screens below may defer from yours
  
1. Change directory into the frontend folder
2. Type ```npm install``` or ```npm i``` for short to install all the node modules used in the front-end folder

![image](https://user-images.githubusercontent.com/89062463/161926166-26749e88-00fe-4297-b52d-072d828bf697.png)
  
  





<br>
<hr>
<br>
  
  
  
 ## 🤓 You are done with the set-up! Now lets run our application on your localhost ##

  
  ### First, run the docker compose file in the backend folder
  
* Note that the screens below may defer from yours
  
1. Change directory into the backend folder
2. Type ```docker-compose up -d``` to build and run all the images in the backend folder

![image](https://user-images.githubusercontent.com/89062463/161928446-ef7fc181-baff-4c2c-b1c9-c24dda09af67.png)

* You should see the following output in the visual studio code terminal
![image](https://user-images.githubusercontent.com/89062463/161928947-4482ab14-3e51-45ba-a702-200a512d681d.png)
 
 
### Next, run the frontend of focustudy in the frontend folder
  
  * Note that the screens below may defer from yours
  
1. Change directory into the front folder
2. Type ```npm run serve``` to run the frontend
  
  
![image](https://user-images.githubusercontent.com/89062463/161932600-d6d1f1a7-6252-411b-a190-3072c56289c6.png)


<br>
<hr>
<br>
  
  
  
  
  
## 🤓 How to Use Our Web Application (for Visitors to our Website) ##
  
**1. Click on "Sign in with Google"**
  
![image](https://user-images.githubusercontent.com/89062463/161939859-c623fddb-2ab6-4529-a3df-38d96cb21ff0.png)
  

<br>

**2. Click on "Sign in with Google"**

<insert image here>
  
<br>

  
**3. Once you have successfully login, you are brought to an overview. On this page, user can see the timer, tasklist and spotify music player. User can also add task or remove task,look for a song, or start the timer for a study session**
  
![image](https://user-images.githubusercontent.com/89062463/161943524-b3f171b0-5324-40c8-9546-1b9a34b2ffe6.png)

<br>
  
  

**4. User starts a study session by, adding a task , looking for a song and setting a time in the timer**
  
![image](https://user-images.githubusercontent.com/89062463/161943877-ec99895e-0e41-452a-bba5-1fc3b694d580.png)

<br>
  

**5. Once the timer countdowns to 0, user is brought to a rating section where user rates his/her experience for this particular study session**
  
![image](https://user-images.githubusercontent.com/89062463/161944166-93ced17d-8ab2-443b-ad9e-bbbfa4811a03.png)

<br>


**6. Once the user completes his/her rating, user sees their rating summary and clicks exit**
  
![image](https://user-images.githubusercontent.com/89062463/161944762-7d016f44-846b-4a96-b6fb-376aacc75cc5.png)

<br>
  

**7. User clicks on the logout button(highlighted in red) to exit FOCUSTUDY**
  
![image](https://user-images.githubusercontent.com/89062463/161947571-a3cd87f9-77e1-4433-99e6-7a22da2fd972.png)






  
  
  




  
  
  

  
  
  
  
  
  
  
  
  
  
 











