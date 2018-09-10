# csvapp
Build on flask micro-framework
On application bootstrap, loads csv file(assests/numbers.csv) into redis DB, then exposes a GET api with endpoint /v1/csvdata/<key> to get details of the csv file being loaded.

Prerequisities with Docker
==========================
install docker
install docker-compose
cd <project-folder, e.g.,csvapp>
run docker-compose up --build
hit http://localhost:8080/v1/csvdata/one

Prerequisities without Docker
=============================
install python 2.7
install redis
run redis-server
cd <project-folder, e.g.,csvapp>
configure config.py(set host/port for app & redis)
run python app.py
hit http://localhost:8080/v1/csvdata/ten

Test cases
==========
run py.test
