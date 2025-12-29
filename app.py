"""
Демонстрация работы всех трех паттернов
"""
from patterns import (
    DatabaseConnection,
    OldSystemAdapter, ModernSystem,
    NewsPublisher, EmailSubscriber, SMSSubscriber
)

def demo_singleton():
    print("=== SINGLETON ===")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Same instance: {db1 is db2}")
    print(f"DB1: {db1.connect()}")
    print(f"DB2 query: {db2.query('SELECT * FROM users')}")
    print()

def demo_adapter():
    print("=== ADAPTER ===")
    adapter = OldSystemAdapter()
    modern = ModernSystem(adapter)
    result = modern.make_request()
    print(f"Result: {result}")
    print()

def demo_observer():
    print("=== OBSERVER ===")
    publisher = NewsPublisher()

    email_sub = EmailSubscriber("user@example.com")
    sms_sub = SMSSubscriber("+79001234567")

    publisher.subscribe(email_sub)
    publisher.subscribe(sms_sub)

    publisher.publish_news("Python 3.12 released!")

    publisher.unsubscribe(email_sub)
    publisher.publish_news("AI conference starts tomorrow")
    print()

if __name__ == "__main__":
    demo_singleton()
    demo_adapter()
    demo_observer()
    print("All patterns demonstrated!")
