

---

# 🤖 Remote Laptop Control (Telegram Bot)

Control your laptop remotely using a **Telegram bot**.
This project allows you to execute system-level actions like shutdown, restart, typing, screenshots, and system monitoring — all from your phone.

---

## 🚀 Features

* 📱 Control your laptop via Telegram
* 🔒 Authorized user access (secure control)
* ⚡ Real-time command execution

### 🧠 Supported Commands

* `/start` → Initialize the bot
* `/shutdown` → Shutdown the system
* `/restart` → Restart the system
* `/open <app>` → Open any application
* `/type <text>` → Type text remotely
* `/screenshot` → Capture and send screen
* `/status` → Get system stats (CPU, RAM, Battery, Disk)
* `/stopbot` → Stop the bot

---

## 🛠️ Tech Stack

* **Python**
* **python-telegram-bot**
* **PyAutoGUI** (automation)
* **psutil** (system monitoring)
* **OS module** (system commands)

---

## 📂 Project Structure

```id="eqh6o5"
├── control_bot.py          # Main bot script
├── control_bot(old version).py  # Legacy version
├── start_bot.bat           # Script to run bot quickly
├── token.txt               # Stores bot token (⚠️ sensitive)
├── screen.png              # Screenshot output
```

---

## ⚙️ How It Works

* The bot listens for commands using Telegram API 
* Only the **authorized user ID** can control the system
* Commands trigger system-level actions using:

  * `os.system()` for shutdown/restart
  * `pyautogui` for typing & screenshots
  * `psutil` for system stats

---

## ▶️ Setup & Run

### 1️⃣ Clone the repository

```id="0gt6wg"
git clone https://github.com/your-username/remote-laptop-control.git
cd remote-laptop-control
```

### 2️⃣ Install dependencies

```id="5ngqx9"
pip install python-telegram-bot pyautogui psutil
```

### 3️⃣ Add your Telegram Bot Token

⚠️ IMPORTANT:
Do NOT hardcode your token like this (your repo already has it exposed 😬 )

Instead:

```id="0rw5ec"
TOKEN = "your_bot_token_here"
```

Or store it securely in environment variables.

---

### 4️⃣ Run the bot

```id="fjrntt"
python control_bot.py
```

Or use:

```id="0v6u9j"
start_bot.bat
```

---

## 🔐 Security Note (VERY IMPORTANT)

* Your **bot token is currently exposed**
* Anyone can control your laptop if they get your user ID

👉 Fix immediately:

1. Regenerate token using BotFather
2. Never upload `token.txt` to GitHub
3. Add this to `.gitignore`:

```id="9i6v2p"
token.txt
screen.png
```

---

## 💡 Future Improvements

* Add file transfer support 📂
* Live screen streaming 🎥
* Voice command integration 🎙️
* Multi-user authentication system 🔐

---

## 📜 License

This project is for educational and personal use.

---

## 👨‍💻 Author

**Varshith**

---

### ⚡ Small but important advice

This project is **resume gold**, but ONLY if:

* You fix the exposed token
* Add a demo GIF/video
* Push clean commits

---
