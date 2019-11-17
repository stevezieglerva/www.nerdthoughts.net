---
layout: post
title: AWS Cloudformation Template for CloudTrail 
description: AWS Cloudwatch Cron Expression for every time minutes
---
Here is a Cloudformation template snippet to create a CloudTrail that is used to also record data events for Lambda invocations and S3 operations in addition to the typical management events from CloudTrail.

```
  CloudTrail:
    Type: AWS::CloudTrail::Trail
    DependsOn:
      - SNSTopicPolicy
      - S3BucketPolicy
    Properties: 
        S3BucketName: 
          Ref: S3Bucket
        SnsTopicName: 
          Fn::GetAtt: 
            - SNSTopic
            - TopicName
        IsLogging: true
        EnableLogFileValidation: true
        IncludeGlobalServiceEvents: true
        IsMultiRegionTrail: true
        EventSelectors:
          - DataResources:
              - Type: AWS::Lambda::Function
                Values: 
                  - arn:aws:lambda
          - DataResources:
              - Type: AWS::S3::Object
                Values: 
                  - "arn:aws:s3:::"
```

