# databricks-sql-query

Lambda function to query Databricks SQL.

This function uses databricks-sql-connector to connect to a running Databricks SQL endpoint, submit a SQL query and fetch the results. 

IMPORTANT LIMITATION: Note that this function will not on functions that are behind a network firewall. 

Since the databricks-sql-connector library is too large for a traditional chalice/lambda application, it is deployed using a docker container.

IMPORTANT NOTE: You must build the docker image on a Linux machine. If you build it on a Mac with an M1/M2 chip, it is incompatible with AWS Lambda, and you will get "exec format error"

Contents of the project are as follows:

1. [app.py](app.py)
2. [Dockerfile](Dockerfile)
3. [requirements.txt](requirements.txt)
4. [1_build.sh](1_build.sh)
5. [2_login.sh](2_login.sh)
6. [3_create_repository.sh](3_create_repository.sh)
7. [4_push.sh](4_push.sh)
8. [5_create_function.sh](5_create_function.sh)
9. [5_update_function.sh](5_update_function.sh)

The project was built using the [lambda-docker boilerplate](https://github.com/vbalasu/lambda-docker)