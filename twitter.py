# Twitter crawler using a specific word

import tweepy
from crawler import CrawlerInterface


class TwitterCrawler(CrawlerInterface):
    """
    Crawl data from Twitter
    
    :param bearer_token: bearer token for Twitter API
    
    Example:
    --------
    
    Create a Twitter crawler:
    >>> twitter_crawler = TwitterCrawler(bearer_token)
    
    Get data with a specific keyword. It will return a list of tweets(default limit is 1):
    >>> tweets = twitter_crawler.get_data_with_keyword(keyword='python')
    >>> tweets
    [{
        'tweet_id': int,
        'user_id': int,
        'user_name': str,
        'text': str,
        'date': str(YYYY-MM-DD HH:MM:SS),
        'retweet_count': int,
        'favorite_count': int,
        'hashtags': list[dict],
        'mentions': list[dict],
        'urls': list[dict]
    }]
    
         
    """

    def __init__(self, bearer_token: str):
        auth = tweepy.OAuth2BearerHandler(bearer_token)
        self.api = tweepy.API(auth)

    def get_data_with_keyword(self, keyword: str, limit: int = 1, **kwargs):
        """
        Get data from Twitter with a specific keyword
        
        :param keyword: keyword to search
        :param limit: number of tweets to get
        :param kwargs: other parameters for search_tweets method(optional)
        :return: list of tweets
            - tweet_id: id of the tweet(int)
            - user_id: id of the user(int)
            - user_name: name of the user(str)
            - text: text of the tweet(str)
            - date: date of the tweet(str(YYYY-MM-DD HH:MM:SS))
            - retweet_count: number of retweets(int)
            - favorite_count: number of favorites(int)
            - hashtags: hashtags in the tweet(list[dict])
            - mentions: mentions in the tweet(list[dict])
            - urls: urls in the tweet(list[dict])
             
        """

        tweets = tweepy.Cursor(self.api.search_tweets, q=keyword,
                               **kwargs).items(limit)
        tweets = [{
            'tweet_id': tweet.id,
            'user_id': tweet.author.id,
            'user_name': tweet.author.screen_name,
            'text': tweet.text,
            'date': tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'retweet_count': tweet.retweet_count,
            'favorite_count': tweet.favorite_count,
            'hashtags': tweet.entities['hashtags'],
            'mentions': tweet.entities['user_mentions'],
            'urls': tweet.entities['urls']
        } for tweet in tweets]
        return tweets


if __name__ == "__main__":
    import sys
    import json
    
    kwargs = {}
    
    bearer_token = sys.argv[sys.argv.index('--bearer_token') + 1]
    
    kwargs['keyword'] = sys.argv[sys.argv.index('--keyword') + 1]
    if '--limit' in sys.argv:
        kwargs['limit'] = int(sys.argv[sys.argv.index('--limit') + 1])
    if '--kwargs' in sys.argv:
        kwargs_input = sys.argv[sys.argv.index('--kwargs') + 1]
        kwargs.update({
            k: v
            for k, v in [kv.split('=') for kv in kwargs_input.split(',')]
        })

    if '--output_path' in sys.argv:
        output_path = sys.argv[sys.argv.index('--output_path') + 1]
    else:
        output_path = 'output.json'

    # Create a Twitter crawler
    twitter_crawler = TwitterCrawler(bearer_token)
    tweets = twitter_crawler.get_data_with_keyword(**kwargs)
    
    # Save the tweets to a json file
    with open(output_path, 'w') as f:
        json.dump(tweets, f, ensure_ascii=False)
