import logging

logger = logging.getLogger(__name__)


def train(run_name):

    logger.info("Starting/resuming training for run %s...", run_name)
