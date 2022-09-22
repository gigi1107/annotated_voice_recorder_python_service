import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """Creates user with given info

     # noqa: E501

    :param body: User object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(user_id):  # noqa: E501
    """Delete an existing user

     # noqa: E501

    :param user_id: The userId of the user you want to delete from the Database
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def edit_user(body):  # noqa: E501
    """Edits user with given info

     # noqa: E501

    :param body: User object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_user(body):  # noqa: E501
    """Get user

     # noqa: E501

    :param body: User object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
