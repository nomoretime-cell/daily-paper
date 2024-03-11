import feedparser
import requests

# cs, physics, math, econ
category = "cs.AI"
# feed_url = f"http://rss.arxiv.org/rss/{category}"
feed_url = f"http://export.arxiv.org/rss/{category}"


class arXiv:
    def __init__(self, feed_url):
        self.feed = feedparser.parse(feed_url)

    def get_pdf_link(self, link):
        return link.replace("abs", "pdf")

    def download_pdf(self, url, filename):
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"Downloaded '{filename}'.")
        else:
            print(f"Failed to download file from {url}.")

    def process(self):
        print(f"arXiv feed title - {self.feed.feed.title}\n")
        print(f"arXiv feed published time - {self.feed.feed.published}\n")
        for entry in self.feed.entries:
            print(f"title: {entry.title}")
            print(f"author: {entry.author}")
            print(f"summary: {entry.summary}")
            print(f"link: {entry.link}")
            print("-" * 100)
            print()
            pdf_url = self.get_pdf_link(entry.link)
            if pdf_url:
                arxiv_id = entry.id.split("/")[-1]
                filename = f"{arxiv_id}.pdf"
                self.download_pdf(pdf_url, filename)


if __name__ == "__main__":
    arxiv = arXiv(feed_url)
    arxiv.process()
