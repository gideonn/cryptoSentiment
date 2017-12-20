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

        #Create a subreddit instance for a given subreddit
        submission = reddit.subreddit('litecoin')

        #Loop through all the hot submissions
        for post in submission.hot(limit=1):
            print("Score: {}, ID: {}. URL:{}, Title: {}".format(post.score,post.id,post.url,post.title))

            #Expand all the comments
            post.comments.replace_more(limit=None)
            allComments = []

            #For each post, iterate through all comments
            for comment in post.comments.list():
                allComments.append(comment.body)


        print(len(allComments))

if __name__ == '__main__':
    obj = redditData()
    reddit = obj.auth('config/config1.txt')
    obj.testReq(reddit)