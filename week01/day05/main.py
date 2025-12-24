import requests
import pandas as pd

r1 = requests.get("https://jsonplaceholder.typicode.com/posts")
r2 = requests.get("https://jsonplaceholder.typicode.com/comments")
post = r1.json()
comment = r2.json()

df1 = pd.DataFrame(post)
df2 = pd.DataFrame(comment)
df3 = (df2.groupby("postId").size().reset_index(name="comment_count"))

fdf =  df1.merge(df3, left_on="id", right_on="postId", how="left")

fdf["comment_count"] = fdf["comment_count"].fillna(0)
fdf.to_csv("postscomment_count.csv", index=False)
