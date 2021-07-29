from src.utils import yaml

from os import walk

path = "minecraft/plugins/Jobs/jobsbase"
dest = "minecraft/plugins/Jobs/jobs"

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for filename in f:
    job = yaml.read_file(f'{path}/{filename}')
    current_job = filename.replace('.yml', '')

    def modify_experience(action):
        job_class = current_job.capitalize()
        for item in job[job_class][action].keys():
            job[job_class][action][item]['experience'] = round(
                job[job_class][action][item]['experience'] * 0.15, 2)

    if current_job.lower() == 'builder':
        modify_experience('Place')
        modify_experience('Kill')
    if current_job.lower() == 'brewer':
        modify_experience('Brew')
    if current_job.lower() == 'crafter':
        modify_experience('Craft')
        modify_experience('Smelt')
        modify_experience('Kill')
    if current_job.lower() == 'digger':
        modify_experience('Break')
        modify_experience('Kill')
    if current_job.lower() == 'enchanter':
        modify_experience('Enchant')
    if current_job.lower() == 'explorer':
        modify_experience('Explore')
        modify_experience('Kill')
    if current_job.lower() == 'farmer':
        modify_experience('Tame')
        modify_experience('Breed')
        modify_experience('Shear')
        modify_experience('Milk')
        modify_experience('Break')
        modify_experience('Place')
        modify_experience('Kill')
    if current_job.lower() == 'fisherman':
        modify_experience('Fish')
        modify_experience('Kill')
    if current_job.lower() == 'hunter':
        modify_experience('Tame')
        modify_experience('Kill')
    if current_job.lower() == 'miner':
        modify_experience('TNTBreak')
        modify_experience('Break')
        modify_experience('Place')
        modify_experience('Kill')
    if current_job.lower() == 'weaponsmith':
        modify_experience('Craft')
        modify_experience('Repair')
        modify_experience('Smelt')
    # if current_job.lower() == 'woodcutter':
    #     break_materials = {}

    #     for row in hjob['Break']['materials']:
    #         row_info = row.split(';')
    #         break_materials[row_info[0]] = {
    #             'income': float(row_info[1]),
    #             'points': float(row_info[2]),
    #             'experience': float(row_info[3]),
    #         }

    #     info_job['rewards'] = {
    #         'break': break_materials,
    #         'kill': hjob['Kill'],
    #     }
    yaml.write_file(f'{dest}/{filename}', job)
