# serverless-sample-app
severless sample application which uses 'localstack' and 'seerless-local'

1. Run the LocalStack container in the background with:
    $ docker-compose up -d
    
    Follow the logs with:
    $ docker logs -f localstack
    
    Till you see:
    ...
    Waiting for all LocalStack services to be ready
    Ready.

2. Install localstack serverless plugin

    npm install -g serverless
    
    npm install --save-dev serverless-localstack
    
    npm install serverless-python-requirements

3. Deploy the lambda

    to localstack : serverless deploy   
    

reference: https://github.com/ciaranevans/localstack_and_pytest_1

https://github.com/ubaniabalogun/serverless-package-python-functions


https://medium.com/uk-hydrographic-office/developing-and-testing-lambdas-with-pytest-and-localstack-21a111b7f6e8

localstack : https://hub.docker.com/r/localstack/localstack

serverless-localstack: https://github.com/localstack/serverless-localstack

https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb#using-the-quick-start-template
https://www.serverless.com/blog/serverless-python-packaging

https://www.serverlessops.io/blog/aws-lambda-serverless-development-workflow-part2-testing-debugging


https://localstack.cloud/


For s3 unit testing:  https://github.com/vincentclaes/serverless_data_pipeline_example

sample-terraform-locastack
https://github.com/UlisesGascon/sample-terraform-localstack
