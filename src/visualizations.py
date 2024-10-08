# Module for creating visualizations
import matplotlib.pyplot as plt
import pandas as pd

"""
ვიზუალიზაცია:

შექმენით სვეტების დიაგრამა, რომელიც აჩვენებს თითო საგნის საშუალო ქულას ყველა სემესტრში.
შექმენით ხაზოვანი გრაფიკი, რომელიც აჩვენებს საშუალო საერთო ქულას სემესტრების მიხედვით.
"""


class Visualize:
    def __init__(self, data):
        self.data = data

    def average_score_for_subjects(self):
        subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
        avg_scores = self.data[subjects].mean()
        plt.figure(figsize=(12, 9))
        avg_scores.plot(kind="bar", color="skyblue")
        plt.title("Average Scores for Each Subject Across All Semesters", fontsize=16)
        plt.xlabel("Subjects", fontsize=14)
        plt.ylabel("Average Score", fontsize=14)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def average_score_by_semester(self):
        subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
        self.data["AverageScore"] = self.data[subjects].mean(axis=1)
        avg_scores_by_semester = self.data.groupby("Semester")["AverageScore"].mean()
        avg_scores_by_semester.plot(
            kind="line", marker="o", title="Average Overall Score by Semester"
        )
        plt.xlabel("Semester")
        plt.ylabel("Average Overall Score")
        plt.grid(True)
        plt.show()
