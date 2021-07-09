## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

###  distribution continue et déploiement continu (sur linux UBUNTU)

Installation de Docker :

- `sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release`
- `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg`
- `echo \
- "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
- $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
- `sudo apt-get update`
- `sudo apt-get install docker-ce docker-ce-cli containerd.io`
- `sudo usermod -aG docker your-user`
- `sudo reboot`

Ajout d'un compte sur Dockerhub :

- `https://hub.docker.com/ avec la création d'un DOCKER_ID et un DOCKER_PASSWORD`
- `docker login (avec DOCKER_ID et DOCKER_PASSWORD)`

Création d'un conteneur :

- `cd /path/to/OC_P13`
- `docker build -t DOCKER_ID/oc-lettings/web .`
- `docker tag DOCKER_ID/oc-lettings/web DOCKER_ID/oc-lettings:latest`

Lancement du conteneur :

- `cd /path/to/OC_P13`
- `docker run -d -e "PORT=8000" -e "DEBUG=1" -p 8000:8000 DOCKER_ID/oc-lettings`
- Verification du lancement du conteneur et récupération du CONTAINER_ID `docker ps`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
- arrêt du conteneur `docker stop CONTAINER_ID`

Ajout du docker sur Dockerhub :

- `docker push DOCKER_ID/oc-lettings:latest`

Ajout du projet sur github

- création d'un repository sur le compte github exemple 'oc-lettings'
- `cd /path/to/OC_P13`
- `git remote add remote-oc-lettings https://github.com/GITHUB_ID/oc-lettings.git`
- `git push remote-oc-lettings avec le GITHUB_ID et GITHUB_PASSWORD`

Ajout d'un compte Heroku : 

- `https://signup.heroku.com/` avec une adresse mail et un password

Installation de heroku

- `sudo snap install --classic heroku`

Ajout de l'application sur Heroku :

- `cd /path/to/OC_P13`
- Dans oc_lettings_site_settings.py :
  changer `ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'oc-lettings-290.herokuapp.com']`
  en `ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'oc-lettings-x.herokuapp.com']`
- `heroku login` (connexion avec le navigateur web)
- `heroku create oc-lettings-x --region eu` x correspond a un chiffre non utilisé
- `heroku config:set SECRET_KEY='(50 chiffres et lettres et caractères spéciaux aléatoires)' -a oc-lettings-x`
- `heroku container:login`
- `docker build -t registry.heroku.com/oc-lettings-x/web .`
- `docker push registry.heroku.com/oc-lettings-x/web`
- `heroku container:release -a oc-lettings-x web`
- Verifier le fonctionnement de l'application sur `https://oc-lettings-x.herokuapp.com/`

Ajout de l'application Sentry :

- `https://sentry.io/signup/` connexion avec github
- Creer un projet avec Django
- Récupérer le dsn ('https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.ingest.sentry.io/xxxxxxx')
- `cd /path/to/OC_P13`
- `heroku config:set SENTRY_DSN='https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.ingest.sentry.io/xxxxxxx' -a oc-lettings-x`
- Test d'une erreur `https://oc-lettings-x.herokuapp.com/sentry-debug/`
- Voir l'erreur `https://sentry.io/organizations/GITHUB_ID/issues/`

Ajout d'un compte Circleci :

- `https://circleci.com/signup/` Connexion avec le compte github et autoriser l'application circleci

Selectionner le projet sur Circleci

- `cd /path/to/OC_P13`
- `git checkout issue_test`
- `git push remote-oc-lettings` connexion avec GITHUB_ID et GITHUB_PASSWORD
- `https://app.circleci.com/projects/`
- `Set Up Project`
- selectionner `If you already have .circleci/config.yml in your repo, select the branch it's on to start building`
- branch `issue_test`
- le pipeline va se lancer
- `https://dashboard.heroku.com/account` récupérer le API_KEY
- ajouter dans `Project settings` => `Environment Variables` => `Environment Variables` :
    - Name: DOCKER_PASS, Value: DOCKER_PASSWORD
    - Name: DOCKER_USER, Value: DOCKER_ID
    - Name: HEROKU_API_KEY, Value: API_KEY
    - Name: HEROKU_APP_NAME, Value: oc-lettings-x
- A chaque git push de la branche master, l'application est testé, un conteneur est crée avec un tag correspondant au hash du commit
  et stocké sur dockerhub et l'application sur Heroku est mise a jour
- A chaque git push de la branche issue_test, l'application est testé   

Pour des raisons de sécurité, il est préférable d'utiliser la double authentification sur Github, Dockerhub et Heroku.
Sur Github, le remote sur le repository peut s'effectuer avec une clé SSH.
Sur Dockerhub, il est preferable d'utiliser les access_tokens pour les authentifications (obligatoire avec le 2FA).