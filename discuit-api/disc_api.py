import logging
from rest_adapter import RestAdapter
from exceptions import DiscuitAPIException
from models import *

class DiscuitAPI:
    def __init__(self, hostname: str = 'discuit.net/api', api_key: str = '', ssl_verify: bool = True,
                 logger: logging.Logger = None):
        
        self._rest_adapter = RestAdapter(hostname, api_key, ssl_verify, logger)
    
    def get_all_posts(self) -> Posts:
        """Gets most recent posts, site-wide.

        Returns:
            Posts: A list of Post objects.
        """
        result = self._rest_adapter.get(endpoint='posts')
        posts = Posts(**result.data)
        return posts
    
    def get_community_posts(self, community_id: str) -> Posts:
        """Gets most recent posts by Community ID

        Args:
            community_id (str): The ID of the community to get posts from.

        Returns:
            Posts: A list of Post objects.
        """
        result = self._rest_adapter.get(endpoint=f'posts?communityID={community_id}')
        posts = Posts(**result.data)
        return posts
    
    def get_post_by_id(self, post_id: str) -> Posts:
        """Get a Post object by Public ID
        Currently returns list of posts, even though its one.

        Args:
            post_id (str): The Public ID of the post (discuit.com/postId)

        Returns:
            Posts: List of Post objects.
        """
        # post ID should be the public ID
        # currently broken, as models are weird
        result = self._rest_adapter.get(endpoint=f'posts/{post_id}')
        post = Posts(**result.data)
        return post[0]
    
    def get_post_comments(self, post_id:str) -> Comments: 
        """Get comments on a post by Public ID

        Args:
            post_id (str): The Public ID of the post.

        Returns:
            Comments: A list of Comment objects
        """
        result = self._rest_adapter.get(endpoint=f'posts/{post_id}/comments')
        comments = Comments(**result.data)
        return comments

    def fetch_link_data(self, link: Link):
        link.data = self._rest_adapter.fetch_data(url=link.url)

    def get_communites(self) -> List[Community]:
        """Gets all communities, sitewide

        Returns:
            List[Community]: A list of community objects
        """
        results = self._rest_adapter.get(endpoint='communities')
        # this doesnt work for adding to list, result not iterable
        # cahnged, now missing positional args for Community class??
        communities = []
        for result in results.data:
            communities.append(Community(**result))
        return communities

    def get_community_by_id(self, community_id: str) -> Community:
        result = self._rest_adapter.get(endpoint=f'communities/{community_id}')
        community = Community(**result.data)
        return community

    def get_community_rules(self, community_id: str):
        pass

    def get_community_mods(self, community_id: str):
        pass

    def get_user_by_id(self, user_id: str):
        pass

    def get_user_by_username(self, username:str):
        pass
    

api = DiscuitAPI()

#res = api.get_community_posts("177a1ae4ee883ca82b22d914")
res = api.get_community_by_id('177a1ae4ee883ca82b22d914')

print(res) 