import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Make sure app subscribes events you want to catch in Event Subscription page of your app setting
@app.event("app_mention")
def print_mention_event(event):
    print("----------Yay! It worked!----------")
    print(event)


if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
