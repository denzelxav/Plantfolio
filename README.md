# Plantfolio documentation
This is a school project made by TU Delft students for the minor computer science.

Contibutors are:
- Owen Moon
- Wybe Mijnendonck
- Yiri Zwart
- Freya van Apeldoorn (did all the art)
- Denzel Träger


## Table of contents
This readme contains the following sections
* Purpose of the application
* Instructions on how to run the application
* List of implemented features
* How to use the application
* Additional documentation for other developers


## Purpose of application
This application is made for people that struggle to take care of their indoor plants and do not have the knowledge necessary to do so. The purpose of the application is thus to help people take care of their plants and improve the general health of the plants. It will help them by tracking their plants and informing them of basic actions they need to take such as watering, repotting and nutritioning. It can then also help remind the user when to water the plants. The application also includes features that help with finding the best place for a plant in your house, based on the sunlight conditions in specific places indoors. 


## Instructions on how to run the application
The application works by simply running a .exe file. To do so, go to the main branch in GitLab and open the dist folder. In the dist folder, open Plantfolio.exe and press download. Save this file somewhere and double click to open the application. On most computers, Window Defender will give a pop-up. In this case, click on 'More information' and click 'Run anyway'.
Alternatively, you can run it straight from python by opening the repository in VScode or PyCharm and running "python -m project" in the terminal.


## List of implemented features and how to use them
The application consists of multiple features, including:
* Adding a room: press 'Add Room', type the name of your room in the box and press 'OK'.

* Opening a room: select a room name in the rooms list and press 'Open Room' or double-click the room name.
    * Deleting a room: when there are no spots left in the room, press 'Delete room'.
    * Adding a spot: press 'Add spot', type in a name and press 'OK'.
    * Deleting a spot: select an empty spot and press 'Delete spot'.
    * Adding a plant: select an empty spot and press 'Add plant' or open a spot and press 'Add plant'. Then search for a species and select it, select an icon, type in a name and press 'OK'.
    * Opening a spot: select a spot and press 'Open spot' or double-click the spot.
        * Deleting a plant: press 'Delete plant'.
        * Adding an image: press 'Add image' and choose an image on your computer
        * Taking care of plant: press 'Water plant', 'Feed plant' or 'Repot plant'.
        * Manual health mode: when the calculated health does not match the actual health, you can control it manually.
        * Adding notes: type your own notes in the corresponding box.
        * Information: read the text in the plant view for the current information of the plant.
        * Moving a plant: press 'Move plant' and choose a different spot to move the plant to.

* Instructions: press on 'Instructions' and choose an action in the combobox.

* Watering all plants: in the main or 'All Plants' window, press 'Water all'.

* Viewing all plants: press 'All plants'.
    * Viewing a plant: select a plant and press 'View plant'.
    * Sorting the plants: choose the criteria to sort by and tick the 'Reverse' box when needed.

* Viewing recommended plants: press 'Recommendations'.
    * Excluding dangerous plants for pets: press 'Only show pet-safe plants'.

* Saving your data manually: press 'Save'. The application saves automatically upon closure but a crash may prevent saving Running the .exe saves the application's data in %appdata%/Plantfolio instead of the project files' .json .

* Viewing all notifications: press 'Notifications'. A less detailed overview is shown in the list on the main window.
    * Viewing a single notification along with its details: choose the right notification in the combobox.

* Sorting notifications: choose 'day', 'type' or 'weight' in the combobox to sort on the corresponding criteria.

* Refreshing notifications: press 'refresh notifications'. This will also delete notifications that have been taken care of in the mean time.


## Use case example
Scenario: Bob, a man with a passion for indoor plants, has difficulties to care for his plants due to his busy schedule. He uses the application to simplify and improve his plant care routine.

1.  Organizing rooms and spots: Bob sets up virtual rooms (e.g. living room and bedroom) and creates specific spots within them, such as window, corner and nightstand.
2.  Adding plants: he assigns plants like his Sansevieria "Sjaak" to the right spots and customizes their names and icons/photos.
3. Caring for the plants: Bob uses the notifications to remind him of tasks like watering, nutritioning and repotting. He marks the tasks as done in the plant view and adjusts plant health using Manual health mode when necessary.
4. Optimizing plant placement: by analyzing sunlight recommendations, Bob moves "Sjaak" to a brighter spot, significantly improving its health.
5. Keeping pets safe: concerned for his cat’s safety, Bob browses pet-friendly plant recommendations and discovers that the Hedera is not a suitable option due to its toxicity.
6. Plant monitoring: Bob uses the All Plants view to track his collection, sorting by different criteria to identify plants needing attention.
7. Saving data: he makes sure his data is safe by manually saving, although his data will most likely be saved automatically (as long as the application or computer does not crash).


## Additional documentation and structure for other developers
This project contains multiple files, most of them ordered in several folders which are listed below.
* database: this folder contains files with helper functions and classes to create the complete database of all the plants available in the application (plant_database.db). The initial database was retrieved with an API from https://perenual.com/docs/api .
* dist: this folder contains the .exe file to run the application. To incorporate recent changes in the .exe file, it has to be updated.
* docs: this folder contains the meeting notes which were made every week during a meeting with the TA of our project group. It also contains the slides that were used during the presentations of W2.6 and W2.10. Additionally, it contains the project plan made in the first two weeks of the project along with a changelog, documenting the changes made to it while working on the project. The project plan discusses the preparations that had to be made before starting to code and the requirements that were imposed beforehand.
* test: this folder contains the testing files to test the functionality of the underlying classes of the application. Most classes from group-10/project/classes have their own corresponding test file.
* Top-level files: there are a few top-level files that do not belong to a subfolder. Most of them were given in the template and are used to specify certain settings, install necessary modules or lint the Python files within the subfolders.
* project: this is the most important folder, containing all the files the application is built upon. "plant_database.db" contains the actual complete database with all the possible plants to choose from. "__main__.py" is the file that is run when starting the application. "user_data.json" is used to save the userdata when the application is closed. In turn, the project folder also has four subfolders, listed below:
    * art: contains the drawings, logo, icons, etc. used in the application.
    * classes: the objects and functions which make the functionality of the application possible.
    * ui: the .ui files made in Qt-designer along with its corresponding .py files.
    * ui_windows: contains the files that connect the functionality of the classes with the ui files.
