Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"

  config.vm.synced_folder "salt/roots/", "/srv/salt/"

  config.vm.provision :salt do |salt|
    salt.minion_config = "salt/minion.yml"
    salt.run_highstate = true
    salt.colorize = true
    salt.log_level = 'info'
    salt.verbose = true
    salt.masterless = true
  end
end