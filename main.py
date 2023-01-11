import classes.application_class as application_class 
import os

application_id = os.environ["application_id"]


app = application_class.Application( id = application_id )
app.run()
