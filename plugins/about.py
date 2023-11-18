import os
from pyrogram import Client, filters
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes

token = os.environ.get('TOKEN', '')
botid = token.split(':')[0]

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client, message):
    botdata(int(botid))
    data = find_one(int(botid))

    try:
        total_rename = data["total_rename"]
        total_size = data["total_size"]
    except KeyError as e:
        # Handle the KeyError, set default values, or take appropriate action
        total_rename = 0
        total_size = 0
        print(f"KeyError: {e}")

    await message.reply_text(
        f"Total User:- {total_user()}\n"
        f"Bot :- @rename_urbot\n"
        f"Creator :- @mrlokaman\n"
        f"Language :- Python3\n"
        f"Library :- Pyrogram 2.0\n"
        f"Server :- Railway\n"
        f"Total Renamed File :- {total_rename}\n"
        f"Total Size Renamed :- {humanbytes(int(total_size))}",
        quote=True
    )
