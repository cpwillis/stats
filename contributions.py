import datetime as mydate
import os
import random
import uuid
import subprocess
import git
import argparse


class FakeGitHistory:
    def __init__(self, push=False):
        self.project_dir = os.path.realpath(os.path.dirname(__file__))
        self.repo = None
        self.remote_url = subprocess.run(
            ["git", "remote", "get-url", "origin"], capture_output=True, text=True
        ).stdout.strip()
        self.repo_username, self.repo_name = self.extract_username_repo(self.remote_url)
        self.push = push
        print("[Info]: Starting")

    def extract_username_repo(self, remote_url):
        if remote_url.endswith(".git"):
            remote_url = remote_url[:-4]
        parts = remote_url.split("/")
        return parts[-2], parts[-1]

    def load_repo(self):
        try:
            print("[Info]: Loading git repository")
            self.repo = git.Repo(self.project_dir)
            print("[Info]: Repo loaded")
        except git.exc.NoSuchPathError:
            print("[Error]: Repo not found. Creating new one from remote-url")
            self.repo = git.Repo.clone_from(self.remote_url, self.project_dir)

    def execute_commit(self, day: int, month: int, year: int):
        action_date = str(mydate.date(year, month, day).strftime("%Y-%m-%d %H:%M:%S"))
        os.environ["GIT_AUTHOR_DATE"] = action_date
        os.environ["GIT_COMMITTER_DATE"] = action_date
        self.repo.index.commit(message=str(uuid.uuid4().hex))
        if self.push:
            self.git_push()

    def single_commit(self, day: int, month: int, year: int):
        current_date = mydate.date(year, month, day)
        commits_range = args.commits.split(",")
        if len(commits_range) == 1:
            min_commits = max_commits = int(commits_range[0])
        else:
            min_commits, max_commits = map(int, commits_range)
        commits_amount = random.randint(min_commits, max_commits)
        print(f"Currently committing {current_date} with {commits_amount} commits")
        for _ in range(commits_amount):
            self.execute_commit(day, month, year)

    def many_commits(
        self,
        start_day: int,
        start_month: int,
        start_year: int,
        stop_day: int,
        stop_month: int,
        stop_year: int,
    ):
        if (
            start_day == stop_day
            and start_month == stop_month
            and start_year == stop_year
        ):
            self.single_commit(start_day, start_month, start_year)
        else:
            commit_start_date = mydate.date(start_year, start_month, start_day)
            commit_stop_date = mydate.date(stop_year, stop_month, stop_day)
            while commit_start_date < commit_stop_date:
                self.single_commit(
                    commit_start_date.day,
                    commit_start_date.month,
                    commit_start_date.year,
                )
                commit_start_date += mydate.timedelta(days=1)

    def git_push(self):
        try:
            origin = self.repo.remote(name="origin")
            origin.push()
        except Exception as e:
            print(f"Error occurred while pushing the code !:\n{e}")
        else:
            print("Changes have been pushed!")


def parse_args():
    parser = argparse.ArgumentParser(description="Generate fake Git commits.")
    parser.add_argument(
        "-c",
        "--commits",
        type=str,
        default="0,3",
        help="Number of commits per day. Specify as 'min,max' or a single number for both min and max. Default is '0,3'. Example: -c 1,5",
    )
    parser.add_argument(
        "-w",
        "--workdays",
        action="store_true",
        help="Commit only on workdays (Monday to Friday).",
    )
    parser.add_argument(
        "-s", "--start", type=str, help="Start date (format: 'DD/MM/YYYY')."
    )
    parser.add_argument(
        "-e", "--end", type=str, help="End date (format: 'DD/MM/YYYY')."
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Automatically push commits after they are created.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    contributions = FakeGitHistory(push=args.push)
    contributions.load_repo()

    if args.start and args.end:
        start_day, start_month, start_year = [int(x) for x in args.start.split("/")]
        stop_day, stop_month, stop_year = [int(x) for x in args.end.split("/")]
        contributions.many_commits(
            start_day, start_month, start_year, stop_day, stop_month, stop_year
        )
    elif args.start or args.end:
        date = args.start if args.start else args.end
        day, month, year = [int(x) for x in date.split("/")]
        contributions.single_commit(day, month, year)
    else:
        print("Please provide at least the start or end date.")
