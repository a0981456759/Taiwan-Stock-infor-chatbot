import re
import time
from MSG_Template.text.stock_info import *
from flask import Flask, request, abort, render_template

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from twstock import *
import twstock

# 全域變數
app = Flask(__name__)

# 基本設定
line_bot_api = LineBotApi(
    'LINE_API_CHANNEL_KEY')
handler = WebhookHandler('LINE_API_SECRET')


@app.route("/")
def home():
    timestamp = int(time.time())
    return render_template('home.html', TimeStamp=timestamp, Status='Success')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    userID = event.source.user_id
    # ================================
    if re.match('^股票 ', text):
        head, key = text.split(' ')
        text_message = text_get_stock_info(key)
        line_bot_api.reply_message(event.reply_token, text_message)

    # elif re.match('^設定 ', text):
    #     head, key, secret, sub = text.split(' ')
    #     text_message = text_auth_api(userID, key, secret, sub)
    #     line_bot_api.reply_message(event.reply_token, text_message)

    # elif re.match('^到期日$', text):
    #     text_message = text_search_expiry_date(userID)
    #     line_bot_api.reply_message(event.reply_token, text_message)

    # # ================================
    # elif re.match('^機器人開關$', text):
    #     flex_message = flex_switch_button(userID)
    #     line_bot_api.reply_message(event.reply_token, flex_message)


# @handler.add(PostbackEvent)
# def handle_postback(event):
#     data = event.postback.data
#     userID = event.source.user_id
#     # ===============================
#     text_message = text_change_status(userID, data)
#     line_bot_api.reply_message(event.reply_token, text_message)


if __name__ == '__main__':
    app.run()
