from pyrogram import *

import asyncio

api_id = 20060719
api_hash = "06ee9168fc91122d05bf3a6df5c68656"

bot_tok = "5473981523:AAFMWsNjHIGSw1uwdqVLmugZfqFs8C9aqpw"





app = Client('S_Name', api_id, api_hash, bot_token=bot_tok)


#dastotat

@app.on_message()
async def my_handler(c, m):
    await m.reply("sam_ri1")
    print(m)

#dastotat


print("bot is started")
app.run()

