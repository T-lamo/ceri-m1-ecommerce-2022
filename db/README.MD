
# Configuration de la base de données

## Creer un volume 
Créer un volume du nom **ecom_db_backup** avec la commande `docker volume create ecom_db_backup` 

## Charger la base 
1. Executer la commande `docker exec -it db sh` après avoir lancer le docker compose (docker compose --build up)
2. Charger la base de données avec cette commande `mysql -u root -p ecom_db < /app/ecom_db.sql`. 
3. Saisir **mypass** comme modepasse.

## Si la base n'existe pas, il faut la crée (Unknown database 'ecom_db')
4. Connecter à mysql en faisant: `mysql -u root -p` . 
5. Saisir **mypass** comme modepasse.
6. Saisir la commande `create database ecom_db`.
7. Deconnecter de mysql `exit`
8. Retourne à la tache 2 pour charger la base de données.
