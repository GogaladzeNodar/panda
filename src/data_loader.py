import pandas as pd
from random import randint


class DataLoader:
    def __init__(self, filepath):
        """
        Initialize the DataLoader object with a file path, load, clean, and preprocess the data.

        Args:
            filepath (str): Path to the CSV file.
        """
        self.filepath = filepath
        self.data = None

        self.load_data()
        self.clean_data()
        # self.preprocess_data()

    def load_data(self):
        """
        Load the CSV data into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.filepath)
            print(f"Data loaded successfully from {self.filepath}")
        except FileNotFoundError as e:
            print(f"Error: File not found. {e}")
            self.data = None
        except Exception as e:
            print(f"An error occurred: {e}")
            self.data = None

    def clean_data(self):
        """
        Clean the loaded data by filling missing values, removing duplicates, and
        ensuring consistent data types.
        """
        if self.data is not None:

            self.data.fillna(
                {
                    "Math": randint(0, 101),
                    "Physics": randint(0, 101),
                    "Chemistry": randint(0, 101),
                    "Biology": randint(0, 101),
                    "English": randint(0, 101),
                    "Student": "",
                    "Semester": "",
                },
                inplace=True,
            )

            subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
            for subject in subjects:
                self.data[subject] = pd.to_numeric(self.data[subject], errors="coerce")

            self.data.drop_duplicates(inplace=True)

            self.data["Semester"] = (
                self.data["Semester"].str.replace("Semester ", "").astype(int)
            )

    # def preprocess_data(self):
    #
    #     if self.data is not None:
    #         # Convert the 'Semester' and 'Student' columns to categorical types
    #         self.data["Semester"] = pd.Categorical(self.data["Semester"])
    #         self.data["Student"] = pd.Categorical(self.data["Student"])

    def get_data(self):
        """
        Return the processed data.

        Returns:
            pd.DataFrame: The cleaned and preprocessed DataFrame.
        """
        return pd.DataFrame(self.data)
