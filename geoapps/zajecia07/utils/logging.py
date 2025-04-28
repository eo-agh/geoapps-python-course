import logging


def get_logger(
    name: str,
    log_level: int | str = logging.INFO,
) -> logging.Logger:
    """Builds a `Logger` instance with provided name and log levels for stream and file.

    Args:
        name: The name for the logger.
        log_level: The default log level for the logger.

    Returns:
        The logger.

    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Avoid adding multiple handlers if the logger already has them
    if not logger.handlers:
        # Formatter for both handlers
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)  # Set level for stream
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger
