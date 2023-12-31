## Introduction

You're a member of the IT team at your company. One of your coworkers has recently set up a Puppet installation, but it doesn't seem to be doing its job. So, you're asked to debug the profile class, which is supposed to append a path to the environment variable `$PATH`. But it's somehow misbehaving and causing the `$PATH` variable to be broken. You'll need to locate the issue and fix it with the knowledge that you learned in this module.

### What you'll do

-   Check out what Puppet rules look like
-   Run the Puppet agent locally
-   Understand how file permissions are represented by numbers
-   Learn how scripts under `/etc/profile.d/` perform startup tasks, including setting up your own environment variables
-   Append a string to an environment variable

You'll have 90 minutes to complete this lab.

## Puppet rules

The Puppet rules are present in the init file. The purpose of this script is to append /java/bin to the environment variable $PATH, so that scripts in that directory can be executed without writing the full path.

The purpose of this rule is to append `/java/bin` to the environment variable `$PATH` so that scripts in that directory can be executed without writing the full path.

## Issue detection

Now, take a look at the environment variable `$PATH` by running the following command:

```echo $PATH```

Output:

![7382a96308ced41f.png](https://cdn.qwiklabs.com/6pm3XtbZkWzWD1oiGK8icgQZ%2FwOosJmy6Y4s8hvfpUA%3D)

Oops, something is wrong; the main directories used for executing binaries in Linux (`/bin` and `/usr/bin`) are missing.

You can check this by executing the following command:

```ls /```

Output:

![c55b4084f426341f.png](https://cdn.qwiklabs.com/3e8NxHc1IQXu6cw1nZ3FMhbdIN8j5W4gSTQ2CpFBFn8%3D)

Commands like `ls`, `cd`, `mkdir`, `rm,` and others are just small programs that usually live inside a directory on our systems called `/usr/bin`.

To get back to a working environment, run the following command:

```export PATH=/bin:/usr/bin```

By running this command, you manually add the directories that contain executing binaries (`/bin` and `/usr/bin`) to the environment variable `$PATH.` That way, the system will be able to find the commands when you try to run them. Now, run the list directory command, again:

```ls /```

Output:

![562848a6585d99fb.png](https://cdn.qwiklabs.com/%2B%2BVtiN3Rjn42vA6h5sa3e7eDZROibgYwK1BkzuySmHY%3D)

Alright, now that we have a working PATH, let's look at the rule responsible for this breakage. It's located in the **profile** module of Puppet's **production** environment. To look at it, go to the `manifests/` directory that contains the Puppet rules by using the following command:

```cd /etc/puppet/code/environments/production/modules/profile/manifests```

Use `cat` to check out the contents of the `init.pp` file:

```cat init.pp```

![1a2fdbf9f06c0679.png](https://cdn.qwiklabs.com/dRI%2FsOmQ%2FU0RQl58oIgKY6y%2FfSeODmXnXMpBCc50c4o%3D)

This rule is creating a script under `/etc/profile.d/`. Scripts in this path will perform startup tasks, including setting up a user's own environment variables. The files under `/etc/profile.d/` should only be editable by root.

We see that the file resource is part of the **profile** class. The general rules for creating a Puppet class definition used here are:

-   The class definition starts with the "class" keyword, followed by the name of the class. In this case, "profile".
-   The contents of the class are defined between curly braces and generally contain at least one resource declaration. In this case, a "file" resource.

There could be other resources in this class, but for now it has only one file resource. Let's look at what it's doing. The file defined by this resource is '`/etc/profile.d/append-path.sh`', and the Puppet rule is using some of the available "file" attributes:

-   It sets both the owner and group of the file to "root".
    
-   It then sets the "mode" of the file to "0646". This number represents the permissions the file will have.
    
-   You might remember that every file and directory on a Linux system is assigned permissions for three groups of people: the owner, the group and the others.. And for each group, the permissions refer to the possibility of reading, writing and executing the file.
    
-   It's common to use numbers to represent the permissions: 4 for read, 2 for write and 1 for execute. The sum of the permissions given to each of the groups is then a part of the final number. For example, a permission of 6 means read and write, a permission of 5 means read and execute, and a permission of 7 means read, write and execute.
    
-   In this example, we are using 4 numbers. The first one represents any special permissions that the file has (no special permissions). The second one is the permissions for the owner, (read and write), and then come the permissions for the group (read), and finally the permissions for the others (read and write)
    
-   Finally, it sets the actual contents of the file. Here, the content is being set to`"PATH=/java/bin\n".`
    

## Fixing the problem

Before fixing the issue, let's learn a bit more about the PATH variable. This is an environment variable that contains an ordered list of paths that Linux will search for executables when running a command. Using these paths implies that we don't have to specify the absolute path for each command we want to run.

The PATH variable typically contains a few different paths, which are separated by colons. The goal of the Puppet rule that we saw was to add one specific directory to the list of paths, but unfortunately it's currently completely overwriting the contents. We need to change the Puppet rule to **append** the directory without overwriting the other paths in the variable.

To do this, we'll first include the current contents of the PATH variable followed by a colon, and then append the new contents we want to add.

Open the file init.pp using the nano editor:

```sudo nano init.pp```

Now, the content attribute should be changed. The line `content => "PATH=/java/bin\n"` should be changed to `content => "PATH=\$PATH:/java/bin\n"` since we want to append `/java/bin` to the environment variable `$PATH`, and not completely replace the current content in `$PATH`.

The extra backslash before the `$` is necessary because Puppet also uses `$` to indicate variables. But in this case, we want the dollar sign in the contents of the file.

On top of this, files in the `/etc/profile.d` directory should only be editable by the root user. In order to do this we'll need to change the mode of the file to avoid giving others permission to write the file. In other words, the mode should be 0644 not 0646.

Once you're done fixing the mode and content attributes, remember to save the file and close it.

After that, you can trigger a manual run of the Puppet agent by running the following command:

```sudo puppet agent -v --test```

Go ahead and initiate a **second SSH connection** following the same instructions from the `Accessing the linux virtual machine` section. Then, verify that the profile is fixed by checking the contents of the PATH variable.

To check the PATH variable has the right contents, use the command below in the second SSH connection:

```echo $PATH```

Output:

![update_path.png](https://cdn.qwiklabs.com/PTjyGi%2B1%2FhWT7Hk3URoj9oOnshRwLF5lLXtZ3QjnOb0%3D)

You've successfully fixed the misbehaving `$PATH` variable.

Click _Check my progress_ to verify the objective. Fix issue in init.pp

## Congratulations!

Woohoo! You have used Puppet to automate the configurations on the machines and fixed the broken `PATH` variable. A great first step towards getting comfortable using Puppet.

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