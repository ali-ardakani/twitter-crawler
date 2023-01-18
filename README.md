# twitter-crawler
Twitter crawler using a specific word

## How to use

Install the requirements

```
pip install -r requirements.txt
```

### Method 1

```python
    # Create a Twitter crawler:
    >>> twitter_crawler = TwitterCrawler(bearer_token)
    
    # Get data with a specific keyword. It will return a list of tweets(default limit is 1):
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
```

### Method 2

```
python twitter.py --bearer_token <bearer_token> \
                  --keyword <keyword> --limit <limit> \
                  --kwargs <kwargs(ex: --kwargs lang=fa,since_id=123456789)> \
                  --output_path <output_path>
```