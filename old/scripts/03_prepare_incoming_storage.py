"""
Living with Machines Project

Script for prepping Azure resources to receive new data (e.g. from an external provider).

Loosely based on the tutorial at:
https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-quickstart-blobs-python#copy-your-credentials-from-the-azure-portal

Author: Tim Hobson, thobson@turing.ac.uk
"""


import argparse, os, sys, uuid
from datetime import datetime, timedelta
import azure.storage.blob as asb
from azure.core.exceptions import ResourceExistsError

#
# Help and usage instructions. #TODO.
#
description = '''Run this script to prepare Azure resources to receive new data (e.g. from an external provider).
Before calling the script, create an environment variable named CONNECT_STR. 
This environment variable must contain the connection string for the Azure 
storage account in which the data will reside.
'''
epilog = '''Next steps:...'''
parser=argparse.ArgumentParser(description=description, epilog=epilog)

#
# Parse the command line arguments.
#
parser.add_argument('--provider_initials', type=str, help='Initials of the data provider', required=True)
parser.add_argument('--data_identifier', type=str, help='Identifier for the dataset', required=True)
parser.add_argument('--sas_duration_days', type=int, help='Duration of the SAS token in days', required=True)
parser.add_argument('--ip_address_range', type=str, help="Provider's IP address range", required=False)
parser.add_argument('-f', dest='force', help='Force use of an existing container', action='store_true')
args=parser.parse_args()

#
# Construct the Azure container name.
#
container_name = args.data_identifier + args.provider_initials

#
# Check for the CONNECT_STR environment variable. Stop if not found.
#
connect_str = os.getenv('CONNECT_STR')
if not connect_str:
    sys.exit("ERROR: CONNECT_STR environment variable not found. For help, call this script with the --help flag.")

#
# Begin the Azure operations.
#
try:
    # old:
    # Create the BlobServiceClient object which will be used to create a container.
    #blob_service_client = asb.BlobServiceClient.from_connection_string(connect_str)

    # Create the ContainerClient object which will be used to create a container.
    container_client = asb.ContainerClient.from_connection_string(connect_str, container_name)

    #blob_client = container_client.get_blob_client("abcblob")

    # Create the container, unless the -f flag was used when calling the script.
    if args.force:
        # TODO: in this case, check that the container already exists. See get_container_client at:
        container_properties = container_client.get_container_properties()
        if not container_properties['name'] == container_name:
            raise ValueError
    else:
        container_client.create_container()
        #container_client = blob_service_client.create_container(container_name)

    # Generate a SAS token.
    resource_types = asb.ResourceTypes(service=True, container=True, object=True)
    #permission = asb.AccountSasPermissions(read=True, write=True, delete=True, list=True, add=False, create=False, update=False, process=False)
    permission = asb.ContainerSasPermissions(read=True, write=True, delete=True, list=True)

    expiry = datetime.utcnow() + timedelta(days=args.sas_duration_days)
    if not args.ip_address_range:
        ip = None
    else:
        ip = args.ip_address_range

    # old:
    # sas = blob_service_client.generate_shared_access_signature(resource_types, permission, expiry, start=None, ip=ip)

    # TODO:
    # The following line, to create a SAS token, fails with the error:
    # 'ContainerClient' object has no attribute 'generate_shared_access_signature'
    #
    # This contradicts the documentation at:
    # https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.containerclient?view=azure-python-preview#generate-shared-access-signature-permission-none--expiry-none--start-none--policy-id-none--ip-none--user-delegation-key-none----kwargs-
    sas = container_client.generate_shared_access_signature(permission = permission, expiry = expiry, start=None, ip=ip)

    print(sas)

except ResourceExistsError as ex:
    print(f'Container {container_name} already exists.\nRerun with the -f flag to use that container.')
    # print(ex)
except ValueError as ex:
    print(f'Container {container_name} does not exist.\nRerun without the -f flag to create it.')
    # print(ex)
except Exception as ex:
    print(ex)
