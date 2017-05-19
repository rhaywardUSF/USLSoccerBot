#This piece of code loops through the flair request messages, checks to see if any flair needs to be assigned, and assigns the flair to the user who made the comment

try:
    from PrintHelper import tPrint
    import praw
    import time
    import datetime
    from dateutil.relativedelta import relativedelta
    import logging
    from FlairTest import FlairList
    loggingCAFlair = logging.getLogger("loggingCAFlair")

    r = None;
    sr = None;
    #Get maximum amount of archived messages (180 days)
    REDDIT_ARCHIVE_AGE = 180
    messageCache = []
    requestFlairSubmission = None
    Me = None

    def run(reddit):
        global r
        global sr
        r = reddit
        loggingCAFlair.info("Start Check and Assign Flair")
        tPrint("Check and Assign Flair")
        # Get Unread PMs
        pms = r.get_unread(True, True)
        if pms is not None:
            for message in pms:
                messageSubject = message.subject.lower()
                messageBody = message.body
                authorName = message.author.name
                command = None
                subredditName = None
                # Check and see if the message subject contains 'assign flair'
                if messageSubject is not None and messageBody is not None and ("assign flair" in messageSubject) and len(messageBody) > 0:
                    messageSubjectArr = messageSubject.lower().split("-")
                    # If we have an assign flair, what subreddit is it for?
                    if messageSubjectArr is not None and len(messageSubjectArr) == 2:
                        command = messageSubjectArr[0].strip().lower()
                        subredditName = messageSubjectArr[1].strip()
                        if command == "assign flair" and subredditName is not None and len(subredditName) > 0 and authorName is not None:
                            #Now  that we have a subreddit, a redditor, and a flair request. Check if Flair Request is in our DB
                            sr = r.get_subreddit(subredditName)
                            redditor = r.get_redditor(authorName)
                            foundFlair = searchFlair(message.body, FlairList)
                            setFlair =  list(foundFlair)
                            ##If we found the flair in our DB, set the flair, and reply to the user
                            if sr is not None and redditor is not None and setFlair is not None and len(setFlair) > 0:
                                if not messageProcessed(message):
                                    sr.set_flair(redditor.name, setFlair[0]['flairLabel'], setFlair[0]['flairClass'])
                                    storeMessageId(message.id)
                                    message.mark_as_read()
                                    message.reply('Your flair was set to ' + setFlair[0]['flairClass'])
                                    tPrint('Flair ' + setFlair[0]['flairClass'] + ' assigned to ' + authorName);
                                
                            else:
                                message.mark_as_read()
                                message.reply('I wasn\'t able to read your message correctly, so I couldn\'t set your flair, sorry! Message /u/YourUserHere if you think this is a mistake')
                                
                        else:
                            message.mark_as_read()
                            message.reply('I wasn\'t able to read your message correctly, so I couldn\'t set your flair, sorry! Message /u/YourUserHere if you think this is a mistake')
                            
                    else:
                        message.mark_as_read()
                        message.reply('I wasn\'t able to find your subreddit')
                else:
                    print('Not a flair message, mark as read')
                    message.mark_as_read()
        else:
            tPrint("=== NO NEW PMS FOUND ===")

    def messageProcessed(message):
        if(message.id not in messageCache):
            return False
        else:
            return True

    def storeMessageId(messageId):
        messageCache.append(messageId)


    def searchFlair(flairClass, flairArray):
        return (flair for flair in flairArray if flair["flairClass"].lower() == flairClass.lower())
except Exception:
    print("Error in Check and Assign Flair")
    pass