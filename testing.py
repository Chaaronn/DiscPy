api = DiscuitAPI()

test_comm_id = '177a1ae4ee883ca82b22d914'
test_post_public_id = 'EBUwou3i'
test_user_id = '1779da1086fb65b89c3407e3'




#res = api.get_all_posts()                          WORKS
#res = api.get_communites()                         WORKS
#res = api.get_community_by_id(test_comm_id)        WORKS
#res = api.get_community_mods(test_comm_id)         WORKS
#res = api.get_community_posts(test_comm_id)        Returns diff community posts
#res = api.get_community_rules(test_comm_id)        WORKS
#res = api.get_post_by_id(test_post_public_id)      WORKS
#res= api.get_post_comments(test_post_public_id)    WORKS
#res = api.get_user_by_username('catwith2rooks')    WORKS
print(res)