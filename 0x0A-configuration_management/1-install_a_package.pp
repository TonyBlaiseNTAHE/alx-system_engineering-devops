# installs flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => '/usr/bin/pip3'
}
