# Final submission
## Team
- 464989 Jin Jin
- 84143N Eppu Halmesaari
- 240938 Roope Palomäki

## Work division
- While the commit statistics in the repository give an indication of the
    workload division, the amount of research/learning done for the features
    varies, which is not always shown in the commits. Thus, we have also listed
    below in the "Implented features" section who implemented which feature.
- (Commit statistics in GitLab -> Graphs -> Contributors)

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
- Views are protected and restricted where needed by utilizing Django
    decorators such as `@login_required`
- **Points given to self: 200/200**
- **Implemented by: Jin, Roope**

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
- **Implemented by: Roope**

#### Basic developer functionalities
- All basic functionalities listed have been implemented
- Games can be added and managed at the "Your games and profile" section where
	the relevant developer options are available for users who are developers
  - Note 1: since Google Chrome does not allow insecure resources inside secure
    HTTPS pages, and our game shop is secured with HTTPS, games will only load
    properly if they are added using an HTTPS URL.
	- Note 2: Due to Note 1 we also copied the provided example game to be served
		from the static files in our project to serve it over HTTPS as well.
- Managed games and sales statistics can also be seen at the "Your games and
	profile" section
	- Sales lists and statistics can be seen for all games or for a single game
- Games have an image that is shown in various places in the store. The image is
	stored in the database as binary data (in Base64) and is injected into
  the `img` tags, but can also be requested with by adding `/image/` to the game
  URL, e.g. `example.com/game/1/image/`
- Developers can have a public name that is shown instead of the username in the
	game information in various places in the store. Defaults to the username, and
	can be changed during registration or in the settings.
- **Points given to self: 200/200**
- **Implemented by: Roope**

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
- **Implemented by: Roope**

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
- About the folder structure
	- The project directory structure seems to include nested apps as the
		"message_service" and "storeutils" folders are inside the "gameshop" folder,
		but the purpose of the message service and store utilities is such that they
		are only meant to be used inside the "gameshop" app, and would not work
		outside. Thus, we have included them in such a nested way since they are
		essentially helpers that are merely separated to improve modularity
		and separation of concerns.
	- Based on the discussion in Piazza, we recognize that our project structure
		is slightly unorthodox and for example the project name is the same as the
		main app name ("gameshop"). However, since really only learned this
		unusuality some half a day before the deadline, we did not risk breaking the
		project by changing the project name as the current structure works as well.
- **Points given to self: 95/100**
	- project structure not perfect
- **Layout and styles implemented by: Roope**

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
- **Implemented by: Roope**

#### 3rd party login
- Facebook login implemented using Django third party app, allauth as the social login solution
- **Points given to self: 100/100**
- **Implemented by: Jin**

#### RESTful API
- RESTful API implemented with a variety of endpoints (listed in below)
- The API also utilizes an API key system to authorize every request
	- A user is generated an API key at registration time, and that key/token
		must be given in the GET/POST data of every request in the `api_key`
		attribute
- In addition, developers can restrict the domains where requests are allowed
	from with their API key, can be changed in the profile settings
- **Points given to self: 90/100**
  - Authorization/Authentication could be more specific, etc. different rights for different API keys
- **Implemented by: Eppu**

#### Own game
- We implemented a "Flappy Bird" copy where the player tries to guide the bird
 	between approaching pipes as far as possible, and every passed pipe gives
	a point
	- The game automatically submits the score at game over if the player
		has at least one point
	- When the game is not running (i.e. at game load or game over when there is
		a message on top of the game), the player can save the current score to the
		service by pressing "S", or load the current savegame (i.e. points) from the
		service by pressing "L"
- The game is located in the "static" folder for serving it with the store. The
	message tester is also in the same folder.
- **Points given to self: 100/100**
- **Implemented by: Roope**

#### Mobile-friendly
- Mobile layout implemented with Bootstrap and custom media queries where
	applicable
- The main navigation adapts by collapsing
- Optional game scaling implemented so that games can be played more comfortably
	on a mobile screen
- **Points given to self: 50/50**
- **Implemented by: Roope**

#### Social media sharing
- Facebook sharing implemented
- On the game page above the game frame
- **Points given to self: 50/50**
- **Implemented by: Jin**

#### Deployment
- Project deployed to Heroku (at https://boiling-gorge-94597.herokuapp.com/)
- **Implemented by: Eppu**

## Successes and failures
- We somewhat fully succeeded in our plan of implementing all the features in
	the project description
- Being new to Django, everything too quite a while in the beginning and the
	actual schedule was thus slightly lagging behind, but we still managed to get
	everything done well in time
- Managed to create the project by communicating only through Slack

## Instructions
- Application available at: https://boiling-gorge-94597.herokuapp.com/

##### Test accounts
- There are 4 pre-created test accounts that can be used for testing the store
- 2 normal players
	- username: user1, password: testuser1
	- username: user2, password: testuser2
- 2 developers
	- username: user3, password: testuser3
	- username: user4, password: testuser4

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
- About our own game "Flappy"
    - Pressing the space key or left clicking the mouse starts the game and
        makes the bird flap to guide it through the pipes
    - When the game is not started yet or in the game over state (i.e. when
        there is text over the game), pressing "S" will save the current score
        to the service, and pressing "L" will load the saved points from
        the service
    - The score is automatically submitted to the service at game over,
        assuming that the score that would be sent is over 0
- API endpoints are at the end of this document



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
