import requests
from bs4 import BeautifulSoup
import csv

def get_ev_download_link(season, episode):
    url = f"https://watchfamilyguyonline.com/episode/family-guy-{season}x{episode}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ScraperBot/1.0)"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    video_section = soup.find("div", class_="video-options-pla")
    if not video_section:
        print(f"No video section found for S{season}E{episode}.")
        return None

    iframe = video_section.find("iframe")
    if not iframe:
        print(f"No iframe found for S{season}E{episode}.")
        return None

    ev_embed_link = iframe.get("src")
    if not ev_embed_link:
        print(f"No src found in iframe for S{season}E{episode}.")
        return None

    # Convert embed link to download link
    ev_download_link = ev_embed_link.replace("/embed/", "/download/")
    return ev_download_link

def main():
    input_csv = "episodes.csv"
    output_csv = "ev_download_links.csv"

    with open(input_csv, newline='') as csvfile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(csvfile)
        writer = csv.writer(outfile)
        writer.writerow(['season', 'episode', 'ev_download_link'])

        for row in reader:
            season = row['season']
            episode = row['episode']
            link = get_ev_download_link(season, episode)
            writer.writerow([season, episode, link if link else "NOT FOUND"])
            print(f"S{season}E{episode}: {link if link else 'NOT FOUND'}")

if __name__ == "__main__":
    main()