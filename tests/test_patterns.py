"""
TDD-тесты для всех трех паттернов
"""
import pytest
from patterns import (
    DatabaseConnection,
    OldSystemAdapter, ModernSystem,
    NewsPublisher, EmailSubscriber, SMSSubscriber
)

# === TESTS FOR SINGLETON ===
def test_singleton_instance():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2

def test_singleton_methods():
    db = DatabaseConnection()
    assert db.connect() == "Database connected"
    assert "SELECT" in db.query("SELECT * FROM users")

# === TESTS FOR ADAPTER ===
def test_adapter():
    adapter = OldSystemAdapter()
    result = adapter.request()
    assert "Adapted: Old system response" in result

def test_modern_system_with_adapter():
    adapter = OldSystemAdapter()
    modern = ModernSystem(adapter)
    assert "Adapted:" in modern.make_request()

# === TESTS FOR OBSERVER ===
def test_observer_subscribe():
    publisher = NewsPublisher()
    subscriber = EmailSubscriber("test@test.com")
    publisher.subscribe(subscriber)
    assert subscriber in publisher._subscribers

def test_observer_publish(capsys):
    publisher = NewsPublisher()
    subscriber = EmailSubscriber("test@test.com")
    publisher.subscribe(subscriber)

    publisher.publish_news("Test news")

    captured = capsys.readouterr()
    assert "Test news" in captured.out
    assert "test@test.com" in captured.out
