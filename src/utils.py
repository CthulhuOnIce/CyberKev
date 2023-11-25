import random
import base64

nouns = open("wordlists/nouns.txt", "r").read().splitlines()
adjectives = open("wordlists/adjectives.txt", "r").read().splitlines()
elements = open("wordlists/elements.txt", "r").read().splitlines()

# Function to receive time in the form of "100d10h10m10s" and return the time in seconds
def time_to_seconds(time: str):
    seconds = 0
    if "d" in time:
        seconds += int(time.split("d")[0]) * 86400
        time = time.split("d")[1]
    if "h" in time:
        seconds += int(time.split("h")[0]) * 3600
        time = time.split("h")[1]
    if "m" in time:
        seconds += int(time.split("m")[0]) * 60
        time = time.split("m")[1]
    if "s" in time:
        seconds += int(time.split("s")[0])
    return seconds

# inverse of previous function, leaves out greatest unit if it is 0
def seconds_to_time(time: int):
    days = time // 86400
    time %= 86400
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    # round all values to 3 decimal places
    days = round(days, 3)
    hours = round(hours, 3)
    minutes = round(minutes, 3)
    seconds = round(seconds, 3)

    if days > 0:
        return f"{days}d{hours}h{minutes}m{seconds}s"
    elif hours > 0:
        return f"{hours}h{minutes}m{seconds}s"
    elif minutes > 0:
        return f"{minutes}m{seconds}s"
    elif seconds > 0:
        return f"{seconds}s"
    else: # 0 seconds
        return "now"

def seconds_to_time_long(time: int):  # "one day, 10 hours, 10 minutes, 10 seconds"
    
    days = time // 86400
    time %= 86400
    hours = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    # round all values to 3 decimal places
    days = round(days, 3)
    hours = round(hours, 3)
    minutes = round(minutes, 3)
    seconds = round(seconds, 3)


    if days > 0:
        return f"{days} day{'s' if days > 1 else ''}, {hours} hour{'s' if hours > 1 else ''}, {minutes} minute{'s' if minutes > 1 else ''}, {seconds} second{'s' if seconds > 1 else ''}"
    elif hours > 0:
        return f"{hours} hour{'s' if hours > 1 else ''}, {minutes} minute{'s' if minutes > 1 else ''}, {seconds} second{'s' if seconds > 1 else ''}"
    elif minutes > 0:
        return f"{minutes} minute{'s' if minutes > 1 else ''}, {seconds} second{'s' if seconds > 1 else ''}"
    elif seconds > 0:
        return f"{seconds} second{'s' if seconds > 1 else ''}"
    else: # 0 seconds
        return "now"

def generate_random_id(): 
    return f"{random.choice(adjectives)}-{random.choice(adjectives)}-{random.choice(nouns)}"

def int_to_base64(n: int):
    # Convert integer to bytes
    int_bytes = n.to_bytes((n.bit_length() + 7) // 8, 'big') or b'\0'
    
    # Encode bytes to base64
    base64_bytes = base64.b64encode(int_bytes)
    
    # Convert bytes to string for the output
    base64_string = base64_bytes.decode('utf-8')
    
    return base64_string

def normalUsername(user):
    if not user.discriminator or user.discriminator == "0":
        return f"@{user.name}"
    else:
        return f"{user}"

# https://twemoji-cheatsheet.vercel.app/
class twemojiPNG:
    normal= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f9fe.png"  # 🧾
    ballot= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f5f3.png"  # 🗳️
    outbox= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4e4.png"  # 📤
    inbox=  "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4e5.png"  # 📥
    sign=   "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1faa7.png"  # 🪧
    lock=   "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f510.png"  # 🔐
    label=  "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f3f7.png"  # 🏷
    scroll= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4dc.png"  # 📜  
    opencab="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f5c3.png"  # 🗃
    scale=  "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/2696.png"   # ⚖
    sentenv="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4e8.png"  # 📨
    pager=  "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4df.png"  # 📟
    chain=  "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/26d3.png"   # ⛓
    aclock= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/23f0.png"   # ⏰
    swatch= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/23f1.png"   # ⏱
    memo=   "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4dd.png"  # 📝
    penlock="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f50f.png"  # 🔏
    unlock= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f513.png"  # 🔓️
    build=  "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f3db.png"  # 🏛
    ticket= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f3ab.png"  # 🎫
    folder= "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f4c1.png"  # 📁
    leftchat = "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f5e8.png"  # 🗨
    eyechat = "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/1f441-200d-1f5e8.png"

def randomKey(length: int):
    # remove similar looking characters
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return "".join(random.choice(chars) for _ in range(length))