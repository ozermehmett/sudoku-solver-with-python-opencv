from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import image_processing

TOKEN = 'YOUR BOT KEY'


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! This bot is designed to solve unsolved "
                                                                    "Sudoku puzzles that you upload in PNG format!")


def solve_to_sudoku(update, context):
    message = update.message
    if message.document and message.document.mime_type == 'image/png':
        try:
            file_id = message.document.file_id
            file = context.bot.get_file(file_id)
            file.download('sudoku.png')

            image_processing.solve('sudoku.png')

            context.bot.send_document(chat_id=message.chat_id, document=open('example.png', 'rb'))

        except:
            context.bot.send_message(chat_id=message.chat_id, text="It didn't resolve; please try sending it as an "
                                                                   "official file! The file format should be PNG!")

    elif message.text:
        context.bot.send_message(chat_id=message.chat_id, text="You can only upload images. Please send it as a file! "
                                                               "The file format should be PNG!")


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text | Filters.document, solve_to_sudoku))
    updater.start_polling()
    updater.idle()
