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
