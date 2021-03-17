steps to run postgres in cookie-cutter django:-


1- install



# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql


2-enable the service

sudo systemctl enable postgresql

service postgresql status

 sudo service postgresql start

sudo service postgresql status

3- after that you need to create new postgresql user and give it the premission to create DB.
to create a user you need to do using the postgres user. so

sudo -u postgres -i

you will go to postgres user

then, type

psql

you will go to postgres CL

CREATE USER POLYSOULZ

i think you need to setup a password afte  that.
create user polysoulz password "adsadsadasd";

then give it the premission

alter user polysoulz createdb;

now you can create the database from the normal CL.


4- another error
now when you run python3 manage.py makemigrations, you will face a problem with authintcation.
seems like the way we set our polysoulz password was wrong.

sudo -u postgres psql -c "ALTER USER polysoulz
PASSWORD '8055465123';"

run this command and you will be good mate.
have fun dude this toke me like 324234 hours to solve.
