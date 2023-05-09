## Introduction

You're an IT professional who's in charge of the deployment and maintenance of software in your company's fleet. A piece of software that's deployed on all machines in your fleet is throwing an error on a number of these machines. You haven't written the software and don't have access to the source code. You'll need to examine the environment where the software is running in and try to work out what's going on.

#### **What you'll do**

-   Understand the error messages
-   Track down the root cause and work to fix it
-   Understand what to do when you can't modify the program that's throwing errors

You'll have 90 minutes to complete this lab.

## ImportError

Since you haven't written the software and don't have access to the source code, you'll need to examine the environment where the software is running and try to work out what's going on. There's a python script named `infrastructure` in `/usr/bin` directory that reads data from a CSV file and prints them to the terminal in a nicely formatted manner. Let's run this script and see whether it generates any errors.

Now change the directory to `root`, and run the script.

```cd / python3 /usr/bin/infrastructure```

Output:

![866e4319baa2aa62.png](https://cdn.qwiklabs.com/fkKbHgAkD8hUPXbA0%2Fvd5Ljq%2Fq3urL6y20eLT7isKEc%3D)

The script crashed, displaying an `ImportError`. This error is raised when an `import` statement has trouble importing a specific module. You could also see the module that the `import` statement hasn't found (i.e. matplotlib). We'll need to import this module before we continue to run the script again.

### Fix:

In order to fix this error, you first need to install **pip3** which is a Python package installer. This downloads and configures new python modules with single-line commands.

```sudo apt install python3-pip -y```

Now, install the `matplotlib` python library using pip3:

```pip3 install matplotlib```

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension **NumPy**(installed upon installing matplotlib). It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits. Even simpler, it's a visualization library in Python for 2D plots of arrays.

Click _Check my progress_ to verify the objective. Download 'matplotlib' module

## NoFileError

After installing the necessary modules, run the script again.

```python3 /usr/bin/infrastructure```

Output:

![ea48b3bd670e6b2e.png](https://cdn.qwiklabs.com/RO%2F8zDIMpD4RcSD1wlaYzKO%2BvfO6l3jT40vZDajX5xI%3D)

This time it returns a `NoFileError` with a message that it could not find data.csv file in the working directory. Try debugging this issue.

### Fix:

Let's navigate to the working directory and see if the `data.csv` file exists.

```cd ~ ls```

Output:

![bc97581598ff3eba.png](https://cdn.qwiklabs.com/vXrPqsIwMlC9lqIWF0VqVzCAairVdN8zDUf7QF5vES8%3D)

As you can see, the file `data` has the extension .bak. As we mentioned earlier, the script `infrastructure` works on CSV files. Interpret the error message, which also says that it didn't find a `data.csv` file. We've now found the root cause of the issue. Let's move forward by renaming the file `data.bak` to `data.csv`.

```mv data.bak data.csv```

Click _Check my progress_ to verify the objective. Rename data.csv file

Now, navigate back to the root directory and run the script again.

```cd / python3 /usr/bin/infrastructure```

Output:

![6d740adde208379.png](https://cdn.qwiklabs.com/pb4muJRIokukTvMeSpLFmE8UJalXnOAEoC7NAMal%2Bf8%3D)

This now gives a `MissingColumnError`. It says that it couldn't find a column named "company" within the `data.csv` file.

## MissingColumnError

Let's check the `data.csv` file for the missing column name.

```cat ~/data.csv```

Output:

![9fa1e5fc77239a6f.png](https://cdn.qwiklabs.com/iXhTahSAgfQwzpBOMuc0DCBjbttqdNhMszQNHq5dg7w%3D)

So, the column name is actually missing. Let's add the column name and run the script again.

Grant the permissions to the data.csv file.

```sudo chmod 777 ~/data.csv```

Open `data.csv` file using nano editor.

```nano ~/data.csv```

Add the missing column name and save the file by clicking Ctrl-o, followed by Enter key and Ctrl-x.

Now, run the script again:

```python3 /usr/bin/infrastructure```

Output:

![24cebe5b9a3ebd40.png](https://cdn.qwiklabs.com/xyyGDtMxCJEBcuWoKxsLxJHejVQ6TBbK06S1Yqw27MA%3D)

This time you fixed all the errors!

Click _Check my progress_ to verify the objective. Add column in data.csv

## Congratulations!

Congrats! You've correctly understood the error messages and fixed them by tracking down the root cause. This will help you as an IT professional who's in charge of the deployment and maintenance of software in your company's fleet.

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