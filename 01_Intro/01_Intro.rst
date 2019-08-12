==============
 Introduction
==============

Azure Portal vs Azure Cloud Shell vs Azure CLI
==============================================

* CLI = Command Line Interface

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
+-------------+----------------------------------------------------------------------------------+-----------------------------------------------+
| CLI         | * Access to local files, tools and environments                                  | * Need to keep it updated                     |
|             | * OS agnostic                                                                    |                                               |
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
| * *General Purpose* - Great for developing, testing or low-use production.                                                        |
| * *Compute optimised* - High performance CPUs for production servers.                                                             |
| * *Memory optimised* - Larger memory options for big databases or in-memory intensive data processing.                            |
| * *Storage optimised* - Low-latency, high-disk performance for disk-intensive applications.                                       |
| * *GPU* - Graphics- specialised VMs for rendering images or video processing.                                                     |
| * *High-performance computing (HPC)* - A bit of everything! Plenty of CPU, memory, etc. for the most demanding workloads.         |
+-----------------------------------------------------------------------------------------------------------------------------------+

.. image:: ../figures/01_Intro/portal_vm_step4.png

.. image:: ../figures/01_Intro/portal_vm_step6.png

.. image:: ../figures/01_Intro/portal_vm_step7.png

.. image:: ../figures/01_Intro/portal_vm_step8.png

.. image:: ../figures/01_Intro/portal_vm_step9.png

.. image:: ../figures/01_Intro/portal_vm_step5.png

.. image:: ../figures/01_Intro/portal_vm_step10.png

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
