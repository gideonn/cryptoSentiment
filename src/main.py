import json
import praw

class redditData(Exception):

    def __init__(self):
        pass

    def getCredentials(self,fileLocation):
        with open(fileLocation, 'r') as f:
            credentials = json.load(f)

        #return a dict
        return credentials


    def auth(self,filePath):
        credentials = self.getCredentials(filePath)
        reddit = praw.Reddit(client_id=credentials['appID'],
                             client_secret=credentials['appSecret'],
                             user_agent='Crypto/0.1 by cryptobot123',
                             username=credentials['username'],
                             password=credentials['password'])

        return reddit

    def testReq(self, reddit):
        for submission in reddit.subreddit('litecoin').hot(limit=10):
            print("Score: {}, ID: {}. URL:{}, Title: {}".format(submission.score,submission.id,submission.url,submission.title))

if __name__ == '__main__':
    obj = redditData()
    reddit = obj.auth('config/config1.txt')
    obj.testReq(reddit)