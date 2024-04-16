import math
import os
import pandas as pd


def recommend_job(df_job, df_seeker):
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

            # Append to result
            if matching_skill_count >= 1:
                output.append({
                    'jobseeker_id': seeker_id,
                    'jobseeker_name': seeker_name,
                    'job_id': job_id,
                    'job_title': job_title,
                    'matching_skill_count': matching_skill_count,
                    'matching_skill_percent': matching_skill_percent
                })

    # Call handle output function
    return handle_output(output)


def read_csv():
    # Handle csv inputs
    # CSV file path
    main_dir = os.path.dirname(os.path.abspath(__file__))
    job_file_path = os.path.join(main_dir, '..', 'resources', 'jobs.csv')
    seeker_file_path = os.path.join(main_dir, '..', 'resources', 'jobseekers.csv')

    # read csv files
    df_job = df_seeker = None
    try:
        df_job = pd.read_csv(job_file_path)
    except FileNotFoundError:
        print("Job csv file not found. Please check the file path.")
    try:
        df_seeker = pd.read_csv(seeker_file_path)
    except FileNotFoundError:
        print("Job seeker csv file not found. Please check the file path.")

    # Final check
    if df_job is None or df_seeker is None:
        print("One or both CSV files could not be loaded. Please check the file paths.")
        exit()

    return df_job, df_seeker


def handle_output(output):
    # Sorting result using pd sort
    # Based on Seeker id, matching skill percentage and job id
    output_df = pd.DataFrame(output)
    output_df.sort_values(by=['jobseeker_id', 'matching_skill_percent', 'job_id'],
                          ascending=[True, False, True], inplace=True)
    print(output_df)
    return output_df


if __name__ == "__main__":
    job, seeker = read_csv()
    recommend_job(job, seeker)
