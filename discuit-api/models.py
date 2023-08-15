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
        self.user_deleted = user_deleted            # ??? 
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
        self.hotness = hotness                      # ???
        self.created_at = created_at                # When the post was created
        self.edited_at = edited_at                  # If it was edited, when
        self.last_activity_at = last_activity_at    # Time of last post activity 
        self.deleted = deleted                      # If post has been deleted
        self.deleted_content = deleted_content      # ???
        self.no_comments = no_comments              # Number of comments
        self.comments = comments                    # List of comments
        self.comments_next = comments_next          # ID for next stack of comments
        self.__dict__.update(kwargs)

class Posts:
    def __init__(self, posts: List[Post], next: str, **kwargs):
        self.posts = posts                          # List of post objects
        self.next = next                            # ID for next set of comments
        self.__dict__.update(kwargs)

'''
Post data model. 

https://discuit.net/api/posts?communityId=17692e122def73f25bd757e0

{
    'posts' : [                                             list
        {
            "id": "177b8f0c5378c9a2fb17f509",               str
            "type": "link",                                 str
            "publicId": "bSfp10ml",                         str
            "userId": "177a18d800357d19d2d73b91",           str
            "username": "Oggidahh",                         str
            "userGroup": "normal",                          str
            "userDeleted": false,                           bool
            "isPinned": false,                              bool
            "communityId": "17692e122def73f25bd757e0",      str
            "communityName": "general",                     str
            "communityProPic: {}                            dict
            "communityBannerImage : {}                      dict
            "title": "Call It Whatevahh",                   str
            "body": null,                                   str
            "link" :                                        dict
            {                                      
                "link" : "hhtps..."                         str
                "hostname" : "youtube.com"                  str
                "image" : {}                                dict
            }            
            "locked": false,                                bool
            "lockedBy": null,                               str
            "lockedAt": null,                               str
            "upvotes": 4,                                   int
            "downvotes": 0,                                 int
            "hotness": 376032970667,                        int
            "createdAt": "2023-08-15T12:42:48Z",            str
            "editedAt": null,                               str
            "lastActivityAt": "2023-08-15T12:42:48Z",       str
            "deleted": false,                               bool
            "deletedAt": null,                              str
            "deletedContent": false,                        bool
            "noComments": 0,                                int
            "comments": null,                               
            "commentsNext": null,                           
            "userVoted": null,
            "userVotedUp": null                         
        },
        {
            ---- NEXT POST ----
        }
    ],
    "next": "177b57b436c86781b3cc5710"                      str

}

'''     