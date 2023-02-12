# django
## Lancement du docker 
docker-compose up -d

## Importation de la base de données

```
docker-compose exec web python manage.py makemigrations bibilio
```
```
docker-compose exec web python manage.py migrate
```
