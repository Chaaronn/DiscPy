from typing import Dict, List, Optional
from datetime import datetime
from exceptions import DiscuitAPIException
import os

class Result:
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        """Results returned from the low-level adapter.

        Args:
            status_code (int): Standard HTTP status code
            message (str, optional): Human readable result. Defaults to ''.
            data (List[Dict], optional): Python list of dictionaries. Defaults to None.
        """
        self.status_code = status_code
        self.message = str(message)
        self.data = data if data else []

class Link:
    def __init__(self, url: str, hostname: str, data: bytes = bytes(), **kwargs):
        self.url = url                              # URL of the link
        self.hostname = hostname                    # Hostname from the link
        self.data = data
        self.__dict__.update(kwargs)

    def save_to(self, path:str = './', file_name: str = ''):
        '''
        This should save the link contents to file. 
        '''
        if not self.data:
            raise DiscuitAPIException("No data to save")
        try:
            save_file_name = file_name if file_name else self.url.split('/')[-1]
            save_path = os.path.join(path, save_file_name)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(self.data)
        except Exception as e:
            raise DiscuitAPIException(str(e)) from e

class Post:
    def __init__(self, id: str, type: str, public_id: str, user_id: str, username: str, 
                 user_group: str, user_deleted: bool, is_pinned: bool, community_id: str, 
                 community_name: str, title: str, body: Optional[str], link: Optional[Link], 
                 locked: bool, locked_by: Optional[str], locked_at: Optional[datetime], 
                 upvotes: int, downvotes: int, hotness: int, created_at: datetime, edited_at: datetime, 
                 last_activity_at: datetime, deleted: bool, deleted_content: bool, no_comments: int, 
                 comments: Optional[List], comments_next: Optional[str], **kwargs):
        
        self.id = id                                # unique post ID
        self.type = type                            # type of post (either link or text)
        self.public_id = public_id                  # public ID of post
        self.user_id = user_id                      # ID of user who created post
        self.username = username                    # username of user who submitted
        self.user_group = user_group                # admin, mod, or normal
        self.user_deleted = user_deleted            # if the users account is deleted
        self.is_pinned = is_pinned                  # if the post is pinned
        self.community_id = community_id            # ID of the community the post is in
        self.community_name = community_name        # Name of community post is in
        self.title = title                          # Title of post
        self.body = body                            # Body of post. If post is a link, this will be null
        self.link = link                            # Link submitted for post
        self.locked = locked                        # If the post is locked
        self.locked_by = locked_by                  # User of who locked it
        self.locked_at = locked_at                  # Time/Date when it was locked
        self.upvotes = upvotes                      # Number of upvotes
        self.downvotes = downvotes                  # Number of downvotes
        self.hotness = hotness                      # Used to order by 'hot'
        self.created_at = created_at                # When the post was created
        self.edited_at = edited_at                  # If it was edited, when
        self.last_activity_at = last_activity_at    # Time of last post activity 
        self.deleted = deleted                      # If post has been deleted
        self.deleted_content = deleted_content      # If true, everything has been deleted
        self.no_comments = no_comments              # Number of comments
        self.comments = comments                    # List of comments
        self.comments_next = comments_next          # ID for next stack of comments
        self.__dict__.update(kwargs)

class Posts:
    def __init__(self, posts: List[Post], next: str, **kwargs):
        self.posts = posts                          # List of post objects
        self.next = next                            # ID for next set of posts
        self.__dict__.update(kwargs)

class Image:
    def __init__(self, mimetype: str, width: int, height: int, size: int, average_color: str, 
                 url: str, **kwargs):
        self.mimetype = mimetype                    # seems to be image/jpeg for most
        self.width = width                          # width of image
        self.height = height                        # height of image
        self.size = size                            # overall image size
        self.average_color = average_color          # average colour in the image
        self.url = url                              # url of stored image
        self.__dict__.update(kwargs)

class CommunityRule:
    def __init__(self, id: int, rule: str, description: Optional[str], community_id: str, z_index: int, 
                 created_by: str, created_at: datetime, **kwargs):
        self.id = id                                # ID of rule
        self.rule = rule                            # The actual rule
        self.description = description              # Could be null
        self.community_id = community_id            # ID of community its a rule in
        self.z_index = z_index                      # Determines rule ordering
        self.created_by = created_by                # User who created the rule
        self.created_at = created_at                # When it was created
        self.__dict__.update(kwargs)

class User:
    def __init__(self, id: str, username: str, email: None, email_confirmed_at: None, 
                 about_me: str, points: int, is_admin: bool, no_posts: int, no_comments: int, 
                 created_at: datetime, deleted_at: None, banned_at: None, is_banned: bool, 
                 notifications_new_count: int, modding_list: List, **kwargs):
        self.id = id                                            # User ID
        self.username = username                                # Username
        self.email = email                                      # Can be null
        self.email_confirmed_at = email_confirmed_at            # Can be null
        self.about_me = about_me                                # About me description
        self.points = points                                    # Points?
        self.is_admin = is_admin                                # If the User is a site admin
        self.no_posts = no_posts                                # Number of posts made by user
        self.no_comments = no_comments                          # Number of comments made by user
        self.created_at = created_at                            # Datetime when the account was created
        self.deleted_at = deleted_at                            # Datetime when it was deleted
        self.banned_at = banned_at                              # Datetime when it was banned
        self.is_banned = is_banned                              # If the user is banned
        self.notifications_new_count = notifications_new_count  # Number of new notifications user has
        self.modding_list = modding_list                        # List of communities the user mods
        self.__dict__.update(**kwargs)


class Community:
    def __init__(self, id: str, user_id: str, name: str, nsfw: bool, about: str, no_members: int, 
                 pro_pic: Image, banner_image: Image, created_at: datetime, deleted_at: Optional[datetime], 
                 user_joined: Optional[bool], user_mod: Optional[bool], mods: Optional[List[User]], 
                 rules: Optional[List[CommunityRule]], reports_details: List[Dict], **kwargs):
        self.id = id                                # Community ID
        self.user_id = user_id                      # ID of user who created community
        self.name = name                            # Community name (i.e., formula1, chess)
        self.nsfw = nsfw                            # If community is NSFW
        self.about = about                          # Description of communiity
        self.no_members = no_members                # How many users have joined
        self.pro_pic = pro_pic                      # Image object of the photo
        self.banner_image = banner_image            # Image object
        self.created_at = created_at                # Datetime the community was created
        self.deleted_at = deleted_at                # Datetime it was deleted
        self.user_joined = user_joined              # If the current AUTH user is subbed
        self.user_mod = user_mod                    # If the current auth user is a mod
        self.mods = mods                            # List of users who are mods
        self.rules = rules                          # List of CommunityRules
        self.reports_details = reports_details      # List of reports to the community
        self.__dict__.update(kwargs)

class Comment:
    def __init__(self, id: str, post_id: str, post_public_id: str, community_id: str, 
                 community_name: str, user_id: str, username: str, user_group: str, 
                 user_deleted: bool, parent_id: Optional[str], depth: int, no_replies: int, 
                 no_replies_direct: int, ancestors: Optional[List[str]], body: str, 
                 upvotes: int, downvotes: int, created_at: datetime, edited_at: Optional[datetime], 
                 deleted_at: Optional[datetime], user_voted: Optional[bool], user_voted_up: Optional[bool], 
                 post_deleted: bool, **kwargs):
        self.id = id                                # ID of comment
        self.post_id = post_id                      # Post ID the comment is on
        self.post_public_id = post_public_id        # Public post ID (discuit.com/postID)
        self.community_id = community_id            # Community ID comment is in
        self.community_name = community_name        # Community Name
        self.user_id = user_id                      # User ID who made the comment
        self.username = username                    # USername who made the comment
        self.user_group = user_group                # Admin, mod, normal
        self.user_deleted = user_deleted            # If author accoutn is deleted
        self.parent_id = parent_id                  # Parent comment ID, can be null
        self.depth = depth                          # Top-most comments have depth of 0
        self.no_replies = no_replies                # Total number of replies to the comment
        self.no_replies_direct = no_replies_direct  # Number of direct replies
        self.ancestors = ancestors                  # List of comment IDs, starting at topmost
        self.body = body                            # Comment body
        self.upvotes = upvotes                      # Number of up
        self.downvotes = downvotes                  # Number of down
        self.created_at = created_at                # Datetime it was created
        self.edited_at = edited_at                  # Datetime edited, can be null
        self.deleted_at = deleted_at                # Datetime deleted, can be null
        self.user_voted = user_voted                # If currently auth'd user voted 
        self.user_voted_up = user_voted_up          # If auth user voteed up
        self.post_deleted = post_deleted            # If the post the comment is on is delted
        self.__dict__.update(kwargs)


class Comments:
    comments: List[Comment]
    next: None

    def __init__(self, comments: List[Comment], next: None) -> None:
        self.comments = comments
        self.next = next
