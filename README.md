# Project-AustonLJM
The repository of the Bachelor degree 1st semester group project.

## Guide to set up the developing environment for the project

The following are the steps to set up your machine to run the project

   1. Create a virtual environment
   2. Install the dependencies in the environment.

<<<<<<< HEAD
###Create a virtual environment
=======
### Create a virtual environment
>>>>>>> 979fa0a3bea4babab6e065f491eb8221ec1e2dcf

Open your terminal or command prompt and create a folder or go to a directory you want to save the project using 'cd' command.

```
cd path/to/your/directory
```

install 'virtualenv' with this command
<<<<<<< HEAD
```Windows
pip install virtualenv
```

```macOS, linux
=======

Windows
```
pip install virtualenv
```
macOS, Linux
```
>>>>>>> 979fa0a3bea4babab6e065f491eb8221ec1e2dcf
pip3 install virtualenv
```


Type the following to create a virtual environment. Replace 'myenv' with the name you want for your virtual environment.
<<<<<<< HEAD
```Windows
python -m venv myenv
```

```macOS, linux
=======

Windows
```
python -m venv myenv
```
macOS, Linux
```
>>>>>>> 979fa0a3bea4babab6e065f491eb8221ec1e2dcf
python3 -m venv myenv
```


Type this to activate the environment. Don't forget to replace 'myenv' with your environment name.
<<<<<<< HEAD
```Windows
myenv\Scripts\activate
```

```macOS, linux
=======

Windows
```
myenv\Scripts\activate
```
macOS, Linux
```
>>>>>>> 979fa0a3bea4babab6e065f491eb8221ec1e2dcf
source myenv/bin/activate
```


Now you're in the environment if the environment name appears inside a '()' at the front of your next line like the following.
```
(myenv)path/to/your/directory>
```


if you are done working on the project and want to get out of the environment, deactivate it by typing
<<<<<<< HEAD
```Windows, macOS, Linux
deactivate
```
=======
>>>>>>> 979fa0a3bea4babab6e065f491eb8221ec1e2dcf

Windows, macOS, Linux
```
deactivate
```

<<<<<<< HEAD
###Install the dependencies in the environment

The project uses Flask, a python web framework for the backend and pyFirmata, to communicate Python with the arduino. Both of the frameworks and the opencv-python library are included in the requirements.txt file. After activating the environment, to install, type the following command.(Do not install these without activating the environment first) 

```Windows
pip install -r requirements.txt
```

```macOS, linux
=======

### Install the dependencies in the environment

clone this repository in your directory using
```
git clone https://github.com/Swam-Htet-Paing/Project-AustonLJM.git
```

The project uses Flask, a python web framework for the backend and pyFirmata, to communicate Python with the arduino. Both of the frameworks and the opencv-python library are included in the requirements.txt file. After activating the environment, to install, type the following command.(Do not install these without activating the environment first) 
Windows
```
pip install -r requirements.txt
```
macOS, Linux
```
>>>>>>> 979fa0a3bea4babab6e065f491eb8221ec1e2dcf
pip3 install -r requirements.txt
```

Once the installation process is complete, the set up is done.
