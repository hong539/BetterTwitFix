import imp
import yt_dlp
from yt_dlp.extractor import twitter
import json

def extractStatus(url):
    twIE = twitter.TwitterIE()
    twIE.set_downloader(yt_dlp.YoutubeDL())
    twid = twIE._match_id(url)
    status = twIE._call_api(
    'statuses/show/%s.json' % twid, twid, {
        'cards_platform': 'Web-12',
        'include_cards': 1,
        'include_reply_count': 1,
        'include_user_entities': 0,
        'tweet_mode': 'extended',
    })
    return status