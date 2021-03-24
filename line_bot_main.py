# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 13:17:43 2021

@author: penguin
"""

from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('QaJ08dNM3i3K5HkfFVlwWlo+ETVqyHnE2XHv/8eAs+FzmgnYAXTnAuRuHHOHXFP58mjJROVD2kPsy/Xju6OZk/jywm8jNa+1TMbk8meDIxlEB4GUnZBpXDOI9d0Kk71Gy5sVBSRy709Vr55Ua1XrgwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('37ba211752bf5e8d752d3f2d53f89fde')

# 接收 LINE 的資訊
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

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

if __name__ == "__main__":
    app.run()