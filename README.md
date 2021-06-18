# slack-scaffold-python

## Setup

```
$ export SLACK_APP_TOKEN=xapp-...
$ export SLACK_BOT_TOKEN=xoxb-...
$ poetry install
$ poetry run python app/main.py
# live reload with watchdog
$ watchmedo shell-command  --patterns="*.py" --recursive --command="python app/main.py
```
