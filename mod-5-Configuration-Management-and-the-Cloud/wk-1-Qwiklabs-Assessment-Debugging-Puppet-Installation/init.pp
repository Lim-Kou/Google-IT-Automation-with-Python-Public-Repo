# Scripts under /etc/profile.d/ are used to perform start up tasks.
# For this Google qwiklabs exercise:
# init.pp file is located in cd /etc/puppet/code/environments/production/modules/profile/manifests

class profile {
        file { '/etc/profile.d/append-path.sh':
                owner   => 'root',
                group   => 'root',
                mode    => '0644',
                content => "PATH=\$PATH:/java/bin\n",
        }
}
