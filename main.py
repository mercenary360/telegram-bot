from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters, CallbackQueryHandler
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext, _updater


TOKEN: Final = '6339310622:AAEiI0DKVkgjVUYmtp4sk38lDiDBA_F45Ww'
BOT_USERNAME: Final = '@directorans'

# Define a command handler for the /start command

# Define a callback function for handling inline button clicks
async def handle_inline_button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    option_selected = query.data
    await query.answer(f"You chose: {option_selected}")

# ...

# Register the callback function for handling inline button clicks

async def start2(update: Update, context: CallbackContext):
    # Create an inline keyboard with two buttons
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data='option1')],
        [InlineKeyboardButton("Option 2", callback_data='option2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)


async def start1(update: Update, context: CallbackContext):
    keyboard = [
        ["mawasiliano", "huduma"],
        ["lengo", "kuhusu"]
    ]
    reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}

    await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

async def mwanzo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Oky thenk for chart with me! am here to help you about graphics')


async def msaada_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''
    
    unaweza kubofya kama ifuatavyo kwa ajili ya msaada kama vile:
    /msaada - kama unahitaji kupata msaada kuhusu kampuni yetu ya ANS PROGRAMMING 
    /lengo - lengo la kuhusiana na kampuni yetu
    /mwanzo - kuanza upya maongezi 
    /kuhusu - taarifa kuhusu kampani yetu
    ''')


async def lengo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('lengo la mimi kuwepo hapa ni kutoa msaada wa kalibu kwako na kama unahisi mimi sina msaada bac jaribu kuwasiliana na boss kupitia @ansprogrammer')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('bofya au command /msaada ili kuweza kupata muongozo kamili wa bot')



async def mawasiliano_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''
    unaweza kuwasiliana na sisi kupitia 
    Email - programmerans@gmail.com
    telegram - @ansprogrammer
    Instagram - @ansprogrammer
    ''')


async def kuhusu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''ANS PROGRAMMING ni kampuni inayojihusisha na mambo mbalimbali kama vile 
    1. GRAPHICS DESIGN
    2. PHOTO EDITING
    3. VIDEOGRAPHY
    4. SOFTWARE DESIGN
    5. WEB APPLICATION
    6. EDUCATION TECH
    7. BOT MAKING
    8. COMPUTER INSTLLATION
    
    kama utakua unahitaji mafunzo ya cozi zilizopo hapo juu. ingia kwenye channel yangu ya youtube https://www.youtube.com/@ansprogrammer/
    ''')




def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello'  in text:
        return 'hey there'

    if 'hi' in text:
        return "hi too"

    if 'hellow' in text:
        return "hellow and you"

    if 'mambo' in text:
        return 'saf mzima wewe '


    return 'nashindwa kuelewa ni kipi umesema kumbuka mimi ni robot siwezi elewa kila kitu'


# Define an asynchronous message handler for handling user choices
async def handle_choice(update: Update, context: CallbackContext):
    user_choice = update.message.text
    # Check if the message is not a command
    if not user_choice.startswith('/'):
        await update.message.reply_text(f"You chose: {user_choice}")


def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Update(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher


#this is an inline kybord
# Define a callback function for handling inline button clicks
def handle_inline_button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    option_selected = query.data
    query.answer(f"You chose: {option_selected}")


def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)
    dispatcher = updater.dispatcher


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat_id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = handle_response(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error{context.error}')



if __name__ == '__main__':
    print('Start poling.....')
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('mwanzo', mwanzo_command))
    app.add_handler(CommandHandler('msaada', msaada_command))
    app.add_handler(CommandHandler('lengo', lengo_command))
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('mawasiliano', mawasiliano_command))
    app.add_handler(CommandHandler('kuhusu', kuhusu_command))
    app.add_handler(CommandHandler("start1", start1))
    app.add_handler(CommandHandler("start2", start2))


    app.add_handler(MessageHandler(filters.TEXT, handle_choice))
    #for inline kybord
    app.add_handler(CallbackQueryHandler(handle_inline_button_click))



    #message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    app.add_error_handler(error)

    #polling the Bot
    print("Poling.....")
    app.run_polling(poll_interval=3)
