## Introduction

Imagine one of your colleagues has written a Python script that's failing to run correctly. They're asking for your help to debug it. In this lab, you'll look into why the script is crashing and apply the problem-solving steps that we've already learned to get information, find the root cause, and remediate the problem.

You'll have 90 minutes to complete this lab.


## Reproduce the error

The script sent by your colleague is in the **scripts** directory. Let's navigate to **scripts** directory using the following command:

```cd ~/scripts```

Now, use the following command to list all the files in this directory:

```ls```

You should now be able to see the file named **greetings.py** which was sent by your colleague.

To view the contents of the file, use the following command:

```cat greetings.py```

Let's update the file's permissions.

```sudo chmod 777 greetings.py```

Now let's reproduce the error by running the file using the following command:

```./greetings.py```

Enter your name at the prompt.

The output should throw an error as shown below:

![6e7aa4c6873e5b88.png](https://cdn.qwiklabs.com/Oyv%2FifLM44eFaWmxI6QaVjmO%2BHHFLnSQyPLkeV9ZxB4%3D)

Great job! You have successfully reproduced the error.

## Find the root cause of the issue

Now that we have successfully reproduced the error, let's find its root cause.

The error message indicates that something in the code is trying to concatenate a string and an integer.

![bd9b0c59ed88baca.png](https://cdn.qwiklabs.com/65BI%2F349hD%2Bkh%2Bcy0vd4Thy1kVATBLD0ygxJQPbLJxU%3D)

When we look at the code, we can see that there are two different data types used, string and int. The variable **name** takes string values and the variable **number** stores integer (int) values.

So, the print statement within the script concatenates both string and integer values, which is causing the error.

`print("hello " + name + ", your random number is " + number)`

So, we can conclude that the root cause of the issue is within the print statement, which is trying to concatenate two different data types (i.e., string and int).

## Debug the issue

In the previous section, we found the root cause of the issue, now let's debug the issue.

The print statement within the script is trying to concatenate two different data types. In Python, you can't add two different data types directly. So in this case, we can't add a string data type with an int data type. To add them, we have to turn the number into a string using _str()_ function.

Once the integer value is converted to a string data type using _str()_ function, the concatenate operation will work because the data types will be similar.

_str()_ function takes in an integer as a parameter and converts it into string data type. So in our case, we will pass the variable **number** to the str() function i.e., **str(number)**.

Open the greetings.py file using nano editor.

```nano greetings.py```

Replace the print statement within the script with the following statement:

```print("hello " + name + ", your random number is " + str(number))```

Save the file by pressing Ctrl-o, followed by the Enter key and Ctrl-x.

Now run the file again.

```./greetings.py```

Enter your name for the prompt. You should now see the correct output.

![86543864f819281e.png](https://cdn.qwiklabs.com/C0TnHguUi4xUwzToNSIwOKJ%2FV6kuCNKaoXIZY%2F%2FwFMw%3D)

Click _Check my progress_ to verify the objective. Debug the issue

## Congratulations!

You successfully debugged your colleague's python script. You reproduced the error, found its root cause, and applied the remediation to the issue. You can now close the RDP/SSH window. The lab will automatically end when the time runs out, or you can end it manually.

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