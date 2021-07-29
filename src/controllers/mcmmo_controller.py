from libs.db import CompCraftSQL


def list_skills():
    response = []
    data = CompCraftSQL().execute("""SELECT COLUMN_NAME
                               FROM INFORMATION_SCHEMA.COLUMNS
                               WHERE TABLE_NAME=N'mcmmo_skills'
                               """)

    for row in data:
        if row['COLUMN_NAME'] not in ['user_id', 'total']:
            response.append(row['COLUMN_NAME'])
    return response


def toplist_power_level(limit: int = 10):
    data = CompCraftSQL().execute(
        query=f'select mcmmo_users.user as username, mcmmo_skills.total as level from mcmmo_users join mcmmo_skills on mcmmo_skills.user_id = mcmmo_users.id order by total desc limit :limit;',
        values={"limit": limit}
    )
    return data


def toplist_skill(skill: str, limit: int = 10):
    data = CompCraftSQL().execute(
        query=f'select mcmmo_users.user as username, mcmmo_skills.{skill} as level from mcmmo_users join mcmmo_skills on mcmmo_skills.user_id = mcmmo_users.id order by {skill} desc limit :limit;',
        values={"limit": limit}
    )
    return data
