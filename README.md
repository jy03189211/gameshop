# Project plan
----
## Team

464989 Jin Jin
84143N Eppu Halmesaari
240938 Roope Palomäki

----
## Goal

In this project, our goal is to make a game store for game developers to offer their games for sale and for players to buy those games. In addition, the games can be playable in an iframe element in the same store. The game store offers multiple different games and in our case the games are different versions of the same game that resembles flappy bird. What makes these games different from each other are the small details such as the changing player icon, background, degree of difficulty and possible control keys.

### Features

### Additional features

- Save/load and resolution feature
    - IFrame passes information to its parent in JSON, which is parsed and added to the database.
- 3rd party login
    - Our plan is to implement Google login provided by the Django social authentication mechanism.
- RESTful API
- Own game
    - A game similar to flappy bird which has different variations, so-called "games", in our store.
- Responsiveness
    - In addition to using Bootstrap, we will make needed adjustments to styling to make app fully responsive.
- Social media sharing
    -

![Draft of the game design](https://git.niksula.hut.fi/palomar1/csc3170/raw/master/plan/game_screenshot.png)

----
##  Schedule and communication

Our development process is divided into a period of 8 weeks. The schedule for those 8 weeks, which starts after Christmas, is as follows:

- Weeks 1-2:
    - Finalize schemas, layout sketches and other initial design
    - Set up our Django app
    - Create a skeleton site with placeholders for views
    - Build basic models and create sample data
    - Implementing login feature and 3rd party
    - Deploy and test the Heroku environment
    - Divide work

- Weeks 3-4:
    - Continue with our own parts and set a meeting to check our progress
    - Implement game and its variations
    - Add save/load feature
    - At the end of week 4, all the basic functions should be ready

- Weeks 5-6:
    - Enhancing responsiveness of the app
    -

- Weeks 7-8:
    - Testing and finalizing

Communication between team members is handled mainly through Slack.

----
## Views

![views](https://git.niksula.hut.fi/palomar1/csc3170/raw/master/plan/views.png)

The site has the following views:

- Landing

  Featured games, suggestions, etc.

- Register

  Register a new user by making a new user or using e.g. Facebook account

- Login

  Login to the service

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
## Models

![models](https://git.niksula.hut.fi/palomar1/csc3170/raw/master/plan/models.png)

The backend includes the following object models:

- User

  Represents a user of the system. All users are players, but also developers. This model extends the default Django User model which already includes the basic authentication-related things, and the naming of this model is also thus likely to change a bit to not conflict with Django.

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

----
## API endpoints

Everything below is prefixed with `/api/v1` and the endpoints requiring authorization will use token-based authentication.

Optional parts of paths or parameters denoted with `[]`.

### Primarily user-related endpoints

`GET /user/[:userid][?q=...]`

  Users. Possible query filter `isDeveloper`.

`GET /user/:userid/inventory/[:gameid]`

  Games the user has added

`POST /user/:userid/inventory`

  Add a new game or update an existing game. (Game ID not known before creation.)

`GET /user/:userid/puchased/[:gameid]`

  The user's purchased games

`GET /user/:userid/sale/[:saleid][?q=...]`

  The sale history of the user's added games. Possible query filters `gameid`, `year`, `month`, `day`.

`GET /user/:userid/order/[:orderid][?q=...]`

  The order history of the user Possible query filters `gameid`, `year`, `month`, `day`.

`GET /user/:userid/savegame/[/:gameid][/:savegameid][?q=...]`

  The savegames of the user. Possible query filters `gameid`, `year`, `month`, `day`.

`POST /user/:userid/savegame/`

  Add a new savegame

`GET /user/:userid/score[?q=...]`

  The user's high scores. Possible query filter `gameid`.

### Primarily game-related endpoints

`GET /game/[:gameid][?q=...]`

  Games. Possible query filters `createdBy`, `priceMin`, `priceMax`, `available`, `category`, `year`, `month`, `day`.

`GET /game/:gameid/score/`

  High scores for the game
