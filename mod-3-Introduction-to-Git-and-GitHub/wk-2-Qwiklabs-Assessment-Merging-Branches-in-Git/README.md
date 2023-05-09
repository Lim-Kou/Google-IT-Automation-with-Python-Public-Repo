## Introduction

In this lab, you'll use your knowledge of Git and Git commit history to check out an existing repo and make some changes to it. You'll also test what you learned about rolling back commits after bad changes in order to fix a script in the repo and run it to produce the correct output.

### What you'll do

-   Check the status and history of an existing Git repo
-   Create a branch
-   Modify content on the branch
-   Make rollback changes
-   Merge the branch

You'll have 90 minutes to complete this lab.


## Explore repository

There is a Git repository named `food-scripts` consisting of a couple of food-related Python scripts.

Navigate to the repository using the following command:

```cd ~/food-scripts```

Now, list the files using the `ls` command. There are three files named **favorite_foods.log**, **food_count.py**, and **food_question.py**.

![1.png](https://cdn.qwiklabs.com/xrqDCNooc0A5Al0Nesw3cwMIwv%2BmXHrpJMNWbLMFTp8%3D)

Let's explore each file. Use the `cat` command to view each file.

1.  **favorite_foods.log**: This file consists of a list of food items. You can view it using the following command:
    

```cat favorite_foods.log```

Output:

![47403089d228e2c1.png](https://cdn.qwiklabs.com/CSGCNDTCo1pF%2FuG00KZzl6xg%2Fm%2FZ4mbBJReHmLs2hF0%3D)

2.  **food_count.py**: This script returns a list of each food and the number of times the food appeared in the `favorite_foods.log` file.

Let's execute the script `food_count.py`:

`````./food_count.py`````

Output:

![1c36a02d5ebaef5d.png](https://cdn.qwiklabs.com/QcfsJ58wgv5XcoHrm0A2OtbyEIaKb5wZTwyId3hOMdA%3D)

3.  **food_question.py**: This prints a list of foods and prompts the user to enter one of those foods as their favorite. It then returns an answer of how many others in the list like that same food.

Run the following command to see the output of `food_question.py` script:

```./food_question.py```

Output:

![5079d715c2f97126.png](https://cdn.qwiklabs.com/22L%2FOVmhvu3LRQLuJhY1KciRckwgzo7Ps9V611zYHvA%3D)

Uh oh , this gives us an error. One of your colleagues reports that this script was working fine until the most recent commit. We'll be fixing this error later during the lab.

## Understanding the repository

Let's use the following Git operations to understand the workflow of the repository:

-   git status
-   git log
-   git branch

**Git status:** This displays paths that have differences between the index file and the current HEAD commit; paths that have differences between the working tree and the index file; and paths in the working tree that are not tracked by Git. You can view the status of the working tree using the command: [**git status]**

```git status```

You can now view the status of the working tree.

**Git log:** This lists the commits done in the repository in reverse chronological order; that is, the most recent commits show up first. This command lists each commit with its SHA-1 checksum, the author's name and email, date, and the commit message.

You can see logs by using the following command:

```git log```

Output:

![37aaa3162a88b121.png](https://cdn.qwiklabs.com/2o6mlSC1uFH%2BeFjDNP8VAEz%2FVCTtgO6xyXNZq3Cxa10%3D)

**Git branch:** Branches are a part of the everyday development process on the master branch. Git branches effectively function as a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug, no matter how big or small, you spawn a new branch to encapsulate your changes. This makes it difficult for unstable code to get merged into the main codebase.

### Configure Git

Before we move forward with the lab, let's configure Git. Git uses a username to associate commits with an identity. It does this by using the **git config** command. Set the Git username with the following command:

```git config user.name "Name"```

Replace **Name** with your name. Any future commits you push to GitHub from the command line will now be represented by this name. You can even use **git config** to change the name associated with your Git commits. This will only affect future commits and won't change the name used for past commits.

Let's set your email address to associate them with your Git commits.

```git config user.email "user@example.com"```

Replace **user@example.com** with your email-id. Any future commits you now push to GitHub will be associated with this email address. You can also use **git config** to change the user email associated with your Git commits.

## Add a new feature

In this section, we'll be modifying the repository to add a new feature, without affecting the current iteration. This new feature is designed to improve the food count (from the file food_count.py) output. So, create a branch named **improve-output** using the following command:

```git branch improve-output```

Move to the `improve-output` branch from the master branch.

```git checkout improve-output```

Here, you can modify the script file without disturbing the existing code. Once modified and tested, you can update the master branch with a working code.

Now, open `food_count.py` in the nano editor using the following command:

```nano food_count.py```

Add the line below before **printing for loop** in the `food_count.py` script:

```print("Favourite foods, from most popular to least popular")```

Save the file by pressing Ctrl-o, the Enter key, and Ctrl-x. Then run the script `food_count.py` again to see the output:

```./food_count.py```

Output:

![food_count_output.png](https://cdn.qwiklabs.com/z8M4Fd628hnP6o2H2f%2FqHNjLWP3Q0hBcBgKJD%2BAfJ0Y%3D)

After running the `food_count.py` script successfully, commit the changes from the `improve-output` branch by adding this script to the staging area using the following command:

```git add food_count.py```

Now, commit the changes you've done in the `improve-output` branch.

```git commit -m "Adding a line in the output describing the utility of food_count.py script"```

Output:

![7.png](https://cdn.qwiklabs.com/IJzJsuo6qpX5%2F6um2d6h7ZkWDysoDMLfiGpY51mICuk%3D)

Click _Check my progress_ to verify the objective. Add a feature

## Fix the script

In this section, we'll fix the script food_question.py, which displayed an error when executing it. You can run the file again to view the error.

```./food_question.py```

Output:

![5079d715c2f97126.png](https://cdn.qwiklabs.com/22L%2FOVmhvu3LRQLuJhY1KciRckwgzo7Ps9V611zYHvA%3D)

This script gives us the error: "**NameError: name 'item' is not defined**" but your colleague says that the file was running fine before the most recent commit they did.

In this case, we'll revert back the previous commit.

For this, check the git log history so that you can revert back to the commit where it was working fine.

```git log```

Output:

![e89b58d398338a9d.png](https://cdn.qwiklabs.com/iB0yunpXeqWg1uXbCDrSkZSEJ1EVsC6i%2Fplr7pvW6FU%3D)

Here, you'll see the commits in reverse chronological order and find the commit having "**Rename item variable to food_item**" as a commit message. Make sure to note the commit ID for this particular commit.

To revert, use the following command:

```git revert [commit-ID]```

Replace `[commit-ID]` with the commit ID you noted earlier.

This creates a new commit again. You can continue with the default commit message on the screen or add your own commit message.

Then continue by clicking Ctrl-o, the Enter key, and Ctrl-x.

Now, run `food_question.py` again and verify that it's working as intended.

```./food_question.py```

Output:

![cedea93d17157044.png](https://cdn.qwiklabs.com/5lmajDZIiOCM35MJIHdrs8nP8obUyOZ3zeZJIyDcTfA%3D)

## Merge operation

Before merging the branch `improve-output,` switch to the master branch from the current branch `improve-output` branch using the command below:

```git checkout master```

Merge the branch `improve-output` into the master branch.

```git merge improve-output```

Output:

![11.png](https://cdn.qwiklabs.com/5doCuaR47qrzBO3J5F%2B4KTmPEdEgEzgwRUi43v2HbVA%3D)

Now, all your changes made in the `improve-output` branch are on the master branch.

```./food_question.py```

Output:

![5216220ceb4627f1.png](https://cdn.qwiklabs.com/ZEm%2F7r3%2Fc7z%2BpX0RcOQBICm9xbFgz5HGoBFOkT1jNQU%3D)

To get the status from the master branch, use the command below:

```git status```

Output:

![c18b4c4d4dd08623.png](https://cdn.qwiklabs.com/Sah1W1pa30ZTzDBh5f%2BbVCf5i%2Fhp%2ByD1E4U%2FcVZSXTA%3D)

To track the git commit logs, use the following command:

```git log```

Output:

![b78661eaf4c93cf1.png](https://cdn.qwiklabs.com/yjeLI4OHbwNjtA5R9Idz2Joezf6LQYwIazPCkvpm458%3D)

Enter **q** to exit.

Click _Check my progress_ to verify the objective. Revert changes

## Congratulations!

In this lab, you successfully created a branch from the master branch to add a new feature. You also rolled back a commit to where the script worked fine, and then merged it to the master branch. This will help as you work with colleagues who are simultaneously on the same repository.

## End your lab

When you have completed your lab, click **End Lab**. Qwiklabs removes the resources you’ve used and cleans the account for you.

You will be given an opportunity to rate the lab experience. Select the applicable number of stars, type a comment, and then click **Submit**.

The number of stars indicates the following:

-   1 star = Very dissatisfied
-   2 stars = Dissatisfied
-   3 stars = Neutral
-   4 stars = Satisfied
-   5 stars = Very satisfied

You can close the dialog box if you don't want to provide feedback.

For feedback, suggestions, or corrections, please use the **Support** tab.