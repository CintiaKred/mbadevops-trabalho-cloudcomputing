import json
import boto3
from boto3.dynamodb.conditions import Key
import random
from datetime import datetime
import uuid

dynamodb = boto3.client('eventos-pizzaria')
sqs = boto3.client('sqs')

clientes = ['rafael','maria','teresa', 'tatiane', 'murilo']
pedidos = ['1234','5647','8910','1112','1314','1416']
status = ['pedido feito','montando', 'no forno','saiu do forno', 'embalando','pronto']
peeker = random.SystemRandom()

def processPedido(event, context):
    for event in range(10000):
        dynamodb.put_item({'clientes':str(uuid.uuid4()), 
        'datetime':str(datetime.now()),'pedidos':peeker.choice(pedidos), 'status':peeker.choice(status)})
    print("event: {}".format(json.dumps(event)))
    return True
   
def enviarParaFila(event, context):
    for record in event['Records']:
        evento = json.loads(record['body'])
        if evento['status'] == 'pronto':
            response = sqs.send_message(
                sqs.get_queue_by_name(QueueName='espera-entrega'),
                MessageBody=json.dumps(evento)
            )
    print(f"Mensagem enviada para a fila de entrega: {response}")
    print("event: {}".format(json.dumps(event)))
    return True
    
def entregue(event, context):
    print("event: {}".format(json.dumps(event)))
    return True
    
    return True
