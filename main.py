import twitter
import time
print()

api = twitter.Api(consumer_key='ArEa5vPCaWESXBG4xq56qLSSs',
                      consumer_secret='yQPjcVW2ufTRHoU5LcdUH0FCcnRLtPkiKLHvrJTUOOqvAarGyy',
                      access_token_key='1363431429611356161-xboein4j6V17DiZIkjhOjVBD7kS4JJ',
                      access_token_secret='1PFJig0fSrw4sBl2IFQxuROyea6iKwuepPOMcY0YYHqID')

tweets = 0
searchs = 0
limitTweets = 300
limitSearchs = 180

def postStatus(update, inReplyTo, media):
    global tweets
    tweets += 1
    api.PostUpdate(update, media=media, in_reply_to_status_id=inReplyTo)

def search(research, howMany):
    global searchs
    searchs += 1
    searchResults = api.GetSearch(raw_query="q="+research+"&result_type=recent&count="+howMany)
    for search in searchResults:
            postStatus("@" + search.user.screen_name + "...", search.id, "repas.jpg")
           
def start():
    global searchs
    global tweets
    global limitTweets
    global limitSearchs
    stop = False
    while(not stop):
        try:
            search("g faim", "50")
        except:
            print("Erreur (on arrete)")
            stop = True
        if(searchs >= limitSearchs):
            print("Limite atteinte de recherche")
            stop = True
        elif(tweets >= limitTweets):
            print("Limite atteinte des tweets")
            stop = True
        print(f"On a tweeté {str(tweets)} fois !")
        time.sleep(5)
    print("Finis, il faut attendre 3H avant de reprendre.")

start()








    