# Norgannon

Norgannon is a trivia bot for Discord, designed to create an engaging and fun quiz experience for users. Named after the titan Norgannon, the Lorekeeper in World of Warcraft lore, this bot asks questions about Azeroth and its rich history, testing the knowledge of its participants.

## Features

1. **Quiz Game**: The bot is capable of conducting a 5-question quiz game. It randomly picks a question, displays it in the chat, and waits for the users to answer. The first user to provide the correct answer is declared as the winner for that question. 

## Code Overview

The code for the bot is written in Python, using the `discord.py` library for interacting with Discord's API.

It employs the following environment and libraries:

- `os` and `dotenv` for handling environment variables
- `discord` and `discord.ext` for the Discord API
- `random` for random selection
- `asyncio` for managing asynchronous tasks

The bot uses a set of trivia questions stored in a dictionary, where each question has a list of valid answers. The bot can accept a valid answer in any case.

```python
quiz = {
    "Who was the last Guardian of Tirisfal?": ["Medivh"],
    "Who was the first Guardian of Tirisfal?": ["Alodi"],
    "Kalimdor translates from Titan and Darnassian to \"land of eternal ____.\"": ["starlight"],
    "The youngest World Tree, Teldrassil, was planted under the leadership of Archdruid ____.": ["Fandral Staghelm", "Fandral", "Staghelm"],
    "Name the first Lich King.": ["Ner'zhul", "Nerzhul", "Ner zhul"],
}
```

## Commands

- `!start_quiz`: This command starts the quiz. The bot will announce the beginning of the quiz, and after 2 minutes it will start posing the questions.

## Setup & Installation

1. Clone this repository to your local machine.

2. Set up a .env file in the same directory as your bot script. Add your bot token to this file:

    ```
    DISCORD_TOKEN=your-token-here
    ```

3. Install the required Python packages if you haven't done so already:

    ```
    pip install -r requirements.txt
    ```

4. Run the bot script:

    ```
    python norgannon.py
    ```

5. The bot is now ready! Use `!start_quiz` in your Discord server to begin the trivia quiz.

## Future Improvements

This is a work-in-progress, and there are numerous potential enhancements, including:

- More varied and numerous quiz questions.
- Customization options for the quiz (e.g. setting the number of questions, time limit, topics).
- Leaderboard or point system to keep track of scores over time.

Feel free to contribute to the development of this bot by submitting a pull request!

## License

This project is licensed under the terms of the MIT license.
