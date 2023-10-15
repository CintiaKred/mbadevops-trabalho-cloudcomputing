import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
import uuid

dao = BaseDAO('eventos-pizzaria')

cliente = ['rafael','pedro','teresa','natalia', 'eduardo']
pedido = ['1234','5678', '9101','1213', '1415','1617']
status = ['pedido feito','montando', 'no forno','saiu do forno', 'embalando','pronto']
peeker = random.SystemRandom()


for i in range(10000):
    dao.put_item({'cliente':str(uuid.uuid4()), 
        'datetime':str(datetime.now()),'pedido':peeker.choice(pedido), 'status':peeker.choice(status)})
