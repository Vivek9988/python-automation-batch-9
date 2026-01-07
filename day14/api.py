import requests

def get_user_details(username):
    url = f'https://api.github.com/users/{username}'  # fixed quotes and variable name
    response = requests.get(url)  # fixed typo 'reguests' -> 'requests'
    
    if response.status_code == 200:  # fixed syntax
        user_data = response.json()  # fixed typo 'ison' -> 'json'
        print("User Name:", user_data["login"])
        print("Public Repos:", user_data["public_repos"])
    else:
        print("Failed to fetch data")

# Example usage
get_user_details("octocat")
