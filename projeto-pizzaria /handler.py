import json
import boto3
from boto3.dynamodb.conditions import Key
import random
from datetime import datetime

dynamodb = boto3.client('dynamodb', region_name='us-east-1')
sqs = boto3.client('sqs')

items = [
    {
        "pedido": "1234",
        "status": "no forno",
        "cliente": "tatiane",
        "time": "2021-09-23T15:35:41Z"
    },
    {
        "pedido": "5678",
        "status": "montando",
        "cliente": "murilo",
        "time": "2021-09-23T15:45:00Z"
    },
    {
        "pedido": "9876",
        "status": "pronto",
        "cliente": "teresa",
        "time": "2021-09-23T16:00:15Z"
    }
]

def processPedido(event, context):
    print("event: {}".format(json.dumps(event)))
    for item in items:
        dynamodb.put_item(
                TableName = 'eventos-pizzaria',
                Item = {
                    "pedido": {"S": item["pedido"]},
                    "status": {"S": item["status"]},
                    "cliente": {"S": item["cliente"]},
                    "time": {"S": item["time"]}
                }
            )
        print(f"Item inserido: {item['pedido']} - {item['status']}")
    return True

def enviarParaFilaSQS(event, context):
    print("event: {}".format(json.dumps(event)))
    for record in event['Records']:
        evento = json.loads(record['body'])
        if evento['status'] == 'pronto':
            response = sqs.send_message(
                QueueUrl='https://sqs.us-east-1.amazonaws.com/775117574036/espera-entrega',
                MessageBody=json.dumps(evento)
            )
            print(f"Mensagem enviada para a fila de entrega: {response}")
    return True
    
def pizzaEntregue(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True
