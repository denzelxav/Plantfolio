# EWI3615TU Template Repository

## Table of contents
This readme contains the following sections
* A description on how to set up the repository
* An overview of the template project
* An overview on how to use the various tools
* A description of what your readme should contain

## Setting up your repository
* Install Git Bash (Windows) or just Git (if not on Windows)
* Install Python 3.12
* (Windows) Add python 3.12 to your path as the installer does not do this
  * You can find python in this location if you used the installer: C:\Users\<your user>\AppData\Local\Programs\Python\Python312
  * Also add C:\Users\<your user>\AppData\Local\Programs\Python\Python312\Scripts
  * Appdata is a hidden folder. You need to configure your file explorer to show those by going to view -> show hidden items
* After updating your path you should reboot your editor and/or terminal
* run `python --version` to double-check that the right version is installed
  * (Windows) If you correctly updated your path, but you now get an error that talks about some microsoft settings, you should:
    * Go to the mentioned settings
    * Scroll down and disable the two items that reference python
    * Everything should now work again
* run `python -m pip install pipenv` to install pipenv. This is an improved version of virtualenv and allows us to easily manage the dependencies

How to download your dependencies and execute your code will depend on your IDE.
We recommend using PyCharm as it has excellent integration with the used tools.
Visual studio code has worse integration with pipenv and other tools and as such we do not recommend using this.
Everything should work in VS code, you will just have to use more manual terminal commands instead of clicking buttons.

Below you will find instructions for both PyCharm and VS code.

### PyCharm
You can use either PyCharm community or PyCharm professional for this project. Using your student email you should be able to get an education license for the pro version.
However, for this project the difference should not be significant.

When you open your cloned repository, PyCharm will ask you if you want to create a pipenv environment from the Pipfile, allow it to do so.
You can execute your code by pressing the button next to your main method and PyCharm will execute it.

If PyCharm did not prompt you to do this, run the following command: `pipenv sync`. 
Then configure the Python interpreter in PyCharm to use the Pipenv environment you just created.


### VS code
* When using VS code you need to run the `pipenv sync` command yourself to install the dependencies.
* Afterwards, you can select the generated virtual environment as the python interpreter, this will fix your editor

## Executing the project

There are a couple of ways to execute your project. You need to execute the project as a module to make sure that relative imports work correctly. This will execute the __main__.py file and all imports should start with project. This ensures that tests can run your project correctly and all files can find each other. Running a specific python file will not work as then all imports need to be relative to that file.

### Command line

* Running `python -m project` in the integrated terminal with the pipenv environment active
* Running `pipenv run python -m project` in a terminal without the pipenv environment active

### VSCode

* Go to run and debug on the left
* Click create a launch.json or add configuration
* Click python debugger
* Click module
* Enter project as module name

### PyCharm

* Go to edit configurations
* Create a new python configuration
* select module instead of script
* Enter project as module name

## Template project overview

The template project already contains quite a few files and configurations. 
These serve to give you an overview of how things can work. You are allowed to change almost everything. 
Please keep your docs folder around for handing in the project plan and any other documentation you want to keep.
Everything else you can change (or should change even in some cases).

Below I will provide a quick overview of everything in the repo at the moment:
* docs folder: Used to store the project plan and any other documentation
* project folder: root folder for all your code. You are allowed to change the name to something more specific.
Do note however, that you will then also need to update most config files as they are all created assuming the folder is called project.
PyCharms refactor functionality cannot deal with all of these, some will need to be fixed manually.
* test folder: This folder contains your tests. The tools have been configured with this as default value, renaming it therefore requires config updates.
* .gitignore: gitignore file for Python, PyCharm and VS code.
* .gitlab-ci.yml: The config file for gitlab pipelines. We have provided you with a minimum working template that integrates the various tools with GitLab features. You can and perhaps should chagne this file.
* .pylintrc: The configuration for Pylint. This is the default configuration of pylint with two changes:
  * Pylint requires explicit configuration for C libraries. PySide has been configured. You might need to add other libraries to this configuration if you decide to use other C libraries as well.
  * The ui folder has been exempted from linting. If you use Qt designer for your GUI you can use this folder to store the auto-generated python code which will not be type-checked or linted.
* Pipfile: This file contains the packages that your project needs, you can add them manually or use `pipenv install <package>` which will automatically add them to the pipfile.
* Pipfile.lock: Contains the actual packages with versions that you use. Generated when ever you use `pipenv update` after adding new packages to Pipfile. 
This file is stored in the repository to ensure that all members use the same version of each library. If someone else updated the Pipfile and generated a new Pipfile.lock
you can update your own libraries by running `pipenv sync`.
* pyproject.toml: Contains configuration for tests and coverage checking
* README.md: This README. You are expected to replace this file with a README for your specific project once you get started with development.

## Installed tools

### QT tools
In this project you will use PyQT to design a GUI. You can do this purely by using code 
or you can use the qt-designer. If you are within the pipenv environment you can start the designer by running `pyside6-designer` otherwise run `pipenv run pyside6-designer`.

Once you have created the ui files you can convert them using `pyside6-uic project/ui/app.ui -o project/ui/output.py`
to Python code. This ensures you can use auto-complete. See application.py for an example on how to load the ui code.

### Testing
For testing we have already installed pytest and coverage. If you do not want to use these libraries you can delete them.
However, they do integrate quite nicely with gitlab. 

If you run `pytest` you will execute your tests normally. You can also use the PyCharm buttons for it.
If you want to see coverage you can do `coverage run` followed by `coverage report` to get a nice table overview.
There are also commands to get for example HTML output.

The coverage tool has been integrated with the gitlab-ci. This means you will see a coverage percentage in your merge requests and the diff overview will show you which lines are tested and which are not.

### Mypy
You can use mypy by using `mypy .` to type-check your code.

### PyLint
To run Pylint you need to specify which files need to be linted. You can find the syntax for this in the gitlab-ci.yml file where we have configured two linting steps.
The test-suite is linted by also disabling the requirement for docstrings. You are allowed to change whatever you want here or even disable linting.
Do note that we will grade your usage of tools and the readability of your code.

## Your README
This README is for the template project. Once you get started with your project you should replace it with a new README.
While the content of this README is partly up to you there are a few things you must cover:
* What is the purpose of your application? What can I do with it?
* How to run your application? Does it require any external software installed? Or perhaps you need to configure a password.
* What features have you implemented?

This is information that is necessary for us to assess your program. However, a good README should contain more than just this.
You could consider adding example use cases with a step-by-step guide on how your software can help with them. 
If you believe adding more information makes your README to cluttered, you can also add links to other pieces of documentation to your README instead.