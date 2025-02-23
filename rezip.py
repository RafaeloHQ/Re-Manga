import praw
import os
import zipfile
import re
from dotenv import load_dotenv


load_dotenv("API.env")

id=os.getenv("CLIENT_ID")
secret=os.getenv("CLIENT_SECRET")

reddit = praw.Reddit(
    client_id = id,
    client_secret = secret,
    user_agent = "Re-Manga Reddit Post Retrieval Script by /u/Leather_Flan5071",
)

def retrieveTitle(url):
     import unicodedata
     try:
          submission = reddit.submission(url=url)
          title=submission.title
          title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
          title = re.sub(r'[:"/\\|?*]', "-", title)
          title = re.sub(r'[<>]', "", title)
          title = title.strip()
          return title
          

     except Exception as e:
          print(f"[Reddit] Error retrieving title: {e}")
          exit(1)

def cbzize(dir,archive_name): #compress the directory
     with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as archiveZ:
          for root, _, files in os.walk(dir):
               for file in files:
                    archiveZ.write(os.path.join(root, file), arcname=file)
               

def differentiateOS(dir):
     if os.name == "nt":
          dir = os.path.abspath(dir)
          return dir


def main():
     import sys

     if len(sys.argv) != 3: 
          print("[Rezip]: Usage: python rezip.py <reddit URL> <Destination>")
          sys.exit(1)
     link = sys.argv[1]
     archive = differentiateOS(sys.argv[2])

     name = retrieveTitle(link)
     print(name)
     cbzize(archive, name + '.cbz')
     

     
if __name__ == '__main__':
     main()