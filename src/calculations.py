# Module for performing the calculations

import pandas as pd

"""
გამოიტანეთ იმ სტუდენტთა სია, რომლებმაც არ ჩააბარეს რომელიმე საგანი (ქულა ნაკლებია 50-ზე).
თითოეული საგნისთვის გამოთვალეთ საშუალო ქულა თითო სემესტრში.
იპოვეთ ის სტუდენტიები, რომელთაც აქვთ ყველაზე მაღალი საშუალო ქულა ყველა სემესტრსა და საგანში.
იპოვეთ საგანი, რომელშიც სტუდენტებს ყველაზე მეტად გაუჭირდათ (ყველაზე დაბალი საშუალო ქულა ყველა სემესტრში).
შექმენით ახალი დატაფრეიმი სადაც დააგენერირებთ საგნების საშუალო ქულებს სემესტრის მიხედვით და შემდეგ შეინახავთ ექსელის ფაილში (ინდექსები შეუსაბამეთ სემესტრებს)
ბონუსი (არასავალდებულო):

გამოავლინეთ სტუდენტები, რომლებმაც თანმიმდევრულად გააუმჯობესეს ქულები სემესტრებში.
"""


class DataCalculations:
    def __init__(self, data):
        """
        Initialize the Calculator with the student scores data.

        Args:
            data (pd.DataFrame): The processed student scores data.
        """
        self.data = data

    def failed_students(self):
        """
        Return a list of students who failed any subject (score < 50).

        Returns:
            pd.DataFrame: DataFrame of students who failed in any subject.
        """

        subjects = self.data.columns[2:]
        failed_students = self.data[self.data[subjects].lt(50).any(axis=1)][
            "Student"
        ].unique()
        return pd.DataFrame({"failedStudent": failed_students})

    def calculate_average_per_subject(self):
        """
        Calculate the average score for each subject across all students, grouped by semester.

        Args:
            data (pd.DataFrame): The student scores data.

        Returns:
            pd.DataFrame: A DataFrame with the average score for each subject per semester.
        """

        avg_per_subject = self.data.groupby("Semester")[
            ["Math", "Physics", "Chemistry", "Biology", "English"]
        ].mean()

        return avg_per_subject

    def get_highest_score_student(self):
        """
        Find the student with the highest score (average score) across all semesters and subjects.

        Returns:
            str: The name of the student with the highest scores.
        """

        subjects = self.data.columns[2:]
        score = self.data.groupby("Student")[subjects].mean().mean(axis=1)
        student_name = score.idxmax()
        highest_score = score.max()
        return student_name, highest_score

    def most_difficult_subject(self):
        """
        Identify the subject with the lowest average score across all semesters.

        Returns:
            tuple: The name of the most difficult subject and its average score.
        """

        subjects_avg = self.data[self.data.columns[2:]].mean()

        difficult_subject = subjects_avg.idxmin()
        lowest_score = round(subjects_avg.min(), 2)

        return difficult_subject, lowest_score

    def average_scores_depending_on_semesters(self):

        subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]

        avg_scores_by_semester = self.data.groupby("Semester")[subjects].mean()
        
        
        avg_scores_by_semester.to_excel(
            "average_scores_by_semester.xlsx", index_label="Semester"
        )

        

    def find_students_with_improvement(self):
        """
        Identify students who have consistently improved their average scores across semesters.

        Returns:
            pd.DataFrame: DataFrame containing student names and their average scores for those who have consistently improved.
        """
        subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]

        self.data["AverageScore"] = self.data[subjects].mean(axis=1)

        def has_improved(group):
            group_sorted = group.sort_values("Semester")
            avg_diff = group_sorted["AverageScore"].diff().dropna()
            return (avg_diff > 0).all()

        improving_students_data = self.data.groupby("Student").filter(has_improved)

        return improving_students_data[
            ["Student", "Semester", "AverageScore"]
        ].sort_values(["Student", "Semester"])
