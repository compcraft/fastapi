from libs.db import CompCraftSQL, CompCraftMONGO
from libs.models import Job
from utils import yaml
from pprint import pprint


def insert_jobs():
    db = CompCraftMONGO().jobs()
    for job in list_all_jobs():
        info_job = deprecated_get_info(job)
        del info_job['color']
        info_job['name'] = info_job['name'].lower()
        db.insert(info_job)


def list_all_jobs():
    db = CompCraftMONGO().jobs()
    jobs = []
    for job in db.find({}, {'name': 1, 'description': 1}):
        jobs.append(Job(**job))
    return jobs


def get_toplist_job(job: str, limit: int = 10):
    data = CompCraftSQL().execute(
        query="""select * from (select jobs_users.username, jobs_jobs.level
                from jobs_users
                join jobs_jobs
                on jobs_jobs.userid = jobs_users.id
                where jobs_jobs.job = :job
                union
                select jobs_users.username, jobs_archive.level
                from jobs_users
                join jobs_archive
                on jobs_archive.userid = jobs_users.id
                where jobs_archive.job = :job)
                as toplist
                order by toplist.level desc
                limit :limit;
                """,
        values={"job": job, "limit": limit},
    )
    return data


def get_info_job(job: str, limit: int = 10, minimal: bool = False, toplist: bool = True):
    db = CompCraftMONGO().jobs()

    if minimal:
        job_info = db.find_one({'name': {'$eq': job.lower()}}, {
                               'name': 1, 'description': 1})
    else:
        job_info = db.find_one({'name': {'$eq': job.lower()}})

    job_info = Job(**job_info)
    job_info = job_info.__dict__

    if minimal:
        return job_info

    if toplist:
        job_info["toplist"] = get_toplist_job(job, limit)

    return job_info


def deprecated_get_info(job: str):
    info_job = {}
    job = job.lower()
    hjob = yaml.read_file(
        f'../plugins/Jobs/jobs/{job}.yml')[job.capitalize()]
    info_job['name'] = hjob['fullname']
    info_job['color'] = hjob['ChatColour'].replace('_', '-').lower()
    info_job['description'] = hjob['FullDescription']

    if job == 'builder':
        info_job['rewards'] = {
            'place': hjob['Place'],
            'kill': hjob['Kill']
        }
    if job == 'brewer':
        info_job['rewards'] = {
            'brew': hjob['Brew']
        }
    if job == 'crafter':
        info_job['rewards'] = {
            'craft': hjob['Craft'],
            'smelt': hjob['Smelt'],
            'kill': hjob['Kill']
        }
    if job == 'digger':
        info_job['rewards'] = {
            'break': hjob['Break'],
            'kill': hjob['Kill']
        }
    if job == 'enchanter':
        info_job['rewards'] = {
            'enchant': hjob['Enchant'],
        }
    if job == 'explorer':
        info_job['rewards'] = {
            'explore': hjob['Explore'],
            'kill': hjob['Kill']
        }
    if job == 'farmer':
        info_job['rewards'] = {
            'tame': hjob['Tame'],
            'breed': hjob['Breed'],
            'shear': hjob['Shear'],
            'milk': hjob['Milk'],
            'break': hjob['Break'],
            'place': hjob['Place'],
            'kill': hjob['Kill']
        }
    if job == 'fisherman':
        info_job['rewards'] = {
            'fish': hjob['Fish'],
            'kill': hjob['Kill']
        }
    if job == 'hunter':
        info_job['rewards'] = {
            'tame': hjob['Tame'],
            'kill': hjob['Kill']
        }
    if job == 'miner':
        info_job['rewards'] = {
            'tntbreak': hjob['TNTBreak'],
            'break': hjob['Break'],
            'place': hjob['Place'],
            'kill': hjob['Kill']
        }
    if job == 'weaponsmith':
        info_job['rewards'] = {
            'craft': hjob['Craft'],
            'repair': hjob['Repair'],
            'smelt': hjob['Smelt'],
        }
    if job == 'woodcutter':
        break_materials = {}

        for row in hjob['Break']['materials']:
            row_info = row.split(';')
            break_materials[row_info[0]] = {
                'income': float(row_info[1]),
                'points': float(row_info[2]),
                'experience': float(row_info[3]),
            }

        info_job['rewards'] = {
            'break': break_materials,
            'kill': hjob['Kill'],
        }

    return info_job
