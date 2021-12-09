import json

"""Text that is fed to user as they navigate the application"""
MESSAGES = json.loads(open("./config/messages.json").read())
