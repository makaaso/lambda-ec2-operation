#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# lambda-ec2-start.py

This repository is AWS Lambda function's upload files.
"""

__authour__ = "masaru.kawabata"
__version__ = 1.3

import botocore
import boto3
import os

def lambda_handler(event, context):
    """ Create Connection """
    try:
        ec2 = boto3.resource('ec2', region_name='ap-northeast-1')
    except:
        print('Connection Error')
        return 1

    """ Get EC2 Instance Info """
    instance = [i for i in ec2.instances.all() for t in i.tags if t["Value"] == os.environ['TAG_NAME']][0]

    """ Start EC2 Instance """
    try:
        instance.start()
    except: 
        print('Start EC2 Instance Error')
        return 1

    return 0

