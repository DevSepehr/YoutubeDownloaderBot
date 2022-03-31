# YouTube downloader [Bot] 

from pytube import YouTube
from pytube.cli import on_progress 
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
import os 


app = Client(
    'myAccount',
    api_id=5501261,
    api_hash="63402a3b7e875edfee3786e911744dd5",
    bot_token='5151460855:AAGTCTX1fsU2kDZO2IllYpRmhtN4MPAALGA'
    )

@app.on_callback_query()
def callBack(client,msg):
    
    url = open('link.txt','r').readline()
    youtube = YouTube(url)    
    cap = f'• Title : {youtube.title}\n• length : {round(youtube.length / 60, 2) if youtube.length > 60 else youtube.length}\n• view : {youtube.views}\n\n * by : @khodesepehram'
    
    if msg.data == 'mp3':
        # write how to download mp3 file
        app.edit_message_text(msg.from_user.id, message_id=msg.message.message_id,text='لطفا کمی صبر کنید...')
        
        app.send_photo(msg.from_user.id,youtube.thumbnail_url,caption=cap)
        
        yt0 = youtube.streams.filter(only_audio=True)
        yt0.first().download(filename="youtubeV.mp3")
        
        app.send_audio(msg.from_user.id,'youtubeV.mp3',caption=cap)
        os.remove('youtubeV.mp3')
        
    elif msg.data == 'mp4':
        res_btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('1080p',callback_data='1080'),
                    InlineKeyboardButton('720p',callback_data='720'),
                    InlineKeyboardButton('480p',callback_data='480')
                    ]
                ]
            )
        app.edit_message_text(msg.from_user.id,text='🔹 کیفیت ویدیو رو انتخاب کن  :',message_id=msg.message.message_id,reply_markup=res_btn)
        
    
    
    if msg.data == '1080':
        
        app.edit_message_text(msg.from_user.id,msg.message.message_id,f'لطفا صبر کنید...')
        
        app.send_photo(msg.from_user.id,youtube.thumbnail_url,caption=cap)
        yt1 = youtube.streams.filter(res='1080p')
        
        yt1.first().download(filename='youtubeV.mp4')
        app.send_audio(msg.from_user.id,'youtubeV.mp4',caption=cap)
        
        os.remove('youtubeV.mp4')
        
    elif msg.data == '720':
        
        app.edit_message_text(msg.from_user.id,msg.message.message_id,'لطفا صبر کنید...')
        
        app.send_photo(msg.from_user.id,youtube.thumbnail_url,caption=cap)
        
        yt2 = youtube.streams.filter(res='720p')
        
        yt2.first().download(filename='youtubeV.mp4')
        app.send_audio(msg.from_user.id,'youtubeV.mp4',caption=cap)
        
        os.remove('youtubeV.mp4')
        
    elif msg.data == '480':
        
        app.edit_message_text(msg.from_user.id,msg.message.message_id,'* لطفا صبر کنید...')
        
        app.send_photo(msg.from_user.id,youtube.thumbnail_url,caption=cap)
        
        yt3 = youtube.streams.filter(res='480p')
        yt3.first().download(filename='youtubeV.mp4')
        
        app.send_audio(msg.from_user.id,'youtubeV.mp4',caption=cap)
        os.remove('youtubeV.mp4')
  
        
@app.on_message()
def utube(client,msg):
    
    
    if msg.text.startswith("https://youtu.be/"):
        link = open('link.txt','w').write(msg.text)
        
        type_btn = InlineKeyboardMarkup(
            [
                [
                
                    InlineKeyboardButton('mp4',callback_data='mp4'),
                    InlineKeyboardButton('mp3',callback_data='mp3')
                ]
            ]
        )
        app.send_message(msg.chat.id,text='**• 🔹 فرمت فایل رو انتخاب کن :**', reply_markup=type_btn)
    elif msg.text == '/start':
        
        btn = InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton('* Creater *',url='https://t.me/khodesepehram')
                ]
            ]
        )
        
        app.send_message(msg.chat.id,text='* سلام به ربات یوتیوب دانلود خوش آمدید.\n برای دانلود ویدیو از یوتیوب باید لینک ویدیو رو برام بفرست :)',reply_markup=btn)
    
app.run()