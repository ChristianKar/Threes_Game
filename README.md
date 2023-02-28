# Threes! by the Internationaux Team

## Description

The **Threes! project** was developed during the second week of **`CentraleSupélec's Coding Weeks 2021`** by the **Internationaux Team** for the **`'2048 and other games'`** subject. It consists of a **variation** of the original **Threes!** game; which is a **puzzle video game** developed by Sirvo and released in 2014. In **Threes!**, the player slides numbered tiles on a grid to combine addends and multiples of three. The game ends when there are no more possible moves left and the tiles are counted to get a final final score. You can get more information about the original game [here](http://en.wikipedia.org/wiki/Threes).

The variations implemented in this project include getting and displaying the **user's name**, **choosing the size of the grid**, a **restart** game button, different **music and sound effects**, **save and reload game** fonctionality, a **high scores ranking** and some variations in the graphical interface.

This application was developped in **Python**, using the libraries **Tkinter**, **Pygame**, **Playsound** and **Shelve**.

The **code** of this project was adapted from the **2048 MVP** developed by **Internationaux Team** during the first week of **`CentraleSupélec's Coding Weeks`**. The GUI was originally implemented with **Tkinter** to test the fontionalities of the game, and then adapted to **PyGame** in order to have a more **user-friendly** interface.

## Organisation of the files

## Requirements
You can find the libraries needed to run the game in the file **REQUIREMENT.txt**

Running the following command in the **shell** will install the **packages and modules** needed according to the configuration file **REQUIREMENTS.txt**:

`pip install -r REQUIREMENTS.txt`  

Or alternatively,

`python -m pip install -r REQUIREMENTS.txt`

You have to execute the previous command in the directory where the REQUIREMENTS.txt is placed. To do so, you can use the following command to change from one directory to another one:

`cd <directoryName>`

If you want to run it from another directory, you have to specify its path:

`pip install -r path/to/REQUIREMENTS.txt`

## How to execute the application
Tkinter version: Run the .py file.  
PyGame version: Run the .py file.  
  
Enjoy the game !


## The Internationaux Team: Group Members

Each  member of the group worked intensely for two weeks to create this game. Here is the list of the **members** and their main **role** in project. 

**Klaus HOLLER**: Tkinter GUI implementation, new fonctionalities implementation;  
  
**Trinidad DUFEY**: inputs/outputs management in Tkinter/PyGame GUI implementation, documentation;
    
**Victor Freitas TEODORO**: background functions, documentation, PyGame GUI implementation, new fonctionalities implementation;  
  
**Ana Luíza Haas BEZERRA**: git management, background functions, PyGame GUI implementation;  
  
**Christos KARATZIAS**: code consistency and junction, documentation, Tkinter and PyGame GUI implementation; 
   
**Isadora Boff de VARGAS**: function testing, planning management and presentation;  

*The group worked together as a whole on many functions and solutions. It’s important to mention that none of the group members had had extensive experience with Python before the last two weeks.

## Threes! RULES:
The original game designed for smartphones has the following set of rules:
-	9 squares initialize with random numbers **`1`**, **`2`** or **`3`**
-	To move the lumbers the player should chose one direction (left, right, up or down). All numbers will then move to the next empty square in the given direction, if possible.
-	Two numbers can only be added if one of them can’t move to the next square in the given position, i.e., it is against a “wall” or against a number which they can’t add.
-	The numbers **`1`** and **`2`** can only add to each other to create **`3`**
-	**`3`** can only add to another **`3`** to create a **`6`**, and **`6`** can only add to another **`6`** to create a **`12`** and so on. The idea is to work with multiples of 3 and add them.
-	Each time a movement is made a random **`1`**, **`2`** or **`3`** number will appear in a border empty square in the direction of the last movement.
-	The game ends when there are no more possible moves.
-	There is no winning condition, the objective is to reach the highest possible score by creating always greater numbers.  

The same rules apply for the **Thees! project** game.

## LICENSE: 
This is an open-source academic project which solely purpose is to increase the developer’s knowledge on Python. The authors do not intend to use the project for any purpose other than academic and do not desire to inflict any copyright from the original authors of the game, all rights being reserved to them.
