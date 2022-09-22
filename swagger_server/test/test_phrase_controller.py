# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.phrase import Phrase  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPhraseController(BaseTestCase):
    """PhraseController integration test stubs"""

    def test_add_phrase(self):
        """Test case for add_phrase

        Add a new phrase to the Database
        """
        body = Phrase()
        response = self.client.open(
            '/v1/phrase',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_phrase(self):
        """Test case for delete_phrase

        Delete an existing phrase
        """
        response = self.client.open(
            '/v1/phrase/{phraseId}'.format(phrase_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_phrase(self):
        """Test case for get_phrase

        Retrieves a given number of phrases from the Database
        """
        response = self.client.open(
            '/v1/phrase/{numberPhrases}'.format(number_phrases=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_phrase(self):
        """Test case for update_phrase

        Update an existing phrase
        """
        body = Phrase()
        response = self.client.open(
            '/v1/phrase',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
