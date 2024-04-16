import unittest
import pandas as pd
from io import StringIO
from recommend_engine import main


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize the csv data
        # Simulate job seeker data
        jobseekers = """id,name,skills
        1,Alice Seeker,"Ruby, SQL"
        2,Bob Applicant,"JavaScript, HTML/CSS"
        """
        self.df_seeker = pd.read_csv(StringIO(jobseekers))

        # Simulate job data
        jobs = """id,title,required_skills
        1,Ruby Developer,"Ruby, SQL, Problem Solving"
        2,Frontend Developer,"JavaScript, HTML/CSS, React, Teamwork"
        """
        self.df_job = pd.read_csv(StringIO(jobs))

        # Simulate expected result
        self.expected_result = """jobseeker_id,jobseeker_name,job_id,job_title,matching_skill_count,matching_skill_percent
        1,Alice Seeker,1,Ruby Developer,2,66
        2,Bob Applicant,2,Frontend Developer,2,50
        """
        self.expected_result_csv = pd.read_csv(StringIO(self.expected_result))

        # Simulate job data 2
        self.jobs_2 = """id,title,required_skills
        4,Fullstack Developer,"JavaScript, HTML/CSS, Node.js, Ruby, SQL, Communication"
        5,Machine Learning Engineer,"Python, Machine Learning, Adaptability"
        """
        self.df_job_2 = pd.read_csv(StringIO(self.jobs_2))

    def test_recommend_job(self):
        # Call recommend job and compare result
        self.assertTrue(main.recommend_job(self.df_job, self.df_seeker).equals(self.expected_result_csv))

    def test_recommend_job_false(self):
        self.assertFalse(main.recommend_job(self.df_job_2, self.df_seeker).equals(self.expected_result_csv))


if __name__ == '__main__':
    unittest.main()
