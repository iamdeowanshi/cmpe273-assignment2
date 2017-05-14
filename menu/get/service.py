''' 
Function to get list of menu items 
'''
import boto3
from botocore.exceptions import ClientError

def handler(event, context):
  try:
    table = boto3.resource('dynamodb', region_name='us-west-2').Table('Menu')
    item = table.get_item(Key={'menu_id': event['menu_id']}).get('Item')
    if item == None:
      response = []
      return response
    return item
  except Exception as e:
    return e.message
