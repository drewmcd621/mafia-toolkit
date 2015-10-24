import praw
import json
from pprint import pprint
from time import gmtime, strftime
from datetime import datetime
from models import *


def getPRAW():
    return praw.Reddit("Mafia Toolkit - /u/SystemOutPrintln")

def get_post_info(url):
    r = getPRAW()
    post = r.get_submission(url)
    return post


def parse_comments(gameO):
    for p in Phase.objects.all():
        parse_comment_thread(gameO, p)


def parse_comment_thread(gameO, phaseO):
    r = getPRAW()
    post = r.get_submission(submission_id=phaseO.redditID)
    comms = praw.helpers.flatten_tree(post.comments)
    ret = []
    for c in comms:

        if Player.objects.filter(username__iexact=c.author.name, game=gameO.id).exists():
            playerO = Player.objects.get(username__iexact=c.author.name, game=gameO.id)
            rID = c.id
            edit = c.edited
            if edit == 'false':
                edit =  datetime.fromtimestamp(0)
            else:
                edit = datetime.fromtimestamp(edit)
            time = datetime.fromtimestamp(c.created_utc)
            url = phaseO.redditLink + rID + "/"

            text = c.body
            if Comment.objects.filter(redditID=rID).exists():
                #Comment already exists
                com = Comment.objects.get(redditID=rID)
                com.text = text
                com.editedTime = edit
                com.updated = datetime.now()
                com.save()
            else:
                #New comment
                com = Comment(game=gameO, player=playerO, phase=phaseO, redditID=rID, text=text, timestamp=time, editedTime=edit, redditLink=url, updated=datetime.now())
                com.save()
