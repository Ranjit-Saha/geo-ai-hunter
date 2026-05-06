import os
import requests
import feedparser
import time
from datetime import datetime

# RnJt's Job Assistant >> Creation Date: 06 May 2026
# --- 1. THE 2026 SPECIALIST CONFIG ---
PRIMARY_KEYWORDS = [
    "Remote", "Data", "Engineer",
    "SAR", "Radar", "Sentinel", "Satellite Imagery", "Carbon Credit", "Flood Detection", "Parametric Insurance", 
    "GeoAI", "Geospatial AI", "Earth Observation", "SatSure", "Pixxel", "GalaxEye", "Cropin", "DeHaat", "ICEYE", 
    "Capella Space", "Blue Sky Analytics", "Lemma Earth", "Varaha", "VANYA", "Sylvera (UK)", "RenewCred", "DeepMatrix",
    "Twyn", "Genesys International", "AgNext", "Intello Labs"
]

SECONDARY_KEYWORDS = [
    "Remote Sensing", "Computer Vision", "Deep Learning", 
    "Climate Tech", "AgTech", "AgriTech", "GIS Developer", 
    "Spatial Data Science", "Digital Twin", "LiDAR"
]

# Filtering out roles you aren't targeting (Management/Sales)
NEGATIVE_KEYWORDS = ["Senior", "Lead", "Manager", "Director", "Sales", "Intern", "Recruiter"]

# --- 2. THE GLOBAL & NICHE FEED HUB ---
# Note: Ensure these URLs point to the actual XML/RSS feed endpoints of these sites
RSS_FEEDS = [
    "https://weworkremotely.com",
    "https://remotive.com",
    "https://aijobs.net",
    "https://gisjobs.com",
    "https://climatetechlist.com"
]

def send_telegram_alert(job_title, job_link, priority="Normal"):
    token = os.environ.get("BOT_TOKEN")
    chat_id = os.environ.get("CHAT_ID")
    
    if not token or not chat_id:
        print("⚠️ Environment variables BOT_TOKEN or CHAT_ID are missing.")
        return

    header = "🔥 **HIGH PRIORITY MATCH**" if priority == "High" else "🛰 **GeoAI Match Found**"
    
    message = (
        f"{header}\n\n"
        f"**Role:** {job_title}\n"
        f"**Context:** IT + GIS Hybrid Specialist\n\n"
        f"🔗 [View & Apply Quickly]({job_link})"
    )
    
    # Corrected Telegram API URL
    url = f"https://telegram.org{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ Alert sent: {job_title}")
        else:
            print(f"❌ Telegram Error: {response.text}")
    except Exception as e:
        print(f"⚠️ Connection Error: {e}")

def check_jobs():
    print(f"🚀 Specialist Hunt Initialized: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    count = 0
    
    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                title = entry.get('title', '')
                link = entry.get('link', '')
                
                # Check for Negative Keywords first
                if any(n.lower() in title.lower() for n in NEGATIVE_KEYWORDS):
                    continue
                
                # Check for Primary (High Priority) Matches
                if any(p.lower() in title.lower() for p in PRIMARY_KEYWORDS):
                    send_telegram_alert(title, link, priority="High")
                    count += 1
                    time.sleep(1) 
                    continue
                
                # Check for Secondary Matches
                if any(s.lower() in title.lower() for s in SECONDARY_KEYWORDS):
                    send_telegram_alert(title, link, priority="Normal")
                    count += 1
                    time.sleep(1)
                    
        except Exception as e:
            print(f"📡 Skip Feed {feed_url} due to error: {e}")
            
    print(f"🎯 Total Specialist Opportunities Hooked: {count}")

if __name__ == '__main__':
    check_jobs()
