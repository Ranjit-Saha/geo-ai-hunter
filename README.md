# 🛰️ GeoAI Specialist Hunter

**Automated Job Intelligence for the 2026 Space & Climate Tech Market**

## 📖 Overview
This is a specialized automation tool designed to hunt for high-priority roles in the **SAR (Synthetic Aperture Radar)**, **Climate Tech**, and **Deep Learning** sectors. It scans niche RSS feeds and sends real-time alerts to Telegram when matches are found for specific entities like **Pixxel, SatSure, and GalaxEye**.

```
geo-ai-hunter/
├── .github/
│   └── workflows/
│       └── hunt.yml      # GitHub Action logic
├── .gitignore            # Keeps things clean
├── main.py               # The core logic (The Brain)
├── README.md             # Project documentation
└── requirements.txt      # Dependencies (requests, feedparser)
```

## 🛠️ Technical Stack
- **Language:** Python 3.9+
- **Automation:** GitHub Actions (CRON)
- **Alerting:** Telegram Bot API
- **Data Sources:** Niche RSS feeds (AgTech, Climate, GIS)

## 🎯 Hunter Configuration
- **Primary Keywords:** SAR, Radar, GeoAI, Carbon Credits, Parametric Insurance, etc.
- **Secondary Keywords:** Remote Sensing, Computer Vision, Digital Twin, LiDAR.
- **Negative Filters:** Automatically skips management, sales, and internship roles to focus on Specialist positions.

## 🚀 Deployment
1. **Secrets:** Add `BOT_TOKEN` and `CHAT_ID` to your GitHub Repository Secrets.
2. **Action:** The hunter is configured to run every 6 hours via `.github/workflows/hunt.yml`.
3. **Manual Trigger:** Use the `workflow_dispatch` button in GitHub Actions to run a scan immediately.

---
*Developed by RnJt | Status: Active Deployment*
