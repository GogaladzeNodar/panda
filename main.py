from src.data_loader import DataLoader
from src.calculations import DataCalculations
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

def main():
    loader = DataLoader("data/student_scores_random_names.csv")

    data = loader.get_data()

    # data.to_csv("test_data.csv", index=False)

    calc = DataCalculations(data)

    failedStudent = calc.failed_students()
    avrage_per_subj = calc.calculate_average_per_subject()
    highest_score_student = calc.get_highest_score_student()
    difficult_subject = calc.most_difficult_subject()
    motivated_student = calc.find_students_with_improvement()
    calc.average_scores_depending_on_semesters()

    motivated_student.to_csv("motivated.csv", index=False)

    # Save it to a CSV file
    data.to_csv("test_data.csv", index=False)


if __name__ == "__main__":
    main()
