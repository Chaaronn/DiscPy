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
    

api = DiscuitAPI()

res = api.get_community_posts("17692e122def73f25bd757e0")

print(res.posts[0])