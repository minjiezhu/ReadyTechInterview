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

        # Simulate actual csvs
        actual_jobseeksers = """id,title,required_skills
        1,Ruby Developer,"Ruby, SQL, Problem Solving"
        2,Frontend Developer,"JavaScript, HTML/CSS, React, Teamwork"
        3,Backend Developer,"Java, SQL, Node.js, Problem Solving"
        4,Fullstack Developer,"JavaScript, HTML/CSS, Node.js, Ruby, SQL, Communication"
        5,Machine Learning Engineer,"Python, Machine Learning, Adaptability"
        6,Cloud Architect,"Cloud Computing, Python, Communication"
        7,Data Analyst,"Python, SQL, Machine Learning, Adaptability"
        8,Web Developer,"HTML/CSS, JavaScript, Ruby, Teamwork"
        9,Python Developer,"Python, SQL, Problem Solving, Self Motivated"
        10,JavaScript Developer,"JavaScript, React, Node.js, Self Motivated"
        """
        self.df_actual_seeker = pd.read_csv(StringIO(actual_jobseeksers))

        actual_jobs = """id,name,skills
        1,Alice Seeker,"Ruby, SQL, Problem Solving"
        2,Bob Applicant,"JavaScript, HTML/CSS, Teamwork"
        3,Charlie Jobhunter,"Java, SQL, Problem Solving"
        4,Danielle Searcher,"Python, Machine Learning, Adaptability"
        5,Eddie Aspirant,"Cloud Computing, Communication"
        6,Fiona Candidate,"Python, SQL, Adaptability"
        7,George Prospect,"HTML/CSS, JavaScript, Ruby, Teamwork"
        8,Hannah Hunter,"Python, Problem Solving"
        9,Ian Jobhunter,"JavaScript, React, Self Motivated"
        10,Jane Applicant,"Ruby, Self Motivated"
        """
        self.df_actual_job = pd.read_csv(StringIO(actual_jobs))

    def test_recommend_job(self):
        # Call recommend job and compare result
        self.assertIsNotNone(main.recommend_job(self.df_job, self.df_seeker))
        self.assertTrue(main.recommend_job(self.df_job, self.df_seeker).equals(self.expected_result_csv))
        self.assertFalse(main.recommend_job(self.df_job_2, self.df_seeker).equals(self.expected_result_csv))

    def test_read_csv(self):
        df_return_seeker, df_return_job = main.read_csv()
        # Test not none
        self.assertIsNotNone(df_return_seeker)
        self.assertIsNotNone(df_return_job)

        # Test returns
        self.assertTrue(df_return_seeker.equals(self.df_actual_seeker))
        self.assertTrue(df_return_job.equals(self.df_actual_job))

        self.assertFalse(df_return_seeker.equals(self.df_seeker))
        self.assertFalse(df_return_job.equals(self.df_job))


if __name__ == '__main__':
    unittest.main()
