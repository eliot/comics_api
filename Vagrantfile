# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2004"
  #config.vm.box_url = "generic/ubuntu1804"
  config.vm.network "forwarded_port", guest: 80, host: 5080
  config.vm.network "forwarded_port", guest: 443, host: 5443

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |v|
    v.memory = "1024"
    v.name = "comics"
    v.cpus = 1
  end

  config.vm.provider "hyperv" do |v|
    v.memory = "1024"
    v.vmname = "comics"
    v.cpus = 1
  end

  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'playbook.yml'
  end

end
