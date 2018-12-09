ansible-role-bind
*****************

Ansible role to setup the Berkeley Internet Name Domain.


Variables
=========

bind_package
   System package with BIND.

   Default:

      bind9

bind_default_release
   Default BIND package release.

   Default: ""

bind_service
   BIND system service name.

   Default:

      {{ bind_package }}

bind_conf_dir
   Directory with BIND configuration file.

   Default:

      /etc/bind

bind_zones_dir
   Directory with BIND zone files.

   Default:

      {{ bind_conf_dir }}/zones

bind_conf_file
   Main BIND configuration file.

   Default:

      {{ bind_conf_dir }}/named.conf.local

bind_options_file
   File with with BIND options.

   Default:

      {{ bind_conf_dir }}/named.conf.options

bind_conf_template
   Template for main configuration file.

   Default:

      named.conf.j2

bind_options_template
   Template for options file.

   Default:

      named.conf.options.j2

bind_zones
   BIND zones definitions.

   Default:

      {}


Examples
========

   ---
   - hosts: instance
     tasks:
       - name: Install dnsutils for tests
         apt:
           name: dnsutils
           state: present
       - import_role:
           name: bind
         vars:
           bind_zones:
             # Newlines are enforced, because named-checkzone
             # throws warning otherwise.
             test.local: "{{ lookup('file', 'test.local') }}\n"
             test2.local: "{{ lookup('file', 'test2.local') }}\n"


Documentation
=============

Compile:

   $ pip3 install -r requirements.txt
   $ make man

View:

   $ man ./docs/man/ansible-role-bind.1
