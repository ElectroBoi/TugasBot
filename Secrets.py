from platform import release
import config

testing = "MzIzMzk1NTY3NjgwMjI1Mjgx.WT0Plw.xOzob-fJ0r_7TX5PaskenLfajGQ"
TugasBot = "OTU3MTk2MTM0NDU4MTk2MDI4.Yj7QXg.cfH8X8fsldgrfIiKhjHx6g9_w4Q"

if config.test:
    token = testing
else:
    token = TugasBot
