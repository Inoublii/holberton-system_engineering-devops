# Install ngnix with puppet and configurate a server

exec {'update':
  provider => shell,
  path => '/usr/bin:usr/sbin:bin',
  command => 'sudo apt-get update -y',
}
exec {'installation':
  provider => shell,
  path => '/usr/bin:usr/sbin:bin',
  command => 'sudo apt-get install nginx -y',
}
exec {'html config':
  provider => shell,
  command => 'sudo echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html',
}
exec {'redirect':
  provider => shell,
  command => 'sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me hhttps://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
}

exec {'starting':
  provider => shell,
  command => 'sudo service nginx start',
}
