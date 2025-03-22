# Caphca

## Instruction

## Configure `hosts` file

### Install kafka

To install kafka on the broker server as the localhost:

```ini
[broker]
localhost ansible_connection=local
```

or as a `*.yml` file

```yaml
all:
  children:
    broker:
      hosts:
        localhost:
          ansible_host: localhost
```

### Deploy tests

```yaml
all:
  children:
    kafka_broker:
      hosts:
        master:
          ansible_host: localhost
          ansible_user: root

    kafka_producer:
      hosts:
        test_producer:
          ansible_host: PRODUCER_SERVER_IP
          ansible_user: root
          ansible_ssh_private_key_file: "/path/to/private_key"

    kafka_consumer:
      hosts:
        test_consumer:
          ansible_host: CONSUMER_SERVER_IP
          ansible_user: root
          ansible_ssh_private_key_file: "/path/to/private_key"
```

In whole project `hosts` and `hosts.yml` are ignored for the security reasons.

## Run

```sh
sudo ansible-playbook -i inventory/hosts.yml kafka-playbook.yml
```
