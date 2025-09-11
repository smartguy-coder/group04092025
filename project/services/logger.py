from logtail import LogtailHandler
import logging

SOURCE_TOKEN = 'RNfEsvTJQ5dZRADj3y5fphog'
HOST = "s1516021.eu-nbg-2.betterstackdata.com"


def get_logger():
    handler = LogtailHandler(
        source_token=SOURCE_TOKEN,
        host=f'https://{HOST}',
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.handlers = []
    logger.addHandler(handler)
    return logger


logger = get_logger()

logger.info('some info log 333333333333333', extra={"user_id": 23556})
logger.error('some error log')


