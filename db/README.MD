
# Configuration de la base de données

## Creer un volume 
Créer un volume du nom **ecom_db_backup** avec la commande `docker volume create ecom_db_backup` 

## Charger la base 
1. Executer la commande `docker exec -it db sh` après avoir lancer le docker compose (docker compose -f docker-compose.dev.yml --build up)
2. Charger la base de données avec cette commande `mysql -u root -p ecom_db < /app/ecom_db.sql`. 
3. Saisir **mypass** comme modepasse.

## Si la base n'existe pas, il faut la crée (Unknown database 'ecom_db')
4. Connecter à mysql en faisant: `mysql -u root -p` . 
5. Saisir **mypass** comme modepasse.
6. Saisir la commande `create database ecom_db`.
7. Deconnecter de mysql `exit`
8. Retourne à la tache 2 pour charger la base de données.


## Connect to terraform cloud using github action
https://developer.hashicorp.com/terraform/tutorials/automation/github-actions?utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS

https://developer.hashicorp.com/terraform/cloud-docs/api-docs
Secret manager 

Architecture microservice
Monolitique
Universal backend
SOA service orienter application 

les port qui est utilisé: sudo netstat -ltnp  | grep -w ':80'

Moteur de recherche
Algolia

### cloud-sql-proxy
Télécharger le binaire CloudSQL proxy pour votre plateforme https://github.com/GoogleCloudPlatform/cloud-sql-proxy?utm_source=cloud.google.com&utm_medium=referral#installation
Assurez vous que le binaire à les perm exec (chmod +x PATH/TO/BIN)
Ensuite il suffit de lancer le binaire avec la commande suivante:
./cloud-sql-proxy --credentials-file PATH/TO/KEY.json ceri-m1-ecommerce-2022:europe-west1:mysql-primary

./cloud-sql-proxy --credentials-file key.json ceri-m1-ecommerce-2022:europe-west1:mysql-primary


GOOGLE_APPLICATION_CREDENTIALS


## credentials-file path
europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/greenfish

## stop mysql service if it is running
sudo systemct stop mysql


## cloud run service basic
google cloud ressource
