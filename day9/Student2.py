import re

class Students:
    def __init__(self):  # fixed constructor
        # Taking input from the user and splitting by commas or spaces
        user_input = input("Enter student IDs (e.g., std_001, std_002): ")
        # Clean the input into a list of strings
        self.student_ids = [s.strip() for s in re.split(r'[,\s]+', user_input) if s]

class Qualifying(Students):
    def __init__(self):  # fixed constructor
        super().__init__()
        self.q1 = []  # To store even student IDs
        self.q2 = []  # To store odd student IDs

    def sort_students(self):
        for sid in self.student_ids:
            # Regex to find the numeric part
            match = re.search(r'\d+', sid)
            if match:
                num = int(match.group())
                # Condition: Even goes to q1, Odd goes to q2
                if num % 2 == 0:
                    self.q1.append(sid)
                else:
                    self.q2.append(sid)

    def display_results(self):
        print("\n--- Qualifying Results ---")
        print(f"Q1 (Even IDs - Allowed to participate first): {self.q1}")
        print(f"Q2 (Odd IDs - Participating later): {self.q2}")


# --- Execution ---
qualifier = Qualifying()
qualifier.sort_students()
qualifier.display_results()
