import requests

class SocialMediaChecker:
    def __init__(self, instagram_token=None):
        self.instagram_token = instagram_token

    def get_instagram_followers(self):
        if not self.instagram_token:
            return "Instagram token not set."
        url = f"https://graph.instagram.com/me?fields=id,username,followers_count&access_token={self.instagram_token}"
        try:
            response = requests.get(url)
            data = response.json()
            if "followers_count" in data:
                return f"Instagram followers: {data['followers_count']}"
            else:
                return f"Instagram error: {data.get('error', 'Unknown error')}"
        except Exception as e:
            return f"Instagram error: {e}"

    def get_instagram_unread_messages(self):
        # Instagram API does not allow access to DMs or unread messages.
        return "Instagram unread messages: Not available via API."

    def get_whatsapp_unread_messages(self):
        # WhatsApp API does not allow access to messages for personal accounts.
        return "WhatsApp unread messages: Not available via API."

    def report(self):
        results = [
            self.get_instagram_followers(),
            self.get_instagram_unread_messages(),
            self.get_whatsapp_unread_messages()
        ]
        return "\n".join(results)

if __name__ == "__main__":
    checker = SocialMediaChecker(
        instagram_token="YOUR_INSTAGRAM_ACCESS_TOKEN"
    )
    print(checker.report())