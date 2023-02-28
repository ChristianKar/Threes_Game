This document keeps track of the process of analysis and conception of the project, including the objectives, sprints and tasks to complete in order to achieve those objectives.

## Objectives
- Develop a **Threes!** game variation, making it more **user friendly**.
- Add **new fonctionalities** to the game: asking for the user's name and displaying it, the score showing in real time, a ranking, a restart button.

## Analysis and Conception

Playing **Threes!** is very similar to playing **2048** developed by Gabrielle Cirulli: you must match up as many numbered tiles as possible to get a high score and you lose the game when you run out of space. You will find more information about 2048 [here](https://en.wikipedia.org/wiki/2048_(video_game)). The main difference between these two games is the numbers you are allowed to add up, but the game mechanics are almost the same. The movement of the tiles is also slightly different.   

In **Threes!** you start by adding **`1`** and **`2`** to create a **`3`**; then, a **`3`** can only be paired with a **`3`** to make **`6`**; in the same way, a **`6`** with another **`6`** adds up to **`12`**, and so on. In **2048**, you start by adding a **`2`** with a **`2`** to get a **`4`**, and then just keep adding up the tiles with the same number. Regarding the movement of the tiles in **2048**, for each direction, they move all the way until they encounter the border of the grid or a tile with a different number and add up when they collide with another tile having the same number. In **Threes!**, the movement of the tiles in any direction is restricted to one space at a time, and the tiles can add up only when they can't move any further because they reached the border of the grid or a another tile is blocking the way.

Since we already have a **2048 MPV** from the first week of Coding Weeks, which is only playable in the **terminal**, the procedure to develop the **Threes!** variation would be:  

- Adapt the 2048 MVP to a Threes! MVP, playable in the **terminal**.  
- Add the **new fonctionalities** to the code.
- Design and implement a first GUI with **Tkinter**.
- Design and implement the definitive GUI with **Pygame**.  

These main tasks are going to be broken down into smaller ones, so that the team members will work in differents tasks in paralelle and then merge their results to accomplish the objectives. The Sprints and Tasks are presented in the next two sections.

## Sprints

The steps to follow in order to develop the Threes! game variation are the following:  
  
**0.** Analysis and Conception of the product, User Story and assigning roles.   
  
*Background functions*  
**1.** Change **`2`** and **`4`** that appear randomly by **`1`**, **`2`** and **`3`**.  
**2.** Change the movement rules of the grid.  
**3.** Create functions to get the highest score, store the score, mute and unmute sound, restart game, check if movement is possible.  
**4** Test the functions.  
  
*Tkinter GUI*  
**5.** Design and implement the graphical interface to show the grid, tiles and movements.   
**6.** Get the user's arrow keys input and link it to the movements.  
**7.** Implement start game, exit game, mute and restart buttons.  
**8.** Create and display an initial window.  
**9.** Create and display a game over window showing the score of the user.  
**10.** Get the user's name as an input in the initial window, store it and display it during the game and at the end of it.  
**11.** Implement the music and sound effects of the game.  
**12.** Link each button to their respective function or window.  
  
*PyGame GUI*  
**13.** Follow Sprints 5 to 12 with PyGame.  
**14.** Improve the aesthetics of the game with more appropiated colors and shapes.  
**15.** Incorporate the top highscores fonctionality in the game over screen.  
  
*Final steps*  
**16** Test Coverage.  
**17.** Clean the code as much as possible.  
**18.** Clean and organize the git main.  
**19.** Mesure the environnemental impact of the project using the CarbonAI tool.  
**20.** Write the documentation for functions.  
**21.** Generate the README.md, Analysis_Conception.md and the REQUIREMENTS.txt files  
**22.** Make a presentation of the project.  
  
The order in which the sprints were listed doesn't necessarily define the order in which they are completed, it just gives a general structure for the tasks that have to get done.  
   
## Tasks
In this section you will find the tasks accomplished by the team members to complete the sprints and accomplish the objectives of the project.  

**Task 1:** Adjusting logic of 2048 to the logic of Threes and creating documentation of the functions  
***--> Members:** Ana, Victor*

**Task 2:** Creating an MVP of the Threes! GUI using Tkinter!  
***--> Members:** Klaus, Trinidad, Christos*

**Task 3:** Working with pygame to display the grid  
***--> Members:** Ana, Isadora*

**Task 4:** Working with pygame to adapt the function that moves the tiles in tkinter  
***--> Members:** Ana, Victor*

**Task 5:** Working with pygame to create a beggining page and in the transition to the game with the start button  
***--> Members:** Ana, Trinidad*

**Task 6:** Working with pygame to display a game over screen with the ranking  
***--> Members:** Victor, Trinidad*

**Task 7:** Updating score function and saving the final game grid with the score  
***--> Members:** Victor, Klaus*

**Task 8:** Creating play, replay, quit, ranking buttons and keep track of the best 5 players  
***--> Members:** Trinidad, Christos*

**Task 9:** Adding music in the movements   
***--> Members:** Victor*

**Task 10:** Making sure everything passes the test functions and verify quality of code  
***--> Members:** Isadora*

**Task 11:** Master of GitLab, organising our main to be awesome!  
***--> Members:***

**Task 12:** Documentation, requirements.txt, README.md, Analysis and Conception document.  
***--> Members:** Trinidad*

**Task 13:** Powerpoint and demo master!  
***--> Members:** Isadora*

**Task 14:** Solving out test of coverage  
***--> Members:***

**Task 15:** Test of CarbonIA  
***--> Members:** Klaus*