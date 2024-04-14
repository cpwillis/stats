import os


def update_pull_shark_automation():
    try:
        with open("pull-shark-automation.txt", "r") as f:
            num = int(f.readline().strip())
            num += 1
        if num <= 1024:
            with open("pull-shark-automation.txt", "w") as f:
                f.write(str(num))
    except Exception as e:
        print(f"Error: {e}")
        with open("pull-shark-automation.txt", "w") as f:
            f.write("1")


if __name__ == "__main__":
    update_pull_shark_automation()
