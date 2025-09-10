import requests

def get_joke():
    """Récupère une blague depuis l'API et la retourne sous forme de tuple (setup, punchline)."""
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        data = response.json()
        return data["setup"], data["punchline"]
    else:
        return None, None

if __name__ == "__main__":
    print("🚀 Running AWS Script...")
    setup, punchline = get_joke()
    if setup and punchline:
        print(f"{setup} - {punchline}")
    else:
        print("Failed to fetch a joke")
