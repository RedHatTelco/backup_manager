# Backup configuration from device

The Backup Manager role provides a function that will restore configuration from a
git repository.  The `restore` function will **replace** the device
configuration.  

## How to use this function

The examples below demonstate how to use this function in a playbook.

## How to restore configuration

Below is an example of how to call the `restore` function.

```
- hosts: ios
  gather_facts: false
  roles:
    - name: namke.backup_manager
      backup_manager_os: "ios"
      backup_manager_function: "restore"
      backup_manager_git_server: "server.acme.com"
      backup_manager_git_repo: "network-backups"
      backup_manager_git_deploy_key: |
        -----BEGIN RSA PRIVATE KEY-----
        ........
        .........
        .......
        -----END RSA PRIVATE KEY-----

```

The example playbook above will restore device's configuration
 based on configuration available onto the target repository.

## Arguments

### backup_manager_pre_tasks

This setting provides the list of files containing tasks to run before
 the backup.

The default value is `[]`


### backup_manager_pre_roles

This setting provides the list of roles to run before the backup.

The default value is `[]`

> NOTE: If your role do not flush handlers, they will only run after the end
 of the backup.


### backup_manager_os

This setting defines the Network Operating System of the target device.

The default value is `"{{ ansible_network_os | default(None, True) }}"`


### backup_manager_function

This setting defines the function: `backup` or `restore`.

The default value is `"{{ function | default('backup') }}"`


### backup_manager_backup_path

This setting defines the path to restore the backup inside of git repository.

The default value is `"{{ inventory_hostname }}/config"`


### backup_manager_git_server

This setting defines the git server.

The default value is `"git.acme.com"`


### backup_manager_git_repo

This setting defines the git repository to restore device's configuration.

The default value is `"backups"`


### backup_manager_git_branch

This setting defines the branch to restore device's configuration.

The default value is `"master"`

> NOTE: By default, some git servers protect against commits in the master branch.


### backup_manager_git_username

This setting defines the username/team/namespace for the repository.

The default value is `"backup_manager"`


### backup_manager_git_deploy_key

This setting defines the deploy key to use when pushing content
 to the repository in git server.

The default value is `""`


### backup_manager_git_deploy_key_file

This setting defines the file containing the deploy keys with write access
 to the repository.

The default value is `"~/.ssh/backup_manager_key"`


### backup_manager_git_committer_email

This setting defines the email to use when commiting content to the repository.

The default value is `"backup@ansible.com"`

> NOTE: By default, some git servers may check this value to validate access permissions.


### backup_manager_git_committer_name

This setting defines the name of the commiter.

The default value is `"backup"`

> NOTE: By default, some git servers check this value to validate access permissions.


### backup_manager_post_tasks

This setting provides the list of files containing tasks to run after
 the backup.

The default value is `[]`


### backup_manager_post_roles

This setting provides the list of roles to run after the backup.

The default value is `[]`


## Notes

PaloAlto Devices requires the role from: https://galaxy.ansible.com/paloaltonetworks/paloaltonetworks

Fortios Devices requires the collection from: https://galaxy.ansible.com/fortinet/fortios
