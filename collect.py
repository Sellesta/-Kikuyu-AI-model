import pandas as pd
import json

# Function to collect data
def collect_translation_data():
    data = []
    print("Enter 'STOP' to end data collection.")
    
    while True:
        kikuyu = input("Enter Kikuyu word/phrase (or 'STOP' to finish): ")
        if kikuyu.lower() == 'stop':
            break
        swahili = input("Enter corresponding Swahili translation: ")
        english = input("Enter corresponding English translation: ")
        
        # Append the collected data as a dictionary
        data.append({
            "Kikuyu": kikuyu,
            "Swahili": swahili,
            "English": english
        })
    
    return data

# Function to save data to CSV
def save_data_to_csv(data, filename='translations.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Data saved to {filename}")

# Function to save data to JSON
def save_data_to_json(data, filename='translations.json'):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

# Main program execution
if __name__ == "__main__":
    collected_data = collect_translation_data()
    if collected_data:
        save_format = input("Enter preferred save format (CSV/JSON): ").lower()
        if save_format == 'csv':
            save_data_to_csv(collected_data)
        elif save_format == 'json':
            save_data_to_json(collected_data)
        else:
            print("Invalid format. Data will not be saved.")
    else:
        print("No data collected.")
