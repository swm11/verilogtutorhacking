# Instalation notes


## Opening network ports on the local server firewall

```
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

## TLS certificate

Install certbot for Python on Linux: [https://certbot.eff.org/instructions?ws=other&os=pip](https://certbot.eff.org/instructions?ws=other&os=pip)
* `sudo pip3 install certbot`

With no webserver running, run:
* `sudo /home/swm11/.venv/bin/certbot certonly --standalone`

This reported certificates being saved:
```
Certificate is saved at: /etc/letsencrypt/live/svr-www-ecad.cl.cam.ac.uk/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/svr-www-ecad.cl.cam.ac.uk/privkey.pem
```

For automatically renew, add a crontab entry vis:
```
5 2,14 * * * root /home/swm11/.venv/bin/python3 -c 'import random; import time; time.sleep(random.random() * 300)' && /home/swm11/.venv/bin/certbot renew -q
```


TODO:
* upgrade certbot, e.g. every month, using:
```
pip install --upgrade certbot
```

* Change the above to get a certificate installed for NGINX
* Explore [https://dylancastillo.co/posts/fastapi-nginx-gunicorn.html](https://dylancastillo.co/posts/fastapi-nginx-gunicorn.html) to see how to deploy using NGINX

