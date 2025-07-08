# 🎧 Personal Bot

A fun and simple Discord bot built with Python.  
It can play music from YouTube, join and leave voice channels, and respond to basic text commands like `!hello`.

---

## ✨ Features

- `!join` — Join your voice channel  
- `!leave` — Leave the voice channel  
- `!play <song name or URL>` — Search and play music from YouTube  
- `!hello` — Greet the bot
- `!roll` — Randomize number  
- `!quote` — Random quote    
- Modular command system using Cogs

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/personal-bobi-bot.git
cd personal-bobi-bot
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the project root folder with the following content:

```env
DISCORD_BOT_TOKEN=your_discord_bot_token_here
```

> ⚠️ Keep your bot token private. Never share it or push it to GitHub!

---

## ▶️ Run the Bot

```bash
python main.py
```

---

## 🛠 Requirements

- Python 3.10+
- `discord.py` v2+
- `yt_dlp`
- `ffmpeg` (must be installed and in system PATH)

---

## 📁 Project Structure

```text
.
├── main.py             # Entry point
├── music.py            # Music commands (Cog)
├── commands.py         # Text commands (Cog)
├── .env                # Bot token (excluded via .gitignore)
├── .gitignore
└── requirements.txt
```

---

## 📜 License

MIT — Free to use, modify, and distribute.

---

## 💡 Credits

Built with [discord.py](https://github.com/Rapptz/discord.py) and [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
Created with ❤️ by Fx. Guntur
