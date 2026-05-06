import os
import requests
import feedparser
import time

# --- SPECIALIST STRATEGY CONFIG ---
KEYWORDS = [
    "Geospatial AI", "SAR", "Remote Sensing", "Computer Vision", 
    "Satellite Imagery", "Deep Learning", "Carbon Credit", 
    "Parametric Insurance", "Earth Observation", "GeoAI"
]

NEGATIVE_KEYWORDS = ["Senior", "Lead", "Manager", "Sales", "Recruiter", "Director"]

RSS_FEEDS = [
    "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "https://remotive.com/remote-jobs/feed",
    "https://workingnomads.com"
]

def send_telegram_alert(job_title, job_link):
    token = os.environ.get("BOT_TOKEN")
    chat_id = os.environ.get("CHAT_ID")
    
    message = (
        f"🛰 **GeoAI Specialist Match!**\n\n"
        f"**Role:** {job_title}\n"
        f"[👉 Apply Now]({job_link})"
    )
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

def check_jobs():
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = entry.title
            if any(k.lower() in title.lower() for k in KEYWORDS):
                if not any(n.lower() in title.lower() for n in NEGATIVE_KEYWORDS):
                    send_telegram_alert(title, entry.link)

if __name__ == '__main__':
    check_jobs()
