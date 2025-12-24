import requests

# Replace these with your own Google API Key and Custom Search Engine ID
API_KEY = "AIzaSyAUsaalFRF6opiYQXgrmIyVtRaQ8Z5K7tQ"
CX = "a2ef6f2a7cdcf4b60"

def get_google_recommendations(missing_skills):
    """
    Get recommended courses/tutorials for missing skills using Google Custom Search API.
    Returns a list of top URLs with titles for each missing skill.
    """
    if not missing_skills:
        return []

    recommendations = []

    for skill in missing_skills:
        # Form a clean search query
        query = f"learn {skill} online course tutorial"

        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": "AIzaSyAUsaalFRF6opiYQXgrmIyVtRaQ8Z5K7tQ",   # Ensure key is a string
            "cx": "a2ef6f2a7cdcf4b60",         # Ensure CX is a string
            "q": query,
            "num": 3          # Top 3 results per skill
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if "items" in data:
                for item in data["items"]:
                    # Append skill + title + link
                    recommendations.append(f"{skill}: {item['title']} - {item['link']}")
            else:
                # Debug: print if no results
                print(f"No results for skill '{skill}':", data)

        except Exception as e:
            print(f"Error fetching recommendations for '{skill}': {e}")

    return recommendations
