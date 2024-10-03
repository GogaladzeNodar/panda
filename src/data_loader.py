import pandas as pd


class DataLoader:
    def __init__(self, filepath):
        """
        Initialize the DataLoader object with a file path, load, clean, and preprocess the data.

        Args:
            filepath (str): Path to the CSV file.
        """
        self.filepath = filepath
        self.data = None

        # Automatically call the necessary functions
        self.load_data()
        self.clean_data()
        self.preprocess_data()

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
            # Fill missing values with 0 for scores and empty strings for 'Student' and 'Semester'
            self.data.fillna(
                {
                    "Math": 0,
                    "Physics": 0,
                    "Chemistry": 0,
                    "Biology": 0,
                    "English": 0,
                    "Student": "",
                    "Semester": "",
                },
                inplace=True,
            )

            # Ensure score columns are numeric
            subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
            for subject in subjects:
                self.data[subject] = pd.to_numeric(self.data[subject], errors="coerce")

            # Remove duplicates
            self.data.drop_duplicates(inplace=True)

    def preprocess_data(self):
        """
        Preprocess the data by converting certain columns to categorical types.
        """
        if self.data is not None:
            # Convert the 'Semester' and 'Student' columns to categorical types
            self.data["Semester"] = pd.Categorical(self.data["Semester"])
            self.data["Student"] = pd.Categorical(self.data["Student"])

    def get_data(self):
        """
        Return the processed data.

        Returns:
            pd.DataFrame: The cleaned and preprocessed DataFrame.
        """
        return self.data
