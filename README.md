# WonderBot
**WonderBot** is a simple telegram bot created using the *Python-telegram-bot* library.

## Features
* Get your Github Repositories and Starred Repositories.
* Get the live news feed.
* Get the Weather Forecast of your area.
* Get the Cubing events of your area.

I know its features are a bit weird, this is because i have integrated some of my already made python-scripts as the features of the bot. You can check them out [here](https://github.com/Ugtan/python-scripts)

## Installation and Usage
* Clone this repository using the below command in the terminal:
`git clone https://github.com/ugtan/WonderBot`
* Once you have successfully cloned the repository then,
`Run pip install -r requirements.txt`
* Now also you won't be able to use the bot till you have your token. For bot token just follow the [steps](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)
* After that just put your token in line 99 of WonderBot.py
* Now you are ready to rock just run the bot using the `python3 WonderBot.py`

**Note:**
 So, Bots can't initiate chat on their own so you have to start the bot using the `/start` command.
 These are some of the commands you can use to handle the bot:
 `/hello - greetings from the bot! :)
/github <username> - To know about your github Repos and Starred repos.
/news - To get some live news feed.
/weather - To get the weather forecast of your area.
/cubicom - To get the upcoming cubing events in your area.
/help - To show the list of commands.`
