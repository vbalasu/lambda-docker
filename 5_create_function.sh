aws lambda create-function --region us-west-2 --function-name hello-world \
    --package-type Image  \
    --code ImageUri=997819012307.dkr.ecr.us-west-2.amazonaws.com/hello-world:latest   \
    --role arn:aws:iam::997819012307:role/psa-reinvent2021-demo-functionRole-W27EZJ2S2NK9
