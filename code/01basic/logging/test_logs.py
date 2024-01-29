# Logging = Capturing details , Which are useful while debugging and
# show the user details about execution of program.

# features: Warning to users
# Information to the users
# Error, Critical Errors to the user.

import logging


def test_print_the_logs():
    Logger = logging.getLogger(__name__)
    # Intentional logging to user
    Logger.info("This is information logs")
    Logger.warning("This is warning logs")
    Logger.error("This is error logs")
    Logger.critical("This is critical logs")
