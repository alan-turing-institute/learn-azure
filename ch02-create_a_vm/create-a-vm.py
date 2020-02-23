import argparse


def parse_args():
    DESCRIPTION = "Create and delete a Virtual Machine in Azure"
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    create_vm = subparsers.add_parser("create", help="Create a VM in Azure")
    create_vm.add_argument("-n", "--name", type=str, help="Name of the VM to create", required=True)
    create_vm.add_argument("-g", "--resource-group", type=str, help="Resource group to deploy the VM into", required=True)
    create_vm.add_argument("-s", "--subscription", type=str, help="Azure subscription name or id to deploy into", required=True)

    return parser.parse_args()


def main():
    args = parse_args()
    print(args)


if __name__ == "__main__":
    main()
