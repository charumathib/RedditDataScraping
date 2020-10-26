import praw
import pandas as pd

posts = []
reddit = praw.Reddit(client_id='q2HbpMCMhoprPg',
                     client_secret='3dDOnoML5V_4xG3K8B0QeLIgxVQ', user_agent='Reddit WebScraping')

ivies = {
    'Yale': 0,
    'Princeton': 0,
    'Dartmouth': 0,
    'Cornell': 0,
    'Upenn': 0,
    'BrownU': 0,
    'Columbia': 0
}

for school in ivies:
    hot_posts = reddit.subreddit(school).hot(limit=10000)
    for post in hot_posts:
        if('harvard' in post.title.lower()):
            ivies[school] += 1
            posts.append([post.title, post.score, post.id, post.subreddit,
                          post.url, "TITLE", post.num_comments, post.selftext, post.created])

        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            if ('harvard' in comment.body.lower().split()):
                ivies[school] += 1
                posts.append([post.title, post.score, post.id, post.subreddit,
                              post.url, comment.body, post.num_comments, post.selftext, post.created])

posts = pd.DataFrame(posts, columns=[
    'title', 'score', 'id', 'subreddit', 'url', 'text', 'num_comments', 'body', 'created'])

for entry, freq in ivies.items():
    print(entry, freq)

posts.to_csv(r'reddit_posts_final.csv')
