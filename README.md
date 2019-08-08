
# Backup Manager

## Overview

Backup Manager is an Ansible Role for network engineers and network operators.  It provides functions to `backup` and `restore` configurations to/from `git` repository.

## Quick start

### Download from ansible galaxy

1) Download the role from ansible_galaxy into your roles directory
```
ansible-galaxy install -p roles nmake.backup_manager
```
2) Call the role by loading it at the top of your playbook

```
- name: "Backup Configurations"
  hosts: all
  gather_facts: False
  roles:
  - role: nmake.backup_manager
    function: backup
    backup_manager_git_key_file: "~/.ssh/my_deploy_key"
```
3) Run your playbook
