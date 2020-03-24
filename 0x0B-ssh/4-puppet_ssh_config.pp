#connect to server withou password
exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config':
        path    => '/bin/'
}
