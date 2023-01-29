# lambda-docker

Boilerplate project containing build and deployment scripts for a Python docker container image launched to AWS Lambda. This includes the steps to build and upload the image to ECR and create/update a Lambda function based on it.

Note that this supersedes the [lambda-container](https://github.com/vbalasu/lambda-container) template.

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
