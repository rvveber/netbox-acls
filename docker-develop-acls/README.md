
# development environment

* docker compose pull
* docker compose build
* docker compose up

```
docker exec -it docker-develop-acls_netbox_1 /opt/netbox/netbox/manage.py makemigrations netbox_acls

docker exec -it docker-develop-acls_netbox_1 /opt/netbox/netbox/manage.py makemigrations migrate

docker exec -it docker-develop-acls_netbox_1 /opt/netbox/netbox/manage.py createsuperuser
```