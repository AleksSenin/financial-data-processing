import subprocess
import time

# Определяем сервисы и их файлы запуска
services = {
    "Data Ingestion Service": "ingestion_service/data_collector.py",
    "Real-Time Processing Service": "processing_service/real_time_processing.py",
    "Storage Service (Cassandra)": "storage_service/cassandra_connector.py",
    "Storage Service (PostgreSQL)": "storage_service/postgresql_connector.py",
    "Data Analysis Service": "analysis_service/machine_learning.py",
    "Data Visualization Service": "visualization_service/web_interface.py",
}

processes = []  # Список для хранения запущенных процессов

try:
    # Запускаем каждый сервис в отдельном процессе
    for name, script in services.items():
        print(f"🚀 Starting {name} ({script})...")
        process = subprocess.Popen(["python", script])
        processes.append(process)
        time.sleep(2)  # Короткая пауза между запусками (можно убрать)

    print("\n✅ All services started successfully!")
    
    # Ожидание завершения всех процессов (чтобы main.py не закрылся сразу)
    for process in processes:
        process.wait()

except KeyboardInterrupt:
    print("\n🛑 Stopping all services...")
    for process in processes:
        process.terminate()
    print("✅ Services stopped.")
