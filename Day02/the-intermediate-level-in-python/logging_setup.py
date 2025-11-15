"""Configures logging with custom format and levels."""
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    logger = logging.getLogger("demo")
    logger.debug("This debug will not show")
    logger.info("Informational message")
    logger.warning("Warning message")
