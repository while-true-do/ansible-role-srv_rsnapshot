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
| Install and configure rsnapshot.

## Motivation

Easy, everyone needs backups. :)
And keep in mind:
**No Backup, No Mercy**

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_rsnapshot)

```
ansible-galaxy install while_true_do.rsnapshot
```

Install from [Github](https://github.com/while-true-do/srv_rsnapshot)

```
git clone https://github.com/while-true-do/srv_rsnapshot.git while_true_do.srv_rsnapshot
```

## Requirements

Used Modules:

-   [packages](http://docs.ansible.com/ansible/latest/package_module.html)
-   [template](http://docs.ansible.com/ansible/latest/template_module.html)
-   [systemd](https://docs.ansible.com/ansible/latest/systemd_module.html)
-   [shell](https://docs.ansible.com/ansible/latest/shell_module.html)
-   [command](https://docs.ansible.com/ansible/latest/command_module.html)
-   [file](https://docs.ansible.com/ansible/latest/file_module.html)

## Dependencies

<!--
Describe, if other roles are needed and link them here.
You also have to put the dependencies in the requirements.yml.

```
ansible-galaxy install -r requirements.yml
```

If nothing is needed, please write "None."
-->

## Role Variables

```yaml
# defaults/main.yml
wtd_rsnapshot_state: "present"
wtd_rsnapshot_packages: "rsnapshot"

wtd_rsnapshot_config_version: 1.2

wtd_rsnapshot_config_snapshot_root: "/backup"

wtd_rsnapshot_config_cmd_rm: "/usr/bin/rm"
wtd_rsnapshot_config_cmd_rsync: "/usr/bin/rsync"
wtd_rsnapshot_config_cmd_logger: "/usr/bin/logger"

wtd_rsnapshot_config_retains:
  - name: "alpha"
    value: "6"
  - name: "beta"
    value: "7"
  - name: "gamma"
    value: "4"
  - name: "delta"
    value: "3"

wtd_rsnapshot_config_verbose: 3
wtd_rsnapshot_config_loglevel: 3
wtd_rsnapshot_config_logfile: "/var/log/rsnapshot"

wtd_rsnapshot_config_lockfile: "/var/run/rsnapshot.pid"

wtd_rsnapshot_config_backups:
  - backup: /home/
    target: localhost/
```

## Example Playbook

Simple Example:

```yaml
- hosts: servers
  roles:
    - { role: while_true_do.rsnapshot }
  vars:
    - wtd_rsnapshot_config_shapshot_root: '/backup/'
    - wtd_rsnapshot_config_retains:
      - name: 'daily'
        value: '7'
    - wtd_rsnapshot_config_backups:
      - backup: /home/cinux
        target: home/
```

Advanced Example:
rsnapshot is not designed to run multiple instance at the same time by using one config-file.
Because of this its possible to set the `wtd_rsnapshot_config_multi_enabled` to `true` and configure multiple configurations of rsnapshot include systemd timers and services.
Below you find a playbook with variable to get an illustration how the role works if you want to use multiple configurations.
*NOTE:* Please only run this playbook in a test machine. Its for testing purpose.

```yaml
- hosts: $VMIP
  become: yes
  roles:
    - { role: while_true_do.rsnapshot }
  vars:
    - wtd_rsnapshot_config:
      - name: Backup_etc_systemd
        retains:
          - name: daily
            value: '7'
        backups:
          - src: /etc/systemd
            target: localhost/
        execStart: "/usr/bin/rsnapshot -c /etc/rsnapshot-Backup_etc_systemd.conf %i"
        logfile: "/var/log/rsnapshot-Backup_etc_systemd"
      - name: homes
        retains:
          - name: hourly
            value: '12'
            time: '*-*-* *:24:00'
          - name: montly
            value: '3'
            time: '1-*-* 00:00:00'
        backups:
          - src: /home/
            target: homes/
        snapshot_root: '/backup_home'
        execStart: "/usr/bin/rsnapshot -c /etc/rsnapshot-homes.conf %i"
        logfile: "/var/log/rsnapshot-homes"
    - wtd_rsnapshot_config_snapshot_root: /backup
    - wtd_rsnapshot_timer_time: "*-*-* 00:00:00"
```

After you have execute the playbook you can check with following commands:
```
systemctl list-timers | grep rsnapshot
ls -la /etc/rsnapshot-*
```

For each entry a separate configuration file gets created under /etc/rsnapshot-*.
Additionally to this for each retains a timer will be created. And of course you can create for each retains a different time. This helps to run different retains at different times. Its also possible to set a default time by set wtd_rsnapshot_timer_time, but the time of a retain will overwrite it (can be seen in the above example by "Backup_etc_systemd"


Following variables, started with __wtd_rsnapshot_config__ get overwritten by wtd_rsnapshot_config_multi if defined:
- config_version
- snapshot_root
- verbose
- loglevel
- lockfile
- timer


## Testing
Most of the "generic" tests are located in the Test Library.
Ansible specific testing is done with Molecule.
Infrastructure testing is done with testinfra.
Automated testing is done with Travis CI.

## Contribute / Bugs

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_rsnapshot/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_rsnapshot/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
