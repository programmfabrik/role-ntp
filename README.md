# Ansible Role NTP

This role installs and configures NTPd.

## Example Play

```yaml
- hosts: all
  vars:
    ntp_timezone: Europe/Berlin
  roles:
     - blunix.role-ntp
```

# License

Apache-2.0

# Author Information

All changes from 2019-05-31 onwards:

```
Programmfabrik GmbH,
Schwedter Str. 9b,
10119 Berlin
```

All changes until 2019-05-30 by:

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
