# Balen Nouri Tic-Tac-Toe Multiplayer

Three in a row or tic tac toe, everyone has played this game, maybe in school with paper and pen or on a real board.  For those who don’t know about the game, it’s a classic old game with 3 x 3 boxes for two players. One will play with the X and the other one with the O and the one who gets three in a row will win. So, if you and your friend want to challenge each other and wake up old memories from the classic game, click on the link below.

[A live version of the website and the project can be accessed here:](https://balen-nouri-tic-tac-toe-5377b5105884.herokuapp.com/)

![Ami Responsive](assets/readme/amiresponsive.png)

## Table of Contents

- [Balen Nouri Tic-Tac-Toe Multiplayer](#balen-nouri-tic-tac-toe-multiplayer)
  - [Table of Contents](#table-of-contents)
  - [User Experience Design](#user-experience-design)
    - [User Demographic](#user-demographic)
    - [User stories](#user-stories)
  - [How To Play](#how-to-play)
  - [Features](#features)
    - [Game](#game)
    - [Social Media Section](#social-media-section)
    - [Future Feature](#future-feature)
  - [Data Model](#data-model)
  - [Flowchart](#flowchart)
  - [Languages Used](#languages-used)
  - [Technologies Used](#technologies-used)
  - [Libraries used](#libraries-used)
  - [Testing and Validation](#testing-and-validation)
    - [Validators](#validators)
      - [Python](#python)
      - [HTML](#html)
      - [CSS](#css)
    - [Manual testing](#manual-testing)
    - [Known Bugs](#known-bugs)
      - [Resolved](#resolved)
      - [Python Warnings and Bugs](#python-warnings-and-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
    - [Content And Code](#content-and-code)
    - [Acknowledgements](#acknowledgements)

## User Experience Design

### User Demographic

This website is meant for:

- Users who want to play a game with a friend
- User who loves old games.
- User who wants to learn an easy game to play.

### User stories

As a user of this website:

- To play a game against a friend.
- Be able to read the rules and the meaning of the game.
- Be able to play again or quit the game when the game is finished.

## How To Play

Tic-tac-toe is a game in which two players take turns in drawing, either an 'O' or an 'X' in one square of a grid, consisting of nine squares. The winner is the first player to get three of the same symbols in a row, vertically, horizontally or diagonally.

## Features

- The game is easy to play and doesn’t need any special configurations.
- When the user comes into the game, they are welcomed and can choose between some options.
- If the user enters an invalid input, the user will get the chance to re-enter a command until it’s valid.

### Game

Screenshots from the game:

- Welcome page for the users(start menu).
- Asks both of the users for their names.
- Asks the users if they want to play, read the rules or quit the game.

![Multiplayer](assets/readme/meny.png)

Rules for the game:

- Explain the game and the rules for Tic Tac Toe.

![Rules](assets/readme/meny-rules.png)

How the game board looks like:

- In the game, users get a reference board and the game board.
- When the first player chooses a spot, the terminal clears everything and shows the first player's move.
- When the second player chooses a spot, the terminal clears everything as well and then shows the new board.

![Gameboard](assets/readme/game-board.png)

When the game is done:

- When the game is done, whether it's a draw or a winner. The users get asked if they want to play again.

![Play Again](assets/readme/meny-third.png)

### Social Media Section

![footer](assets/readme/footer.png)

- Underneath the terminal the user will see my social media accounts.
- There are three social media icons. Instagram, GitHub and LinkedIn.
- When the user click on one of the icons it will open in a new tab.

### Future Feature

Features to be added in the future:

- Be able to play single player.
- Be able to see scoreboard.
- Be able to choose an own sign instead of X or O.
- Put in some color to the game.

## Data Model

I choose to use global variables for the game and different functions that give the users the ability to play the game and be able to choose different options throughout the game.

Some important function is the display_board() shows how the game board will look, the have the play_game() that make the game playable.

All of the functions later go through the main() function, so the users can start a new match or quit the game.

## Flowchart

A flowchart describing the logic behind this application has been created using [Lucidchart.](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433237648&km_CPC_TargetID=kwd-33511936169&km_CPC_Country=21003&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=Cj0KCQiAhc-sBhCEARIsAOVwHuS-QAiBPSXj3yOMy75khyNm4_a4nkKCQMtc0JOHhSl6XZthZn-xZxoaAioqEALw_wcB) It served as a guideline when the actual game was coded.

![Lucid Chart](assets/readme/lucid-chart-2.png)

## Languages Used

- Python

## Technologies Used

- Visual Studio Code to write the code and pushing to Github.
- Github was used to store and create the repository.
- Heroku was used to deploy the project.

## Libraries used

- Os to create a clear_reset_screen(), which clears the screens so there's not so much clutter on the page.

## Testing and Validation

### Validators

#### Python

- [Code Institute Python linter](https://pep8ci.herokuapp.com/#) was used to validate my project to se if there were any Python errors.

![Py test](assets/readme/test-py.png)

#### HTML

- [Validator.w3](https://validator.w3.org/nu/) was used to test both of the HTML files to see if there were any errors.

index.html

![index test](assets/readme/index.test.png)

layout.html

![layout test](assets/readme/index.test.png)

#### CSS

- [Jigsaw.w3](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fbalen-nouri-tic-tac-toe-5377b5105884.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv) Was used to test my CSS part on the website to see if there was any errors.

![CSS TEST](assets/readme/css-test.png)

### Manual testing

I have tested the website on different browsers and didn't find any bugs or errors on it.

### Known Bugs

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

No unfixed bugs.

## Deployment

### Heroku Deployment

To deploy this page to Heroku from its GitHub repository the following steps were taken:

- Log into or register a new account at [Heroku](https://www.heroku.com/).
- Click on the button New in the top right corner of the dashboard.
- From the drop-down menu then select Create new app.
- Enter your app name in the first field, the names must be unique so check that the name you have chosen is available on Heroku, then select your region.
- Click on Create App.
- Set the buildbacks to python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on Deploy.

[A live version of the website and the project can be accessed here:](https://balen-nouri-tic-tac-toe-5377b5105884.herokuapp.com/)

## Credits

### Content And Code

To style the page and the content to Read me:

- The screenshot at the top of the ReadMe was built from [Ami Responsive.](https://ui.dev/amiresponsive)
- The information about the game in the readme is taken from [wikipedia.](https://sv.wikipedia.org/wiki/Tre_i_rad)
- The flowchart in readme was made by [Lucidchart.](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433237648&km_CPC_TargetID=kwd-33511936169&km_CPC_Country=21003&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=Cj0KCQiAhc-sBhCEARIsAOVwHuS-QAiBPSXj3yOMy75khyNm4_a4nkKCQMtc0JOHhSl6XZthZn-xZxoaAioqEALw_wcB)
- The code for clear_reset_screen() function was taken from [Coding4you.](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf)
- The favicon code was taken from my second project that was inspired by the Love Running project in the beginning.

To write the code for HTML and Python:

- [Code institute LMS](https://learn.codeinstitute.net/dashboard)
- [W3Schools](https://www.w3schools.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)
- [Coding 4 You](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf)

### Acknowledgements

This site was developed as my Third portfolio project for the Code Institute course in Full Stack Software Development. I would like to thank my mentor David Bowers, the slack community and the Code Institute team.

[Back to Table of contents](#balen-nouri-tic-tac-toe-multiplayer)
