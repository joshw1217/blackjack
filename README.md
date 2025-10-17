# Blackjack
Welcome to a fully functional Django Blackjack game

## Features
- Player hand can be played by hitting or standing with given cards
- Dealer hand is automatically played - per Bicycle Blackjack rules
- Game is evaluated and winner is determined throughout

## Additional Features
- Player can also set a starting balance when playing for the first time
- Player can choose a bet amount each round of play
- Player can "Double Down" as their first action in a round, doubling their bet and getting one card
- NOTE: The game was initially built as a console based app, and then migrated to Django with a full web UI;
the game is intended to play on the UI, but you can pull the older commits to play the console version if desired

## Setup
1. Clone the repository
``` 
git clone https://github.com/joshw1217/blackjack.git 
cd blackjack
```
2. Make sure Django is installed (command might vary depending on how you installed python)
```
pip install django
```
3. Run migrations (database is not used but files are still present for infrastructure)
```
python3 manage.py migrate
```
4. Run the dev server
```
python3 manage.py runserver
```
5. Open link - either click the link the server is running on or paste it into your browswer

## A few notes
- I love blackjack and thought it would be fun to implement my favorite part - doubling down - which also requires
playing with a balance and live bet
- Because a balance is already made and functional, I would probably add splitting and insurance as the next (and final) features, as both rely on a live bet
- There is no live database being used, so the data is being stored in the browser's cache. Once you've set an initial balance, it will persist until you clear the cache or lose the game by going to 0. Once you hit 0 you'll be prompted to enter a new balance
- Another feature to add would be to have a button that allows you to reset your session at any time
- The deck automatically reshuffles when under 18 cards (~1/3 cards remaining, like some casinos)
- Blackjack pays the standard payout of 3:2
- You are allowed to hit even when reaching a value of 21 when it is not a natural, which I think is actually allowed but could be changed if wanted