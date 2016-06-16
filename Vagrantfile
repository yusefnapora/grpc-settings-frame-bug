# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "phusion/ubuntu-14.04-amd64"

  config.vm.provision "shell", inline: <<-SHELL
    echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
    apt-get -y update
    apt-get install -y sbt python-pip python-dev python-virtualenv libtool autoconf automake
    pip install --upgrade pip
  SHELL
end
