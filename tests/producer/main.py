import kafka, json
import yml

if __name__ == '__main__':
    with open('../servers-info.yml', 'r') as servers:
        servers_data = yml.safe_load(servers)
        
    producer = kafka.KafkaProducer(
        bootstrap_servers = [f"{servers_data['kafka']['broker']['ip']}:{servers_data['kafka']['broker']['port']}"],
        value_serializer = lambda x: json.dumps(x).encode('utf-8')
    )
    
    with open('messages.txt', 'r') as message_file:
        message_list = message_file.read().replace('\n', ' ').split()

    print(message_list)

    for msg in message_list:
        data = {"msg": msg}
        producer.send(value = data, topic = servers_data["kafka"]['broker']['topic'])
        producer.flush()
        print(f"message sent {data}")
