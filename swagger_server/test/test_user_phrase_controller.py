# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user_phrase import UserPhrase  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserPhraseController(BaseTestCase):
    """UserPhraseController integration test stubs"""

    def test_delete_user_phrase_db(self):
        """Test case for delete_user_phrase_db

        Delete a userPhrase from Database
        """
        response = self.client.open(
            '/v1/userPhrase/database/{userPhraseId}'.format(user_phrase_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user_phrase_s3(self):
        """Test case for delete_user_phrase_s3

        Delete a userPhrase from S3
        """
        response = self.client.open(
            '/v1/userPhrase/s3/{userPhraseId}'.format(user_phrase_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_user_phrase_database(self):
        """Test case for edit_user_phrase_database

        Edit a userPhrase to Database
        """
        body = UserPhrase()
        response = self.client.open(
            '/v1/userPhrase/database',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_user_phrase_s3(self):
        """Test case for edit_user_phrase_s3

        Edits a userPhrase in S3
        """
        body = UserPhrase()
        response = self.client.open(
            '/v1/userPhrase/s3',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_phrase_db(self):
        """Test case for get_user_phrase_db

        Gets a userPhrase by ID from Database
        """
        response = self.client.open(
            '/v1/userPhrase/database/{userPhraseId}'.format(user_phrase_id=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_phrase_s3(self):
        """Test case for get_user_phrase_s3

        Get a userPhrase by ID from S3
        """
        response = self.client.open(
            '/v1/userPhrase/s3/{userPhraseId}'.format(user_phrase_id=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_user_phrase_database(self):
        """Test case for save_user_phrase_database

        Saves a userPhrase to Database
        """
        body = UserPhrase()
        response = self.client.open(
            '/v1/userPhrase/database',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_save_user_phrase_s3(self):
        """Test case for save_user_phrase_s3

        Saves a userPhrase to S3
        """
        body = UserPhrase()
        response = self.client.open(
            '/v1/userPhrase/s3',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
