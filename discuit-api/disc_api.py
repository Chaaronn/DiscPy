import logging
from rest_adapter import RestAdapter
from exceptions import DiscuitAPIException
from models import *

class DiscuitAPI:
    def __init__(self, hostname: str = 'discuit.net/api', api_key: str = '', ssl_verify: bool = True,
                 logger: logging.Logger = None):
        
        self._rest_adapter = RestAdapter(hostname, api_key, ssl_verify, logger)
    
    def get_all_posts(self) -> Posts:
        result = self._rest_adapter.get(endpoint='posts')
        posts = Posts(**result.data)
        return posts
    
    def get_community_posts(self, community_id: str = '') -> Posts:
        result = self._rest_adapter.get(endpoint=f'posts?communityID={community_id}')
        posts = Posts(**result.data)
        return posts
    
    def get_post_by_id(self, post_id: str) -> Posts:
        # post ID should be the public ID
        # currently broken, as models are weird
        result = self._rest_adapter.get(endpoint=f'posts/{post_id}')
        post = Posts(**result.data)
        return post[0]

    def fetch_link_data(self, link: Link):
        link.data = self._rest_adapter.fetch_data(url=link.url)
    

api = DiscuitAPI()

#res = api.get_community_posts("177a1ae4ee883ca82b22d914")
res = api.get_post_by_id("6yiiXeJt")

print(res)