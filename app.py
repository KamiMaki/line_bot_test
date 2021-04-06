from flask import Flask, request, abort
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('QaJ08dNM3i3K5HkfFVlwWlo+ETVqyHnE2XHv/8eAs+FzmgnYAXTnAuRuHHOHXFP58mjJROVD2kPsy/Xju6OZk/jywm8jNa+1TMbk8meDIxlEB4GUnZBpXDOI9d0Kk71Gy5sVBSRy709Vr55Ua1XrgwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('37ba211752bf5e8d752d3f2d53f89fde')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    with open('card.json',encoding='utf-8-sig', errors='ignore') as f:
        card = json.loads(f.read())
    with open('news.json',encoding='utf-8-sig', errors='ignore') as f:
        news = json.loads(f.read())
    flex_message = FlexSendMessage('card',card)
    news = FlexSendMessage('news',news)
    
    quick_reply = TextSendMessage(text='可透過下方類別了解更多：',quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label="CIO每周觀點", text="CIO每周觀點")), QuickReplyButton(action=MessageAction(label="ESG投資", text="ESG投資")), QuickReplyButton(action=MessageAction(label="股票", text="股票")),QuickReplyButton(action=MessageAction(label="固定收益", text="固定收益")),QuickReplyButton(action=MessageAction(label="新興市場債券", text="新興市場債券")),QuickReplyButton(action=MessageAction(label="label6", text="text6")),QuickReplyButton(action=MessageAction(label="label7", text="text7")),QuickReplyButton(action=MessageAction(label="label8", text="text8")),QuickReplyButton(action=MessageAction(label="label9", text="text9")),QuickReplyButton(action=MessageAction(label="label10", text="text10"))]))
    if event.message.text == '圖卡':
        line_bot_api.reply_message(event.reply_token,flex_message)
    elif event.message.text == '觀點':
        line_bot_api.reply_message(event.reply_token,news)
    else:
        # line_bot_api.reply_message(event.reply_token,flex_message)
        line_bot_api.reply_message(event.reply_token,[flex_message,quick_reply])
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
