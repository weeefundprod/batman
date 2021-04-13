# myenv.py (à configurer)
password =
db =
url =
username =
**Installation des modules et packages**
sudo apt-get install v4l-utils
**Installer sqlite**
sudo apt-get install sqlite3 libsqlite3-dev
**Installer sqliteBrowser**
sudo apt-get install sqlitebrowser
 ATTENTION ne pas ouvrir sqlitebrowser pendant une requête!!!!!

# INSTALLER PIP POUR PYTHON2**


# INSTALLER SHORTUUID FOR PYTHON2**

wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
sudo python2.7 get-pip.py
python2 -m pip install shortuuid

# si erreur fichier non trouvé lors du lancement du script**
update working_directory in launch_script.sh

# Installation Anaconda vraiment si vous décidez de l'utiliser**
Prendre la dernère version d'anaconda: https://docs.anaconda.com/anaconda/user-guide/getting-started/

sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

check key hash : sha256sum /home/lisa/Téléchargements/Anaconda2-2019.10-Linux-ppc64le.sh 0521743829c1b3c301542a20fa0daecda20ee85a69e57b5751a07c629001587b

bash [path-to-anaconda.sh]

say yes to licence terms and yes to init conda

source ~/.bashrc

Conda va nous aider à configurer les environnements: conda create --name py2 python=2.7 conda activate py2 source ~/anaconda3/bin/activate root