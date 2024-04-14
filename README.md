# stats

This repository delves into GitHub activity metrics, contrasting the allure of polished profiles with the question of their relevance in assessing coding proficiency. By scrutinising the underlying data and methodologies, we aim to demonstrate how easily these metrics can be replicated and challenge the notion that "activity" equates to competence.

In today's digital landscape, GitHub profiles serve as more than just repositories for code - they've become symbolic representations of developers' identities. However, the authenticity of these profiles often comes into question, especially when evaluating coding proficiency solely based on activity metrics. This repository seeks to dissect GitHub activity metrics, unraveling the complexities behind them, and challenging the assumption that mere "activity" equates to competence.

However, several points of issue arise when relying on these statistics to gauge proficiency;

- Emphasises the significance of organisation membership in conferring credibility.
- Warns against relying solely on verification symbols, which attest to domain validity rather than individual affiliation.
- Exposes how GitHub achievements can be easily spoofed through automation, undermining their reliability as indicators of genuine activity or skill.
- Reveals how commit date manipulation can create the illusion of sustained engagement, regardless of actual involvement.
- Discusses the ease with which celebrity contributors can be fabricated, undermining the authenticity of project associations.
- Notes the lack of mechanisms to verify the accuracy of statistics in profile README files, rendering them susceptible to embellishment.

## How it works

A commit acts as a snapshot of the repository at a specific point in time, capturing changes made to the codebase. At a fundamental level, Git stores everything as objects, with commits being the building blocks. Our comprehension of how commits work is crucial for harnessing Git's capabilities effectively.

A Git commit comprises comprehensive metadata detailing various aspects of the commit. This includes the date, author, committer, commit message, as well as identifiers for the commit's directory tree object and parent commit(s). The parent commit's hash serves as a pointer, linking commits together, and a commit may have multiple parent commits, especially after merging branches.

The tree object referenced in a commit contains the directory listing for that commit, composed of branching Tree objects (sub-directories) and Blob objects (Binary Large Objects containing file contents). Understanding these objects provides insight into the repository's structure and the changes introduced at each commit.

## Contributions

### Demonstration

[contributions.py](.contributions.py) is a Python script designed to create a simulated Git repository history. It generates pseudo-random commit messages and commit dates, allowing users to mimic a busy commit activity. It serves as a basic demonstration of how one can modify commit histories for various purposes. Similar alternatives include [artiebits/fake-git-history](https://github.com/artiebits/fake-git-history) and [theveloper-pl/Fake-Git-History](https://github.com/theveloper-pl/Fake-Git-History).

**Usage**

```sh
usage: contributions.py [-h] [-c COMMITS] [-w] [-s START] [-e END] [--push]

Generate fake Git commits.

options:
  -h, --help            show this help message and exit
  -c COMMITS, --commits COMMITS
                        Number of commits per day. Specify as 'min,max'. Default is '0,3'. Example: -c 1,5
  -w, --workdays        Commit only on workdays (Monday to Friday).
  -s START, --start START
                        Start date (format: 'DD/MM/YYYY').
  -e END, --end END     End date (format: 'DD/MM/YYYY').
  --push                Automatically push commits after they are created.
```

## Achievements

[All Achievements](https://github.com/drknzz/GitHub-Achievements)
Uncover insights into GitHub achievements and their potential manipulation:

### Demonstration

Forked from [Anurag-gg/pull-shark-automation](https://github.com/Anurag-gg/pull-shark-automation)

**Usage**

1. Save Script: Save the `pull-shark-automation.py` script to your repository.
2. Save Workflow: Save the `pull-shark-automation.yml` file in the `.github/workflows` directory of your repository.
3. Setup GitHub Secrets: Create a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) named `PAT` in your repository [secrets](https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md). This token will be used for authentication when creating pull requests.
4. Enable GitHub Actions: Go to the "Actions" tab of your repository on GitHub and enable workflows.
5. Run Workflow: The workflow will automatically run every minute, updating the pull request count in the `pull-shark-automation.txt` file and creating a new pull request if necessary.
6. Monitor Progress: Check the pull request count in the `pull-shark-automation.txt` file and monitor the creation of pull requests in your repository.
7. Disable Workflow (_Optional_): Once you've achieved the desired number of pull requests or badges, you can disable the workflow in the "Actions" tab.

## Trophies

[GitHub Profile Trophy](https://github.com/ryo-ma/github-profile-trophy)
