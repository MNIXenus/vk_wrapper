from group import Group
from user import User
group = Group(124823913)
posts = group.wall.get_all()
posts_id_list = []
for batch in posts:
    for post in batch['items']:
        posts_id_list.append(post['id'])

comments_list = []

for post_id in posts_id_list[7:10]:
    comments_batch = group.wall.Comments(group.wall.owner_id, post_id)
    for comment in comments_batch.get_all()[0]['items']:
        comments_list.append({'comment': comment['text'], 'id': comment['from_id']})

print(comments_list)
