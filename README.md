# discord-poll-bot

A bot to poll on Discord and save the entries to a database. Currently developed only for the Atlas Discord server in preparation for their launch. Eventually I plan to make this scalable to create polls dynamically.


Instructions for running the code:

1. Clone the git repository.
2. Remove C:\sqlite\library.db file and pycache folder (this deletes the db so you can start fresh).
3. Run:
      python3 config.py (ONLY RUN THIS ONCE)
4. Run:
      python3 main.py (leave this running, the bot will wait for input)

If you need to restart the bot, just run python3 main.py again, no need to run config.py again after initial db creation.


This bot will lock the user out of the channel after they vote in order to prevent re-casting votes. It's the only way that I was able to accomplish this, because I was unable to store the user id reliably.
