from serpapi import GoogleSearch
import webbrowser
from Backend.TextToSpeech import TextToSpeech

def ShoppingRecommendations(query):
    print("🧠 Running ShoppingRecommendations for:", query)

    api_key = "8026a7c29cd67c68fc54c5f4027224c30962376fc6c3f2b424b4912e7a7a7b75"

    # Clean the query
    query = query.lower()
    for word in ["i want", "please", "could you", "show me", "recommend", "suggest", "some", "a", "an", "the"]:
        query = query.replace(word, "")
    query = query.strip()

    params = {
        "engine": "google",
        "q": f"buy {query} site:amazon.in",
        "hl": "en",
        "gl": "in",
        "api_key": api_key
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic = results.get("organic_results", [])

        if not organic:
            print("❌ No products found.")
            TextToSpeech("Sorry, I couldn't find any results on Amazon.")
            return

        for i, result in enumerate(organic[:5], start=1):
            title = result.get("title", "No title")
            link = result.get("link", "")
            price = "Price not listed"

            # ✅ Try rich_snippet -> top -> extensions
            try:
                extensions = result["rich_snippet"]["top"]["extensions"]
                for ext in extensions:
                    if "₹" in ext:
                        price = ext
                        break
            except:
                pass  # ignore if not found

            if not link or "amazon.in" not in link:
                continue  # skip non-Amazon links

            print(f"\n🔹 Product {i}")
            print(f"🛍️ {title}")
            print(f"💰 {price}")
            print(f"🔗 {link}")

            TextToSpeech(f"{title}. Opening link now.")
            webbrowser.open(link)

            if i >= 3:
                break

    except Exception as e:
        print("❌ Error:", e)
        TextToSpeech("Something went wrong while fetching results, Sir.")

