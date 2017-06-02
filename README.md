Ansible Role NTP
=========

Installs and configures the NTP service daemon.

Role Variables
--------------

- **ntp_timezone: ""**
  Timezone string.  
  Example: `ntp_timezone: Europe/Berlin`

- **ntp_servers: []**  
  List of NTP timeserver strings that will be written to `ntp.conf`.  
  Example: `ntp_servers: ['0.europe.pool.ntp.org', '1.europe.pool.ntp.org']`
  
Dependencies
------------

none.

Example Playbook
----------------

    - hosts: servers
      roles:
         - ntp

License
-------

Apache

Author Information
------------------

Service and support for orchestrated hosting environments, continuous integration/deployment/delivery and various Linux and open-source technology stacks are available from:

```
Blunix GmbH - Professional Linux Service
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: mailto:service@blunix.org
```
