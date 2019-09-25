from instagram_web_api import Client, ClientCompatPatch, ClientError, ClientLoginError
import os, ssl
from datetime import datetime

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

web_api = Client(auto_patch=True, drop_incompat_keys=False)
user_feed_info = web_api.user_feed('5522879792', count=10)
insta_items = []
insta_items_details = []
for post in user_feed_info:
    url = post['node']['images']['standard_resolution']['url']
    text = post['node']['caption']['text']
    id = post['node']['id'].split('_')[0][-8:-1]
    short_code = post['node']['shortcode']
    comments_list = []
    post_created_time = datetime.fromtimestamp(int(post['node']['created_time']))
    days_from_post = (datetime.now() - post_created_time).days
    for comment in post['node']['edge_media_to_comment']['edges']:
        com_text = comment['node']['text']
        com_owner = comment['node']['owner']['username']
        com_created_time = datetime.fromtimestamp(int(comment['node']['created_at']))
        comments_list.append([com_text, com_owner, com_created_time])

    comments_count = post['node']['comments']['count']
    likes_count = post['node']['likes']['count']
    link = post['node']['link']
    insta_items.append([url, text, comments_count, likes_count, link, id])
    insta_items_details.append([url, text, comments_count, likes_count, link, id, comments_list, days_from_post])
    url = None
    text = None
