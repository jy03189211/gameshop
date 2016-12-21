# Project plan
----
## Team

464989 Jin Jin
84143N Eppu Halmesaari
240938 Roope Palomäki

----
## Goal

In this project, our goal is to make a game store for game developers to offer their games for sale and for players to buy those games. In addition, the games can be playable in an iframe element in the same store. The game store offers multiple different games and in our case the games are different versions of the same game that resembles flappy bird. What makes these games different from each other are the small details such as the changing player icon, background, degree of difficulty and possible control keys.

Generally, our goal is to implement all features mentioned on the project description page in A+, including the mandatory features and those mentioned in the "More Features" section.

### Features
- Authentication

	- A user will be able to register both as a developer or a player. Email validation will be integrated as a sub-feature. A user will be able to login and logout with their registered account. (Django authentication)

	- A user will be able to login and logout using their Gmail or Facebook ID.(third pary api)

- Player

	- A player will be able to buy games (mockup payment) by adding a game to the shopping basket and checkout.
	- A player can play the game they bought. (sample game such as flappy bird will be used for demo)
	- A player is resticted to play the games only from their library (a list of games they bought).
	- A user can search game by name.

- Developer
	- A developer can submit his game by providing an URL and set up a price for it and remove it from the store. 
	- Each developer has his own inventory and sales statistics. A developer can modify their inventory by adding or removing games from it.
	- A developer can only add games to their own inventory.

- Game/service interaction
	- When player has finished playing a game (or presses submit score), the game sends a postMessage to the parent window containing the current score. The score will be recorded to that player's scores and golobal top score
	- When a saved gamed state is detected for a player, the service will send a message to the game so the state will be loaded.

- Mobile Friendly 
	- the website works with devices with varying screen width and is usable with touch based devices 
- Social media sharing
	- share games and player's score on facebook with a sensible description and an image
		
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
    - Implementing social media sharing feature for Facebook

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
    - Define test cases
    - Continue with our own parts and set a meeting to check our progress
    - Implement game and its variations
    - Add save/load feature
    - At the end of week 4, all the basic functions should be ready

- Weeks 5-6:
    - Meeting to check progress
    - Enhancing responsiveness of the app
    - Implementing social media sharing (metadata)

- Weeks 7-8:
    - Testing and polishing

Communication between team members is handled mainly through Slack.

----
## Testing

To test the application we will do both systematic testing based on test cases as well as free form testing by using the service randomly as a normal user would. For this, we will define a list of test cases in the early phase of the project based on the expected features, and will test through the cases at the time of finishing development of the relevant features. In addition, we will have a User Acceptance Test at the time of completing development of the features, although the UAT will be performed by ourselves.

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
