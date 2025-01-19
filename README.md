---

## **Affirmation Bot**

Create and schedule personalized affirmations to be delivered as notifications directly to your smartwatch using this Telegram bot.

---

### **Step 1: Set Up a Telegram Bot**

1. **Create a Bot**:  
    - Open Telegram and search for `BotFather`.  
    - Start a chat with BotFather and use the `/newbot` command.  
    - Provide a name and username for your bot. The username must end with "bot" (e.g., `MyCustomBot`).  
    - BotFather will provide you with a bot token (e.g., `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).  

2. **Save the Bot Token**:  
    - Store the token securely. It will be used to send messages via the Telegram Bot API.  

---

### **Step 2: Set Up Your Telegram User ID**

1. **Find Your User ID**:  
    - Use the bot [@userinfobot](https://t.me/userinfobot).  
    - Start a chat with this bot, and it will display your Telegram user ID.  

---

### **Step 3: Update the Bot Code**

1. Open the bot script file (`my_bot.py`).  
2. Locate the following lines in the code:  

   ```python
   BOT_TOKEN = "your_bot_token_here"
   CHAT_ID = "your_user_id_here"
   ```
3. Replace `your_bot_token_here` with the bot token you received from BotFather.  
4. Replace `your_user_id_here` with the Telegram user ID you received from @userinfobot.  

---

### **Step 4: Configure the Time Zone**

This bot supports time zone localization for scheduling affirmations. The default time zone is set to **Asia/Kolkata**. If you need a different time zone:  

1. Locate the following line in the bot code:  
   ```python
   TIMEZONE = pytz.timezone("Asia/Kolkata")
   ```  
2. Replace `"Asia/Kolkata"` with your desired time zone.  
3. A list of supported time zones can be found in the [Python `pytz` documentation](https://pythonhosted.org/pytz/).  

---

### **Step 5: Install Prerequisites**

Run the following commands to install the necessary Python packages (with `break-system-packages` to avoid permission issues):  

```bash
pip install python-telegram-bot --break-system-packages
pip install "python-telegram-bot[job-queue]" --break-system-packages
```

---

### **Step 6: Set Up an AWS Free Tier EC2 Instance**

The author ran this bot on an **AWS EC2 Ubuntu instance (Free Tier)**. AWS Free Tier provides a way to explore cloud computing for free.  

1. **Why AWS Free Tier?**  
   AWS Free Tier includes 750 hours of t2.micro instances per month for 12 months, sufficient for small projects like this bot.  

2. **Set Up Your EC2 Instance**:  
   - Search for easy walkthroughs on platforms like [AWS Documentation](https://docs.aws.amazon.com/), [YouTube](https://www.youtube.com/), or [Medium](https://medium.com/) using keywords like:  
     - *"Set up AWS Free Tier account"*  
     - *"Launch Ubuntu EC2 instance on AWS Free Tier"*  

3. **Update and Upgrade Your Machine**:  
   After launching your EC2 instance, always run:  
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```  
   This ensures the machine has the latest software and prevents unexpected errors.  

---

### **Step 7: Run the Bot in a tmux Session**

1. Install `tmux`:  
   ```bash
   sudo apt install tmux
   ```  
2. Start a new tmux session:  
   ```bash
   tmux new -s affirmation_bot
   ```  
3. Run the bot script inside the tmux session:  
   ```bash
   python3 my_bot.py
   ```  
4. Detach from the session:  
   ```bash
   Ctrl+b, then press d
   ```  
   This keeps the bot running even if you close the terminal.  

---

### **Usage**

- **Start the Bot**: Use the `/start` command to initialize the bot.  
- **Add an Affirmation**: Use the `/add <HH:MM> <message>` command to schedule an affirmation (e.g., `/add 08:00 You are amazing!`). The time is to be entered in **24 hour format.**
- **List Affirmations**: Use the `/list` command to see all scheduled affirmations.  
- **Remove an Affirmation**: Use the `/remove <ID>` command to delete an affirmation by its ID.  

---


**Note:**
The code was written with the assistance of ChatGPT and required nearly 30 iterations to achieve the desired functionality.

**Timing Behavior:**
Please note that the affirmation appears exactly one minute later than the defined time. This behavior is intentional based on how the bot’s job queue scheduling is set up, and it should not be considered an error.

Here's the refined disclaimer or note you can add to the README:

---

### **Disclaimer on Receiving Affirmations on Smartwatch**  
To receive the affirmation notifications on your smartwatch, please ensure the following:  
1. **Active Internet and Bluetooth**: Keep your smartphone's internet connection and Bluetooth enabled.
2. **Smartwatch Pairing**: Ensure that your smartwatch is properly paired with your smartphone.
3. **Telegram Notifications**: To ensure that only affirmation notifications are received, I recommend muting all other Telegram groups and chats, leaving only the bot unmuted. This strategy helps in avoiding interruptions and ensures that you get the affirmations as intended.

---


