# 🤖 Telegram Bot – Search Restaurant

🍽️ This bot helps users find restaurants by cuisine type (e.g., 🍣 sushi, 🍕 pizza) and saves the search history.  
🎓 Created as a Python diploma project, it demonstrates:  
- 🔗 Integration with Telegram API  
- 🗄️ SQLite database via Peewee ORM  
- ⚙️ Command handling and user interaction  

---

## ✨ Features
- 🔍 Search restaurants by keywords (e.g., `/find sushi`)  
- 🏠 Display restaurant name, address, and photo  
- 📜 Save user search history  
- 📂 View recent queries with `/history`  
- ❓ Help menu with `/help`  
- 👋 Welcome message with `/start`  

---

## 📖 Commands
- `/start` — Welcome message and bot description 🤖  
- `/help` — List of all available commands 📖  
- `/find <cuisine>` — Search restaurant by cuisine type (e.g., `/find pizza`) 🍕  
- `/history` — Show recent user queries 🗂️  

---

## 🚀 Installation & Run

## 1. Clone the project
   ```bash
   git clone https://github.com/yourusername/Telegram-Bot-Search-Restaurant.git
   cd Telegram-Bot-Search-Restaurant
   ```

 ## 2.Activate virtual environment
 **Windows:**
   ```bash
   .venv\Scripts\activate
   ```

 **Linux/Mac:**
   ```bash
   source .venv/bin/activate
   ```

## 3.Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Libraries used:
- 🤖 Aiogram — Telegram API
- 🗄️ Peewee ORM — SQLite database
- 🌐 Requests — HTTP requests

  ---

## 4. Configure token
**In Token_and_Database/config.py set your bot token:**
## python
   ```bash
   BOT_TOKEN = "your_bot_token"
   ```

## 5. Run the bot
   ```bash
   python Start_Bot/bot.py
   ```

## 🔎 How to Test
- /start → Bot sends greeting 👋
- /help → Bot shows all commands 📖
- /find sushi → Bot returns restaurant 🍣
- /history → Bot shows recent queries 🗂️

---

## 📂 Project Structure
**Код**
 **📦 Telegram-Bot-Search-Restaurant**
 ```
 ┣ 📂 Handlers_Bot/         # Command handlers (start.py, help.py, find.py, history.py)
 ┣ 📂 Start_Bot/            # Main bot script (bot.py)
 ┣ 📂 Token_and_Database/   # Config: token, database, date format
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 README.md             # Instructions
 ┗ 📂 .venv/                # Virtual environment
```

## 🛠 Technologies
- 🐍 Python
- 🤖 Aiogram (Telegram API)
- 🗄️ Peewee ORM (SQLite)
- 💾 SQLite

---

## 👩‍💻 Author
## Filip — Diploma project in Python 🎓🐍
