==============
 Introduction
==============

A Brief Introduction to Azure
=============================

A couple of links to get an overview.

* https://www.youtube.com/watch?v=2zscgz-Pj_A <-- video!
* https://docs.microsoft.com/en-us/learn/paths/azure-fundamentals/
* https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/

Beginner's Command Line
=======================

Throughout this course we will be using the command line as much as possible.
This is because submersing oneself in a new topic is often the most effective way of learning :wink:

Open the Azure Cloud Shell (follow along with instructor for how to do this!) and we'll get started with some basic bash commands.

+---------------------------------------------------------------------------------------------------------------------------------------+
+ **Info:**                                                                                                                             +
+                                                                                                                                       +
+ The first time you open the Cloud Shell, you'll be asked to create a storage account.                                                 +
+ You set the subscription your storage will be associated with and, by using the advanced settings, you can also set a resource group. +
+---------------------------------------------------------------------------------------------------------------------------------------+

1. ``pwd`` - This command tells you which directory you're in.
2. ``ls`` - This command shows you what files are in the directory you're in. Use ``ls -a`` to see hidden files as well.
3. ``cd`` - This command will take you to a different directory. It is case sensitive so type the directory name exactly as it is! It is also sensitive to white space, so we need to "escape" these with a backslash (``\``), e.g. ``cd My\ Folder``. To go "back" (or "up") one folder, use ``cd ..``.
4. ``mkdir`` - This command will make a new directory.
5. ``rmdir`` - This command will delete a directory *only if it is empty*.
6. ``rm`` - This command will delete files. ``rm -r`` will also delete a directory *that is not empty*.
7. ``cp`` - This command copies files. It takes two arguments: the first is the file to be copied, the second is where it should be copied to.
8. ``mv`` - This command moves files to new locations and works similarly to ``cp``.

This should be enough to get us started.
See the `Intro to Command Line Bash Wiki page <https://github.com/alan-turing-institute/learn-azure/wiki/Intro-to-Command-Line-Bash>`_ for a more in-depth overview of commands and links to other tutorials.

Azure Portal vs Azure Cloud Shell vs Azure CLI
==============================================

* CLI = Command Line Interface. *A tool used in the terminal to connect to/interact with some service.*

+-------------+----------------------------------------------------------------------------------+-----------------------------------------------+
|             | **Pros**                                                                         | **Cons**                                      |
+=============+==================================================================================+===============================================+
| Portal      | * Works in any web browser                                                       | * Changes regularly as new features are added |
|             | * Does not require any installation                                              | * Not reproducible                            |
|             | * Provides a visual representation of everything                                 |                                               |
+-------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| Cloud Shell | * Provides preinstalled software (e.g. git)                                      | * No access to local files or tools           |
|             | * Compatible with VSCode and a mobile app                                        |                                               |
|             | * Latest version is always available                                             |                                               |
|             | * Persistent storage is attached so you can create/save scripts, templates, etc. |                                               |
|             | * Commands can be collated into a script, making the process reproducible.       |                                               |
+-------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| CLI         | * Access to local files, tools and environments                                  | * Need to keep it updated                     |
|             | * OS agnostic                                                                    |                                               |
|             | * Commands can be collated into a script, making the process reproducible.       |                                               |
+-------------+----------------------------------------------------------------------------------+-----------------------------------------------+

Creating a Virtual Machine
==========================

In the Portal
-------------

1. Login to the Azure Portal at https://portal.azure.com.
   Once logged in, select "Create a Resource" in the upper-left corner of the dashboard.
   Choose "Compute" from the list of resources and then select "See all" next to the "Featured" column.

.. image:: ../figures/01_Intro/portal_vm_step1.png

2. Select "Ubuntu 18.04 LTS" from the list (you may need to search for it).
   This is the most recent version of Ubuntu.
   LTS stands for Long Term Support.
   If there's a newer version of Unbuntu LTS at time of reading, you should select that.
   In the new window, click "Create".

.. image:: ../figures/01_Intro/portal_vm_step2.png

.. image:: ../figures/01_Intro/portal_vm_step3.png

3. We begin by completing the information on the "Basics" panel.
   We select the subscription from the drop-down menu and create a new Resource Group we want to deploy the VM into by clicking "Create new" underneath the Resource Group box - the example will create a new group called ``learn-azure-01``.
   (You could also deploy this into an existing Resource Group by selecting from the drop-down menu.)
   Give your VM a name - the example uses ``webvm``, you can use this or choose your own.
   Assign your VM a Region - the example uses "West Europe".
   This refers to where your VM will physically run.
   You can also choose a different sized VM if you find you need more CPUs or memory, etc.
   This example will deploy a DS2 v3 machine, which is classified as "General Purpose".

+--------------------------------------------------------------------------------------------------------------+
| **Info:** Azure Resource Groups                                                                              |
|                                                                                                              |
| A Resource Group in Azure is nothing more than a labelling system.                                           |
| By selecting a Resource Group, you can easily list all the resources that have been allocated to that group. |
| In general, it's good practice to gather related resources into the same Resource Group.                     |
+--------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Info:** Azure Regions and Locations                                                                                                                                 |
|                                                                                                                                                                       |
| When creating resources in Azure, we often have to specify a Region or Location.                                                                                      |
| This refers to the Data Centres where the physical infrastructure are situated.                                                                                       |
|                                                                                                                                                                       |
| A Location, for example "London", usually refers to a specific Data Centre whereas a Region, for example "UK South", may encompass multiple Data Centres.             |
| Generally, it is best practice to define a Region and allow Azure to automatically place your resources based on availability, capacity and performance requirements. |
| See the `Microsoft Docs <https://azure.microsoft.com/en-gb/global-infrastructure/locations/>`_ for more information.                                                  |
|                                                                                                                                                                       |
| There are no specific rules to consider when choosing a Region/Location to host your resources.                                                                       |
| It is good practice to co-locate resources that interact with each other in order to reduce connection times.                                                         |
| Sometimes a specific project may require resources be located in a certain region because of legal jurisdiction, local intellectual property laws, costs, etc.        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------+
| **Info:** Azure VM sizes                                                                                                          |
|                                                                                                                                   |
| There are *a lot* of different VM types and sizes available within Azure and it can seem overwhelming when trying to pick one.    |
| However, they have been categorised into *families* that contain similar virtual hardware and are targeted for certain workloads. |
|                                                                                                                                   |
| * *General Purpose* - Great for developing, testing or low-use production.                                                        |
| * *Compute optimised* - High performance CPUs for production servers.                                                             |
| * *Memory optimised* - Larger memory options for big databases or in-memory intensive data processing.                            |
| * *Storage optimised* - Low-latency, high-disk performance for disk-intensive applications.                                       |
| * *GPU* - Graphics- specialised VMs for rendering images or video processing.                                                     |
| * *High-performance computing (HPC)* - A bit of everything! Plenty of CPU, memory, etc. for the most demanding workloads.         |
+-----------------------------------------------------------------------------------------------------------------------------------+

.. image:: ../figures/01_Intro/portal_vm_step4.png

4. Next, create a user account on the VM.
   This will be the account you login to when accessing the VM.
   Choose a username and we will create SSH keys for the authentication protocol in the following steps.

+------------------------------------------------------------------------------------------------------------------------------------+
| **Info:** Secure shell (SSH) key pairs                                                                                             |
|                                                                                                                                    |
| Secure shell is a protocol used to communicate securely with remote computers and it's the most common way to login to a Linux VM. |
| With public-key cryptography, a digital key pair can be used to authenticate you with a remote Linux VM.                           |
|                                                                                                                                    |
| An SSH key pair has two parts: a public key and a private key.                                                                     |
| The public key is stored on the VM in Azure and you keep a copy of the private key.                                                |
| When a login request is made to the VM, the public key on the VM is matched with the private key on the computer trying to login.  |
| If the key pairs match, the requesting computer is authenticated to login to the VM.                                               |
| Public-key cryptography is a great way to verify identity.                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------+

Open the Cloud Shell by selecting the icon in the top bar of the dashboard.
(**N.B.:** The following commands could be executed in your own terminal as well, but we'll stick to one open window for now.)
The first time you launch the Cloud Shell, it will create some persistent storage that's always connected to your sessions.
This will allow you to save and retrieve scripts, configuration files and SSH keys.
Accept any prompts to create the storage account.
Make sure the "Bash" is selected from the drop-down menu in the upper-left corner of the Cloud Shell.

.. image:: ../figures/01_Intro/portal_vm_step6.png

5. To create an SSH key pair, run the command: ``ssh-keygen``.
   Accept the default prompts by pressing the "Enter" key (we won't use a pass phrase).
   This command defaults to a `2,048-bit length <https://en.wikipedia.org/wiki/Password_strength#Required_bits_of_entropy>`_ key using the `RSA version 2 <https://en.wikipedia.org/wiki/RSA_(cryptosystem)>`_ protocol, which is a good balance of security.

.. image:: ../figures/01_Intro/portal_vm_step7.png

6. We now give the public SSH key to the VM.
   To view the key, run the command: ``cat .ssh/id_rsa.pub``.
   Copy the output, and paste it into the "SSH public key" field.

.. image:: ../figures/01_Intro/portal_vm_step8.png

7. By default, Azure locks down access to the VM so we have to define how we want to receive login requests.
   Select the "Allow selected ports" option and then select SSH from the drop-down menu.
   Without this step, our login request would be denied even if the SSH keys pass the authentication step.

.. image:: ../figures/01_Intro/portal_vm_step9.png

8. On the "Disks" tab at the top of the pane, we can define the type of storage to attach to the VM.
   We are going to use "Standard HDD" from the drop-down menu.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Info:** Azure storage                                                                                                                                                                         |
|                                                                                                                                                                                                 |
| This is a brief introduction to basic disk storage.                                                                                                                                             |
| Other types of storage with different levels of structure are available and will be discussed in another session.                                                                               |
|                                                                                                                                                                                                 |
| * *Standard Hard Disk Drives* - This is a regular spinning disk. Ideal for infrequent data access.                                                                                              |
| * *Standard Solid State Drives* - These lack the spinning disks and the movable read/write heads of HDDs. They have low-latency, quicker access times and are more resistent to physical shock. |
| * *Premium SSDs* - High-performance SSDs for production workloads.                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. image:: ../figures/01_Intro/portal_vm_step5.png

9. We're just about finished now!
   From the top of the pane, select "Review + create".
   When the green "Validation passed" banner appears, click "Create" at the bottom of the page.
   Your VM is now being deployed!

.. image:: ../figures/01_Intro/portal_vm_step10.png

Using the Cloud Shell or CLI
----------------------------

These commands will be identical in either the Cloud Shell or CLI.

1. Login to Azure.
   (This step is only necessary for the CLI. The Cloud Shell is linked to your Portal login.)

.. code-block::

    az login

2. Set your subscription.

.. code-block::

    az account set --subscription SUBSCRIPTION_NAME

If your subscription name has spaces in it, you will need to surround it with quote marks.
For example::

    az account set --subscription "Living with Machines"

3. Create a Resource Group.

.. code-block::

    az group create --name learn-azure-01 --location westeurope --output table

4. Create a VM.

.. code-block::

    az vm create \
        --name webvm \
        --resource-group learn-azure-01 \
        --admin-username YOUR_USERNAME \
        --authentication-type ssh \
        --generate-ssh-keys \
        --image UbuntuLTS \
        --size Standard_D2S_v3 \
        --storage-sku Standard_LRS \
        --output table

**Or** if you want to create an SSH key pair yourself like in the Portal example (perhaps pass a different filename when prompted), then::

        az vm create \
            --name webvm \
            --resource-group learn-azure-01 \
            --admin-username YOUR_USERNAME \
            --authentication-type ssh \
            --ssh-key-value .ssh/new_rsa.pub \
            --image UbuntuLTS \
            --size Standard_D2S_v3 \
            --storage-sku Standard_LRS \
            --output table

This approach in much less involved than through the Portal.
These commands can also be collated into a script so that they can be executed automatically.

Introduction to the Azure CLI
=============================

Now you've played with the CLI a little bit, let's delve deeper into its structure.

The CLI is broken down and organised into *commands* of *groups*.
Each group represents a service, for example ``vm`` is "Virtual Machines", and commands operate on that service.
There may also be sub-groups or sub-commands available, depending on the service you're working with.

We usually need to parse arguments to the command and we do this using "flags".
Flags are denoted by the double dash ``--`` (for example, ``--name``), or may be shortened to a single dash and single character combination (for example, ``--name`` becomes ``-n``).
Some of these flags are *global*, that is to say they are available for every command.

Let's break down the command we used to create a VM.

.. code-block::

    az vm create \
        --name webvm \
        --resource-group learn-azure-01 \
        --admin-username YOUR_USERNAME \
        --authentication-type ssh \
        --generate-ssh-keys \
        --image UbuntuLTS \
        --size Standard_D2S_v3 \
        --storage-sku Standard_LRS \
        --output table

* All commands must start with ``az``. This tells your shell to use the Azure CLI software to interpret the following commands.
* Since we're working with VMs, we use the *group* ``vm``.
* We want to create a VM so we parse the ``create`` command.
* We then parse a selection of arguments to define the properties of the VM we would like. In this case, only ``--name`` and ``--resource-group`` are required arguments.
* The `--storge-sku Standard_LRS` flag is deploying a Standard HDD disk like we did in the Portal.

The `Azure CLI Reference <https://docs.microsoft.com/en-gb/cli/azure/reference-index?view=azure-cli-latest>`_ is an excellent source of information on CLI groups and commands.

Global Arguments
----------------

There are five global arguments available to all Azure CLI commands:

* ``--help [-h]``: Prints the CLI reference information about commands and their arguments and also lists available sub-groups and commands.
* ``--output [-o]``: Changes the output format. The available formats are ``json``, ``jsonc`` (colorised JSON), ``tsv`` (Tab-Separated Values), ``table`` (human-readable ASCII tables), and ``yaml``. By default, the CLI outputs JSON.
* ``--query``: Uses the `JMESPath query language <http://jmespath.org/>`_ to filter the output returned from Azure services. To learn more about queries, see `Query command results with Azure CLI <https://docs.microsoft.com/en-us/cli/azure/query-azure-cli?view=azure-cli-latest>`_ and the `JMESPath tutorial <http://jmespath.org/tutorial.html>`_.
* ``--verbose``: Prints useful information about resources created in Azure during an operation.
* ``--debug``: Prints even more information about CLI operations for debugging purposes.

Connecting to the VM
====================

+--------------------------------------------------------------------------------------------------------------+
+ **Info:**                                                                                                    +
+                                                                                                              +
+ If you created your SSH key in the Cloud shell, you will **have** to connect to the VM from the Cloud shell. +
+ This is because your SSH key is stored in the Cloud Shell storage, **not** on your local machine.            +
+--------------------------------------------------------------------------------------------------------------+

In the Portal
-------------

Now we have created a VM, how do we connect to it?

1. When the VM has deployed, go to the resource page.
   Then find the SSH command to login to the machine.
   Click on "Connect" and this will open a panel on the right hand side.
   The third box in the panel will be the SSH command to connect to the VM.
   Copy this using the blue button.

.. image:: ../figures/01_Intro/portal_vm_ssh1.png

2. Open the Cloud Shell, paste the command into it and run it.
   You will be asked to verify the host's authenticity - type "yes".

.. image:: ../figures/01_Intro/portal_vm_ssh2.png

You have now logged in to the VM!
The VM used your SSH key to authenticate your login request.
Since we have requested a Ubuntu server, all of the bash commands we learned will still work on this new machine.

To exit the VM, type ``exit``.

Using the Cloud Shell or CLI
----------------------------

We can achieve this more programatically using the CLI and bash variables.
We are going to use the Azure CLI (in either a local terminal or the Cloud Shell) to return the username and IP address to access our VM and save them to bash variables.

1. First we call return the username and save it to the variable ``USERNAME``.

.. code-block::

    USERNAME=$(az vm show \
        --name webvm \
        --resource-group learn-azure-01 \
        --show-details \
        --query "osProfile.adminUsername" \
        --output tsv)

2. Now we will do the same for the IP address of the VM.

.. code-block::

    IP_ADDRESS=$(az vm show \
        --name webvm \
        --resource-group learn-azure-01 \
        --show-details \
        --query "publicIps" \
        --output tsv)

+--------------------------------------------------------------------+
| **Info:**                                                          |
|                                                                    |
| To see the values saved in the bash variables, run the following:: |
|                                                                    |
|     echo $USERNAME                                                 |
|     echo $IP_ADDRESS                                               |
+--------------------------------------------------------------------+

3. We can now use the variables to SSH into the machine.

.. code-block::

    ssh $USERNAME@$IP_ADDRESS

+-------------------------------------------------------------------------------------------------------------------------------------+
+ **Info:**                                                                                                                           +
+                                                                                                                                     +
+ The argument we parse to ``query`` is a `JMESPath <http://jmespath.org/>`_ expression, which is a query language for JSON files.    +
+ To see the JSON file where these values came from, run::                                                                            +
+                                                                                                                                     +
+     az vm show --name webvm --resource-group learn-azure-01 --show-details                                                          +
+-------------------------------------------------------------------------------------------------------------------------------------+

Cleaning Up Resources
=====================

Cloud resources are not free so it's very important to clean up once resources are no longer being used in order to avoid large expenditure!
We will be deleting the resource group we created at the end of every session to instill good habits!

Deallocation versus Deletion
----------------------------

Some resources (for example, virtual machines) can be "deallocated".
This means the physical hardware you have reserved in a data centre can be used by another Cloud customer.
The resources can then be reallocated to you when you next need them.

Deleting a resource also deallocates it, but all of your data is also removed and cannot be recovered.
Make sure that you're certain you want to delete resources or that you have downloaded all your data elsewhere!

Resources can be deleted individually, but also deleting the Resource Group removes all resources affiliated with it.
This is the quickest way to remove a project in one step.

In the Portal
-------------

1. Navigate to your Resource Groups and select ``learn-azure-01``.

.. image:: ../figures/01_Intro/delete1.png

2. In the top banner, select "Delete resource group".
   In the panel that opens on the right, type the name of the resource group into the box (as confirmation) and click "Delete".

.. image:: ../figures/01_Intro/delete2.png

This will begin the deletion process which may take some time.

Using the Cloud Shell or CLI
----------------------------

The CLI command to delete a resource group is as follows.

.. code-block::

    az group delete --name learn-azure-01

It will ask for confirmation, type "yes" and continue.

Resource groups can take a long time to be deleted, so if you don't want to want to wait for this process to be completed before reclaiming your shell session, pass the ``--no-wait`` flag.
The confirmation step can also be bypassed by passing the ``--yes [-y]`` flag.
