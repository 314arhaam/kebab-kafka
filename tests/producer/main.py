import kafka, yaml

if __name__ == '__main__':
    with open('../servers-info.yml', 'r') as servers:
        servers_data = yaml.safe_load(servers)
        
    producer = kafka.KafkaProducer(
        bootstrap_servers = [f"{servers_data['kafka']['broker']['ip']}:{servers_data['kafka']['broker']['port']}"],
        value_serializer = lambda x: json.dumps(x).encode('utf-8')
    )
    
    with open('messages.txt', 'r') as message_file:
        message_list = message_file.read().replace('\n', ' ').split()

    for msg in message_list:
        data = {"msg": msg}
        producer.send(value = data, topic = servers_data['broker']['topic'])

    producer.flush()
