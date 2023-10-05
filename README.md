Trabalho Final da disciplina de Computação em Nuvem

Nessa arquitetura um barramento do eventBridge vai receber todos os eventos de uma pizzaria. Desde o pedido até a entrega. Onde cada um dos eventos deve ser salvo no banco de dados dínamo e apenas os eventos de pizza prontos que devem ser acrescentados a fila SQS que posteriormente devem ser consumidos por outro lambda.

- EventBridge: pizzaria

- DynamoDB: eventos-pizzaria

- SQS: espera-entrega

- Serverless: projeto pizzaria
