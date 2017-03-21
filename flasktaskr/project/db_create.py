from views import db
from models import Task
from datetime import date

# create the database and the table
db.create_all()

# insert some data
db.session.add(Task("Finish this tutorial.", date(2017, 3, 27), 10, 1))
db.session.add(Task("Finish this Real Python.", date(2017, 4, 20), 10, 1))

# commit the changes
db.session.commit()

