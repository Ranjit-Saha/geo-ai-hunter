import os
import requests
import feedparser
import time
from datetime import datetime

# RnJt's Job Assistant >> Specialized GeoAI Target Matrix
# --- 1. KEYWORD FILTERS ---
PRIMARY_KEYWORDS = [
    "SAR", "Radar", "Sentinel", "Satellite Imagery", "Carbon Credit", "Flood Detection", "Parametric Insurance", 
    "GeoAI", "Geospatial AI", "Earth Observation", "SatSure", "Pixxel", "GalaxEye", "Cropin", "DeHaat", "ICEYE", 
    "Capella Space", "Blue Sky Analytics", "Lemma Earth", "Varaha", "VANYA", "Sylvera", "RenewCred", "DeepMatrix",
    "Twyn", "Genesys International", "AgNext", "Intello Labs"
]

SECONDARY_KEYWORDS = [
    "Remote Sensing", "Computer Vision", "Deep Learning", 
    "Climate Tech", "AgTech", "AgriTech", "GIS Developer", 
    "Spatial Data Science", "Digital Twin", "LiDAR"
]

NEGATIVE_KEYWORDS = ["Senior", "Lead", "Manager", "Director", "Sales", "Intern", "Recruiter"]

# --- 2. LIVE OPERATIONAL RSS FEED ENDPOINTS (FIXED TO RAW XML DATA) ---
RSS_FEEDS = [
    "https://weworkremotely.com/categories/remote-data-science-jobs.rss",
    "https://remotive.com/api/remote-jobs/feed",
    "https://aijobs.net/feed/",
    "https://climatetechlist.com/feed.xml"
]

def send_telegram_alert(job_title, job_link, priority="Normal"):
    token = os.environ.get("BOT_TOKEN")
    chat_id = os.environ.get("CHAT_ID")

    if not token or not chat_id:
        print("⚠️ Configuration Error: Environment variables BOT_TOKEN or CHAT_ID are missing.")
        return

    # Clean token to ensure 'bot' prefix is handled seamlessly
    token_str = str(token).strip()
    if not token_str.startswith("bot"):
        bot_endpoint = f"bot{token_str}"
    else:
        bot_endpoint = token_str

    header = "🔥 **HIGH PRIORITY MATCH**" if priority == "High" else "🛰 **GeoAI Match Found**"

    message = (
        f"{header}\n\n"
        f"**Role:** {job_title}\n"
        f"**Context:** IT + GIS Hybrid Specialist\n\n"
        f"🔗 [View & Apply Quickly]({job_link})"
    )

    # FIXED: True Telegram API Subdomain address
    url = f"https://api.telegram.org/{bot_endpoint}/sendMessage"
    payload = {"chat_id": str(chat_id).strip(), "text": message, "parse_mode": "Markdown"}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ Alert dispatched successfully: {job_title}")
        else:
            print(f"❌ Telegram Gateway Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"⚠️ System Network Exception: {e}")

def check_jobs():
    print(f"🚀 Specialist Hunt Initialized: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    count = 0

    for feed_url in RSS_FEEDS:
        try:
            print(f"📡 Parsing Core Stream: {feed_url}")
            feed = feedparser.parse(feed_url)
            
            if not feed.entries:
                print(f"⚠️ Target structure empty or skipped: {feed_url}")
                continue
                
            for entry in feed.entries:
                title = entry.get('title', '')
                link = entry.get('link', '')

                # Filter out management/sales
                if any(n.lower() in title.lower() for n in NEGATIVE_KEYWORDS):
                    continue

                # Primary target matches
                if any(p.lower() in title.lower() for p in PRIMARY_KEYWORDS):
                    send_telegram_alert(title, link, priority="High")
                    count += 1
                    time.sleep(1) 
                    continue

                # Secondary target matches
                if any(s.lower() in title.lower() for s in SECONDARY_KEYWORDS):
                    send_telegram_alert(title, link, priority="Normal")
                    count += 1
                    time.sleep(1)

        except Exception as e:
            print(f"📡 Feed read interruption at {feed_url}: {e}")

    print(f"🎯 Total Specialist Opportunities Hooked: {count}")

if __name__ == '__main__':
    check_jobs()
