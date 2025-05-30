import unittest
from unittest.mock import patch, AsyncMock
import asyncio
from main import main
import glob, os

# test_main.py


# Absolute import since parent has no __init__.py

class TestMain(unittest.IsolatedAsyncioTestCase):
    @patch('main.send_message', new_callable=AsyncMock)
    @patch('main.translator')
    @patch('main.fetch_articles')
    async def test_main_real_html_and_send_message(
        self, mock_fetch_articles, mock_translator, mock_send_message
    ):
        # Arrange
        mock_fetch_articles.return_value = [
            {'heading': 'Test Heading', 'paragraph': 'Test Paragraph.\nThis is a test.\nAnother line.'},
        ]
        mock_translator.side_effect = lambda text: f"dummy:{text}"

        # Remove old HTML files before test
        for f in glob.glob("translated_news/*.html"):
            os.remove(f)

        # Act
        await main()

        # Assert
        html_files = glob.glob("translated_news/*.html")
        self.assertTrue(len(html_files) > 0, "No HTML file was generated.")
        self.assertTrue(mock_send_message.await_count == 1, "send_message was not called once.")

        with open(html_files[0], encoding="utf-8") as f:
            content = f.read()
            self.assertIn("dummy:", content)

    # @patch('main.send_message', new_callable=AsyncMock)
    # @patch('main.translator')
    # @patch('main.fetch_articles')
    # async def test_main_no_articles(
    #     self, mock_fetch_articles, mock_translator, mock_send_message
    # ):
    #     # Arrange
    #     mock_fetch_articles.return_value = []
    #     mock_translator.side_effect = lambda text: f"dummy:{text}"

    #     # Remove old HTML files before test
    #     for f in glob.glob("translated_news/*.html"):
    #         os.remove(f)

    #     # Act
    #     await main()

    #     # Assert
    #     html_files = glob.glob("translated_news/*.html")
    #     self.assertTrue(len(html_files) == 0, "HTML file should not be generated when no articles.")
    #     self.assertTrue(mock_send_message.await_count == 1, "send_message was not called once.")

if __name__ == "__main__":
    unittest.main()