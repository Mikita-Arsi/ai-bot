import time
from db import models as m


async def delete_comments(timeout: int):
    tn = time.time()
    comments = await m.Comment.objects.filter().all()
    for comment in comments:
        print(tn - comment.time)
        if tn - comment.time > timeout:
            await m.Comment.objects.delete(comment_id=comment.comment_id)
