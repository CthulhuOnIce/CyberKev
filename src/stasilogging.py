import os
import datetime
import base64
import sys

def discord_dynamic_timestamp(timestamp: datetime.datetime, format_style: str = 'f') -> str:
    """
    Converts a datetime object to a Discord dynamic timestamp.

    Args:
        timestamp (datetime.datetime): The datetime object to be converted.
        format_style (str): The format style for the timestamp. Default is 'f'.
            Available format styles:
                - 't': Short time format (e.g., 1:13 PM)
                - 'T': Long time format (e.g., 1:13:00 PM)
                - 'd': Short date format (e.g., 4/18/23)
                - 'D': Long date format (e.g., April 18, 2023)
                - 'f': Short date and time format (e.g., April 18, 2023 at 1:13 PM)
                - 'F': Long date and time format (e.g., Tuesday, April 18, 2023 at 1:13 PM)
                - 'R': Relative time format (e.g., 2 months ago)
                - 'FR': Custom: F and R (e.g., Tuesday, April 18, 2023 at 1:13 PM (2 months ago))
                - 'RF' Custom: R and F (e.g., 2 months ago (Tuesday, April 18, 2023 at 1:13 PM))

    Returns:
        str: The Discord dynamic timestamp string.
    """
    if format_style not in ['t', 'T', 'd', 'D', 'f', 'F', 'R', 'FR', 'RF']:
        raise ValueError("Invalid format style. Please use one of the following: 't', 'T', 'd', 'D', 'f', 'F'")

    if timestamp.tzinfo is None:
        timestamp = timestamp.replace(tzinfo=datetime.timezone.utc)

    # Convert the timezone aware datetime object to Unix timestamp (epoch time)
    epoch = int(timestamp.timestamp())
    
    if format_style == 'FR':
        return f'<t:{epoch}:F> (<t:{epoch}:R>)'
    
    elif format_style == 'RF':
        return f'<t:{epoch}:R> (<t:{epoch}:F>)'
    
    else:
        return f'<t:{epoch}:{format_style}>'

def log(category_broad, category_fine, message, print_message=True, preserve_newlines=False):
    
    if "--debug" in sys.argv or "--verbose" in sys.argv:
        print_message = True
        
    # create timestamp like JAN 6 2021 12:00:00
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
    if not preserve_newlines:
        message = message.replace("\n", " ")
    # clean emojis, special characters
    print_msg = message.encode("latin-1", "replace").decode('latin-1')
    if print_message: print(f"[{timestamp}] [{category_broad.upper()}] [{category_fine.upper()}] {print_msg}")
    with open(f"logs/{category_broad.lower()}.log", "a+", encoding='utf-8') as f:
        f.write(f"[{timestamp}] [{category_fine.upper()}] {message}\n")

def log_user(user):
    return f"{user} ({user.id})"

def lid(object):  # convert the id(object) to base64
    return base64.b64encode(str(id(object)).encode("utf-8")).decode("utf-8")
