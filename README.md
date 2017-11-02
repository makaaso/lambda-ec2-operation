# lambda-ec2-operation.py

This repository is AWS Lambda function's upload files.

## Language

- python3.6.2

## Package

- botocore
- boto3
- os

## How To Use

### 1.clone git repository

```
git clone https://github.com/makaaso/lambda-ec2-operation.git
cd lambda-ec2-operation
```

### 2.prepare upload zip file

```
pip install botocore -t ./ --upgrade
pip install boto3 -t ./ --upgrade
zip -r ../lambda-ec2-operation.zip .
```

### 3.set environment variables on AWS Console

```
TAG_NAME : <TAG NAME>
```

