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
  "type": "carousel",
  "contents": [
    {
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
          }
        ]
      },
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/zR4DXfB.png",
        "margin": "xxl",
        "align": "center",
        "gravity": "bottom",
        "size": "full",
        "aspectRatio": "1.51:1",
        "aspectMode": "fit",
        "backgroundColor": "#FFFFFFFF",
        "action": {
          "type": "uri",
          "label": "5G",
          "uri": "https://www.nb.com/zh-tw/tw/products/site/taiwan-5g-equity"
        },
        "offsetTop": "17px"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "margin": "xxl",
        "contents": [
          {
            "type": "separator",
            "margin": "xxl"
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
    },
    {
      "type": "bubble",
      "direction": "ltr",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "路博邁ESG新興市場債券基金",
            "weight": "bold",
            "size": "lg",
            "color": "#123A5F",
            "align": "center",
            "contents": []
          },
          {
            "type": "text",
            "text": "(本基金有相當比重投資於非投資等級之高風險債券且配息來源可能為本金)",
            "weight": "bold",
            "size": "sm",
            "align": "center",
            "wrap": True,
            "contents": []
          }
        ]
      },
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/k8WABcP.png",
        "size": "full",
        "aspectRatio": "1.51:1",
        "aspectMode": "fit"
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
                "text": "透過投資於美元計價的全球新興市場債券，掌握並參與新興市場持續強勁的成長動能投資機會",
                "weight": "bold",
                "size": "sm",
                "color": "#000000FF",
                "align": "start",
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
                    "text": "$9.84",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "$0.01",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": "0.10%",
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
              "uri": "https://pse.is/3ds9nx"
            }
          }
        ]
      }
    }
  ]
})
    if event.message.text == '圖卡':
        line_bot_api.reply_message(event.reply_token,flex_message )
    else:
        line_bot_api.reply_message(event.reply_token,
  TextSendMessage(quick_reply=QuickReply(items=[QuickReplyButton(action=MessageAction(label="label1", text="text1")), QuickReplyButton(action=MessageAction(label="label2", text="text2")), QuickReplyButton(action=MessageAction(label="label3", text="text3")),QuickReplyButton(action=MessageAction(label="label4", text="text4")),QuickReplyButton(action=MessageAction(label="label5", text="text5")),QuickReplyButton(action=MessageAction(label="label6", text="text6")),QuickReplyButton(action=MessageAction(label="label7", text="text7")),QuickReplyButton(action=MessageAction(label="label8", text="text8")),QuickReplyButton(action=MessageAction(label="label9", text="text9")),QuickReplyButton(action=MessageAction(label="label10", text="text10"))])))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
