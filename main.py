from src.data_loader import DataLoader
from src.calculations import DataCalculations
from src.visualizations import Visualize
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

    calc = DataCalculations(data)

    print(
        "###################################################################################################################### \n"
    )

    failedStudent = calc.failed_students()
    print(f"Failed Students - \n {failedStudent}")
    print(
        "###################################################################################################################### \n"
    )

    avrage_per_subj = calc.calculate_average_per_subject()
    print(f"Average Per Subject - \n {avrage_per_subj}")
    print(
        "###################################################################################################################### \n"
    )

    student_name, highest_score = calc.get_highest_score_student()
    print(
        f"The student with the highest average score is {student_name} with a score of {highest_score:.2f}."
    )
    print(
        "###################################################################################################################### \n"
    )

    difficult_subject = calc.most_difficult_subject()
    print(f"Most Difficult subject - \n {difficult_subject}")
    print(
        "###################################################################################################################### \n"
    )

    motivated_student = calc.find_students_with_improvement()
    motivated_student.to_csv("data/motivated.csv", index=False)
    
    calc.average_scores_depending_on_semesters()
    

    print(
        "###################################################################################################################### \n"
    )

    visualize = Visualize(data)
    visualize.average_score_for_subjects()
    visualize.average_score_by_semester()


if __name__ == "__main__":
    main()
