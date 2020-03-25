# Install ngnix with puppet and configurate a server
#The redirection must be a “301 Permanently”
exec {'updates':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get update -y ',
}

exec {'installation':
  provider => shell,
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo apt-get install nginx -y ',
}

exec {'redirection':
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me http://www.youtube.com permanent;" /etc/nginx/sites-available/default',
}

exec {'html config':
  provider => shell,
  command  => 'sudo echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
}



exec {'start':
  provider => shell,
  command  => 'sudo service nginx start',
}
