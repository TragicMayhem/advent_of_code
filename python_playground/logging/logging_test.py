import logging

# Print out info about call
# print(dir(logging))

# Create and configure logger
LOG_FORMAT = "%(asctime)s: %(levelname)s - %(message)s"
logging.basicConfig(filename='./test_log.txt',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

# Test Messages
logger.debug("Test debug message")
logger.info("Test info message")
logger.warning("Test warning message")
logger.error("Test error message")
logger.critical("Test critical message")

# if __name__ == '__main__':
#     main()
