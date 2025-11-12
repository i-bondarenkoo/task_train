from client import Client
from zen_tracker import ZenTracker


if __name__ == "__main__":
    # client = Client("https://zenquotes.io")
    # result = client.get_request("/api/random")
    # assert isinstance(result, list)
    # assert isinstance(result[0], dict)
    tracker = ZenTracker("https://zenquotes.io")
    print(tracker.get_quote())
