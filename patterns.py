"""
Все три шаблона проектирования в одном файле:
1. Singleton (Порождающий)
2. Adapter (Структурный)
3. Observer (Поведенческий)
"""

# ====== 1. SINGLETON (Порождающий) ======
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        return "Database connected"

    def query(self, sql):
        return f"Executed: {sql}"


# ====== 2. ADAPTER (Структурный) ======
class OldSystem:
    def legacy_request(self):
        return "Old system response"

class ModernSystem:
    def __init__(self, adapter):
        self.adapter = adapter

    def make_request(self):
        return self.adapter.request()

class OldSystemAdapter:
    def __init__(self):
        self.old_system = OldSystem()

    def request(self):
        old_response = self.old_system.legacy_request()
        return f"Adapted: {old_response}"


# ====== 3. OBSERVER (Поведенческий) ======
class NewsPublisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def publish_news(self, news):
        print(f" Publishing: {news}")
        for subscriber in self._subscribers:
            subscriber.update(news)

class EmailSubscriber:
    def __init__(self, email):
        self.email = email

    def update(self, news):
        print(f" Email to {self.email}: {news}")

class SMSSubscriber:
    def __init__(self, phone):
        self.phone = phone

    def update(self, news):
        print(f" SMS to {self.phone}: {news}")
