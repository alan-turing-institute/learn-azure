==============
 Introduction
==============

Azure Portal vs Azure Cloud Shell vs Azure CLI
==============================================

* CLI = Command Line Interface - A tool used in the terminal to connect to/interact with some service.

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
   We select the subscription from the drop-down menu and create a new Resource Group we want to deploy the VM into by clicking "Create new" underneath the Resource Group box - the example will create a new group called ``learn-azure``.
   (You could also deploy this into an existing Resource Group by selecting from the drop-down menu.)
   Give your VM a name - the example uses ``webvm``.
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
   We are going to use "Standard SSD" from the drop-down menu.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Info:** Azure storage                                                                                                                                                                         |
|                                                                                                                                                                                                 |
| This is a brief introduction to basic disk storage.                                                                                                                                             |
| Other types of storage with different levels of structure are available and will be discussed in another session.                                                                               |
|                                                                                                                                                                                                 |
| * *Standard Hard Drive disks* - This is a regular spinning disk. Ideal for infrequent data access.                                                                                              |
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

3. Create a Resource Group.

.. code-block::

    az group create --name learn-azure --location westeurope

4. Create a VM.

.. code-block::

    az vm create \
        --name webvm \
        --resource-group learn-azure \
        --admin-username YOUR_USERNAME \
        --authentication-type ssh \
        --generate-ssh-keys \
        --image UbuntuLTS
