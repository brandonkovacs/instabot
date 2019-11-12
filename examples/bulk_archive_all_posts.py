"""
    Bulk Archive All Instagram Posts

    Using instabot library

"""

import argparse
import os
import sys

from tqdm import tqdm

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

# Method to archive a set of posts for a given user
def archive_medias(bot, medias):
    for media in tqdm(medias, desc="Medias"):
        bot.archive(media)
    return True

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p, proxy=args.proxy)

# Fetch all posts for the user
medias = bot.get_total_user_medias(bot.user_id)

# Bulk archive posts
archive_medias(bot, medias)
