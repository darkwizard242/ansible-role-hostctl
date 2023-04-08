[![build-test](https://github.com/darkwizard242/ansible-role-hostctl/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-hostctl/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-hostctl/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-hostctl/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/59280?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/59280?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/59280?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-hostctl&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-hostctl) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-hostctl&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-hostctl) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-hostctl&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-hostctl) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-hostctl&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-hostctl) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-hostctl?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-hostctl?color=orange&style=flat-square)

# Ansible Role: hostctl

Role to install (_by default_) [hostctl](https://github.com/guumaster/hostctl) on **Debian/Ubuntu** and **EL** systems. **hostctl** is a tool that gives you more control over the use of your hosts file. You can have multiple profiles and switch them on/off as you need.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
hostctl_app: hostctl
hostctl_version: 1.1.3
hostctl_os: linux
hostctl_arch: 64-bit
hostctl_dl_url: https://github.com/guumaster/{{ hostctl_app }}/releases/download/v{{ hostctl_version }}/hostctl_{{ hostctl_version }}_{{ hostctl_os }}_{{ hostctl_arch }}.tar.gz
hostctl_bin_path: /usr/local/bin
hostctl_file_owner: root
hostctl_file_group: root
hostctl_file_permission_mode: '0755'
```

### Variables table:

Variable                     | Description
---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------
hostctl_app                  | Defines the app to install i.e. **hostctl**
hostctl_version              | Defined to dynamically fetch the desired version to install. Defaults to: **1.1.3**
hostctl_os                   | Defines os type. Defaults to: **linux**
hostctl_arch                 | Defines os architecture. Defaults to: **64-bit**
hostctl_dl_url               | Defines URL to download the hostctl binary from.
hostctl_bin_path             | Defined to dynamically set the appropriate path to store hostctl binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
hostctl_file_owner           | Owner for the binary file of hostctl.
hostctl_file_group           | Group for the binary file of hostctl.
hostctl_file_permission_mode | Defines the permission mode level for the file. Defaults to: `0755`

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **hostctl**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.hostctl
```

For customizing behavior of role (i.e. specifying the desired **hostctl** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.hostctl
  vars:
    hostctl_version: 1.1.2
```

For customizing behavior of role (i.e. placing binary of **hostctl** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.hostctl
  vars:
    hostctl_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-hostctl/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
