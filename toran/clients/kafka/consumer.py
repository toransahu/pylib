#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2019-12-19 13:42

"""Kafka Consumer."""

import json
from pprint import pprint

from kafka import KafkaConsumer
from kafka.structs import TopicPartition


__author__ = 'Toran Sahu <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the MIT license'


class KafkaUtil:
    def __init__(self, **kwargs):
        self.__servers = kwargs.pop('servers', None)
        self.__topics = kwargs.pop('topics', None)
        self.__topic = kwargs.pop('topic', None)
        self.__partition = kwargs.pop('partition', 0)
        self.__offset = kwargs.pop('offset', None)
        self.__value_deserializer = kwargs.pop(
            'value_deserializer',
            lambda m: json.loads(m.decode('utf-8'))  # or ascii?
        )

        self.topic_partition = TopicPartition(self.__topic, self.__partition)
        self.assigned_topics = [self.topic_partition, ]

        self.consumer = KafkaConsumer(
            bootstrap_servers=self.__servers,
            # auto_offset_reset='earliest',
            # auto_offset_reset='latest',
            enable_auto_commit=False,
            consumer_timeout_ms=1000,  # StopIteration if no message after 1sec
            group_id="toran's_kafka_cli",
            value_deserializer=self.__value_deserializer,
            # api_version=(0, 10, 1)
        )
        self.consumer.assign(self.assigned_topics)

        # start from an offset
        if self.__offset:
            self.consumer.seek(partition=self.topic_partition, offset=self.__offset)

BROKER_HOSTS = ["11.128.4.169"]
BROKER_PORTS = ["9093", "9094"]

def run_consumer(env, topic):
    try:
        util = KafkaUtil(
            topic="postdb_v3",
            servers=[f"{host}:{port}" for host in BROKER_HOSTS for port in BROKER_PORTS][0],
            # offset=356183784,
        )
        for record in util.consumer:
            pprint(record.value)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    env = 'production'
    topic = 'client-events'
    run_consumer(env, topic)
