from twython import TwythonStreamer

# Search terms
TERMS = '#yes'



# Twitter application authentication
APP_KEY = '4esOINzdxaabf9T78mYIYV5OZ'
APP_SECRET = 'BW7OOJ8HY8PlwKkahnfL7mQUX7kG6aoAIJhIIR30AB9BU3g9uE'
OAUTH_TOKEN = '115716352-aDghyUPSUk3ZNXVtiL4OwMvNyYvSTsoqp9RuXNTF'
OAUTH_TOKEN_SECRET = 'QtxOqPcrA3pgY5iwxZRMiNnwu9pGjdudnXmCh00H6XX8X'


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data

# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(follow='115716352')
# stream.user()
# Read the authenticated users home timeline
# (what they see on Twitter) in real-time
# stream.site(follow='twitter')