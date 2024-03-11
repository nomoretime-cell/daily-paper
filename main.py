import feedparser
from datetime import datetime, timedelta

# 构造arXiv的RSS订阅源URL，这里以计算机科学为例
category = "cs"
feed_url = f"http://export.arxiv.org/rss/{category}"

# 解析订阅源
feed = feedparser.parse(feed_url)

# 获取一周前的日期
one_week_ago = datetime.now() - timedelta(days=7)

print(f"arXiv论文 - {feed.feed.title}\n")

# 遍历并打印最近一周的条目
for entry in feed.entries:
    print(f"标题: {entry.title}")
    print(f"链接: {entry.link}")
    print()
