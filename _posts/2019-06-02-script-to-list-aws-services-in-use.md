---
layout: post
title: Script To List AWS Services In Use
description: script that uses the AWS CLI to list basic information about the AWS services in use
---
I recently created [aws-account-summary](https://github.com/icfnext/aws-account-summary) to list out basic information on the AWS services in use by an account. It comes in handy when trying to confirm current or newly created infrastructure. I went with quick-and-dirty approach of just finding text in AWS CLI output. It's suprisingly useful for such little code.

ddd zieglerddk

### Sample Output
```
Sun 06/02/2019  8:47:59.33
*
*
* API Gateway
            "name": "TestAPI",
*
*
* Cloudfront
                            "DomainName": "jekyll-site-1.s3.amazonaws.com",
                "DomainName": "d1xau5ri19gn0n.cloudfront.net",
                            "DomainName": "www.nerdthoughts.net.s3.amazonaws.com",
                "DomainName": "d20ip71gqm0ltw.cloudfront.net",
*
*
* Cloudwatch
            "logGroupName": "/aws/aes/domains/ziegler-es/application-logs",
            "logGroupName": "/aws/codebuild/DocumentLambdas",
            "logGroupName": "/aws/codebuild/NCStateFair",
            "logGroupName": "/aws/codebuild/nerdthoughts",
            "logGroupName": "/aws/lambda/aws-code-index-bulk-load",
            "logGroupName": "/aws/lambda/aws-code-index-escape-files",
            "logGroupName": "/aws/lambda/aws-code-index-escape-files-2",
            "logGroupName": "/aws/lambda/aws-code-index-format-files",
            "logGroupName": "/aws/lambda/aws-code-index-stream-bulk-load",
            "logGroupName": "/aws/lambda/aws-dynamodb-to-es-bulk",
            "logGroupName": "/aws/lambda/aws-lnkchk-cache-stream",
            "logGroupName": "/aws/lambda/aws-lnkchk-dynamodb-stream-to-es",
            "logGroupName": "/aws/lambda/aws-lnkchk-extract-links",
            "logGroupName": "/aws/lambda/aws-lnkchk-log-stream-to-es",
            "logGroupName": "/aws/lambda/aws-lnkchk-queue-stream",
            "logGroupName": "/aws/lambda/aws-lnkchk-start",
            "logGroupName": "/aws/lambda/aws-read-s3-es-events-in-chunks",
            "logGroupName": "/aws/lambda/aws-s3-to-es",
            "logGroupName": "/aws/lambda/aws-tika-app",
*
*
* Running EC2 instance
                    "KeyName": "linux",
*
*
* Elasticsearch Domains
    "DomainNames": [
            "DomainName": "my-es"
*
*
* Firehose
{
    "DeliveryStreamNames": [
        "code-index-files-csv",
        "code-index-files-es-bulk",
        "code-index-logs"
    ],
    "HasMoreDeliveryStreams": false
}
*
*
* Lambdas
            "FunctionName": "aws-lnkchk-start",
            "FunctionName": "aws-code-index-escape-files",
            "FunctionName": "BlogBuild",
            "FunctionName": "nc-state-fair-food-finder",
            "FunctionName": "aws-read-s3-es-events-in-chunks",
            "FunctionName": "aws-lnkchk-dynamodb-stream-to-es",
            "FunctionName": "aws-dynamodb-to-es-bulk",
            "FunctionName": "ephemeral",
            "FunctionName": "aws-code-index-format-files",
                    "type": "code-index"
            "FunctionName": "aws-s3-to-es",
            "FunctionName": "BingSpellcheck",
            "FunctionName": "aws-lnkchk-extract-links",
            "FunctionName": "aws-code-index-bulk-load",
            "FunctionName": "aws-code-index-stream-bulk-load",
            "FunctionName": "aws-lnkchk-log-stream-to-es",
            "FunctionName": "aws-tika-app",
                    "type": "tika"
*
*
* RDS
*
*
* S3 Buckets
            "Name": "aws-s3-to-es",
            "Name": "aws-tika-app-code",
            "Name": "code-index",
            "Name": "code-index-2",
            "Name": "code-index-3",
            "Name": "link-checker",
            "Name": "lnkchk",
            "Name": "lnkchk-100-pages",
            "Name": "lnkchk-complex-site-integration",
            "Name": "lnkchk-simple-site-integration",
*
*
* Sagemaker
*
*
* Secretsmanager
*
*
* SQS
{
    "QueueUrls": [
        "https://queue.amazonaws.com/9999/code-index",
        "https://queue.amazonaws.com/9999/code-index.fifo",
        "https://queue.amazonaws.com/9999/link-checker"
    ]
}
*
*
* Users
            "UserName": "joesmith"

```