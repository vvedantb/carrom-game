





















<div style="text-align:center; font-size:40px; vertical-align: middle;">Vedant Bhopatrao 13B</div>

<div style="text-align:center; font-size:30px">NEA Design Section</div>

<div style="text-align:center; font-size:20px">1st October 2021</div>

<div style="page-break-after: always; break-after: page;"></div>



# Contents

[TOC]

<div style="page-break-after: always; break-after: page;"></div>



# Design

## Overview

I will be writing my project using the programming language Python, and I will be using Visual Studio Code as my IDE. Using Python means I will be able to use the Pygame module which will aid me in the creation of the GUI for my program. 

It also allows me to manage and control the collisions between objects, inputs entered by the user and graphics, giving me a vast control in which way I can design my game. 
I have chosen to use Visual Studio Code as my preferred IDE compared to others such as the Python IDE because of the several advantages it offers, such as:

- Performance is much faster 
- Offers syntax highlighting
- Debugging tools provided by the IDE used to locate and fix syntax errors in the program

## Modules

The modules that I will be using in my program are:

- Pygame
  - This will be used to create the GUI
- Time
  - This will be used to set the refresh rate
- OS
  - This will be used to import images 
- Random
  - This will be used to randomise events

## Top down modular diagram

### Breakdown of the problem

In this section I will create a diagram that shows the main problem being split into several, smaller, manageable modules. This way, I can program each individual module separately so that during the development phase I can just link the modules together to form the final solution.

Using decomposition benefits the process of producing the final solution as each module can be tackled individually, rather than attempting to code the final program as a whole. This also allows me to test each module for errors - syntax or logical, which helps me in finding any bugs the program may have in a shorter amount of time. Overall, this reduces the amount of effort and time spent in creating the program.

A simple way to show how decomposition is used is through the use of a top down modular diagram where each box is represented as a module. The first box at the top shows the main problem that needs to be tackled, and as you go further down the diagram it shows how it is broken down, and the links that are formed between them through the arrows.

### Diagrams

#### Initial Decomposition

![initial-decomp](C:\Users\vedan\OneDrive\Desktop\NEA\design\top-down-modular-images\initial-decomp.png)



#### Game Decomposition

![game-decomp](C:\Users\vedan\OneDrive\Desktop\NEA\design\top-down-modular-images\game-decomp.png)

#### User Interface Decomposition

![user-interface-decomp](C:\Users\vedan\OneDrive\Desktop\NEA\design\top-down-modular-images\user-interface-decomp.png)

#### Settings Decomposition

![settings-decomp](C:\Users\vedan\OneDrive\Desktop\NEA\design\top-down-modular-images\settings-decomp.png)

#### Overall Decomposition

![overall-decomp](C:\Users\vedan\OneDrive\Desktop\NEA\design\top-down-modular-images\overall-decomp.png)

### Explaining the modules

 #### Main Menu/GUI

##### User Interface

Here, the player can see all the options offered on this page. The buttons for the game modes can include an animation once hovered on them to give a small preview into what they can expect. There is also an information tab on the button which will present the manual to the user and provide detailed information on how to play the game.

##### Logical

Each button will trigger certain modules to be run after the user has clicked on an option. Each module can be written in its own specific file, which will be stored in the same folder as the main program, which will be linked so the module can be accessed when it has been called. 

#### Game

##### Player

Player pieces should be differentiated using colouring to define which pieces belong to whose side.

##### Enemy

Enemy pieces should be differentiated using colouring to define which pieces belong to whose side.

#### Movement

The program must have rules defined so that movement of the pieces is restricted to within the board only - it should not be able to go outside the border of the board. Separate validation must be created for the striker, so that it stays within its boundary and can only be shot within the region of its boundary limits. 

##### Piece Collisions 

The game should be able to detect collisions between pieces. This can be done by detecting if one pixel of each of the pieces overlaps each other, it will be considered as a collision.

##### Reaction of Collisions

The game should also be able to react to a collision between pieces after it has occurred. 
After collision, the pieces should not stand still, or continue moving at a uniform rate - deceleration should not be constant. This factors in other elements that slows down the rate at which the piece travels, such as friction, which simulates the real life experience of playing Carrom. Instead, they should react by changing direction and decrease its momentum depending on the speed of collision, which can be measured by how long it took the pieces to collide from start. 

#### Inputs

##### Buttons

The program should be able to detect when a button has been pressed and react accordingly, i.e. perform the function the button was created for.

##### Keyboard key press

The program should be able to detect when a key has been pressed on the keyboard and react accordingly.

##### Mouse click

The program should be able to detect when a mouse button has been clicked and react accordingly.

##### Logical

I will need to check that the correct inputs lead to the correct outputs. Therefore, validation for each input will need to be used to ensure the robustness of the system. Once validated, the certain operation may be carried out.

#### Settings

##### Options

An options button would need to be created that navigates the user to the main menu.

##### Sensitivity

A method would need to be created that allows the player to change the sensitivity of the cursor or of how much a piece moves after a key is pressed on the keyboard.

##### Change controls

This page should allow the user to change their key bindings. It should be easy to change, i.e. simply click on the current set keybind and press the new character that you would like to bind the control to. A method would need to be created that syncs the new changes made to the settings.

##### Store settings

There are two options on where to save the settings per user: locally on the user’s system, or online with the use of a database. Storing the settings data online would require some method of linking to the specific user so they can restore their settings if accidentally reset which would require a login system. 

Although storing the contents online would mean faster and smoother performance for the user, running a server to hold the data also comes at a cost. Therefore, storing the settings locally would be the best option for this project. A method would need to be created that loads the new settings upon startup of the game each time.

### Flowchart

![OVERALL FLOWCHART](C:\Users\vedan\OneDrive\Desktop\NEA\design\OVERALL FLOWCHART.png)

### Algorithms

#### Main Menu

##### Pseudocode

```python

def mainMenu():     

    while True:
        
        screen.fill(WHITE) # Fills the screen in the desired colour
        drawText("Main Menu", font, WHITE, screen, 20, 20)

        mx, my = pygame.mouse.get_pos() # Retrieves the current position of where the mouse is

        button_1 = pygame.Rect(50,100,200,50)
        button_2 = pygame.Rect(50,200,200,50)
        button_3 = pygame.Rect(50,300,200,50)
        button_4 = pygame.Rect(50,400,200,50)
        

        if button_1.collidepoint((mx,my)): # Checks if mouse location overlaps button 1 location
            if mouse_click: # Checks if button has been clicked
                game()
        if button_2.collidepoint((mx, my)):
            if mouse_click:
                options()
        if button_3.collidepoint((mx, my)): 
            if mouse_click:
                import settings
        if button_4.collidepoint((mx, my)): 
            if mouse_click:
                quit_game()
        
        pygame.draw.rect(screen, WHITE, button_1) # Draws a rectangle onto the screen in white colour for button 1
        drawText("Play Game", font, BLACK, screen, ( screen.get_width()/10 ), ( screen.get_height()/6 )) # Writes text onto the screen with the specified font at the start with a black colour onto the screen
        
        pygame.draw.rect(screen, WHITE, button_2)
        drawText("Options", font, BLACK, screen, ( screen.get_width()/10 ), ( screen.get_height()*2/6 ))
        
        pygame.draw.rect(screen, WHITE, button_3)
        drawText("Settings", font, BLACK, screen, ( screen.get_width()/10 ), ( screen.get_height()*3/6 ))

        pygame.draw.rect(screen, WHITE, button_4)
        drawText("Quit", font, BLACK, screen, ( screen.get_width()/10 ), ( screen.get_height()*4/6 ))

        mouse_click = False

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT: # Checks if the cross (top right button) has been pressed
                pygame.quit() # Program ends
                sys.exit()
            if event.type == KEYDOWN: # Checks if a key has been pressed
                if event.key == K_ESCAPE: # Checks if escape key has been pressed
                    pygame.quit() # Programs ends
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN: # Checks if mouse button has been pressed
                if event.button == 1: # Checks if button has been clicked
                    mouse_click = True

        pygame.display.update() # Updates display
        clock.tick(FPS) # 
```

##### Explanation

This algorithm is used to create the main menu, where the user is able to select the options they would like to carry out. Text is written onto the screen to show which button corresponds to what function using the *drawText* function. 

Validation is then used to check where the mouse is hovering over and whether it overlaps with where the button is placed. If it overlapping and a click has been made, the algorithm continues to the specific function for whichever button had been pressed. This loop is run constantly, checking whether a click has been made by the mouse and whether it overlaps with a button, until successful. 

At any moment, if the user decides to press the 'ESC' key, they will be returned to the main menu. This key acts as the back function.

##### Flowchart

![main menu new](C:\Users\vedan\OneDrive\Desktop\NEA\design\new flowchart\main menu new.png)

##### Test Plan

To test whether this module is successful, I will do unit tests to validate whether it accepts and correctly outputs the data given.

| Test Data                      | Test Type  | Justification                                                | Validation                                                   |
| ------------------------------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Mouse click                    | Function   | Checks whether a click is performed by either the mouse of trackpad in the area of the button and enters the function if so | If mouse click is not registered and overlapping with the button, nothing should happen. If it is, game function should be run. E.g. ```if button_1.collidepoint((mx,my)): if mouse_click: game()``` |
| Random keys and clicks spammed | Robustness | Checks whether the program can mass handle lots of different values of inputs with different data and the same time and to see what the program will do | The program has a refresh rate of 60 times per second, so it should be able to constantly check for new inputs provided to the program and validate using the `if` statement above. |

#### Game

##### Pseudocode

```python
def game():
    run = True

    while run:
        screen.fill(WHITE)

        drawText("Play Game", font, BLACK, screen, ( screen.get_width()/20 ), ( screen.get_height()/10 )) # Writes text onto the screen 
        
        # player1 = Player(False, 0, 20)
        # player2 = Player(False, 0, 20)


        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    striker_shot()
                    
        
        pygame.display.update()
        clock.tick(FPS)
```


##### Explanation

This algorithm is used to create the Carrom game, where the user is able to play against a friend via passing turns manually. Text is written onto the screen to show whose turn it is to shoot the striker by using the \textit{drawText} function. 

First, the turn is randomly determined. Whoever it lands upon, they get the first opportunity to take a shot at the pieces with their striker. If the user pockets a piece, they get another shot. If the striker collided with any nearby pieces along the way, the pieceCollision function is run. This is where the amount of speed, direction, distance and time each surrounding collided pieces travels by, and this is determined by using the equations of motion.  

If the piece that had been pocketed by the striker was a black piece, 1 point is added to the total score of that user. If the piece pocketed was white, 2 points are added to the total score, if the piece pocketed was purple, 5 points are added to the total score. The algorithm continually checks whether pieces have been pocketed and by who, then determines which piece was pocketed and its corresponding value for number of points, which is then added to the total points gained by the user. 

If a piece had not been pocketed after the striker was shot, the turn is passed onto the opponent. This entire process occurs until a player has obtained more points than the opponent and the remaining possible points currently available on the board, from which point a winner can be determined.

At any moment, if the user decides to press the 'ESC' key, they will be returned to the main menu. This key acts as the back function.

##### Flowchart

![game function](C:\Users\vedan\OneDrive\Desktop\NEA\design\new flowchart\game function.png)

##### Test Plan

To test whether this module is successful, I will do unit tests to validate whether it accepts and correctly outputs the data given.

| Test Data                      | Test Type  | Justification                                                | Validation                                                   |
| ------------------------------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Mouse click                    | Function   | Checks whether a click is performed by either the mouse of trackpad in the area of the button and enters the function if so | If mouse click is not registered and overlapping with the button, nothing should happen. If it is, game function should be run. E.g. ```if button_1.collidepoint((mx,my)): if mouse_click: game()``` |
| Random keys and clicks spammed | Robustness | Checks whether the program can mass handle lots of different values of inputs with different data and the same time and to see what the program will do | The program has a refresh rate of 60 times per second, so it should be able to constantly check for new inputs provided to the program and validate using the `if` statement above. |



#### Options

##### Pseudocode

`````` python

def options():
    
    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Options', font, WHITE, screen, 20, 20)
        
        button_7 = pygame.Rect(20,60,300,50)
        pygame.draw.rect(screen, WHITE, button_7)
        drawText('Select Striker Colour', font, BLACK, screen, 20, 60)
        



        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False


        pygame.display.update()
        clock.tick(FPS)
``````



##### Explanation

After the user has selected the option to go to the options of the game through the main menu, they are presented with a screen of cosmetic customisations for their items. From there, they are able to change the colour, or add design to the: pieces, boards or striker. 

At any moment, if the user decides to press the 'ESC' key, they will be returned to the main menu. This key acts as the back function.

##### Flowchart

![options new](C:\Users\vedan\OneDrive\Desktop\NEA\design\new flowchart\options new.png)

##### Test Plan

| Test Data                      | Test Type  | Justification                                                | Validation                                                   |
| ------------------------------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Mouse click                    | Function   | Checks whether a click is performed by either the mouse of trackpad in the area of the button and enters the function if so | If mouse click is not registered and overlapping with the button, nothing should happen. If it is, game function should be run. E.g. ```if button_1.collidepoint((mx,my)): if mouse_click: game()``` |
| Random keys and clicks spammed | Robustness | Checks whether the program can mass handle lots of different values of inputs with different data and the same time and to see what the program will do | The program has a refresh rate of 60 times per second, so it should be able to constantly check for new inputs provided to the program and validate using the `if` statement above. |



#### Settings

##### Pseudocode

``````python
def settings():

    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Settings', font, WHITE, screen, 20, 20)

        drawText('X-Senstivity', font, WHITE, screen, 20, 60)
        drawText('Y-Senstivity', font, WHITE, screen, 20, 100)
        
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        
        pygame.display.update()
        clock.tick(FPS)
``````



##### Explanation

After the user has selected the option to go to the settings of the game through he main menu, they are presented with a screen of controls. Firstly, they are presented with the sensitivity of the movement of their mouse, through co-ordinates; x-sensitivity and y-sensitivity. Changing the value for each sensitivity directly affects how quickly the mouse will move for each axis. 

Next, they are able to change their key binds for every operation available, all they would simple need to do is click on the keybind that would need changing and press on what they would like to set the new keybind as. This will then be displayed onto the screen using the \textit{drawText} function which writes the text onto the screen. 

At any moment, if the user decides to press the 'ESC' key, they will be returned to the main menu. This key acts as the back function.

##### Flowchart

![settings function](C:\Users\vedan\OneDrive\Desktop\NEA\design\new flowchart\settings function.png)

##### Test Plan

| Test Data                      | Test Type  | Justification                                                | Validation                                                   |
| ------------------------------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Mouse click                    | Function   | Checks whether a click is performed by either the mouse of trackpad in the area of the button and enters the function if so | If mouse click is not registered and overlapping with the button, nothing should happen. If it is, game function should be run. E.g. ```if button_1.collidepoint((mx,my)): if mouse_click: game()``` |
| Random keys and clicks spammed | Robustness | Checks whether the program can mass handle lots of different values of inputs with different data and the same time and to see what the program will do | The program has a refresh rate of 60 times per second, so it should be able to constantly check for new inputs provided to the program and validate using the `if` statement above. |



#### Quit Game

##### Pseudocode

``````python


def quit_game():

    run = True
    
    while run:
        screen.fill(BLACK)

        drawText('Quit?', font, BLACK, screen, 20, 20)
        drawText('Press Q to confirm', font, BLACK, screen, 20, 60)
        drawText('Press ESC to return', font, BLACK, screen, 20, 100)
        
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    run = False
                    pygame.quit()
        
        pygame.display.update()
        clock.tick(FPS)
``````



##### Explanation

After the user has selected the option to quit the game through he main menu, they are presented with a message to confirm whether they would like to quit or not. This function first displays the command to confirm to quit the program through the use of the \textit{drawText} function, which writes the text onto the screen. 

Next, all the possible inputs events are retrieved from the Pygame module through the use of *pygame.event.get*, and all of these events are stored in the \textit{events} variable. It is then validated and compared against if the user has pressed the 'Q' key on their keyboard, to which the program exits, or if the user presses the 'ESC' key, to which the user is returned to the main menu. 

At any moment, if the user decides to press the 'ESC' key, they will be returned to the main menu. This key acts as the back function.

##### Flowchart

![quit function new](C:\Users\vedan\OneDrive\Desktop\NEA\design\new flowchart\quit function new.png)

##### Test Plan

| Test No. | Test                                      | Output                                                       |
| -------- | ----------------------------------------- | ------------------------------------------------------------ |
| 1        | Allow user to press the close button      | The window should close after the close button is pressed    |
| 2        | Allow user to press Q to close the window | The window should close after the close button is pressed    |
| 3        | No errors when closing game               | The window closes successfully, without lagging, freezing, crashing or using too much resources on the system |



### Usability Features

#### Initial Main Menu Design

This is the initial design of the main menu that I will be using. It is a template, and will not be how it will be looking exactly on the program. It has been made to be quite simply, making it easy for the user to navigate through. I will get feedback from my stakeholder to see what their thoughts are on my design and if they would like any changes to improve the design in the next iteration. 

<img src="C:\Users\vedan\OneDrive\Desktop\NEA\design\ui design pics\main menu old.png" alt="main menu old" style="zoom:100%;" />

| **No.** | **Feature** | **Description**                                              |
| ------- | ----------- | ------------------------------------------------------------ |
| 1       | Start       | A button that the user clicks to start the game. Once clicked, it will run the game function |
| 2       | Help        | A button that the user clicks to get more information on whatever current stage they are at in the game |
| 3       | Exit        | A button that the user clicks on to exit the game            |



#### Stakeholder Feedback

After speaking with my stakeholders, they have mentioned some valuable points on how to improve the design which are listed below:

- The design is simple, so would be easy for new users to navigate through the menu, as it isn't cluttered with irrelevant features or options. However, with that being said, the design seems too simple - perhaps more detail could be added to the background, something to represent that this is a Carrom game. An example of what to keep as the background could be an image of a Carrom board itself.
- The 'i' button should be removed, and replaced with a standard information button. 
- The position of the 'i' button should be moved to the centre, as all the buttons would be closer to the centre, so the user would have less movement between buttons to click on them, making it easier.
- The buttons should have their own separate individual boxes behind them, to indicate they are buttons, not just regular text. It can also show and represent the exact area which is a button and is clickable. The opacity of these boxes should not be set to 100\% so to make the design more stylish.
- Colour scheme of the text is too simple - it has just been set as white. Instead, a drop shadow should be added on top of the text box, to give emphasis to the text. Similarly, a inner glow should be added to the text too.
- Overall colour scheme of the main menu should be similar to the colours of a Carrom board itself, i.e. a brown, peachy colour.

#### Iterated Main Menu Design

Using the comments from my stakeholders, I have redesigned the main menu to include the feedback and areas which I needed to improve on.

![main menu](C:\Users\vedan\OneDrive\Desktop\NEA\design\ui design pics\main menu.png)

| No.  | Feature     | Description                                                  |
| ---- | ----------- | ------------------------------------------------------------ |
| 1    | Game button | Main button the users clicks on to start the game            |
| 2    | Options     | Button the user clicks on                                    |
| 3    | Settings    | Button the user clicks on to change their sensitivity of contorl of the pieces |
| 4    | Information | Button the user clicks on to gain more information of Carrom, such as rules, pieces points value |
| 5    | Tutorial    | Button the user clicks on to view a video and information into how to play Carrom |
| 6    | Help        | Button the user clicks on to view frequently asked beginners questions into how Carrom is played |

**What the updated design offers:**

- Bigger, brighter buttons
- Higher contrast 
- Carrom picture in background
- Glow on text
- Buttons split into two sections: game features, and game information

#### Game Design 

![design omg](C:\Users\vedan\OneDrive\Desktop\design omg.png)

### Key Variables and Objects

#### Key Variables

| **Variable Name** | **Data Type** | **Justification**                                            | **Value**                                                    | **Validation**                                               |
| ----------------- | ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| WIDTH             | Integer       | Defines the width of the resolution of the program           | I will set the starting screen size as 1280x720, as this is the minimum resolution for most monitors. But, I will make the window resizable for the user, so that the screen is compatible for most monitor display sizes, e.g. if the user is using a ultra wide monitor they can simply make the screen fullscreen or drag the display to the value they desire. | I will be using pygame.RESIZABLE() to automatically resize the window. Therefore, this will not require any validation as is it automatically resized depending on what the user prefers to set their  resolution as. |
| HEIGHT            | Integer       | Defines the height of the resolution of the program          | I will set the starting screen size as 1280x720, as this is the minimum resolution for most monitors. But, I will make the window resizable for the user, so that the screen is compatible for most monitor display sizes, e.g. if the user is using a ultra wide monitor they can simply make the screen fullscreen or drag the display to the value they desire. | I will be using pygame.RESIZABLE() to automatically resize the window. Therefore, this will not require any validation as is it automatically resized depending on what the user prefers to set their  resolution as. |
| FPS               | Integer       | Defines the number of times the program will refresh/update in a second | I will set the FPS constant to 60, providing a smooth experience for the user while at the same time allowing it to run on most hardware available. However, it can drop below 60 if the hardware is not capable of handling this frame rate. | N/A                                                          |
| run               | Boolean       | Defines whether the program should run or not                | This will be set to True until the user decides to quit the game in which case it will be set to False. | While run is true, the game will keep running forever. Run will be set to false when the user wants to quit, in which case the game and the program ends. |
| mx                | Integer       | Retrieves and stores the x co-ordinate of the current location of the cursor of the mouse into the variable mx | This is constantly changes if the mouse or trackpad (whichever is controlling the cursor) is constantly moving. | mx is the value of the x coordinate of the mouse. To validate this to make sure only reasonable values can be used, the value cannot be greater than the width of the screen size. |
| my                | Integer       | Retrieves and stores the y co-ordinate of the current location of the cursor of the mouse into the variable my | This is constantly changes if the mouse or trackpad (whichever is controlling the cursor) is constantly moving. | my is the value of the y coordinate of the mouse. To validate this to make sure only reasonable values can be used, the value cannot be greater than the height of the screen size. |
| mouseClick        | Boolean       | Used to determine whether a click has been made by the mouse or not | This will be set to True when a user has clicked using their mouse, otherwise it is False. | I will be using `IF`statements to check whether a click has been made. I will use a nested `IF`statement to determine whether the click has been made in a certain area (where the button is) and program it to react to this accordingly. |

#### Objects 

| **Object Name** | **Object Function**                                          |
| --------------- | ------------------------------------------------------------ |
| Player          | This allows to create an object for the player where it can hold information about the player such as: number of taken pieces, number of remaining pieces, total points obtained, etc |
| Enemy           | This allows to create an object for the enemy where it can hold information about the player such as: number of taken pieces, number of remaining pieces, total points obtained, etc |
| Collision       | This allows show the effect of two or more colliding pieces together |
| Striker         | This allows me to create an object for the striker so that I can set personal cosmetics for the object for each user, such as: custom colours, custom design |
| Pieces          | This allows me to create an object for the pieces so that they can have their own unique characteristics such as: number of points it is worth, colour of piece, etc |
| button1         | Creates a button in the main menu for the option for the user to play the game |
| button2         | Creates a button in the main menu for the option for the user to play the game |
| button3         | Creates a button in the main menu for the option for the user to play the game |
| button4         | Creates a button in the main menu for the option for the user to play the game |
| button5         | Creates a button in the main menu for the option for the user to play the game |
| font            | Sets the font to be used within the program when text is written to the screen |



### Testing 

#### Alpha Testing

Alpha testing performs commonly carried out tasks that a user might do, and test them to see if they work successfully. It is a type of acceptance testing.

| **Function**                         | **Justification**                                            | **Method of Input**                                          | **Input**   | **Expected Result**                                          |
| ------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- | ------------------------------------------------------------ |
| User can click the button            | User should be able to click buttons to navigate through the menu | Go to main menu and click on options                         | Mouse click | Should be able to freely navigate through the options available |
| User can change sensitivity of mouse | This allows them to change how quickly or slowly a mouse moves, giving the user greater control of their mouse based on the level they have chosen | Go to main menu, click settings then should be able to adjust it from there | Mouse drag  | User should be able to freely change the sensitivity of the mouse |



#### Function and Robustness Testing

This type of testing is to show how well the program can withstand against invalid data types being inputted into the system.

| Function                                              | Justification                                                | Method of Input                                              | Input                                                        | Expected Result                                              |
| ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Stress input handling                                 | Random keys on keyboard spammed to see what the program will do over a certain length of time | The user should do this using a keyboard                     | Random keys spammed                                          | Program should continue running smoothly as ever and not react unless the keys correspond to a valid function |
| User inputs string instead of integer for sensitivity | Validation would need to be required within the program to ensure that only one data type can be accepted when changing the value of the sensitivity - integer only. | User can inputs words by typing phrases using their keyboard | Example of an input would be "test", to see if the algorithms accepts it or not | Algorithm should not accept data inputted if it is not in integer form |



#### Usability Testing

This tests show how usable the program is to the user.

| Function                                         | Justification                                                | Expected Result                                              |
| ------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Change sensitivity of mouse                      | User should be able to change sensitivity of the mouse to suit their personal preference, and make it more comfortable for them | User should be able to change sensitivity of mouse successfully, with no errors or bugs |
| Change colour of striker                         | User should be able to change colour of their striker for their personal cosmetic reasons | User should be able to change colour of striker successfully, with no errors or bugs |
| Change colour of board                           | User should be able to change colour of the board for their personal cosmetic reasons | User should be able to change colour of board successfully, with no errors or bugs |
| Play a game of Carrom five times                 | Play an entire game of Carrom with no errors occurring at least 5 times | Playing the game around 5 times should cover all scenarios that could occur in a game, so if all times the game has been played were successful, i.e. program runs smoothly, the test is a success |
| Change key binds and play another game of Carrom | This test should show that the key binds can be changed successfully and that the new settings are applied immediately. This is shown by playing another game of Carrom with the new binds successfully | New key binds are applied successfully and changes have been made. The changes are seen in the game |

#### Acceptance Testing

| Test No. | Description                                                  | Expected Outcome                           |
| -------- | ------------------------------------------------------------ | ------------------------------------------ |
| 1        | Users should be able to input variables                      | User can input variables                   |
| 2        | User is shown main menu and a functioning GUI                | GUI is working as expected                 |
| 3        | Animation updates as a user event occurs (mouse click or keyboard press) | Animation updates as per user interactions |
| 4        | User can restart or quit the game                            | User can restart/quit                      |



### Post Development Testing

#### Beta Testing

I will complete this testing by sending the final product before it is released to my stakeholders to a group of people that can test the game for me and can identify any bugs that occur. This will help advance me to the next stage of development and so I can release the game to my stakeholders.

#### GUI Testing

| Test        | Justification                                                | Expected Outcome                                             |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Main Game   | This is required and should be functioning properly so that the user is able to input whatever they like correctly, and even if not the program should respond accordingly. | Main game is displayed to the user and the screen works as expected. |
| Settings    | This is required to allow the user the option to change how quickly or slowly they want to move their pieces if they are unable to do it through external settings | User is able to change sensitivity of cursor through this menu |
| Options     | This is required so users can set their own custom key binds of keys which they prefer. Right handed players may prefer W, A, S, D keys for movement whereas left handed players may prefer the Up, Down, Left, Right keys for movement. | User is able to change keybinds through this menu            |
| Information | This is required to be displayed to all new users, teaching them how to play | User is able to view point system in Carrom                  |
| Tutorial    | This is required to be displayed to all new users, teaching them how to play | User is able to view a tutorial on how to play Carrom        |







































