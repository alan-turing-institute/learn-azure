# This script sample is part of "Learn Azure in a Month of Lunches" (Manning
# Publications) by Iain Foulds.
#
# This sample script covers the exercises from chapter 4 of the book. For more
# information and context to these commands, read a sample of the book and
# purchase at https://www.manning.com/books/learn-azure-in-a-month-of-lunches
#
# This script sample is released under the MIT license. For more information,
# see https://github.com/fouldsy/azure-mol-samples/blob/master/LICENSE

import string, random, time, azurerm, json, subprocess

from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

# Define variables to handle Azure authentication
get_token_cli = subprocess.Popen(['az account get-access-token | jq  -r .accessToken'], stdout=subprocess.PIPE, shell=True)
auth_token = get_token_cli.communicate()[0].decode(encoding="utf-8").rstrip()
subscription_id = azurerm.get_subscription_from_cli()

# Define variables with random resource group and storage account names
resourcegroup_name = 'learnazure'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
storageaccount_name = 'learnazure'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
location = 'westeurope'

###
# Create the a resource group for our demo
# We need a resource group and a storage account. A random name is generated, as each storage account name must be globally unique.
###
response = azurerm.create_resource_group(auth_token, subscription_id, resourcegroup_name, location)
if (response.status_code == 200) or (response.status_code == 201):
    print("Resource group: {} created successfully.".format(resourcegroup_name))
else:
    print('Error creating resource group')

# Create a storage account for our demo
response = azurerm.create_storage_account(auth_token, subscription_id, resourcegroup_name, storageaccount_name,  location, storage_type='Standard_LRS')
if response.status_code == 202:
    print('Storage account: {} created successfully.'.format(storageaccount_name))
    print('\nWaiting for storage account to be ready before we create a Table')
    time.sleep(15)
else:
    print('Error creating storage account')

###
# Use the Azure Storage Storage SDK for Python to create a Table
###
print('\nLet\'s create an Azure Storage Table to store some data.')
input('Press Enter to continue...')

# Each storage account has a primary and secondary access key.
# These keys are used by applications to access data in your storage account, such as Tables.
# Obtain the primary storage access key for use with the rest of the demo

response = azurerm.get_storage_account_keys(auth_token, subscription_id, resourcegroup_name, storageaccount_name)
storageaccount_keys = json.loads(response.text)
storageaccount_primarykey = storageaccount_keys['keys'][0]['value']
