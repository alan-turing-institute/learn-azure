
# Session 4 - Continue python API for blob storage,

Fix the script to generate a SAS token

Explain the data ingest procedure (e.g. from partner)

Try the upload procedure, given a SAS (i.e. data provider's perspective).

# Session 3 - Blob Storage

Scenario:
You want to receive data from a data provider directly into Azure storage.
Once received, you want to make a list of what data has been uploaded, including it's size (in GB).

Plan:
Split into two groups, each aiming to write a script for different purposes:
1) create blob storage container, download keys, generate SAS token ready to send to a data provider

The [quickstart](https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-quickstart-blobs-python) shows how to do this, but it's artificial.

So let's try to write a script named `prepare_incoming_storage` taking command-line arguments:
  - provider_initials (the initials of the data provider)
  - sas_duration_days (to set the expiry of the SAS token)
  - -f (to force use of an existing container)

that does the following:
  - checks for the `CONNECT_STR` environment variable (see the quickstart)
  - takes as command line arguments:
    - the name or initials of the data provider (e.g. fmp, nls)
    - an identifier for the dataset (e.g. 'maps')
    - the duration of the SAS token in days
    - (optionally) the IP address range for the SAS.
  - constructs a string for the appropriate container name (e.g. <dataset-identifier><data-provider-initials>)
  - checks whether the container already exists
    - if so, exits with a warning that you must run with a "force" flag to use an existing container
  - creates a container with the given name (unless it already exists and the force flag was applied)
  - generates a SAS token with the specified parameters (expiry, IP range)
  - prints the SAS token (with simple instructions on what to do next)
  - prints the URL to which the data provider must navigate to perform the upload

  - ALSO: include help via argparse (see https://stackoverflow.com/questions/9037828/writing-a-help-for-python-script)
    - including how to get the connection string as per https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-quickstart-blobs-python#copy-your-credentials-from-the-azure-portal


2) list existing containers with their size (in GB)

Reference:
https://docs.microsoft.com/en-gb/azure/storage/blobs/storage-quickstart-blobs-python

BlobServiceClient api:
https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blobserviceclient?view=azure-python-preview#from-connection-string-conn-str--credential-none----kwargs-
