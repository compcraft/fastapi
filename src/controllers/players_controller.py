from libs.db import CompCraftSQL
from os import walk
import datetime
from utils import yaml


def toplist_playedtime(limit: int = 10):
    data = CompCraftSQL().execute(
        query="""select name as username, round(sum(session_time)) as played_time
from (
select name, ((session_end - session_start - afk_time)/1000) as session_time
from plan_sessions
join plan_users
on plan_sessions.uuid = plan_users.uuid
) as player_played_time 
group by name 
order by played_time desc
limit :limit;""",
        values={"limit": limit}
    )

    response = []
    for player in data:
        s = player["played_time"]
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time = '{:02}:{:02}:{:02}'.format(
            int(hours), int(minutes), int(seconds))
        response.append(
            {"username": player["username"], "played_time": formatted_time,
                "raw_played_time": player["played_time"]}
        )
    return response


def player_playtime(username: str):
    data = CompCraftSQL().execute(
        query="""select name as username, round(sum(session_time)) as played_time
from (
select name, ((session_end - session_start - afk_time)/1000) as session_time
from plan_sessions
join plan_users
on plan_sessions.uuid = plan_users.uuid
) as player_played_time 
where name = :username
group by name 
order by played_time desc;""",
        values={"username": username}
    )

    response = []
    for player in data:
        s = player["played_time"]
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time = '{:02}:{:02}:{:02}'.format(
            int(hours), int(minutes), int(seconds))
        response.append(
            {"username": player["username"], "played_time": formatted_time,
                "raw_played_time": player["played_time"]}
        )
    return response


def toplist_balance(limit: int = 10):
    data = CompCraftSQL().execute(
        query="""
        select name as username, round(double_value) as balance
        from plan_extension_user_values
        join plan_users
        on plan_users.uuid = plan_extension_user_values.uuid
        where plan_extension_user_values.provider_id = 11
        order by balance desc
        limit :limit;
    """,
        values={"limit": limit})
    return data


def player_balance(username: str):
    data = CompCraftSQL().execute(
        query="""
        select name as username, round(double_value) as balance
        from plan_extension_user_values
        join plan_users
        on plan_users.uuid = plan_extension_user_values.uuid
        where plan_extension_user_values.provider_id = 11
        and plan_users.name = :username
        order by balance desc;
    """,
        values={"username": username})
    return data


def list_players():
    data = CompCraftSQL().execute("select * from luckperms_players;")
    return data


def player_mcmmo(username: str):
    data = CompCraftSQL().execute(
        query="select mcmmo_users.user, mcmmo_skills.* from mcmmo_users join mcmmo_skills on mcmmo_skills.user_id = mcmmo_users.id where mcmmo_users.user = :username;",
        values={"username": username},
    )
    return data


def player_jobs(username: str):
    data = CompCraftSQL().execute(
        query="""select jobs_jobs.job, jobs_jobs.level
from jobs_users 
join jobs_jobs
on jobs_jobs.userid = jobs_users.id
where jobs_users.username = :username
union
select jobs_archive.job, jobs_archive.level
from jobs_users 
join jobs_archive
on jobs_archive.userid = jobs_users.id
where jobs_users.username = :username
union
select distinct jobs_jobNames.name as job, 0 as level
from jobs_jobNames 
where not exists (
select jobs_jobs.job, jobs_jobs.level
from jobs_users 
join jobs_jobs
on jobs_jobs.userid = jobs_users.id
where jobs_users.username = :username
and jobs_jobs.jobid  = jobs_jobNames.id
union
select jobs_archive.job, jobs_archive.level
from jobs_users 
join jobs_archive
on jobs_archive.userid = jobs_users.id
where jobs_users.username = :username
and jobs_archive.jobid = jobs_jobNames.id
); """,
        values={"username": username},
    )

    response = {}

    for row in data:
        response[row["job"]] = row["level"]

    return [response]
