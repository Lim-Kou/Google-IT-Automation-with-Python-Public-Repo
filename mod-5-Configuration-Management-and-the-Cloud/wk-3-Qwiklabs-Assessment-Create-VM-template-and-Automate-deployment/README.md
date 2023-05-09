## Introduction

You're an IT Administrator for your company and you're assigned to work on a project that requires you to deploy eight virtual machines (VMs) as web servers. Each of them should have the same configuration. You'll create a VM, set up an auto-enabled service, and make it a template. Then you'll use the template to create seven more VMs.

### What you'll do

-   Create a VM using GCP web UI and make a template out of it
    
-   Use a command-line interface to interact with VMs
    
-   Learn how to configure an auto-enabled service
    
-   Learn to use `gcloud` to deploy VMs with a template
    

## Setup

### What you need

To complete this lab, you need:

-   Access to a standard internet browser (the Chrome browser is recommended)
-   Time to complete the lab

**Note:** If you already have your own personal GCP account or project, please don't use it for this lab.

In this lab, you will be using **gcloud command-line interface**, which is a tool that provides the primary CLI to Google Cloud Platform, to interact with VMs. To use this, you should install the Google Cloud SDK, initialize it, and run core gcloud commands from the command line on your local computer.

To install Google Cloud SDK follow the instructions given below based on your device's operating system:

-   [Windows](https://cloud.google.com/sdk/docs/install-sdk#windows)
-   [Linux](https://cloud.google.com/sdk/docs/install-sdk#linux)
-   [Debian and Ubuntu](https://cloud.google.com/sdk/docs/install-sdk#deb)
-   [Red Hat and Cento](https://cloud.google.com/sdk/docs/install-sdk#rpm)
-   [macOS](https://cloud.google.com/sdk/docs/install-sdk#mac)

You'll have 90 minutes to complete this lab.

### Start your lab by signing in to the Console

**Before you click the Start Lab button** read these instructions. Labs are timed and you cannot pause them. The timer, which starts when you click **Start Lab** , shows how long Google Cloud resources will be made available to you.

This Qwiklab hands-on lab lets you do the lab activities yourself in a real cloud environment, not in a simulation or demo environment. It does so by giving you new, temporary credentials that you use to sign in and access Google Cloud for the duration of the lab.

1.  Click the **Start Lab** button.

![Start Lab](https://cdn.qwiklabs.com/m8bGh8IYyYTzRYAJCj2t0DqCOLRDVcr%2BFy5bwhKxwvU%3D)

On the left is a panel populated with the temporary credentials that you'll need to use for this lab.

![4880287cd5d22ca4.png](https://cdn.qwiklabs.com/TpKeJce4iGJZA%2BF7GH6FA2py1qIEE6I0Dc%2BJP5J0j1Y%3D)

2.  Copy the username, then click **Open Google Console**. The lab spins up resources, and then opens another tab that shows the **Choose an account** page.

**_Tip:_** Open the tabs in separate windows, side by side.

**Note:** Using a new Incognito window (Chrome) or another browser for the Qwiklabs session is recommended. Alternatively, you can log out of all other Google / Gmail accounts before beginning the labs.

3.  On the **Choose an account** page, click **Use another account**. ![8fed3c9c506e07fd.png](https://cdn.qwiklabs.com/%2Be70H%2FyM0AB5gBe4t7m6%2BwFtugOjh4nT7e98Aj3TioA%3D)
4.  The **Sign in** page opens. Paste the username that you copied from the **Connection Details** panel. Then copy and paste the password.

**_Important:_** You must use the credentials from the **Connection Details** panel. Please do **not** use your Qwiklabs credentials. If you have your own GCP account, do **not** use it for this lab in order to avoid incurring charges.

5.  Click through the subsequent pages:
    
6.  Accept the terms and conditions.
    
7.  Do **not** add recovery options or two-factor authentication, since this is a temporary account.
    
8.  Do **not** sign up for free trials.
    

After a few moments, the GCP console opens in this tab.

### What you need

To complete this lab, you need:

-   Access to a standard internet browser (Chrome browser recommended).
-   Time to complete the lab.

**Note:** If you already have your own personal Google Cloud account or project, do not use it for this lab.

## Create a VM instance from the Cloud Console

In this section, you'll learn how to create new, predefined machine types with Google Compute Engine from the Cloud Console.

In the GCP Console, on the top left of the screen, select **Navigation menu** > **Compute Engine** > **VM instances**:

![cc9e3026f41f7b50.png](https://cdn.qwiklabs.com/9Wp4iBZ8Pv4iE0Tdi2fs5zKYfuPOcq%2FrN0CtPBg2E20%3D)

This may take a moment to initialize for the first time.

To create a new instance, click **Create instance**.

![eee8fc21631bacd3.png](https://cdn.qwiklabs.com/AtN%2FzJWJMEUM8m2y5Qc66zSHeix4oRK1Do9Q2kiKx9Y%3D)

There are lots of parameters you can configure when creating a new instance. Use the following for this lab:

<table><tbody><tr><td colspan="1" rowspan="1"><p><strong>Field</strong></p></td><td colspan="1" rowspan="1"><p><strong>Value</strong></p></td><td colspan="1" rowspan="1"><p><strong>Additional Information</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p>Name</p></td><td colspan="1" rowspan="1"><p>vm1</p></td><td colspan="1" rowspan="1"><p>Name for the VM instance</p></td></tr><tr><td colspan="1" rowspan="1"><p>Region</p></td><td colspan="1" rowspan="1"><p>us-east1</p></td><td colspan="1" rowspan="1"><p>Learn more about regions in <a href="https://cloud.google.com/compute/docs/zones" target="blank">Regions &amp; Zones documentation</a>.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Zone</p></td><td colspan="1" rowspan="1"><p>us-east1-b</p></td><td colspan="1" rowspan="1"><p>Learn more about regions in <a href="https://cloud.google.com/compute/docs/zones" target="blank">Regions &amp; Zones documentation</a>.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Series</p></td><td colspan="1" rowspan="1"><p>N1</p></td><td colspan="1" rowspan="1"><p>The N1 machine series is Compute Engine's first generation general-purpose machine series.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Machine Type</p></td><td colspan="1" rowspan="1"><p>n1-standard-1</p></td><td colspan="1" rowspan="1"><p><strong>Note</strong>: A new project has a default <a href="https://cloud.google.com/compute/docs/resource-quotas" target="blank">resource quota</a>, which may limit the number of CPU cores. You can request more when you work on projects outside of this lab.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Boot Disk</p></td><td colspan="1" rowspan="1"><p>Ubuntu 18.04 LTS</p></td><td colspan="1" rowspan="1"><p>Click on the <strong>change</strong> button, click on the <strong>Operating system</strong> and select Ubuntu then for version, select Ubuntu 18.04 LTS. Learn more about boot disk check out this <a href="https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes" target="blank">link</a>.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Boot disk type</p></td><td colspan="1" rowspan="1"><p>standard persistent disk</p></td><td colspan="1" rowspan="1"><p>Learn more about standard persistent disk check out this <a href="https://cloud.google.com/compute/docs/disks/" target="blank">link.</a></p></td></tr><tr><td colspan="1" rowspan="1"><p>Firewall</p></td><td colspan="1" rowspan="1"><p>allow HTTP and HTTPS traffic</p></td><td colspan="1" rowspan="1"><p>Learn more about firewall check out this <a href="https://cloud.google.com/vpc/docs/firewalls" target="blank">link.</a></p></td></tr></tbody></table>

Leave all the other configurations set to their defaults.

After entering the above parameters, click on the **Create** button to create your VM.

![d341df6a049c430.png](https://cdn.qwiklabs.com/%2Bl9gU0E1%2BJNZanJ2bP7kwxYGbLSLo5mG4rno3G5FE4Q%3D)

SSH into `vm1` by clicking on the `SSH` button, as shown in the image above.

### Git clone

Use Git to clone the repository by using the following command:

git clone https://www.github.com/google/it-cert-automation-practice.git

Output:

![output_clonw.png](https://cdn.qwiklabs.com/0CfdnUbvYuOqBLhJeL9avkYvN3gB889m2jo10YrerOE%3D)

### File operation

Once you have the repository successfully cloned, navigate to the `Lab3/`directory.

```cd ~/it-cert-automation-practice/Course5/Lab3```

To list the files in the working directory `Lab3/` use the **list** command.

```ls```

Output:

![4550b17ad349eb37.png](https://cdn.qwiklabs.com/oBLVxxbHoRqi2hyZuaE8vljaw%2B3AmPS8eY9AfXVsYVU%3D)

In order to enable `hello_cloud.py` to run on boot, copy the file `hello_cloud.py` to the `/usr/local/bin/` location.

```sudo cp hello_cloud.py /usr/local/bin/```

Also copy `hello_cloud.service` to the `/etc/systemd/system/` location.

```sudo cp hello_cloud.service /etc/systemd/system```

Now, use the systemctl command to enable the service **hello_cloud**.

```sudo systemctl enable hello_cloud.service```

### Restart the VM

After enabling the **hello_cloud** service, reboot the VM to ensure that the service is up. To reboot the VM instance **vm1** go to the **Compute Engine** > **VM instance** and stop the VM instance `vm1` by selecting the VM instance vm1 and clicking on the **Stop** button at the top. Again, click on the **Stop** button in the popup.

![c2f90138ce8d0502.png](https://cdn.qwiklabs.com/PCCUpVIIIdjnpwSfYtX2bS%2BG6b52vsmKGWX5%2BBAI%2B6A%3D)

The start method restarts an instance in a TERMINATED state. To start the VM instance **vm1**, select it first by tick marking it, then click on the **Start/Resume** button at the top. Again, click on the **Start** button in the popup. You can this in the image below.

![a113d8c1e6f8c57.png](https://cdn.qwiklabs.com/%2ByZt%2B9zkTmOsxUlZQvIrLrNuB72UY9ACY78ZRnVSZBA%3D)

After restarting the VM instance **vm1,** visit the External IP link of the vm1 that's shown in the image below:

![b8b253f28bec3850.png](https://cdn.qwiklabs.com/sdplGyHz8kK3EEfIzs8yBaAmOiIfDPa6xSDpLn%2B8kQg%3D)

**Note:** If you are getting any error then click on the url and use http://EXTERNAL-IP.

Output:

![f91ec09cf705d62f.png](https://cdn.qwiklabs.com/rTKvL5emvdix8R1IgEh9qdDCQP6e4es8SXvHovJJdxQ%3D)

## Create VMs using a template

You'll now create a template for `vm1`.

First, **shut down** the VM instance **vm1** by going to the **Compute Engine** > **VM instance**, selecting the VM instance `vm1`, and clicking on the **stop** button at the top.

Now, create an image named `vm-image` based on the **vm1** disk by following the steps below:

In the GCP Console, on the top left of the screen, select **Navigation menu > Compute Engine > Images:**

![9b40fe5b82e5eab0.png](https://cdn.qwiklabs.com/q9KPJOskS8wNZ3SjeDNSBB1wxDPUdzy5BpcrbfkK1vc%3D)

Click on the **CREATE IMAGE** button below.

![20786877379305cb.png](https://cdn.qwiklabs.com/lmkc1fSxA4ka3anW5fmZOJUiXorYB3vQSeI%2FvK1tva0%3D)

Then, create an image based on the **vm1's** disk, using the following parameters:

<table><tbody><tr><td colspan="1" rowspan="1"><p><strong>Field</strong></p></td><td colspan="1" rowspan="1"><p><strong>Value</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p>Name</p></td><td colspan="1" rowspan="1"><p>vm-image</p></td></tr><tr><td colspan="1" rowspan="1"><p>Source</p></td><td colspan="1" rowspan="1"><p>Disk</p></td></tr><tr><td colspan="1" rowspan="1"><p>Source Disk</p></td><td colspan="1" rowspan="1"><p>vm1</p></td></tr></tbody></table>

Leave all of the other values set to their default settings. Click on the **create** button to create your image.

![ec769bfa09b20b09.png](https://cdn.qwiklabs.com/%2F8GuCXRNxP5rRcWqUxOup13YokAel0eNmzAjh%2FkAk1o%3D)

Now, create an instance template using `vm-image` for the boot disk you just created.

To create a instance template, follow the instructions below:

In the GCP Console, on the top left of the screen, select **Navigation menu > Compute Engine > Instance templates:**

![92dd009e4768ccd0.png](https://cdn.qwiklabs.com/Nfmpa5%2BiCnX6HLrxBo0A5btekgl7RVGkTfXMVbqoY3o%3D)

Now, click on **Create instance template** to create a new template.

There are lots of parameters that you can configure when creating a new instance. Use the following for this lab:

<table><tbody><tr><td colspan="1" rowspan="1"><p><strong>Field</strong></p></td><td colspan="1" rowspan="1"><p><strong>Value</strong></p></td><td colspan="1" rowspan="1"><p><strong>Additional information</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p>Name</p></td><td colspan="1" rowspan="1"><p>vm1-template</p></td><td colspan="1" rowspan="1"><p>Name for the VM instance template</p></td></tr><tr><td colspan="1" rowspan="1"><p>Series</p></td><td colspan="1" rowspan="1"><p>N1</p></td><td colspan="1" rowspan="1"><p>The N1 machine series is Compute Engine's first generation general-purpose machine series.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Machine Type</p></td><td colspan="1" rowspan="1"><p>n1-standard-1</p></td><td colspan="1" rowspan="1"><p><strong>Note</strong>: A new project has a default <a href="https://cloud.google.com/compute/docs/resource-quotas" target="blank">resource quota</a>, which may limit the number of CPU cores. You can request more when you work on projects outside of this lab.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Boot Disk</p></td><td colspan="1" rowspan="1"><p>vm-image</p></td><td colspan="1" rowspan="1"><p>Click on the <strong>change</strong> button, click on the <strong>custom images</strong> section. Now, select <strong>vm-image</strong> by selecting the project you are working on.</p></td></tr><tr><td colspan="1" rowspan="1"><p>Boot disk type</p></td><td colspan="1" rowspan="1"><p>standard persistent disk</p></td><td colspan="1" rowspan="1"><p>Learn more about standard persistent disk check out this <a href="https://cloud.google.com/compute/docs/disks/" target="blank">link.</a></p></td></tr><tr><td colspan="1" rowspan="1"><p>Firewall</p></td><td colspan="1" rowspan="1"><p>allow HTTP and HTTPS traffic</p></td><td colspan="1" rowspan="1"><p>Learn more about firewall check out this <a href="https://cloud.google.com/vpc/docs/firewalls" target="blank">link.</a></p></td></tr></tbody></table>

Leave the rest of the values set to their default settings. Click on the **create** button to create the instance template `vm1-template.`

![b8c93fa07d239079.png](https://cdn.qwiklabs.com/iBLO5B4xoR9vClQwBFreiDTQPAPbzQu6BPatq0Eib7I%3D)

Click _Check my progress_ to verify the objective. Create an instance template

Now, you'll create new VM instances with the template named `vm1-template` from your local computer using **gcloud command-line interface**. To do this, return back to the command line interface on your local computer, and enter the following command:

```gcloud compute instances create --zone us-west1-b --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8```

Wait for the command to finish. Once it's done, you can view the instances through the Console or by using the following `gcloud` command on your local terminal:

```gcloud compute instances list```

Now, open the external links for `vm2` and `vm8` to check if all the configuration set up properly as vm1.

Output:

![ec54802a55124f88.png](https://cdn.qwiklabs.com/K6u0IGP8f%2Fhdggn7XU4UPTFE2U7emYi02uJ00YvpOUw%3D)

![e9aaa2636fed19aa.png](https://cdn.qwiklabs.com/w4xhJ6aBLSx3K%2BT9H4PopZ7Y7Cytdqaadr6I3pHDV%2Bw%3D)

Click _Check my progress_ to verify the objective. Create instances using the template

## Congratulations!

Nice work! You've successfully deployed eight VMs as web servers, each with the same configuration.

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