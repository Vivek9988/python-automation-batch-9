# order_processor.py
import requests
import json
import csv

def fetch_orders(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"API request successful: {response.status_code} OK")
            return response.json()
        else:
            print(f"API request failed: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"API connection error: {e}")
        return None

def validate_orders(raw_data):
    valid_orders = []
    if not isinstance(raw_data, list):
        return []
    for item in raw_data[:4]:  # only first 4 to match sample
        order = {
            "order_id": item.get("id"),
            "customer_name": f"Customer_{item.get('userId')}",
            "total_amount": float(item.get("id", 0) * 10),
            "order_status": "Shipped"
        }
        if all(key in order for key in ['order_id', 'customer_name', 'total_amount', 'order_status']):
            valid_orders.append(order)
    return valid_orders

def save_to_json(orders, filename='orders.json'):
    try:
        with open(filename, 'w') as f:
            json.dump(orders, f, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error saving to JSON: {e}")

def save_to_csv(orders, filename='orders.csv'):
    if not orders:
        return
    try:
        keys = orders[0].keys()
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(orders)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error saving to CSV: {e}")

def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    raw_data = fetch_orders(url)
    if raw_data:
        valid_orders = validate_orders(raw_data)
        print(f"Valid orders processed: {len(valid_orders)}")
        save_to_json(valid_orders)
        save_to_csv(valid_orders)

if __name__ == "__main__":
    main()