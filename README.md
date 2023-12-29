# Balen Nouri Tic-Tac-Toe For 2 Players

## Table of Contents

- [Balen Nouri Tic-Tac-Toe For 2 Players](#balen-nouri-tic-tac-toe-for-2-players)
  - [Table of Contents](#table-of-contents)
  - [UX](#ux)
    - [Website owners goals](#website-owners-goals)
    - [User goals](#user-goals)
  - [Features](#features)
    - [Game](#game)
    - [Future feature to implement](#future-feature-to-implement)
  - [Technologies Used](#technologies-used)
  - [Libraries used](#libraries-used)
  - [Testing and Validation](#testing-and-validation)
    - [PEP8](#pep8)
    - [Manual testing](#manual-testing)
    - [User stories testing](#user-stories-testing)
    - [Bugs](#bugs)
      - [Resolved](#resolved)
      - [Python Warnings and Bugs](#python-warnings-and-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [How to deploy](#how-to-deploy)
  - [Credits](#credits)

## UX

### Website owners goals

### User goals

## Features

### Game

### Future feature to implement

## Technologies Used

## Libraries used

## Testing and Validation

### PEP8

### Manual testing

### User stories testing

### Bugs

#### Resolved

During code validation and testing the game, these warnings were shown:

#### Python Warnings and Bugs

At the start of the game, when the user can choose between rules, quit or play, the game will give the message to the user that they used an invalid command. The problem was, when the message showed up it just kept coming more and more. Below you can see how I solved it.

- This is the code I used first that caused the bug.

![Bug picture of code](assets/readme/bug-one-two.png)

- This is the code I used that worked and removed the bug.

![Bug solution](assets/readme/bug-one.png)

This was causing error when the user pushed on any of the options, Below you can see how I solved it.

- The code i used, that didn't work.

![bug](assets/readme/bug-two.png)

- This is the code i used that worked.

![bug solution1](assets/readme/bug-two-two.png)

### Unfixed Bugs

## Deployment

### How to deploy

To deploy this page to Heroku from its [GitHub repository]() the following steps were taken:

- Log into or register a new account at [Heroku](https://www.heroku.com/).
- Click on the button **New** in the top right corner of the dashboard.
- From the drop-down menu then select **Create new app**.
- Enter your app name in the first field, the names must be unique so check that then name you have chosen is available on Heroku, then select your region.
- Click on **Create App**.
- Once the app is created you will see the Overview panel of the application. Now move to the **Settings** tab.
- Once you are in the **Settings** tab scroll down till you find **Config Vars**.
- Press the button **Reveal Config Vars** and for 'KEY' field, type in 'PORT' and for the value field type in '8000'.
Then press the **Add** button.
- Scroll down to **Buildpacks**. Click the button **Add buildpack** and select 'python'. Do the same step and add 'node.js'.
**PYTHON MUST BE ON TOP OF THE BUILDPACKS. IF IN YOUR CASE NODE.JS IS FIRST, CLICK AND DRAG PYTHON TO TOP AND SAVE.**
- Return back to the **Deploy** tab. From the deployment method, select 'Github' as the deployment.
- You will be asked to connect your github account. Confirm and proceed.
- Search for your repository name and connect.
- Once that is done and successfully connected, select how you want to push updates from the following options.

  _Clicking **Enable Automatic Deploys**. This will update once you push updates to your Github._

  _Selecting the correct branch for deployment from drop-down menu and pressing **Deploy Branch** button. This will have to be done everytime manually._

## Credits

[Back to Table of contents](#balen-nouri-tic-tac-toe-for-2-players)
