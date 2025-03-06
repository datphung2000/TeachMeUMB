
# TeachMeUMB

## Table of Contents
- [Resources](https://github.com/dimarcode/TeachMeUMB/new/main?filename=README.md#resources)
- [Set Up Local Environment](https://github.com/dimarcode/TeachMeUMB/new/main?filename=README.md#set-up-local-environment)
	- [Prerequisites](https://github.com/dimarcode/TeachMeUMB/new/main?filename=README.md#prerequisites)
	- [Directions](https://github.com/dimarcode/TeachMeUMB/new/main?filename=README.md#directions)
- [Next Steps](https://github.com/dimarcode/TeachMeUMB/new/main?filename=README.md#next-steps)
# Resources:

Github Repo: [https://github.com/dimarcode/TeachMeUMB](https://github.com/dimarcode/TeachMeUMB)

Flask: [https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/)

React: [https://react.dev/](https://react.dev/)

MySQL: [https://www.mysql.com/](https://www.mysql.com/)

HTML Forms: [https://www.w3schools.com/html/html_forms.asp](https://www.w3schools.com/html/html_forms.asp)

# Set Up Local Environment
## Prerequisites:

**VSCode:**
- [https://code.visualstudio.com/](https://code.visualstudio.com/)
    
**Github account:**
- [https://github.com/](https://github.com/)
    
**Github extension for VSCode:**
- [https://code.visualstudio.com/docs/sourcecontrol/github](https://code.visualstudio.com/docs/sourcecontrol/github)
- Make sure to log in to extension within VSCode
    
**Docker:**
- Windows or Mac users (Docker for Desktop Personal): [https://docs.docker.com/get-started/get-docker/](https://docs.docker.com/get-started/get-docker/)
- Linux/VM users: [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
- Docker extension for VSCode
    
**WSL (Windows users):**
- If you are on windows, you will not be able to run Docker without **Windows Subsystem for Linux.** (Obviously, this is not necessary for Mac)
    - [https://gcore.com/learning/how-to-install-wsl-2-on-windows/](https://gcore.com/learning/how-to-install-wsl-2-on-windows/)
    - Make sure it is WSL2!!!!
        
## Directions

1. Install prerequisites.
    
2. Open VSCode and choose the “clone a github repository” option
    
3. Paste the TeachMeUMB repository URL into VSCode and choose a directory to keep the project in
    
    1. [More about cloning a repository](https://code.visualstudio.com/docs/sourcecontrol/overview)
        
4. Clone the repo to that location
    
5. Make sure docker is running in the background, either by starting docker desktop, or by running `sudo systemctl start docker`
    
6. Right click the docker-compose.yml file and click `compose up`
    
    1. The compose file will create four containers, and between them, they will have all the dependencies necessary to run Javascript, python, SQL queries, html, css, flask, and react.
        
    2. Almost every folder is kept locally on your computer. I set it up this way so you can just edit the files.
        
    3. The files/folders you should **not** mess with are:
        
        1. Anything with “Docker” in the name.
            
        2. .Json files that you did not create
            
        3. requirements.txt
            
        4. .gitignore
            
7. Right now, if everything has been installed correctly, you should be able to open up chrome on your local machine and go to
    
    1. [http://localhost:5000/](http://localhost:5000/) and see "Flask is Running! 🚀" - this means the front end is working
        
    2. [http://localhost:5000/db-test](http://localhost:5000/db-test)“ and see “Object of type Row is not JSON serializable" - this means the back end is working, and your front end can talk to the MySQL database running in the other container
        
8. If there are any issues, please let me know ASAP ![(smile)](https://umb-capstone.atlassian.net/wiki/s/2089941738/6452/9284258a473d8a1043657188f7dc7de0057f64a0/_/images/icons/emoticons/smile.png "(smile)")
    
## NEXT:

Watch this video:

[https://www.youtube.com/watch?v=PppslXOR7TA&list=PL91V7rFux1JlBhO6RZ0WtK-pDcDRL-R0K&index=12](https://www.youtube.com/watch?v=PppslXOR7TA&list=PL91V7rFux1JlBhO6RZ0WtK-pDcDRL-R0K&index=12)

- This is a basic template for a CRUD app, I just adapted his framework to include MySQL instead of SQLite.
    
- CRUD is an acronym that describes the ways a system can interact with data in a database:
    

1. **C**reate
    
2. **R**equest
    
3. **U**pdate
    
4. **D**elete
    

Which is basically what we need to do for the basic functionality of our app. He used React (a javascript framework) for the front-end, and Flask (an API framework for talking to databases) for the backend (links to the websites for both at the beginning of this doc). Watch the video and then decide if this seems doable. He describes what’s happening pretty well as he goes. I only wrote enough code to do a test to see if it’s working.
