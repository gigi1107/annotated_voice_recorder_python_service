import connexion
import six

from swagger_server.models.phrase import Phrase  # noqa: E501
from swagger_server import util


def add_phrase(body):  # noqa: E501
    """Add a new phrase to the Database

     # noqa: E501

    :param body: Phrase object that needs to be added to the Database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Phrase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_phrase(phrase_id):  # noqa: E501
    """Delete an existing phrase

     # noqa: E501

    :param phrase_id: The phraseId of the phrase you want to delete from the Database
    :type phrase_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_phrase(number_phrases):  # noqa: E501
    """Retrieves a given number of phrases from the Database

    Number should be greater than 0. # noqa: E501

    :param number_phrases: The number(amount) of phrases to retrieve from the Database
    :type number_phrases: int

    :rtype: List[Phrase]
    """
    return 'do some magic!'


def update_phrase(body):  # noqa: E501
    """Update an existing phrase

     # noqa: E501

    :param body: Phrase object that needs to be added to the Database
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Phrase.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
