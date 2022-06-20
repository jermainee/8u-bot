# 8u.com Bot
Tooling that automates your betting interactions on 8u.com implemented in Python using the Selenium module.
<p>
    <a href="https://github.com/SeleniumHQ/selenium">
      <img src="https://img.shields.io/badge/built%20with-Selenium-yellow.svg" />
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
</p>

## Installation
Execute `sudo ./install.sh` in your command line interface.

Or install the following packages manually:

- [Python3](https://www.python.org/download/releases/)
- [Selenium](https://pypi.org/project/selenium/)
- [Selenium Requests](https://pypi.org/project/selenium-requests/)
- [Firefox](https://www.mozilla.org/de/firefox/download/thanks/)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

### Starting the bot (cli)
```
python3 main.py
```
or double click on `main.py`

### Stopping the bot
To stop the bot, simply press `CTRL + C` in the cli window.

## GUI Settings
### Credentials
Enter your 8u.com user credentials, with which the bot logs into your account.

### Settings

| Tables   |      Are      |
|----------|:-------------:|
| game_name | Game identifier of 8u.com, which can be found in the url of the game |
| minutes | Number of minutes of one game round |
| history_length | Number of past games to be used to calculate the score |
| initial_bet_amount | Amount of the first bet placed as decimal number, e.g. 0.50 |
| loss_multiplicator | Number with which the initial_bet_amount is to be multiplied in case of a loss |
| low_threshold | First lowest threshold from which score a bet should be placed, e.g. -10 |
| low_bet_type | Bet type which should be set when the low_threshold is reached, e.g. "big" |
| high_threshold | First highest threshold from which score a bet should be placed, e.g. 10 |
| high_bet_type | Bet type which should be set when the high_threshold is reached, e.g. "small" |