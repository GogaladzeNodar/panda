from src.data_loader import DataLoader


def main():
    loader = DataLoader("data/student_scores_random_names.csv")

    data = loader.get_data()

    print(data)


if __name__ == "__main__":
    main()
