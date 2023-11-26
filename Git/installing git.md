# GIT

Git is a free and open-source distributed version control system (DVCS) that was created by Linus Torvalds in 2005. It is widely used in software development to manage code revisions and track changes made to source code files.

## Installing Git

- Windows
Download the Git installer: Visit <https://git-scm.com/download/win> to download the latest version of Git for Windows.

Run the installer: Locate the downloaded installer file and double-click on it to run the installation process.

Customize the installation (optional): Proceed through the installer screens, accepting the default settings or customizing them as needed.

Install Git: Click 'Install' to begin the installation process.

Complete the installation: Click 'Finish' once the installation is complete.

Verify the installation: Open a new command prompt or Git Bash, and type git --version to check the installed Git version.

- macOS
Check for existing Git: Open the Terminal app and type git --version. If Git is already installed, you'll see the installed version. If not, you'll receive a prompt to install the Xcode Command Line Tools.
Install Git using Xcode Command Line Tools (if not already installed): Type xcode-select --install in the Terminal app and follow the on-screen instructions. This will install Git along with other command line tools. If you prefer to install Git separately, proceed to step 3.
Install Git using Homebrew (alternative method): If you have Homebrew installed, you can install Git by typing brew install git in the Terminal app.
Verify the installation: Type git --version in the Terminal app to check the installed Git version.

To get started with Git using Git Bash, follow these step-by-step instructions:

1 Open Git Bash:
Search for Git Bash in the Start menu (Windows) or Launchpad (macOS), and open it.

2 Configure Git:
Before you start using Git, you need to configure your name and email address, which will be used for commit messages. Run the following commands, replacing "Your Name" and "<youremail@example.com>" with your own information:

git config --global user.name "Your Name"
git config --global user.email "<youremail@example.com>"

3 Create directory/Folder
Open Git Bash:
Search for Git Bash in the Start menu (Windows) or Launchpad (macOS), and open it.

make your folder:
you can create it using the mkdir command in the gitbash

## make directory ADSnotes

mkdir directory_name

## enter ADSnotes

cd directory_name

## create files (OPTIONAL)

touch  notebook1.ipynb

4 Now, initialize a new Git repository in the current folder by running:
git init

5 Add a file to the staging environment

## Staging files: Stages the current directory and all its content

git add .
The . will stage all files in the folder. To stage only specific files, replace the . with the file names separated by spaces.

6 Commit the changes: Commit the staged files with a descriptive message using the git commit command:

## Commits with a one-line message

git commit -m "Your commit message here"

7 Check the status: Use the git status command to view the current state of your repository:
git status

8 Review the commit history: To view a log of all commits in the repository, use the git log command:
git log

## Github

GitHub is a web-based platform for hosting Git repositories.

It provides a wide range of tools and features to help developers collaborate on code and manage software projects.

GitHub offers both free and paid plans, with the free plan providing basic functionality and the paid plans offering more advanced features.

GitHub allows developers to host their Git repositories on their servers, and provides a web-based interface that makes it easy to manage and track changes to code.

It offers features like pull requests, which allow developers to propose changes to a codebase and have them reviewed by other developers, and issues, which can be used to track bugs, feature requests, and other tasks related to a project.

GitHub also offers collaboration tools like code reviews, project management tools, and team communication features, making it a powerful platform for software development teams.

GitHub has become one of the most popular platforms for hosting open-source projects, and many software development teams use GitHub to manage their code and collaborate with other developers.

By using GitHub, developers can benefit from the power and flexibility of Git, while also taking advantage of the many tools and features provided by the GitHub platform.

GitHub also provides a wide range of integrations and extensions that can be used to extend its functionality and integrate it with other development tools and services.

In addition to hosting Git repositories, GitHub also offers a wide range of resources, including documentation, tutorials, and community forums, that can be used to learn about Git, software development best practices, and other topics related to software development.

## Push Your REPO to GitHub

9 Create a GitHub Account
The first step is to create a GitHub account. Go to the GitHub website (https://github.com/) and click on the "Sign up" button in the top-right corner. Follow the instructions to create your account.

10 Create a New Repository
Once you have created your account, you can create a new repository.
*Click on the "+" icon in the top-right corner of the GitHub website and select "New repository" from the drop-down menu. Give your repository a name and click on the "Create repository" button.

11 Push local Repo to GitHub
git remote add origin <https://github.com/YOUR-USERNAME/YOUR-REPOSITORY>
git branch -M main
git push -u origin main

## Cloning a GitHub Repository to Your Computer

If you want to work on a project hosted on GitHub, you can clone it to your local computer using Git. Here are the steps to do so:

Step 1: Navigate to the Repository on GitHub
Go to the main page of the repository that you want to clone.

Step 2: Click the Code Button
Click the "Code" button located above the list of files in the repository.

Step 3: Select the Clone URL
Under the "Clone with HTTPS" section, select the URL for the repository that you want to clone.

Step 4: Open Git Bash
Open Git Bash, a command line interface for Git.

Step 5: Change the Directory
Use the "cd" command to navigate to the directory where you want to store your cloned repository. For example, if you want to store your cloned repository in the "Documents" folder on your computer, you can run the following command:

$ cd Documents/
Step 6: Clone the Repository
Run the "git clone" command, followed by the URL of the repository that you want to clone. For example:

$ git clone <https://github.com/YOUR-USERNAME/YOUR-REPOSITORY>