import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "21489763")
    API_HASH  = os.environ.get("API_HASH", "308f5362db7844a59272c33634e9e792")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7376265328:AAERJUwTDfdDu5P08Zavjz1TeKs1XaiYwVg") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Movies7x")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://7xmovieshub:uoc0ajFxBrQ0wksk@movies7x.4axozzk.mongodb.net/?retryWrites=true&w=majority&appName=Movies7x")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://files.catbox.moe/4kwe69.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6474779115').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))

    # Token Verification
    API = os.environ.get("API", "") # shortlink api
    URL = os.environ.get("URL", "") # shortlink domain without https://
    VERIFY_TUTORIAL = os.environ.get("VERIFY_TUTORIAL", "https://t.me/+cXIPgHSu") # how to open link 
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Auto_x_Rename_Robot") # bot username without @
    VERIFY = os.environ.get("VERIFY", "False") # set True Or False and make sure spelling is correct and first letter capital.


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.
    
<b>Bot Is Made By </b>"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename One Piece S01 - EPepisode - quality  [Dual Audio] - @net_pro_max </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>🤖 My Name :</b> <a href='https://t.me/AutoRenameXBot'>Auto Rename Bot ⚡</a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>

    
<b>♻️ Bot Made By :</b> """

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>madflixofficial@axl</code> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Here Is The Help For My Commands."""



