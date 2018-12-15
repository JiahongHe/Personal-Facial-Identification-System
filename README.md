# Personal-Facial-Identification-System
Final project of team HGCG for Advanced Software Engineering (COMS W4156)
Team members:
<ul>
	<li>Tvisha Gangwani</li>
	<li>Jiawen Li</li>
	<li>Evan Ziebart</li>
	<li>Jiahong He</li>
</ul>

# Abstract
We are working towards integrating facial recognition into our everyday lives. The system will identify the user as he/she walks in through the door and play their favorite song. 

## First Iteration
For our first iteration we have gotten the facial recognition API set up and are able to draw and test similarities between different people’s pictures. We have also been able to set up a server to hold the data- picture of person being identified, favourite song, user name and password. 

## Second Iteration
For our second iteration, we've got the server side set up and the users are now able to update their preferences/information with a preset password.

## Final Iteration
For our final iteration, we've completed what we've left before: the system now would really play the user's favourite music when he/she is detected by the camera, and the administrator of the system would be able to specify some default settings, for example, what the system would do if the detected user didn't specify a favourite song or the song the user specified is somehow not playable right now (file missing, corrupted, or removed).

# Installation
Operating System Supported: MacOS (Other OS not tested)
Python: 3.6.2

1. ```$ git clone https://github.com/JiahongHe/Personal-Facial-Identification-System``` 
2. ```$ cd Personal-Facial-Identification-System```
3. ```$ pip3 install -r requirements.txt```

# Usage

```$ cd sh``` \\

1. Start the server 
```$ bash startServer.sh```

2. Adminitration page (used for the administrator to change the settings/user information, off the shelf from Django)
```$ bash administration.sh```

3. New user registration
```$ bash registration.sh```

4. Registered user update their information (email and password set during registration required)
```$ update.sh```

5. Start face recognition (main utility)
```$ bash main.sh```

# Create administrator
The new adminitrator creation follows the standard way to creating a new superuser with Django.
```$ cd src/backendServer```
```$ python3 manage.py createsuperuser```

# To specify default behavior
<ol>
	<li> Go to administration page and login </li>
	<li> Click <code> System settings </code> </li>
	<li> Change the settings </li>
</ol>

# Run tests
1. ```$ cd test```
2. Static code analysis (optional) ```$ bash pre_commit.sh```
3. Main tests ```$ bash test_main.sh``` 


# Technical Components
<ul>
	<li>	We are using the face_recognition API available on Python and compatible with dlib. </li>
	<li>    The original design is to deploy this app on Raspberry Pi, however due the difficulty of installing dlib on the Pi model we have, this project has been moved to MacOS. </li>
	<li>	We mainly use Django as the framework when building our backend server to store and serve user information.  </li>
</ul>