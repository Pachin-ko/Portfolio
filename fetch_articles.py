import feedparser
import datetime
import re

# === Sources RSS sur le Quantum Computing ===
FEEDS = [
    {
        "name": "MIT Technology Review – Quantum",
        "url": "https://www.technologyreview.com/feed/",
        "keyword": "quantum"
    },
    {
        "name": "Quanta Magazine",
        "url": "https://api.quantamagazine.org/feed/",
        "keyword": "quantum"
    },
    {
        "name": "IBM Research Blog",
        "url": "https://research.ibm.com/blog/rss.xml",
        "keyword": "quantum"
    },
    {
        "name": "Nature – Quantum Information",
        "url": "https://www.nature.com/npjqi.rss",
        "keyword": None  # Tout le feed est pertinent
    },
    {
        "name": "Physics Today",
        "url": "https://pubs.aip.org/rss/site_1000043/1000024.xml",
        "keyword": "quantum"
    },
    {
        "name": "Hacker News – Quantum",
        "url": "https://hnrss.org/newest?q=quantum+computing",
        "keyword": None
    },
]

MAX_ARTICLES_PER_SOURCE = 5
DAYS_BACK = 7  # Articles des 7 derniers jours


def fetch_articles():
    all_articles = []
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=DAYS_BACK)

    for feed_info in FEEDS:
        feed = feedparser.parse(feed_info["url"])
        count = 0

        for entry in feed.entries:
            if count >= MAX_ARTICLES_PER_SOURCE:
                break

            # Filtrage par mot-clé si nécessaire
            if feed_info["keyword"]:
                text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
                if feed_info["keyword"].lower() not in text:
                    continue

            # Filtrage par date
            published = entry.get("published_parsed") or entry.get("updated_parsed")
            if published:
                pub_date = datetime.datetime(*published[:6], tzinfo=datetime.timezone.utc)
                if pub_date < cutoff:
                    continue
                date_str = pub_date.strftime("%d %b %Y")
            else:
                date_str = "Date inconnue"

            all_articles.append({
                "source": feed_info["name"],
                "title": entry.get("title", "Sans titre"),
                "link": entry.get("link", "#"),
                "date": date_str,
            })
            count += 1

    return all_articles


def generate_readme(articles):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%d %B %Y à %H:%M UTC")

    # Grouper par source
    by_source = {}
    for a in articles:
        by_source.setdefault(a["source"], []).append(a)

    lines = [
        "# ⚛️ Veille Quantum Computing",
        "",
        f"> 🔄 Mise à jour automatique — dernière actualisation : **{now}**",
        "",
        "Cette page recense automatiquement les derniers articles sur l'informatique quantique,",
        "agrégés depuis des sources académiques, tech et communautaires.",
        "",
        "---",
        "",
    ]

    if not articles:
        lines.append("*Aucun article trouvé cette semaine. Réessaie dans quelques jours !*")
    else:
        for source, items in by_source.items():
            lines.append(f"## 📰 {source}")
            lines.append("")
            for item in items:
                lines.append(f"- [{item['title']}]({item['link']}) — *{item['date']}*")
            lines.append("")

    lines += [
        "---",
        "",
        "## 📡 Sources suivies",
        "",
    ]
    for feed in FEEDS:
        lines.append(f"- [{feed['name']}]({feed['url']})")

    lines += [
        "",
        "---",
        "",
        "*Veille générée automatiquement avec Python + GitHub Actions.*",
    ]

    return "\n".join(lines)


def generate_json(articles):
    import json
    data = {
        "last_updated": datetime.datetime.now(datetime.timezone.utc).strftime("%d %B %Y à %H:%M UTC"),
        "articles": articles
    }
    with open("articles.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("articles.json généré avec succès !")


if __name__ == "__main__":
    print("Récupération des articles...")
    articles = fetch_articles()
    print(f"{len(articles)} articles trouvés.")

    readme_content = generate_readme(articles)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README.md mis à jour avec succès !")
    generate_json(articles)
