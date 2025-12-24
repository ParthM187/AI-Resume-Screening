import requests

API_KEY = "AIzaSyD88JbFlVIV6op8AxjA8prQYKDVhYZ9SHs"

def get_learning_resources(skill, max_results=3):
    query = f"{skill} tutorial for beginners"

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": API_KEY,
        "maxResults": max_results,
        "type": "video"
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []

    if "items" in data:
        for item in data["items"]:
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            results.append({
                "title": video_title,
                "url": video_url
            })

    return results
