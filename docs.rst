ansible-role-bind
================================================================================

Ansible role to setup the Berkeley Internet Name Domain.

Variables
--------------------------------------------------------------------------------

.. autoyaml:: defaults/main.yml

Examples
--------------------------------------------------------------------------------

.. literalinclude:: molecule/default/playbook.yml
   :language: yaml

Documentation
--------------------------------------------------------------------------------

Compile::

   $ pip3 install -r requirements.txt
   $ make man

View::

   $ man ./docs/man/ansible-role-bind.1
