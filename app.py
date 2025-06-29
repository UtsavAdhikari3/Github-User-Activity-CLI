import requests
import json



def main():
    git_username = input("Enter your github user_name: ")
    res = requests.get(f"https://api.github.com/users/{git_username}/events")

    data = res.json()

    if len(data) == 0:
        print(f"{git_username} not found.")
    git_activity(git_username, data)  


def git_activity(git_username,data):
    for items in data:
        if items["type"] == "CreateEvent":
            print(f"{git_username} created a new repository. {items["repo"]["name"]}")
        elif items["type"] == "PushEvent":
            print(f"{git_username} pushed a commit to {items["repo"]["name"]}")
        elif items["type"] == "PullRequestEvent":
            print(f"{git_username} created a new pull request on {items["repo"]["name"]}")
        elif items["type"] == "WatchEvent" and items["payload"]["action"] == "started":
            print(f"{git_username} Starred {items["repo"]["name"]}")


if __name__ == "__main__":
    main()