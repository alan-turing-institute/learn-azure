=============
Azure Storage
=============

In this session, we're going to lookg at the different types of storage available in Azure and when to use them.

Introduction
============

In Azure, there's much more available than "just" somewhere to store files or virtual disks for your VMs.

Let's think about a fictional pizza company running an online service!
The "backend" app needs a data store that holds the available pizzas, list of toppings, and prices.
As orders are received, the app needs to be able to send messages between the different components.
The "frontend" website then needs images to show customers what the pizzas look like.

Azure Storage can cover all of these needs!

.. code-block::

    |--* Azure Storage account
       |--* Blob
       |  |--* Unstructured data, such as the images of the pizzas.
       |--* Table
       |  |--* Unstructured datastore, such as the list of available pizzas.
       |--* Queue
       |  |--* Messages between app components to process pizza orders.
       |--* File
       |  |--* Traditional file shares for VMs, such as storing logs from the app.

Azure Storage for VMs is stragiht forward.
You can create and use Azure managed disks, which is a type of virtual hard disk (VHD) that abstracts away a lot of design considerations around performance and distribution.
The Azure platform will figure out redundancy and availability when you create a VM and attach any managed data disk.

Types of Storage
================

Table Storage
-------------

You may have heard of SQL databases such as Microsoft SQL Server, MySQL or PostgreSQL.
These are *relational* databases, made up of one or more tables that contain one or more rows of data.
These types of databases are common for application development and can be designed, visualised, and queried in a structured manner - the *S* in *SQL* (for Structured Query Language).

NoSQL databases are different.
They don't follow the same structured approach, and data isn't stored in tables where each row contains the same fields.
There are different implementations of NoSQL databases such as: MongoDB, Cassandra, SAP HANA, CouchDB, and Redis.
The advantages of NoSQL databases are that they scale horizontally (you can add more servers rather than more memory or CPU), can handle larger amounts of data, and are more efficient at processing those large datasets.

How the data is stored in such a database can be defined in a few ways:

* *Key-value* (like a dictionary), such as Redis,
* *Column*, such as Cassandra,
* *Document*, such as MongoDB.

Each approach has pros and cons for performance, flexibility, or complexity point of view.
An Azure storage table uses a *key-value* and is a good introduction to NoSQL databases.

+----------------------------------------------------------------------------------------------------------------+
| **Info:** You can download and install the Microsoft Azure Storage Explorer if you like to visualise the data. |
| www.storageexplorer.com                                                                                        |
+----------------------------------------------------------------------------------------------------------------+

Exercise
--------

We are now going to see Azure Tables in action using Python!

1. Open the Azure Portal in a web browser and then open the Cloud Shell.

2. Login to your Azure account.

.. code-block::

    az login

3. Set your active subscription.

.. code-block::

    az account set --subscription "Living with Machines"

4. Clone this GitHub repo and change into the directory.

.. code-block::

    git clone https://github.com/alan-turing-institute/learn-azure.git
    cd learn-azure

5. Install the dependencies.

.. code-block::

    pip install -r requirements.txt --user

6. Now run the storage table demo script.

.. code-block::

    python scripts/02_storage_table_demo.py

7. Once you've worked through the script, read it to see how Python can be used to automate Azure commands.
   `02_storage_table_demo.py <https://github.com/alan-turing-institute/learn-azure/blob/sessions/2-storage/sessions/02_Storage.rst>`_
