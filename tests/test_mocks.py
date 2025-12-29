"""
Тесты с использованием Mock-объектов
"""
from unittest.mock import Mock, patch
from patterns import DatabaseConnection, NewsPublisher

def test_singleton_with_mock():
    db = DatabaseConnection()

    with patch.object(db, 'connect', return_value="Mocked Connection"):
        result = db.connect()
        assert result == "Mocked Connection"
        db.connect.assert_called_once()

def test_observer_with_mocks():
    publisher = NewsPublisher()
    mock_subscriber = Mock()

    publisher.subscribe(mock_subscriber)
    publisher.publish_news("Mocked news")

    mock_subscriber.update.assert_called_once_with("Mocked news")
