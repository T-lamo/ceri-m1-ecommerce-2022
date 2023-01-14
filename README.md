# S-E06-0632: Projet e-commerce

[![slack](https://img.shields.io/badge/slack-join-yellow.svg?logo=slack)](https://join.slack.com/t/cerim1ecommer-qy81374/shared_invite/zt-1hgh8de7q-v1Mb4g6rwPH6yNzmU7bKNA)

Les instructions sont disponibles [ici](https://github.com/Faylixe/ceri-m1-ecommerce-2022/tree/main/docs).

## Dream team

> :warning: Veuillez remplir le nom de votre équipe avant la fin de
> la première séance. L'identifiant vous sera renseigné via une
> Pull Request plus tard.

|             |        |
| ----------- | ------ |
| Nom         | greenfish |
| Identifiant | team-greenfish |

<br>

### Staff

> Les membres de l'équipe 

| Role                      | Membre |
| ------------------------- | ------ |
| Backend engineer          | Amos DORCEUS |
| Frontend engineer         | Faraniaina Rabarisoa |
| Site reliability engineer | Amos DORCEUS |

# Pour lancer localement 
## Configuration de la base de données

### Creer un volume 
Créer un volume du nom **ecom_db_backup** avec la commande `docker volume create ecom_db_backup` 

### Charger la base 
1. Executer la commande `docker exec -it db sh` après avoir lancer le docker compose (docker compose -f docker-compose.dev.yml --build up)
2. Charger la base de données avec cette commande `mysql -u root -p ecom_db < /app/ecom_db.sql`. 
3. Saisir **mypass** comme modepasse.

### Si la base n'existe pas, il faut la crée (Unknown database 'ecom_db')
4. Connecter à mysql en faisant: `mysql -u root -p` . 
5. Saisir **mypass** comme modepasse.
6. Saisir la commande `create database ecom_db`.
7. Deconnecter de mysql `exit`
8. Retourne à la tache 2 pour charger la base de données.


### Lancer avec docker le fichier docker-compose.dev.yml
docker compose -f docker-compose.dev.yml up --build


### Pour utiliser la base de données GCP en local 
### cloud-sql-proxy
Télécharger le binaire CloudSQL proxy pour votre plateforme https://github.com/GoogleCloudPlatform/cloud-sql-proxy?utm_source=cloud.google.com&utm_medium=referral#installation
Assurez vous que le binaire à les perm exec (chmod +x PATH/TO/BIN)
Ensuite il suffit de lancer le binaire avec la commande suivante:
./cloud-sql-proxy --credentials-file PATH/TO/KEY.json ceri-m1-ecommerce-2022:europe-west1:mysql-primary

./cloud-sql-proxy --credentials-file [key.json] ceri-m1-ecommerce-2022:europe-west1:mysql-primary


# Pour le developpment il faut configurer les champs suivants du fichier backend/src/config/conf.py
DATABASE_ADDRESS: str = ""
DATABASE_USER: str =""
DATABASE_PASSWORD: str = ""
DATABASE_NAME: str=""
ALGOLIA_APP_ID: str =""
ALGOLIA_KEY: str = ""


