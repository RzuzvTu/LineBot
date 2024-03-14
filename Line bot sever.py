from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, ImageSendMessage,PostbackAction,URIAction, MessageAction, TemplateSendMessage, ButtonsTemplate
from linebot.models import TemplateSendMessage, CarouselTemplate,  CarouselColumn    # 載入 TextSendMessage 和 ImageSendMessage 模組
import json,random

app = Flask(__name__)
@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    try:
        line_bot_api = LineBotApi('uQwu1BJddb1uXL9bEmjpf6ysFNqcz1QxSYrz1sgWWfYQ8rsSJ5xZWszCQWFwhbX4MSo2174gIyLA3qj+s2ynoF1k/lXFmbBICPJAn8xXc5v9ba4rEPZUfH2cujsJcsqJP/Ueox0LLIgkhUiS0LfOQAdB04t89/1O/w1cDnyilFU=')
        handler = WebhookHandler('89e9c4a6998410861ae696a5b4947d00')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        tp = json_data['events'][0]['message']['type']
        if tp == 'text':
            if json_data['events'][0]['message']['text'] == '選單':
                line_bot_api = LineBotApi('uQwu1BJddb1uXL9bEmjpf6ysFNqcz1QxSYrz1sgWWfYQ8rsSJ5xZWszCQWFwhbX4MSo2174gIyLA3qj+s2ynoF1k/lXFmbBICPJAn8xXc5v9ba4rEPZUfH2cujsJcsqJP/Ueox0LLIgkhUiS0LfOQAdB04t89/1O/w1cDnyilFU=')
                line_bot_api.push_message('U6c66b225d7835a66ca8839be8612103f', TemplateSendMessage(
                    alt_text='CarouselTemplate',
                    template=CarouselTemplate(
                        columns=[
                            CarouselColumn(
                                    thumbnail_image_url='https://pbs.twimg.com/media/GHvpPnDXMAAFZ8Q?format=jpg&name=large',
                                    title='熱門歌曲',
                                    text='Calliope 熱門三大首歌曲',
                                    actions=[
                                        URIAction(
                                            label='失礼しますが、RIP♡ ',
                                            uri='https://www.youtube.com/watch?v=5y3xh8gs24c'
                                        ),
                                        URIAction(
                                            label='「Q」',
                                            uri='https://www.youtube.com/watch?v=aetXqd9B8WE'
                                        ),
                                        URIAction(
                                            label='end of life',
                                            uri='https://www.youtube.com/watch?v=BXB26PzV31k'
                                        )
                                    ]
                                ),
                                CarouselColumn(
                                    thumbnail_image_url='https://pbs.twimg.com/media/GHsum0DWoAAtXgs?format=jpg&name=4096x4096',
                                    title='選單 2',
                                    text='說明文字 2',
                                    actions=[
                                        PostbackAction(
                                            label='postback',
                                            data='data1'
                                        ),
                                        MessageAction(
                                            label='使用說明',
                                            text='使用說明'
                                        ),
                                        URIAction(
                                            label='HoloShop',
                                            uri='https://shop.hololivepro.com/pages/search-results-page?q=Calliope&tab=products&page=1'
                                        )
                                    ]
                                )
                            ]
                        )
                    ))      
            
            if json_data['events'][0]['message']['text'] == '圖':
                def selectRandom(calli):
                    return random.choice(calli)

                calli = ['calli1', 'calli2', 'calli3', 'calli4', 'calli5']

                json_data['events'][0]['message']['text'] = selectRandom(calli)
            print(json_data['events'][0]['message']['text'])
            msg = reply_msg(json_data['events'][0]['message']['text'])
            if msg[0] == 'text':
                # 如果要回傳的訊息是 text，使用 TextSendMessage 方法
                line_bot_api.reply_message(tk,TextSendMessage(text=msg[1]))
            if msg[0] == 'image':
                # 如果要回傳的訊息是 image，使用 ImageSendMessage 方法
                line_bot_api.reply_message(tk,ImageSendMessage(original_content_url=msg[1],preview_image_url=msg[1]))
    except:
        print('error')
        print("12344")
    return 'OK'
# 建立回覆圖片的函式
def test():
    print("hello")           
def reply_msg(text):
    # 客製化回覆文字
    msg_dict = {
        'hi':'Hi! 你好呀～',
        'hello':'Hello World!!!!',
        '你好':'你好呦～',
        '使用說明':'正上方點擊可以進入Calliope頻道主頁,點擊下一可獲得隨機一張Calliope圖片,點擊中間可以前往Calliope推特'
    }
    # 如果出現特定圖片文字，提供圖片網址
    img_dict = {
        'calli1':'https://pbs.twimg.com/media/GHpzrfqWMAA-W1-?format=jpg&name=medium',
        'calli2':'https://pbs.twimg.com/media/GHAqynLasAAYnYw?format=jpg&name=4096x4096',
        'calli3':'https://pbs.twimg.com/media/GHLpYy5bkAAkowJ?format=jpg&name=medium',
        'calli4':'https://pbs.twimg.com/media/GHbKcVGa8AE1VS2?format=jpg&name=4096x4096',
        'calli5':'https://pbs.twimg.com/media/GHgwxnMbsAAjRto?format=jpg&name=large',
    }
    test_dice = {
        '選單':test
    }
    
     # 預設回覆的文字就是收到的訊息
    reply_msg_content = ['text',text]
    if text in msg_dict:
        reply_msg_content = ['text',msg_dict[text.lower()]]
    if text in img_dict:
        reply_msg_content = ['image',img_dict[text.lower()]]
    return reply_msg_content
if __name__ == "__main__":
    app.run()