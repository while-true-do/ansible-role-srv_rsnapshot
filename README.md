<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_rsnapshot.svg)](https://github.com/while-true-do/ansible-role-srv_rsnapshot/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_rsnapshot.svg)](https://github.com/while-true-do/ansible-role-srv_rsnapshot/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_rsnapshot.svg)](https://github.com/while-true-do/ansible-role-srv_rsnapshot/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_rsnapshot.svg)](https://github.com/while-true-do/ansible-role-srv_rsnapshot/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_rsnapshot.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_rsnapshot)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_rsnapshot%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_rsnapshot)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_rsnapshot%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_rsnapshot)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_rsnapshot%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_rsnapshot)


# Ansible Role: srv_rsnapshot

An Ansible Role to install and configure rsanpshot.

## Motivation

Everybody needs a valid backup. As often stated: "no backup, no mercy".

## Description

This Ansible Role installs and configures [rsnapshot](https://rsansphot.org).

-   install packages
-   configure rsnapshot
-   create systemd service
-   create systemd timers

## Requirements

Used Modules:

-   [Ansible package Module](http://docs.ansible.com/ansible/latest/package_module.html)
-   [Ansible template Module](http://docs.ansible.com/ansible/latest/template_module.html)
-   [Ansible systemd Module](https://docs.ansible.com/ansible/latest/systemd_module.html)
-   [Ansible service Module](https://docs.ansible.com/ansible/latest/service_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_rsnapshot)
```
ansible-galaxy install while_true_do.srv_rsnapshot
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_rsnapshot)
```
git clone https://github.com/while-true-do/ansible-role-srv_rsnapshot.git while_true_do.srv_rsnapshot
```

Dependencies:

For CentOS Systems, the [EPEL](https://fedoraproject.org/wiki/EPEL) repository
must be enabled. You can achive this by running the
[while_true_do.rpo_epel](https://github.com/while-true-do/ansible-role-rpo_epel)
Ansible Role.

```
ansible-galaxy install -r requirements.yml
```

## Usage

### Role Variables

```
---
# defaults/main.yml for rsnapshot

## Package Management
wtd_srv_rsnapshot_package: "rsnapshot"
# State can be present|latest|absent
wtd_srv_rsnapshot_package_state: "present"

## Configuration Management
# Below you can find some example configuration.
# You MUST define "retains: []" and "backup: []"
# Please consult man rsnapshot for more information or https://rsnapshot.org
wtd_srv_rsnapshot_conf: []
# version: 1.2
# snapshot_root: "/.snapshots/"
# no_create_root: 1
# cmd_cp: "/usr/bin/cp"
# cmd_rm: "/usr/bin/rm"
# cmd_rsync: "/usr/bin/rsync"
# cmd_ssh: "/usr/bin/ssh"
# cmd_logger: "/usr/bin/logger"
# cmd_du: "/usr/bin/du"
# cmd_rsnapshot_diff: "/usr/bin/rsnapshot-diff"
# cmd_preexec: ""
# cmd_postexec: ""
# linux_lvm_cmd_lvcreate: "/usr/sbin/lvcreate"
# linux_lvm_cmd_lvremove: "/usr/sbin/lvremove"
# linux_lvm_cmd_mount: "/usr/bin/mount"
# linux_lvm_cmd_umount: "/usr/bin/umount"
# retains:
#   - name: "some name" # the name for the retains
#     value: 15         # how many backups do want to keep
#     time: "daily"     # systemd timer time format
#     enabled: true     # define if the timer should be enabled (default true)
# verbose: 2
# loglevel: 3
# logfile: "/var/log/rsnapshot/rsnapshot.log"
# lockfile: "/var/run/rsnapshot.pid"
# stop_on_stale_lockfile: 0
# rsync_short_args: ""
# rsync_long_args: ""
# ssh_args: "-p 22"
# du_args: "-csh"
# one_fs: 0
# includes: []          # global include patterns
# excludes: []          # global exclude patterns
# include_files: []     # global include_files
# exclude_files: []     # global exclude_files
# link_dest: 0
# sync_first: 0
# use_lazy_deletes: 0
# rsync_numtries: 0
# linux_lvm_snapshotsize: "100M"
# linux_lvm_snapshotname: "rsnapshot"
# linux_lvm_vgpath: "/dev"
# linux_lvm_mountpath: "/path/to/mount/lvm/snapshot/during/backup"
# The backup list can take multiple statements
# backups:
#   - comment: ""       # useful, if you need a comment line
#   - src: "/foo/"      # define source and destination of your backups
#     dest: "foo/"
#     options: ""       # you can backup specific options like excludes
#   - script: "foo.sh"  # define a script and a destination for a scripted backup
#     dest: "foo/"
#   - exec: "foo.sh"    # Just run some command
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

Doing daily backups of your localhost and keep them for 14 days.

```
---
- hosts: all
  roles:
    - role: while_true_do.rpo_epel
    - role: while_true_do.srv_rsnapshot
      wtd_srv_rsnapshot_conf:
        retains:
          - name: "daily"
            value: 14
            time: "daily"
            enabled: true
        backups:
          - comment: "# LOCALHOST"
          - src: "/home/"
            dest: "localhost/"
          - src: "/var/log"
            dest: "localhost/"
          - src: "/etc/"
            dest: "localhost/"
```

#### Advanced

This example does daily, weekly and monthly backups for localhost and
example.com (via backup user).

```
- hosts: all
  roles:
    - role: while_true_do.rpo_epel
    - role: while_true_do.srv_rsnapshot
      wtd_srv_rsnapshot_conf:
      retains:
        - name: "daily"
          value: 14
          time: "daily"
        - name: "weekly"
          value: 8
          time: "weekly"
        - name: "monthly"
          value: 12
          time: "monthly"
      backups:
        - comment: "LOCALHOST"
        - src: "/etc/"
          dest: "localhost/"
        - src: "/home/"
          dest: "localhost/"
        - src: "/var/log/"
          dest: "localhost/"
        - comment: "EXAMPLE.COM"
        - src: "backup@example.com:/etc/"
          dest: "example.com/"
        - src: "backup@example.com:/home/"
          dest: "example.com/"
        - src: "backup@example.com:/var/log/"
          dest: "example.com/"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_rsnapshot/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_rsnapshot/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
