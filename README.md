# Final submission
## Team

464989 Jin Jin
84143N Eppu Halmesaari
240938 Roope Palomäki

## Implemented features

#### Authentication
- We implemented all requirements in the project description
- Uses Django auth
- Extends the Django `User` model with the `AbstractUser` class
- The email activation message that would be sent for completing registration
	is logged into the backend Django console
- A user account can be only a player or both a player and a developer. This is
	indicated by the `is_developer` field in the `User` model. A user can choose
	this at the time of registration, but can also become a developer later in the
	profile settings (which is under "Your games and profile").
- Users can also change their password in the profile settings
- **Points given to self: 200/200**

#### Basic player functionalities
- All basic functionalities listed have been implemented and payments are handled
	through the payment service
- Games are played on the game's store page but are only loaded and shown if the
	logged-in user owns the game
- All owned games can be seen under the "Your games and profile" page
- Users can find games through the "Search" page and the "Categories" page
- The store landing page shows featured games (which are simply the most
	recently added games)
- The checkout process handles free games separately without the payment service
- Extra features implemented:
	- The game frame can optionally be scaled to fit the screen, which allows for
	 	a much better experience for smaller screen sizes
- **Points given to self: 300/300**

#### Basic developer functionalities
- All basic functionalities listed have been implemented
- Games can be added and managed at the "Your games and profile" section where
	the relevant developer options are available for users who are developers
- Managed games and sales statistics can also be seen at the "Your games and
	profile" section
	- Sales lists and statistics can be seen for all games or for a single game
- Games have an image that is shown in various places in the store. The image is
	stored in the database as binary data and is injected into the `img` tags,
	but can also be requested with by adding `/image/` to the game URL,
	e.g. `example.com/game/1/image/`
- Developers can have a public name that is shown instead of the username in the
	game information in various places in the store. Defaults to the username, and
	can be changed during registration or in the settings.
- **Points given to self: 200/200**

#### Game/service interaction
- We implemented all 6 message types as described in the project description
- The Django backend has the message service helpers in the `message_service`
	folder, and the client side is implemented in `static/js/message.js`
- Scores are recorded and shown under the actual game on the game page
	- Scores are stored with the `Score` model, and per-game lists for global
		leaderboards and per-user highscores are compiled in the game page view
	- New scores are shown after a page reload
- We also implemented a message tester that demonstrates the resolution changing
	and other messages. It can be found with the name "Message tester" in the
	demo store. (Score and savegame data hardcoded in the tester)
	- Shows incoming messages
- **Points given to self: 195/200**
	- highscores only showing after page reload

#### Quality of work
- Code commented where needed for understanding, while the aim is for the code
	to be understandable through variable naming etc.
- Used plenty of the available Django features and shortcuts for DRY
- The site _layout_ builds on Bootstrap 3, i.e. mostly the grid system
	- Visual style almost fully hand-built
	- The base styles are in `base.sass` which is compiled to a minified
		`base.min.css`
	- `theme.sass` defines a visual theme on top of the base styles, and is
		compiled to `theme.min.css`
	- The theme could be easily changed with theme CSS files without doing
		damage in the base layout file
	- (SASS compiled to CSS every time the files are saved by a handy editor
		plugin)
- **Points given to self: 100/100**

#### Non-functional requirements
- Git used extensively throughout the project

#### Save/load and resolution feature
- SAVE, LOAD, and SETTING messages are supported as described in the project
	description
- Resolution is clamped to [(150x150), (1024x768)] for sensible limits
	- (can be tested easily with the "Message tester")
- In addition to the resolution, we also implemented a scaling feature that is
	useful especially for smaller screens
	- (used with the "Toggle scaling" button above the game frame)
- **Points given to self: 100/100**


#### 3rd party login
- Facebook login implemented
- **Points given to self: ???/100**

#### RESTful API
- RESTful API implemented with a variety of endpoints
- ???
- The API also utilizes an API key system to authenticate every requested
	- A user is generated an API key at registration time, and that key/token
		must be given in the POST data of every request in the `api_key`
		attribute
- In addition, developers can restrict the domains where requests are allowed
	from with their API key, can be changed in the profile settings
- **Points given to self: ???/100**

#### 3rd party login
- ???
- **Points given to self: ???/100**

#### Own game
- We implemented a "Flappy Bird" copy where the player tries to guide the bird
 	between approaching pipes as far as possible, and every passed pipe gives
	a point
	- The game automatically submits the score when at "game over" if the player
		has at least one point
- **Points given to self: 60/100**
	- The game does not use the SAVE and LOAD messages, due to the realization
		that the "Flappy Bird" concept does not really support the whole concept
		of saving and loading since it is an endless runner

#### Mobile-friendly
- Mobile layout implemented with Bootstrap and custom media queries where
	applicable
- The main navigation adapts by collapsing
- Optional game scaling implemented so that games can be played more comfortably
	on a mobile screen
- **Points given to self: 50/50**

#### Social media sharing
- Facebook sharing implemented
- On the game page above the game frame
- **Points given to self: ???/50**

## Successes and failures
- We somewhat fully succeeded in our plan of implementing all the features in
	the project description

## Work division
- ???

## Instructions
- Application available at: https://boiling-gorge-94597.herokuapp.com/

##### Test accounts
- There are 4 pre-created test accounts that can be used for testing the store
- 2 normal players
	- ???
	- ???
- 2 developers
	- ???
	- ???

##### General instructions
- Login and registration happen on the "Login/Register" page that can be
	accessed with the link at the top-right corner
	- Registration requires account activation through the link that is in the
		email sent to the newly registered user (and that is printed in the
		backend console)
- Games can be added to the cart at the game's page that can be accessed
	with the "Buy and Play" and "Play" links wherever the game is listed in
	the store
	- Look for games with the "Search" and "Categories" pages
- The cart can be accessed with the cart icon at the top-right corner
- Pressing "Checkout" at the cart page will start the checkout process
	- Checkout for free games bypasses the payment service
- Once a user owns a game, the actual game appears on the game's page
- The "Your games and profile" section shows all owned games and orders
	as well as managed games (called "inventory" in the project description) and
	sales for developers
- Developers can add new games in the "Your games and profile" section
- Users who are not developers can become developers in the "Settings" page
	under "Your games and profile"
- Sales can be viewed for all games or per game using the dropdown at the top
	of the "Sales" page


---
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

	- A user will be able to register both as a developer or a player. Every user is a player, but in addition a user can be a developer. This allows developers to play games also. Email validation will be integrated as a sub-feature. A user will be able to login and logout with their registered account. (Django authentication)

	- A user will be able to login and logout using their Gmail or Facebook ID.(third pary api)

- Player

	- A player will be able to buy games (mockup payment) by adding a game to the shopping basket and checkout.
	- A player can play the game they bought. (sample game such as flappy bird will be used for demo)
	- A player is restricted to play the games only from their library (a list of games they bought).
	- A user can search games by the games' properties such as name, category, or price.

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
