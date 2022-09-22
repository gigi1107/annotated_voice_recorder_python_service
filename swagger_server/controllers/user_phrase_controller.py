import connexion
import six
import boto3
import logging

from datetime import datetime


from swagger_server.models.user_phrase import UserPhrase  # noqa: E501
from swagger_server import util

s3_client = boto3.client('s3')
logger = logging.getLogger(__name__)



def delete_user_phrase_db(user_phrase_id):  # noqa: E501
    """Delete a userPhrase from Database

     # noqa: E501

    :param user_phrase_id: The userPhrase Id of the userPhrase you want to delete from the Database
    :type user_phrase_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_user_phrase_s3(user_phrase_id):  # noqa: E501
    """Delete a userPhrase from S3

     # noqa: E501

    :param user_phrase_id: The userPhraseID of the userPhrase you want to delete from S3
    :type user_phrase_id: int

    :rtype: None
    """
    return 'do some magic!'


def edit_user_phrase_database(body):  # noqa: E501
    """Edit a userPhrase to Database

     # noqa: E501

    :param body: UserPhrase object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserPhrase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_user_phrase_s3(body):  # noqa: E501
    """Edits a userPhrase in S3

     # noqa: E501

    :param body: UserPhrase object
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = UserPhrase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_user_phrase_db(user_phrase_id):  # noqa: E501
    """Gets a userPhrase by ID from Database

     # noqa: E501

    :param user_phrase_id: The userPhrase Id of the userPhrase you want to get from the Database
    :type user_phrase_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_user_phrase_s3(user_phrase_id):  # noqa: E501
    """Get a userPhrase by ID from S3

     # noqa: E501

    :param user_phrase_id: The userPhraseID of the userPhrase you want to get from S3
    :type user_phrase_id: int

    :rtype: None
    """
    return 'do some magic!'


def save_user_phrase_database(body):  # noqa: E501
    """Saves a userPhrase to Database

     # noqa: E501

    :param body: UserPhrase object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserPhrase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def save_user_phrase_s3(body):  # noqa: E501
    """Saves a userPhrase to S3

     # noqa: E501

    :param body: UserPhrase object
    :type body: dict | bytes

    :rtype: str
    """
    print(str(body))

    if not connexion.request.is_json:
        return
    
    body = UserPhrase.from_dict(connexion.request.get_json())  # noqa: E501
    logger.debug("saving file to s3 bucket ")
    recording = body.recording
    recording_series = body.recording_series
    datetime_now = datetime.today()
    # key = 'recorded/'+recording_series+'/'+phrase_id + '_' + user_id+ "_"+ datetime_now.strftime("%Y-%m-%d_%H:%M:%S")+".txt"
    key = 'recorded/gigiKeyTest.txt'
    logger.debug("saving word {0} for user {1}".format(body.phrase.id, body.user.id))
    result = s3_client.put_object(
        Body=recording, 
        Bucket='makah-asr', 
        Key=key)
    logger.debug("S3 Key: {0}".format(key))
    ## TODO should actually return path to this file in S3
    return key
