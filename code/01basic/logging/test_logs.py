# Logging = Capturing details , Which are useful while debugging and
# show the user details about execution of program.

# features: Warning to users
# Information to the users
# Error, Critical Errors to the user.

import logging


def test_print_the_logs():
    Logger = logging.getLogger(__name__)

    # Intentional logging to user
    Logger.info("This is an Information logs")
    Logger.warning("This is a Warning logs")
    Logger.error("This is an Error logs")
    Logger.critical("This is a Critical logs")
