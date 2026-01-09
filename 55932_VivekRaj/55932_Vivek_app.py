import requests
import json
import csv

MANDATORY_FIELDS = ["id", "name", "email"]


def fetch_users(api_url):
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()

        # Validate content type
        if "application/json" not in response.headers.get("Content-Type", ""):
            raise ValueError("Invalid Content-Type")

        data = response.json()

        if not isinstance(data, list):
            raise ValueError("API did not return a list")

        return data

    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        raise


def is_valid_record(record):
    for field in MANDATORY_FIELDS:
        if field not in record or record[field] is None:
            return False
    return True

def filter_valid_records(records):
    return [r for r in records if is_valid_record(r)]


def save_to_json(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print("File write error (JSON):", e)
        raise

def save_to_csv(filename, data):
    try:
        if not data:
            return

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    except IOError as e:
        print("File write error (CSV):", e)
        raise


def process_users(api_url):
    users = fetch_users(api_url)
    valid_users = filter_valid_records(users)

    print(f"Valid records processed: {len(valid_users)}")

    save_to_json("users.json", valid_users)
    save_to_csv("users.csv", valid_users)

    print("Data saved to users.json")
    print("Data saved to users.csv")

    return valid_users



if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/users"
    process_users(API_URL)

    
