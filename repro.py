import logging
import pika

log_format = "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) -35s %(lineno) -5d: %(message)s"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=log_format)


def on_open(connection):
    # Invoked when the connection is open
    pass


def on_close(connection, exception):
    # Invoked when the connection is closed
    connection.ioloop.stop()


# Create our connection object, passing in the on_open method
connection = pika.SelectConnection(on_open_callback=on_open, on_close_callback=on_close)

try:
    # Loop so we can communicate with RabbitMQ
    connection.ioloop.start()
except KeyboardInterrupt:
    logger.info("CTRL-C caught, exiting!")
    # Gracefully close the connection
    connection.close()
    # Loop until we're fully closed, will stop on its own
    connection.ioloop.start()
