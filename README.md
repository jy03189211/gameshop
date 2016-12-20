# Project plan (NOTE: Draft)
----
## Team

464989 Jin Jin
84143N Eppu Halmesaari
240938 Roope Palomäki

## Goal

In this project, our goal is to make a game store for game developers to offer their games for sale and for players to buy those games. In addition, the games can be playable in an iframe element in the same store. The game store offers multiple different games and in our case the games are different versions of the same game that resembles flappy bird. What makes these games different from each other are the small details such as the changing player icon, background, degree of difficulty and possible control keys.

### Additional features

- Save/load and resolution feature
- 3rd party login
- RESTful API
- Own game
- Responsiveness
- Social media sharing

![Draft of the game design](https://git.niksula.hut.fi/palomar1/csc3170/raw/master/plan/game_screenshot.png)

----

##  Schedule and communication (started by Eppu, in progress...)

Our development process is divided into a period of 8 weeks. The schedule for those 8 weeks, which starts after Christmas, is as follows:

- Weeks 1-2:
    - Finalize schemas, layout sketches and other initial design.
    - Divide work.
    - Set and test Heroku environment(?)

- Weeks 3-4:
    -

- Weeks 5-6:

- Weeks 7-8:
    - Testing

Communication between team members is handled mainly through Slack.


## Process

### Views

![views](https://git.niksula.hut.fi/palomar1/csc3170/raw/master/plan/views.png)

The site has the following views:

- Landing

  Featured games, suggestions, etc.

- Search

  Search based on game properties, e.g. price, category

- Categories

  A list of game categories

- Game (buy)

  The details page for an individual game in the store

- Basket

  The shopping basket

- Checkout

  The order complete / checkout page

- Login

  User login

- User (dashboard)

  The main page for a user

- User (settings)

  The user's settings for profile, password change, etc.

- User (inventory)

  A list of games added by a developer, for developers

- User (new game)

  Inserting the information for a new game, for developers

- User (sales) (dev only)

  Sales history and statistics, for developers

- User (purchased games)

  A list of the user's purchased / owned games

- User (orders)

  Order / purchase history

- User (savegames)

  A list of all of the user's saved games

- Game (play)

  Where the game is played

- Leaderboards

  A summary page for all games' high scores


----
### Models

![models](https://git.niksula.hut.fi/palomar1/csc3170/raw/master/plan/models.png)

The backend includes the following object models:

- User

  Represents a user of the system. All users are players, but also developers.

- Game

  Represents a game in the system. Added by a developer.

- Score

  Represents a high score result. Is created based on the information sent by the game when played.

- Order

  Represents a purchase of one or more games in a single transaction. A collection of Purchases.

- Purchase

  Represents a purchase of a single game.

- Savegame

  Represents a saved game state. Is created based on the information sent by the game when played. Can contain any data as determined by the game.
