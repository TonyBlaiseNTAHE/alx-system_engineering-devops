#!/usr/bin/env bash
# client configuration file

file { '/etc/ssh/ssh_config':
  ensure => file,
  content => "
         # ssh client configuration
         PasswordAuthentication no
         IndentityFile ~/.ssh/school
         "
}
