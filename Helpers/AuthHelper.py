#Ex app_userAgent = 'MySoccerB0t v0.1'
app_userAgent = '<YourSoccerBotAgent>'
app_clientId = '<YourAppKey>'
app_appSecret = '<YourAppSecret>'
#Ex: app_callbackURI = 'http://127.0.0.1:65010/authorize_callback'
app_callbackURI = '<YourCallbackUri>'
app_scope = ['edit','flair','history', 'identity', 'modconfig', 'modcontributors', 'modflair', 'modlog', 'modposts', 'modself', 'modwiki', 'mysubreddits', 'privatemessages', 'read', 'report', 'save', 'submit', 'subscribe', 'vote', 'wikiedit', 'wikiread']

import praw
import OAuth2Util
from PrintHelper import tPrint

def login(configFile):
    tPrint("Logging In")
    r = praw.Reddit(app_userAgent)
    o = OAuth2Util.OAuth2Util(r, configfile=configFile) 
    o.refresh(force=True)
    tPrint("Logged In")
    return r