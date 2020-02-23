import os
import argparse
import subprocess


class AzureVirtualMachine:
    def __init__(self, argsDict):
        for k, v in argsDict.items():
            setattr(self, k, v)

    def create(self):
        self.login()
        self.set_subscription()
        self.resource_group()

        cmd = [
            "az",
            "vm",
            "create",
            "--name",
            self.name,
            "--resource-group",
            self.resource_group,
            "--admin-username",
            self.admin_username,
            "--authentication-type",
            "ssh",
            "--ssh-key-value",
            self.path_to_public_ssh_key,
            "--image",
            self.image,
            "--size",
            self.size,
            "--storage-sku",
            self.storage,
            "--output",
            "table",
        ]

        subprocess.check_call(cmd)

    def delete(self):
        self.login()
        subprocess.check_call(["az", "group", "delete", "--name", self.resource_group])

    def login(self):
        subprocess.check_call(["az", "login", "--output", "none"])

    def resource_group(self):
        resource_group_exists = subprocess.check_output(
            ["az", "group", "exists", "--name", self.resource_group]
        )

        if not resource_group_exists:
            if " " in self.location:
                self.location = "".join(self.location.lower().split(" "))
            subprocess.check_call(
                [
                    "az",
                    "group",
                    "create",
                    "--name",
                    self.resource_group,
                    "--location",
                    self.location,
                    "--output",
                    "table",
                ]
            )

    def set_subscription(self):
        cmd = ["az", "account", "set", "--subscription"]

        if " " in self.subscription:
            cmd.append(f'"{self.subscription}"')
        else:
            cmd.append(self.subscription)

        subprocess.check_output(cmd)


def parse_args():
    DESCRIPTION = "Create and delete a Virtual Machine in Azure"
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    create_vm = subparsers.add_parser(
        "create", help="Create a Virtual Machine in Azure"
    )
    create_vm.add_argument(
        "name", type=str, help="Name of the Virtual Machine to create"
    )
    create_vm.add_argument(
        "resource_group",
        type=str,
        help="Resource group to deploy the Virtual Machine into",
    )
    create_vm.add_argument(
        "subscription", type=str, help="Azure subscription name or id to deploy into"
    )
    create_vm.add_argument(
        "location", type=str, help="The data centre location to deploy resources into"
    )
    create_vm.add_argument(
        "--admin-username", type=str, help="Username for admin account"
    )
    create_vm.add_argument(
        "--path-to-public-ssh-key",
        type=os.path.abspath,
        help="Path to public ssh key for admin account",
    )
    create_vm.add_argument(
        "--image",
        type=str,
        default="UbuntuLTS",
        help="OS image to install on the Virtual Machine. Default: UbuntuLRS.",
    )
    create_vm.add_argument(
        "--size",
        type=str,
        default="Standard_D2s_v3",
        help="Size of Virtual Machine to deploy. Default: Standard_D2s_v3.",
    )
    create_vm.add_argument(
        "--storage",
        type=str,
        default="Standard_LRS",
        help="Storage type to deploy. Default: Standard_LRS.",
    )

    delete_vm = subparsers.add_parser(
        "delete", help="Delete a Resource Group containing a Virtual Machine in Azure"
    )
    delete_vm.add_argument(
        "resource_group", type=str, help="The resource group to be deleted"
    )

    return parser.parse_args()


def main():
    args = parse_args()
    print(args)

    azure_vm = AzureVirtualMachine(vars(args))

    if args.subcommand == "create":
        azure_vm.create()
    elif args.subcommand == "delete":
        azure_vm.delete()


if __name__ == "__main__":
    main()
