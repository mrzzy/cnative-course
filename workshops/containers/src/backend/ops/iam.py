#
# Memento
# Backend
# IAM Operations
#

from ..app import db
from ..models.iam import *
from ..mapping.iam import *
from .assignment import *
from ..utils import map_dict, apply_bound
from .notification import query_channels, delete_channel
from ..api.error import NotFoundError

## Organisation Ops
# query ids of organisations. 
# skip - skip the first skip organisations
# limit - output ids limit to the first limit organisations
def query_orgs(skip=0, limit=None):
    org_ids = Organisation.query.with_entities(Organisation.id)
    org_ids = [ i[0] for i in org_ids ]
    org_ids = apply_bound(org_ids, skip, limit)

    return org_ids

# get organisation by id
# throws NotFoundError if no org with org_id is found
# returns organisation as a dict
def get_org(org_id):
    org = Organisation.query.get(org_id)
    if org is None: raise NotFoundError
    # map model fields to dict
    return map_dict(org, org_mapping)

# create a new organisation
# name - name of the organisation, must be uniqu
# logo_url - logo url for organisation. Optional.
# returns the id of the new organisation
def create_org(name, logo_url=None):
    org = Organisation(name=name, logo_url=logo_url)
    db.session.add(org)
    db.session.commit()

    return org.id

# update the organisation with given org_id
# org_id - update organisation with given id
# name - name of the organisation, must be uniqu
# logo_url - logo url for organisation. Optional.
# throws NotFoundError if no org with org_id is found
def update_org(org_id, name=None, logo_url=None):
    org = Organisation.query.get(org_id)
    if org is None: raise NotFoundError

    # update org fields
    if not name is None: org.name = name
    org.logo_url = logo_url
    db.session.commit()

# delete an organisation 
# throws NotFoundError if no org with org_id is found
# also cascade deletes all objects depending on organisation
# org_id - delete organisation with given id
def delete_org(org_id):
    org = Organisation.query.get(org_id)
    if org is None: raise NotFoundError

    # cascade delete dependent teams and users
    user_ids = query_users(org_id=org_id)
    for user_id in user_ids: delete_user(user_id)
    team_ids = query_teams(org_id=org_id)
    for team_id in team_ids: delete_team(team_id)

    db.session.delete(org)
    db.session.commit()

## Team Ops
# query ids of teams.
# org_ids - show only teams that belong to organisation given by org_id
# skip - skip the first skip organisations
# limit - output ids limit to the first limit organisations
def query_teams(org_id=None, skip=0, limit=None):
    team_ids = Team.query.with_entities(Team.id)
    if not org_id is None: team_ids = team_ids.filter_by(org_id=org_id)
    team_ids = [ i[0] for i in team_ids ]
    team_ids = apply_bound(team_ids, skip, limit)

    return team_ids

# get team by team_id
# throws NotFoundError if no team with team_id is found
# returns team as a dict
def get_team(team_id):
    team = Team.query.get(team_id)
    if team is None: raise NotFoundError
    # map model fields to dict
    return map_dict(team, team_mapping)

# create a new team
# org_id - id of organisation that team belongs to 
# name - name for team
# returns team id
def create_team(org_id, name):
    team = Team(org_id=org_id, name=name)
    db.session.add(team)
    db.session.commit()

    return team.id

# update a existing team
# team_id - id of team being updated
# org_id - id of organisation that team belongs to 
# name - name for team
# throws NotFoundError if no team with team_id is found
def update_team(team_id, org_id=None, name=None):
    team = Team.query.get(team_id)
    if team is None: raise NotFoundError
    # update team fields
    if not org_id is None: team.org_id = org_id
    if not name is None: team.name = name
    db.session.commit()


# delete team for id 
# also cascade deletes all objects depending on team
# throws NotFoundError if no team with team_id is found
def delete_team(team_id):
    team = Team.query.get(team_id)
    if team is None: raise NotFoundError
    # cascade delete
    manage_ids = query_manage(kind=Management.Kind.Team, target_id=team_id)
    for manage_id in manage_ids: delete_manage(delete_manage)

    db.session.delete(team)
    db.session.commit()


## User Ops
# query ids of users
# org_id - show only users that belong to organisation given by org_id
# team_id - show only users that belong to team given by team_id
# kind - show only users that are of this kind
# skip - skip the first skip organisations
# limit - output ids limit to the first limit organisations
def query_users(org_id=None, team_id=None, kind=None, skip=0, limit=None):
    user_ids = User.query.with_entities(User.id)
    # apply filters
    if not org_id is None: user_ids = user_ids.filter_by(org_id=org_id)
    if not team_id is None: user_ids = user_ids.filter_by(team_id=team_id)
    if not kind is None: user_ids = user_ids.filter_by(kind=kind)

    # apply skip & limit
    user_ids = [ i[0] for i in user_ids ]
    user_ids = apply_bound(user_ids, skip, limit)

    return user_ids

# get user by id
# returns user as dict
# throws NotFoundError if no user with user_id is found
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None: raise NotFoundError
    # map fields to dict
    return map_dict(user, user_mapping)

# create a user
# kind - kind of user
# name - name of the user
# password - password of the user
# email - email address of the user
# org_id - id of organisation that the user belongs to
# team_id - id of the team that the user belongs to, optional
# returns the id of the created user
def create_user(kind, name, password, email, org_id, team_id=None):
    user = User(kind=kind, name=name, password=password,
                email=email, org_id=org_id, team_id=team_id)
    db.session.add(user)
    db.session.commit()

    return user.id

# update the user for the given user_id
# kind - kind of user
# name - name of the user
# password - password of the user
# email - email address of the user
# org_id - id of organisation that the user belongs to
# team_id - id of the team that the user belongs to, optional
# throws NotFoundError if no user with user_id is found
def update_user(user_id, kind=None, name=None, password=None,
                email=None, org_id=None, team_id=None):
    user = User.query.get(user_id)
    if user is None: raise NotFoundError
    # update user fields
    if not kind is None: user.kind = kind
    if not name is None: user.name = name
    if not password is None: user.password = password
    if not email is None: user.email = email
    if not org_id is None: user.org_id = org_id
    user.team_id = team_id
    db.session.commit()

# delete a user
# also cascade deletes all objects depending on user
# user_id - delete organisation with given id
# throws NotFoundError if no user with user_id is found
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None: raise NotFoundError
    # cascade delete
    # cascade delete mangement 
    manage_ids = query_manage(manager_id=user_id) + \
        query_manage(kind=Management.Kind.User, target_id=user_id)
    for manage_id in manage_ids: delete_manage(manage_id)
    # cascade delete assignments created
    assign_ids = query_assigns(assigner_id=user_id)
    for assign_id in assign_ids: delete_assign(assign_id)
    # cascade delete tasks/events created
    task_ids = query_tasks(author_id=user_id)
    for task_id in task_ids: delete_task(task_id)
    event_ids = query_events(author_id=user_id)
    for event_id in event_ids: delete_event(event_id)
    # cascde delete channel
    channel_ids = query_channels(user_id=user_id)
    for channel_id in channel_ids: delete_channel(channel_id)

    db.session.delete(user)
    db.session.commit()

## Management Ops
# query id of managements
# kind - show only managements with the given kind (worker/team)
# target_id - show only mangements for target with given id
# org_id - show only managements that belong to the given organisation
# manager_id - show only mangements with manager with given id
# skip - skip the first skip organisations
# limit - output ids limit to the first limit organisations
def query_manage(kind=None, org_id=None, target_id=None,
                 manager_id=None, skip=0, limit=None):
    manage_ids = Management.query.with_entities(Management.id)
    # apply filters
    if not kind is None: manage_ids = manage_ids.filter_by(kind=kind)
    if not target_id is None: manage_ids = manage_ids.filter_by(target_id=target_id)
    if not manager_id is None: manage_ids = manage_ids.filter_by(manager_id=manager_id)
    if not org_id is None:
        manage_ids = manage_ids.join(User, User.id == Management.manager_id)
        manage_ids = manage_ids.filter(User.org_id == org_id)

    # apply skip & limit
    manage_ids = [ i[0] for i in manage_ids ]
    manage_ids = apply_bound(manage_ids, skip, limit)

    return manage_ids

# get management for id
# returns managements as a dict
# throws NotFoundError if no manage with manage_id is found
def get_manage(manage_id):
    manage = Management.query.get(manage_id)
    if manage is None: raise NotFoundError
    # map fields to dict
    return map_dict(manage, manage_mapping)

# create a management
# kind - kind of management target (worker/team)
# target_id - id of the worker/team that is being managed
# manager_id - id of the user that is assigned to manage target
# returns the id of the management
def create_manage(kind, target_id, manager_id):
    manage = Management(kind=kind, target_id=target_id, manager_id=manager_id)
    db.session.add(manage)
    db.session.commit()

    return manage.id

# update management for given manage_id
# kind - kind of management target (worker/team)
# target_id - id of the worker/team that is being managed
# manager_id - id of the user that is assigned to manage target
# throws NotFoundError if no manage with manage_id is found
def update_manage(manage_id, kind=None, target_id=None, manager_id=None):
    manage = Management.query.get(manage_id)
    if manage is None: raise NotFoundError
    # update management fields
    if not kind is None: manage.kind = kind
    if not target_id is None: manage.target_id = target_id
    if not manager_id is None: manage.manager_id = manager_id
    db.session.commit()

# delete the managment for the given manage id
# throws NotFoundError if no manage with manage_id is found
def delete_manage(manage_id):
    manage = Management.query.get(manage_id)
    if manage is None: raise NotFoundError
    db.session.delete(manage)
    db.session.commit()
