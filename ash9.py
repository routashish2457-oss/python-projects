import requests
import time
import csv

def get_reddit_posts(query, subreddit="", size=10):
    url = "https://api.pushshift.io/reddit/search/submission/"
    params = {
        "q": query,
        "subreddit": subreddit or None,
        "size": size,
        "sort": "desc",
        "sort_type": "created_utc"
    }
    print(f"Fetching posts with query='{query}' subreddit='{subreddit}'")
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json().get("data", [])
        print(f"Found {len(data)} posts")
        return data
    else:
        print("Error:", response.status_code)
    return []

def get_comments_for_post(post_id, size=5):
    url = "https://api.pushshift.io/reddit/search/comment/"
    params = {
        "link_id": f"t3_{post_id}",
        "size": size
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    return []

def scrape_and_save(query, subreddit="", post_limit=10, comment_limit=5, output_file="reddit_data.csv"):
    posts = get_reddit_posts(query, subreddit, size=post_limit)
    if not posts:
        print("No posts found. Try using a broader query or no subreddit.")
        return

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Post Title", "Post Text", "Post URL", "Comment"])

        for post in posts:
            title = post.get("title", "")
            selftext = post.get("selftext", "")
            post_id = post.get("id", "")
            url = f"https://www.reddit.com{post.get('permalink', '')}"

            print(f"📌 Post: {title[:60]}...")

            comments = get_comments_for_post(post_id, size=comment_limit)
            if not comments:
                writer.writerow([title, selftext, url, ""])
            else:
                for comment in comments:
                    comment_text = comment.get("body", "")
                    writer.writerow([title, selftext, url, comment_text])
            time.sleep(1)

    print(f"\n✅ Data saved to {output_file}")

# Run the scraper
if __name__ == "__main__":
    scrape_and_save(
        query="AI job displacement",
        subreddit="",               # Empty to search all of Reddit
        post_limit=10,
        comment_limit=5,
        output_file="ai_job_displacement_reddit.csv"
    )
