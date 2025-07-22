# Family Guy EV Download Link Scraper

This Python script scrapes [watchfamilyguyonline.com](https://watchfamilyguyonline.com/) for **EV server download links** for Family Guy episodes.  
It reads a list of season and episode numbers from a CSV file, fetches each episode’s page, extracts the EV server embed link, and converts it to a direct download link.

## Features

- **Batch processing:** Input multiple episodes via CSV.
- **Automatic conversion:** Converts EV embed links to download links.
- **CSV output:** Saves results in a new CSV file for easy access.

---

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies with:
```bash
pip install requests beautifulsoup4
```

---

## Usage

1. **Prepare your input CSV file**  
   Create a file named `episodes.csv` with the following format:

   ```csv
   season,episode
   7,13
   7,14
   8,1
   ```

2. **Run the script**

   ```bash
   python familyguy_ev_scraper.py
   ```

3. **Check the output**  
   The script will create a file called `ev_download_links.csv` with this format:

   ```csv
   season,episode,ev_download_link
   7,13,https://movearnpre.com/download/47di79o7bn5w
   7,14,https://movearnpre.com/download/abc123xyz456
   8,1,NOT FOUND
   ```

---

## How it Works

- For each episode in your CSV, the script:
  1. Fetches the episode page from `watchfamilyguyonline.com`.
  2. Locates the EV server embed link (the first video server).
  3. Converts the embed URL to a download URL by replacing `/embed/` with `/download/`.
  4. Writes the result to the output CSV.

---

## Notes

- This script is for educational purposes only.
- The availability and legality of these links depend on your region and local laws.
- Please use responsibly and do not overload the website with requests.

---

## Troubleshooting

- If you get `NOT FOUND` for some episodes, the EV server may not be available for that episode, or the site structure may have changed.
- Make sure your input CSV is correctly formatted and that you have a stable internet connection.

---

**Enjoy!**  
