# git code .                                //Open vs code

## git status                                //Show file status

## git status -s                             //show short file status

## git add <filename>                        //Add the particular file to staging area

## git add .                                  //Add all the file to the staging area

## git commit --amend                        //Add these changes to the last commit (will have to use vim editor)

## git commit -m "message"                   //Commit the files in the staging area

## git commit -am "message"                  //Will commit without adding the file to the staging area

## git checkout --<filename>                 //will restore the file from the last commit

## git checkout -f                           //All the files will be replaced with last commit

## git checkout -b <branch_name>   	         //Create a branch

## git branch                                 //To see the branches

## git branch -d <branch name>                //To delete a branch

## git branch -v                              //will show the branch and its last commit

## git branch --merged                        //will show the branches that are merged

## git branch --no-merged                    //will show the branches that are not merged

## git merge <branch name>                   //while in a branch you can merge another branch

## git log                                   //Show all the commits

## git log -n                                //n can be replaced by any number "will show last n commits"

## git log -p                                //Will show detailed discription of the commits

## git log -p -n                             //use of n is similar as described above

## git log --stat                            //will show short detailing of the commits

## git log --stat -n                         //use of n is similar as described above

## git log --since=n.days                    //commit of last n days/weeks/months "days can be replaced by weeks,months"

## git rm --cached <filename>                //will remove to file from the tracking area

## git rm -rf                                //will uninitialized the current repository

## git rm <filename>                         //will delete the file

## git mv <Present filename> <The filename after the change>  //to Rename the file

## git clone <URL>                           //Cloning a repository in the current folder

## git clone <URL> foldername               //Cloning the repository in the given folder name (Folder will be created by itself)

## git config --global alias. <new name> 'old command'  //while create an alias command for the given command

## git remote                               //Show all the name of remote repository

## git remote -v                            //Show all the path (fetch/push) of the remote repository

## git remote add <name> url                //Add a remote repository

## git remote rm <name>                     //To remove a remote

## git push <remote name> <branch name>	    //To push a branch to remote repository

## git push <remote name> <branch name>:     <branch name you want to have in the remote repository>

## git reset HEAD                         //To move to a previous commit

## to fix conflicts ------<https://amigoscode.com/courses/>

Git commands you'll often use:

git init - Initializes a new Git repository in the current directory.
git clone <repository> - Creates a local copy of a remote repository.
git add <file> - Adds a file (or changes in a file) to the staging area, preparing it for a commit.
git add . - Adds all changes in the working directory to the staging area.
git status - Displays the status of your working directory.
git commit -m "<message>" - Creates a new commit with the changes in the staging area and a descriptive message.
git log - Displays the commit history of the current branch.
git diff - Shows the differences between the working directory and the latest commit.
git diff <commit1> <commit2> - Shows the differences between two specific commits.
git remote add <name> <repository> - Adds a remote repository to your local repository with a reference name.
git fetch <remote> - Fetches changes from a remote repository but doesn't merge them.
git pull <remote> <branch> - Fetches changes from a remote repository and merges them into your local repository.
git push <remote> <branch> - Pushes your local changes to a remote repository.
git branch - Lists all branches in your local repository.
git branch <branch-name> - Creates a new branch with the given name.
git checkout <branch> - Switches to the specified branch.
git merge <branch> - Merges the specified branch into the current branch.
git stash - Temporarily saves changes in the working directory that are not yet committed.
git stash apply - Applies the most recent stashed changes to the working directory.
git stash list - Lists all stashed changes in the repository.
git stash drop - Removes the most recent stashed changes.
