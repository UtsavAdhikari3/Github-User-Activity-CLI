import requests
import json



def get_activity():
    git_username = input("Enter your github user_name: ")
    res = requests.get(f"https://api.github.com/users/{git_username}/events")

    data = res.json()
    for items in data:
        if items["type"] == "CreateEvent":
            print(f"{git_username} created a new repository. {items["repo"]["name"]}")
        elif items["type"] == "PushEvent":
            print(f"{git_username} pushed a commit to {items["repo"]["name"]}")
        elif items["type"] == "PullRequestEvent":
            print(f"{git_username} created a new pull request on {items["repo"]["name"]}")
        


if __name__ == "__main__":
    get_activity()