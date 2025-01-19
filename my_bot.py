import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from datetime import datetime, time
import pytz

# Suppress excessive logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.WARNING)

# Set up the logger
logger = logging.getLogger(__name__)

# Define your bot token and chat ID
BOT_TOKEN = "YOUR-TOKEN-HERE"
CHAT_ID = "USER-ID-HERE"

# Define the desired time zone
TIMEZONE = pytz.timezone("Asia/Kolkata")  # Change to your desired time zone

# Define an empty dictionary for storing affirmations and their timings
affirmations = {}

# Create the application
application = Application.builder().token(BOT_TOKEN).build()

# Function to start the bot
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm your affirmation bot.")

# Function to add affirmations with timings
async def add_affirmation(update: Update, context: CallbackContext):
    try:
        # Extract the time and affirmation from the message
        time_str = context.args[0]
        affirmation = " ".join(context.args[1:])
        
        # Parse the time
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        
        # Localize the time to the desired time zone
        localized_time = TIMEZONE.localize(datetime.combine(datetime.today(), time_obj)).time()
        
        # Get the current ID (based on the length of the affirmations dictionary + 1)
        affirmation_id = len(affirmations) + 1
        
        # Add the affirmation and localized time to the dictionary
        affirmations[affirmation_id] = {
            "affirmation": affirmation,
            "time": localized_time
        }

        # Notify the user that the affirmation was added
        await update.message.reply_text(f"Affirmation added! Time: {localized_time.strftime('%I:%M %p')} Message: {affirmation}")
    
    except Exception as e:
        await update.message.reply_text(f"Error: {e}. Please use the format: /add <HH:MM> <affirmation>")

# Function to list all affirmations
async def list_affirmations(update: Update, context: CallbackContext):
    if affirmations:
        response = "Here are all your affirmations:\n"
        for affirmation_id, data in affirmations.items():
            # Format the time for display
            formatted_time = data["time"].strftime("%I:%M %p")
            response += f"ID: {affirmation_id}, Time: {formatted_time}, Message: {data['affirmation']}\n"
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("No affirmations found.")

# Function to remove an affirmation by ID
async def remove_affirmation(update: Update, context: CallbackContext):
    try:
        affirmation_id = int(context.args[0])
        if affirmation_id in affirmations:
            del affirmations[affirmation_id]
            await update.message.reply_text(f"Affirmation with ID {affirmation_id} removed.")
        else:
            await update.message.reply_text(f"No affirmation found with ID {affirmation_id}.")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}. Please use the format: /remove <ID>")

# Function to send affirmations at the scheduled time
async def send_affirmations(context: CallbackContext):
    current_time = datetime.now(TIMEZONE).time()
    for affirmation_id, data in list(affirmations.items()):
        if current_time >= data["time"]:
            await context.bot.send_message(chat_id=CHAT_ID, text=data["     affirmation"])
            del affirmations[affirmation_id]  # Remove the affirmation after sending

# Adding handlers for commands
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("add", add_affirmation))
application.add_handler(CommandHandler("list", list_affirmations))
application.add_handler(CommandHandler("remove", remove_affirmation))

# Schedule the sending of affirmations at regular intervals
application.job_queue.run_repeating(send_affirmations, interval=60, first=0)

# Start polling to listen for updates
application.run_polling()
