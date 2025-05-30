# Instalation notes


## Opening network ports on the local server firewall

```
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

Or better to use the following?:
```
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
```

## TLS certificate

Install certbot for Python on Linux: [https://certbot.eff.org/instructions?ws=other&os=pip](https://certbot.eff.org/instructions?ws=other&os=pip)
* `sudo pip3 install certbot certbot-nginx`

With no webserver running, run:
* `sudo certbot --nginx -d svr-www-ecad.cl.cam.ac.uk`


For automatically renew, add a crontab entry vis:
```
5 2,14 * * * root /home/swm11/.venv/bin/python3 -c 'import random; import time; time.sleep(random.random() * 300)' && /home/swm11/.venv/bin/certbot renew -q
```


TODO:
* upgrade certbot, e.g. every month, using:
```
pip install --upgrade certbot
```

## NGINX setup

Based on [https://docs.marimo.io/guides/deploying/deploying_nginx/](https://docs.marimo.io/guides/deploying/deploying_nginx/)

* Configuration file created in: `verilogtutorhacking/nginx/nginx-marimo.conf`

* Copy the configuration file: /etc/nginx/conf.d

* Test: `sudo nginx -t`

* Start/restart the server: `sudo service nginx restart`

