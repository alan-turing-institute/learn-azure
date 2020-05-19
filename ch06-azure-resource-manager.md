# Chapter 6: Azure resource manager

## Concepts covered

1. Why use resource groups?
   * Group resources altogether
   * Group resources based on role

2. Permission roles, locks and tags.

3. Templates: "Infrastructure as code"

## Terraform versus Azure Resource Manager (not in the book)

### Input format

**ARM:** JSON  
**Terraform:** HashiCorp Configuration Language (HCL). HCL supports commenting – useful! Terraform also supports JSON.

### Cloud providers

**ARM:** Azure only  
**Terraform:** Azure, GCP, AWS

### Parameter support

**ARM:** Yes  
**Terraform:** Yes

### Template storage

**ARM:** Manual management via git repository, Azure storage, network shared drive  
**Terraform:** Automatic management via Azure storage; Terraform Cloud is a SaaS product for managing shared templates.

### Template visualisation

**ARM:** http://armviz.io (third-party)  
**Terraform:** Built-in command `terraform graph`

### VS Code extension

**ARM:** Yes  
**Terraform:** Yes

### Use locally with Docker

**ARM:** No  
**Terraform:** Yes

## Common Terraform commands

```shell
terraform init
terraform plan
terraform plan -destroy
terraform apply
terraform plan -out=newplan
terraform apply "newplan"
terraform show
terraform destroy
```

## References

* How Spotify Accidentally Deleted All its Kube Clusters with No User Impact: https://youtu.be/ix0Tw8uinWs?t=877

* Terraform Azure tutorial: https://learn.hashicorp.com/terraform/azure/intro_az

* ARM quickstart templates https://github.com/Azure/azure-quickstart-templates

* ARM designer: http://armviz.io/designer (third-party)

  
