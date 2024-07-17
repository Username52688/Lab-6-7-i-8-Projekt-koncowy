import sys
import json

#Task1
def parse_arguments():
    if len(sys.argv) != 3:
        print(" program.exe pathFile1.x pathFile2.y")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file


#task2


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd w zapisywaniu pliku JSON: {e}")
        sys.exit(1)



#Task3
def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Błąd w zapisywaniu pliku JSON: {e}")
        sys.exit(1)



#Wykonywanie skryptu
if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    
    if input_file.endswith('.json'):
        data = load_json(input_file)
        print(data)
        
        if output_file.endswith('.json'):
            save_json(data, output_file)
            print(f"Dane zostały zapisane do {output_file}")
        else:
            print("Plik wyjściowy musi mieć rozszerzenie .json")
    else:
        print("Plik wejściowy musi mieć rozszerzenie .json")
