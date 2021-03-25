# Bootstrapping the server
Setting up the server before using ansible

1. Log in to fresh VM with root user and password

  local$ ssh root@myserver.com

2. create user 'mgmt'

  vm# useradd -m mgmt -G sudo -s /bin/bash

3. copy ssh key for 'mgmt' user to server (assumed to be created already)

  local$ ssh-copy-id -i ~/.ssh/mgmt_myserver.com.pub root@myserver.com
  vm# echo /home/root
  vm# sudo su - mgmt
  mgmt@vm$ mkdir -p ~/.ssh
  mgmt@vm$ chmod 700 ~/.ssh
  mgmt@vm$ touch ~/.ssh/authorized_keys
  mgmt@vm$ chmod 600 ~/.ssh/authorized_keys
  mgmt@vm$ exit
  vm# cat /root/.ssh/authorized_keys > /home/mgmt/.ssh/authorized_keys

4. add mgmt to sudoers

  vm# EDITOR=vim visudo

  # add this line to the very end of the file (after the #includedir)
  mgmt ALL=(ALL) NOPASSWD: ALL

5. change ssh port to xxx (randomly generated number)

  vm$ vim /etc/ssh/sshd_config

  # Uncomment and edit this line to the new port
  #Port 22

  # change this line to "no"
  PermitRootLogin yes

  # uncomment and change this line to "no"
  #PasswordAuthentication yes


6. restart sshd

  vm# systemctl restart sshd

7. update production.inventory file with your servers name and test ansible without

  ansible -i production.inventory -m ping webservers
