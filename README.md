# 🤖 Telegram Bot — Restaurant Search

🌐 **Documentation Languages**

🇬🇧 **English** | 🇷🇺 [Русский](README.ru.md) | 🇷🇴 [Română](README.ro.md)

## 📖 Overview

Telegram Bot — Restaurant Search is a Python-based Telegram bot that helps users discover restaurants based on cuisine types and food preferences.

Users can search for restaurants, view restaurant information, and access their previous search queries.

The application was developed as an educational diploma project in Python, demonstrating practical experience with Telegram Bot API integration, asynchronous command handling, database operations, and user interaction.

## ✨ Features

- 🔍 Search restaurants by cuisine type or keywords
- 🍣 Search for sushi, pizza, and other food categories
- 🏠 Display restaurant names, addresses, and available photos
- 📜 Save user search history
- 🗂️ View previous search queries
- 🤖 Handle Telegram commands and user interactions
- 👋 Display welcome messages and help information

## 📖 Available Commands

| Command | Description |
|---|---|
| `/start` | Start the bot and display a welcome message |
| `/help` | Show available commands |
| `/find <cuisine>` | Search restaurants by cuisine type |
| `/history` | Display recent search queries |

### Usage Examples

```text
/start
/help
/find sushi
/find pizza
/history
```

## 🛠 Technology Stack

- **Programming Language:** Python
- **Telegram Integration:** Aiogram
- **Database:** SQLite
- **ORM:** Peewee
- **HTTP Requests:** Requests
- **Version Control:** Git, GitHub

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PhilipTataroii/Telegram-Bot-Search-Restaurant.git
cd Telegram-Bot-Search-Restaurant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate on Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Telegram Bot Token

Open the configuration file:

`Token_and_Database/config.py`

Set your Telegram bot token:

```python
BOT_TOKEN = "your_bot_token"
```

Obtain a bot token through Telegram's official @BotFather.

**Security:** Never commit a real bot token to a public repository. Use environment variables or a local configuration file excluded from Git for production use.

### 5. Run the Bot

```bash
python Start_Bot/bot.py
```

## 🔎 Testing the Bot

After launching the application, open your bot in Telegram and execute:

| Command | Expected Behavior |
|---|---|
| `/start` | Displays a welcome message |
| `/help` | Shows the command list |
| `/find sushi` | Searches for sushi restaurants |
| `/find pizza` | Searches for pizza restaurants |
| `/history` | Displays previous search queries |

The bot must be running locally for commands to work.

## 📂 Project Structure

```text
Telegram-Bot-Search-Restaurant/
├── Handlers_Bot/
│   ├── start.py
│   ├── help.py
│   ├── find.py
│   └── history.py
├── Start_Bot/
│   └── bot.py
├── Token_and_Database/
│   └── config.py
├── requirements.txt
├── README.md
├── README.ru.md
└── README.ro.md
```

## 🗄️ Database

The application uses SQLite for storing user search history.

Peewee ORM provides database interaction and simplifies data management.

## 📝 Development Notes

This project was developed for educational and portfolio purposes.

The Telegram bot runs locally and requires an active Python process to respond to messages.

For continuous availability, the application can be deployed to a server with the appropriate configuration.

## 👨‍💻 Author

**Filip Tataroi**

Python Developer

GitHub: https://github.com/PhilipTataroii

LinkedIn: https://www.linkedin.com/in/filip-tataroi/

**Project Type:** Educational Python Diploma Project
