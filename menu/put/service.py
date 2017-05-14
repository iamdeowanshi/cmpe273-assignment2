import boto3

def handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource("dynamodb").Table("Menu")
        menu_id = {"menu_id": event["menu_id"]}
        key = event["update"].keys()[0]
        value = event["update"][key]
        table.update_item(Key=menu_id, UpdateExpression="SET #key = :val",ExpressionAttributeNames={"#key":key}, ExpressionAttributeValues={ ":val" :value})
        return "Item with menu id=",menu_id,"updated succesfully"
    except Exception as e:
        return e.message
