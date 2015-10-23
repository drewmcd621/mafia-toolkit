import praw
import json
from pprint import pprint
from models import *

def parse_comments(game, thing):
    r = praw.Reddit("Mafia Toolkit - /u/SystemOutPrintln")
    post = r.get_submission(submission_id=thing)
    comms = praw.helpers.flatten_tree(post.comments)
    ret = []
    for c in comms:

        if Player.objects.filter(username__iexact=c.author.name, game=game.id).exists():
            tc = {}
            tc['author'] = c.author.name;
            tc['body'] = c.body
            ret.append(tc)
    return ret
