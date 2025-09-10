import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/jokes/random"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        data = response.json()
        print(f"{data['setup']} - {data['punchline']}")
    else:
        print("Failed to fetch a joke")

if __name__ == "__main__":
    print("🚀 Running AWS Playground Script...")
    get_joke()
