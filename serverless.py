service: pizzaria-project

frameworkVersion: '3'

provider:
    name: aws
    runtime: python3.8
    region: 'us-east-1'
    iam:
        role: !Sub arn:aws:iam::${AWS::AccountId}:role/LabRole
    eventBridge:
        useCloudFormation: true
        
functions:
    processPedido:
        handler: handler.processPedidoHandler
        events:
            - eventBridge:
                eventBus:
                    - arn:aws:events:${aws:region}:${aws:accountId}:event-bus/pizzaria
                pattern:
                    source:
                        - com.pizza.status
            - stream:
                type: dynamodb
                arn: arn:aws:dynamodb:us-east-1:940915789164:table/eventos-pizzaria/stream/2023-10-15T01:38:35.724
                enabled: true
    enviarParaFila:
        handler: handler.enviarParaFilaHandler
        events:
            - eventBridge:
                eventBus:
                    - arn:aws:events:${aws:region}:${aws:accountId}:event-bus/pizzaria
                pattern:
                    detail-type:
                        - Alteracao Pizza
                    source:
                        - com.pizza.status
                    detail:
                        status:
                            - pronto
    entregue:
        handler: handler.entregueHandler
        events:
            - eventBridge:
                eventBus:
                    - arn:aws:events:${aws:region}:${aws:accountId}:event-bus/pizzaria
                pattern:
                    detail-type:
                        - Alteracao Pizza
                    source:
                        - com.pizza.status
                    detail:
                        status:
                            - pronto
