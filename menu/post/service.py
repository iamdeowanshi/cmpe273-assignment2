import boto3
import json
from botocore.exceptions import ClientError

def handler(event, context):
  try:
    table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')
# Adding sequence to item
    sequence = '["selection", "size"]'
    event['sequence'] = json.loads(sequence)
    table.put_item(Item=event)
    response = {}
    return response
  except Exception as e:
    return e.message
