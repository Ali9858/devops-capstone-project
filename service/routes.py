"""
Account Service

This microservice handles the lifecycle of Accounts
"""
# pylint: disable=unused-import
from flask import abort, jsonify, make_response, request, url_for
from service.models import Account
from service.common import status  # HTTP Status Codes
from . import app  # Import Flask application


############################################################
# Health Endpoint
############################################################
@app.route("/health")
def health():
    """Health Status"""
    return jsonify(dict(status="OK")), status.HTTP_200_OK


######################################################################
# GET INDEX
######################################################################
@app.route("/")
def index():
    """Root URL response"""
    return (
        jsonify(
            name="Account REST API Service",
            version="1.0",
            # paths=url_for("list_accounts", _external=True),
        ),
        status.HTTP_200_OK,
    )


######################################################################
# CREATE A NEW ACCOUNT
######################################################################
@app.route("/accounts", methods=["POST"])
def create_accounts():
    """
    Creates an Account
    This endpoint will create an Account based the data in the body that is posted
    """
    app.logger.info("Request to create an Account")
    check_content_type("application/json")
    account = Account()
    account.deserialize(request.get_json(silent=True))
    account.create()
    location_url = url_for("get_accounts", account_id=account.id)
    return make_response(
        jsonify(account.serialize()),
        status.HTTP_201_CREATED,
        {"Location": location_url},
    )


######################################################################
# LIST ALL ACCOUNTS
######################################################################

@app.route("/accounts", methods=["GET"])
def list_accounts():
    """Return every account."""
    accounts = Account.all()
    return jsonify([account.serialize() for account in accounts]), status.HTTP_200_OK


######################################################################
# READ AN ACCOUNT
######################################################################

@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    """Return one account by ID."""
    account = Account.find(account_id)
    if account is None:
        abort(status.HTTP_404_NOT_FOUND, f"Account {account_id} was not found")
    return jsonify(account.serialize()), status.HTTP_200_OK


######################################################################
# UPDATE AN EXISTING ACCOUNT
######################################################################

@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    """Replace an existing account."""
    account = Account.find(account_id)
    if account is None:
        abort(status.HTTP_404_NOT_FOUND, f"Account {account_id} was not found")
    check_content_type("application/json")
    account.deserialize(request.get_json(silent=True))
    account.update()
    return jsonify(account.serialize()), status.HTTP_200_OK


######################################################################
# DELETE AN ACCOUNT
######################################################################

@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    """Delete an existing account."""
    account = Account.find(account_id)
    if account is None:
        abort(status.HTTP_404_NOT_FOUND, f"Account {account_id} was not found")
    account.delete()
    return "", status.HTTP_204_NO_CONTENT


######################################################################
#  U T I L I T Y   F U N C T I O N S
######################################################################


def check_content_type(media_type):
    """Checks that the media type is correct"""
    content_type = request.mimetype
    if content_type == media_type:
        return
    app.logger.error("Invalid Content-Type: %s", content_type)
    abort(
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        f"Content-Type must be {media_type}",
    )
