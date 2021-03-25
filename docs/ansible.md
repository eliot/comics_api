# Useful Ansible commands

## ping hosts
ansible -i production.inventory -m ping webservers


## run main playbook
ansible-playbook -i production.inventory first_playbook.yml

## install an ansible module
ansible-galaxy collection install community.crypto
