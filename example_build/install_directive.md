Install MyAptlyRepo
====================


  To Install the MyAptlyRepo Run the following command
  
  `curl -sSL http://my.aptly.repo/install_repo.deb.sh | sudo bash`


this will install the repository to your apt/sources.list and add the gpg key for the server

______________________________________
**Install a Package**

in order to install a package run

`sudo apt-get install -o Dpkg::Options::="--force-overwrite" <packagename>[=<version>]`

e.g. `sudo apt-get install -o Dpkg::Options::="--force-overwrite" awesomedeb=1.0.391.84.gab65e`

__________________________________________
**List Available Versions**

in order to list the available versions of a package run

`apt-cache madison <packagename>`

e.g.`apt-cache madison awesomedeb`
