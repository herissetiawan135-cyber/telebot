# Telegram Font Changer Bot

A simple Telegram bot that converts your text into various fancy styles (Bold, Italic, Cursive, etc.). Built with Python and Pyrogram.

## Features

- **Text Conversion**: Send any text to get multiple styled versions.
- **Inline Mode**: Use `@YourBotName text` in any chat.
- **Click to Copy**: Inline buttons to easily get specific styles.

## Prerequisites

- Python 3.10+
- A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- API ID & Hash (from [my.telegram.org](https://my.telegram.org))

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuration**:
   - Rename `.env.example` to `.env` or create a new `.env` file.
   - Fill in your `API_ID`, `API_HASH`, and `BOT_TOKEN`.

   ```env
   API_ID=123456
   API_HASH=your_api_hash
   BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
   ```

3. **Run the Bot**:
   ```bash
   python bot.py
   ```

## Usage

- Start the bot with `/start`.
- Send any text to receive styled responses.
- Use `/fonts` to see all available styles.

## Credits

- **Developer**: [MUFAZ-VK](https://github.com/MUFAZ-VK)
