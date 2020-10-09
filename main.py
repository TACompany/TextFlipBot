# -*- coding: utf-8 -*-


from config import token
from telebot import types
import telebot


bot = telebot.TeleBot(token)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    text = query.query[::-1]

    res = types.InlineQueryResultArticle(
        id='1', title='Flipped text',
        description=f'Result: {text}',
        input_message_content=types.InputTextMessageContent(
            message_text=text
        )
    )

    bot.answer_inline_query(query.id, [res], cache_time=2147483646)


@bot.message_handler()
def on_message(message):
    markup = types.InlineKeyboardMarkup()
    next_chat = types.InlineKeyboardButton(text='Use in another chat...', switch_inline_query='')
    markup.add(next_chat)

    bot.send_message(message.chat.id,
        'Send me a text and I\'ll flip it! 👀',
        reply_markup=markup, parse_mode='HTML'
    )


bot.polling()