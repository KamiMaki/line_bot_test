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
    
    flex_message = FlexSendMessage('card',{
  "type": "bubble",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "路博邁5G股票基金",
        "weight": "bold",
        "size": "lg",
        "color": "#123A5F",
        "align": "center",
        "margin": "xxl",
        "contents": []
      },
      {
        "type": "spacer",
        "size": "xxl"
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/zR4DXfB.png",
    "align": "start",
    "size": "full",
    "aspectRatio": "1.51:1",
    "aspectMode": "fit",
    "backgroundColor": "#FFFFFFFF",
    "action": {
      "type": "uri",
      "label": "5G",
      "uri": "https://www.nb.com/zh-tw/tw/products/site/taiwan-5g-equity"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator",
        "margin": "sm"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "基金優勢",
            "weight": "bold",
            "size": "lg",
            "color": "#EA6715FF",
            "margin": "sm",
            "contents": []
          },
          {
            "type": "text",
            "text": "在5G的創新趨勢中，依據未來營運能見度與可預測性，找尋策略性高成長的投資機會，以獲取最佳長期增值利益。",
            "weight": "bold",
            "size": "sm",
            "color": "#000000FF",
            "margin": "sm",
            "wrap": True,
            "contents": []
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "margin": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "淨值($)",
                "weight": "bold",
                "color": "#0D2A45FF",
                "gravity": "bottom",
                "wrap": True,
                "contents": []
              },
              {
                "type": "text",
                "text": "每日變動($)",
                "weight": "bold",
                "color": "#0D2A45FF",
                "contents": []
              },
              {
                "type": "text",
                "text": "日漲跌幅(%)",
                "weight": "bold",
                "color": "#0D2A45FF",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "offsetStart": "70px",
            "contents": [
              {
                "type": "text",
                "text": "$14.46",
                "contents": []
              },
              {
                "type": "text",
                "text": "$0.14",
                "contents": []
              },
              {
                "type": "text",
                "text": "0.98%",
                "color": "#FF0000FF",
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "查看更多基金資訊",
          "uri": "https://www.nb.com/zh-tw/tw/products/site/taiwan-5g-equity"
        }
      }
    ]
  },
  "styles": {
    "header": {
      "separatorColor": "#FFFFFFFF"
    },
    "body": {
      "backgroundColor": "#FFFFFFFF"
    }
  }
})
    if event.message.text == '圖卡':
        line_bot_api.reply_message(event.reply_token,flex_message )
    else:
        print(event.source.user_id)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(event.source.user_id))
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
