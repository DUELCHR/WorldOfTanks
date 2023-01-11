import classes.application_class as application_class 
import json

application_infos = {}
with open('application_env.json', 'r') as env_json:    
    application_infos = json.load(env_json)


app = application_class.Application( id = application_infos["application_id"] )
app.run()
