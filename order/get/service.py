# -*- coding: utf-8 -*-
import boto3
import json
from botocore.exceptions import ClientError

def handler(event, context):
  keys = {'order_id'}
  # Fetching order details
  if all(key in event for key in keys):
    try:
      table = boto3.resource('dynamodb', region_name='us-west-2').Table('Order')
    except Exception as e:
      return e.message

    orders = table.get_item(Key={'order_id': event['order_id']}).get('Item')
    return orders
  else:
    return "missing key: order_id"
