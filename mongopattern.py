import datetime
from datetime import timezone

URL = "https://github.com/MongoEngine/mongoengine/issues/652"


"""
#### GENERAL
- Owner ID in each entry?
- all collections free to have additional data
- comment tag for identifying developers (# atodo: add try except)

#### AUTH
- refresh token on every request?
- additional Auth security field for JWT? "role"
"""


USER_AUTH = {
    "_id": "ObjectID",

    "email": "string", # Emailfield, unique (verification required)

    "password_hashed": "string", # frontend should do the hashing

    "role": "string" # default user, additional developer, god
}

USER_SETTINGS = {
    "_id": "ObjectID",

    "identity": USER_AUTH._id,

    "name": "string", # default = email -@

    "creation_date": datetime, # auto 

    "email": "string", # ref USER_AUTH.email

    "language": "string", # options EN, DE... etc

    "timezone": "string", # if unset use local machine time. 

    "last_login": datetime, 

    "has_items": [] # do we need this?
                    # each item seperate? task, habit, goal
                    
}



CATHEGORY = {
    "_id": "ObjectID",

    "name": "string",

    "has_items": ["ObjectID"] # do we need this?
}



HABIT = {
    "_id": "ObjectID", #auto
    "name": "string", # required

    "start_date": datetime, # required (auto datetime.now() -- ISODate("2013-10-10T23:06:38.000Z"))

    "finish_date": datetime, # user Input ISODate("2013-10-10T20:00:00.000Z")
                             # datetime.datetime.now(timezone.utc).astimezone().isoformat()

    "description": "string", # optional

    "resources": [{ # List of dicts
            "url": URL, # class URLField(StringField) -Mongoengine
            "label": "string" # required?
        }],
    
    "parent_goal": GOAL._id,
    
    "time_blocks": [TIMEBLOCK._id],

    "cathegory": CATHEGORY._id,

    "status": "string", # options: active, archived, completed

    "progress": [{
        "date": datetime, # no timezone needed?
        "status": "str" # options: skipped, mini, failed, completed
    }]
}


TASK = {
    "_id": "ObjectID", #auto
    "name": "string", # required

    "due_date": datetime, # required? user Input?

    "end_date": datetime, # user Input ISODate("2013-10-10T20:00:00.000Z")
                             # datetime.datetime.now(timezone.utc).astimezone().isoformat()

    "description": "string", # optional

    "time_block": TIMEBLOCK._id,

    "parent_goal": GOAL._id,

    "cathegory": CATHEGORY._id,

    "recursive_pattern": "?"

}



TIMEBLOCK = {
    "_id": "ObjectID", #auto
    "name": "string", # required

    "due_date": datetime, # required? user Input?

    "end_date": datetime, # user Input ISODate("2013-10-10T20:00:00.000Z")
                             # datetime.datetime.now(timezone.utc).astimezone().isoformat()

    "description": "string", # optional

    "time_block": TIMEBLOCK._id,

    "parent_goal": GOAL._id,

    "cathegory": CATHEGORY._id,

    "recursive_pattern": "?"

}


GOAL = {
    "_id": "ObjectID", #auto
    "name": "string", # required

    "start date": datetime, # required (auto datetime.now() -- ISODate("2013-10-10T23:06:38.000Z"))

    "finish date": datetime, # user Input ISODate("2013-10-10T20:00:00.000Z")
                             # datetime.datetime.now(timezone.utc).astimezone().isoformat()

    "description": "string", # optional

    "resources": [{ # List of dicts
            "url": URL, # class URLField(StringField) -Mongoengine
            "label": "string" # required?
        }],

    "subgoals": [GOAL._id], # subgoals same as goals in db?
                            # if yes add a new field designating level?
    
    "habits": [HABIT._id], 

    "tasks": [TASK._id],

    "time_blocks": [TIMEBLOCK._id],

    "cathegory": CATHEGORY._id, # auto = Default Cathegory

    "status": "string" # options: active, archived, completed
}


