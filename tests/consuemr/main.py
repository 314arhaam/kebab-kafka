import kafka, json
import yml

if __name__ == '__main__':
    with open('../servers-info.yml', 'r') as servers:
        servers_data = yml.safe_load(servers)

    consumer = kafka.KafkaConsumer(
        servers_data['kafka']['broker']['topic'],
        bootstrap_servers = [f"{servers_data['kafka']['broker']['ip']}:{servers_data['kafka']['broker']['port']}"],
        auto_offset_reset = 'latest',
        value_deserializer= lambda x: json.loads(x.decode('utf-8'))
    )

    for msg in consumer:
        print(msg)
