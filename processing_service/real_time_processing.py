from kafka import KafkaConsumer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

KAFKA_SERVER = "localhost:9092"
TOPIC = "financial_data"

def process_stream():
    sc = SparkContext("local[2]", "RealTimeProcessing")
    ssc = StreamingContext(sc, 10)

    # Подключение к Kafka
    consumer = KafkaConsumer(TOPIC, bootstrap_servers=[KAFKA_SERVER])

    def process_data(rdd):
        if not rdd.isEmpty():
            print("Processing data:", rdd.collect())

    stream = ssc.socketTextStream("localhost", 9999)
    stream.foreachRDD(process_data)
    ssc.start()
    ssc.awaitTermination()

if __name__ == "__main__":
    process_stream()
