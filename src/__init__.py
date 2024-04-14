import math
import pandas as pd


def recommend_job():
    # CSV file path
    job_file_path = '../resources/jobs.csv'
    seeker_file_path = '../resources/jobseekers.csv'

    # read csv files
    df_job = pd.read_csv(job_file_path)
    df_seeker = pd.read_csv(seeker_file_path)
    pd.set_option('display.max_columns', None)

    # For each jobseeker, iterate each job and sort the results
    # Complexity O(N*M) where N is no. of jobseekers and M is no. of jobs
    output = []

    # Iterate the jobseekers
    for i, seeker_row in df_seeker.iterrows():
        seeker_id = seeker_row['id']
        seeker_name = seeker_row['name']
        seeker_skills = set(seeker_row['skills'].split(','))
        # Iterate the jobs
        for _, job_row in df_job.iterrows():
            job_id = job_row['id']
            job_title = job_row['title']
            job_skills = set(job_row['required_skills'].split(','))
            job_skills_count = len(job_skills)

            # Find overlap for skills
            matching_skill = seeker_skills & job_skills
            matching_skill_count = len(matching_skill)
            matching_skill_percent = math.floor((matching_skill_count / job_skills_count) * 100)

            # Append to seeker result
            if matching_skill_count >= 1:
                output.append({
                    'jobseeker_id': seeker_id,
                    'jobseeker_name': seeker_name,
                    'job_id': job_id,
                    'job_title': job_title,
                    'matching_skill_count': matching_skill_count,
                    'matching_skill_percent': matching_skill_percent
                })

    # Sorting result using pd sort
    # Based on Seeker id, matching skill percentage and job id
    output_df = pd.DataFrame(output)
    output_df.sort_values(by=['jobseeker_id', 'matching_skill_percent', 'job_id'],
                          ascending=[True, False, True], inplace=True)
    print(output_df)


if __name__ == "__main__":
    recommend_job()
