from platform import release
import config

testing = ""
TugasBot = ""

if config.test:
    token = testing
else:
    token = TugasBot
