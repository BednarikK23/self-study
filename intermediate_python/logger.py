# 5 security levels:
# DEBUG - when u testing debugging -> what is value of x, what is now in db...
# INFO - informatioon messages - just know u have x mail in mailbox...
# WARNING - nothing happened jett but it maight happen  -> u running low on storage
# ERROR - not critical but got some exception or culdnt calculate something
# CRITICAl - server is down security is down or something

import logging
# we start with default rootlogger

# this means that we will see all logs with priority info or higher
# default is set Warning
logging.basicConfig(level=logging.INFO)

logging.info("you have x mails in your inbox!")
logging.critical("All components failed!!")

# we can specify oour own logger - see in the console now will print MyLogger
logger = logging.getLogger("MyLogger")
logger.info("Laalalal")
logger.critical("hehe")

logger.log(logging.ERROR, "An error occured!")

# now we want to have log files cause i cannot just sit infront of the screen

logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("myLog.log")
handler.setLevel(logging.INFO)

# now our log would not have any formatting if we didnt add formatter:
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s") # this is not random see something on net when u wanna change...
handler.setFormatter(formatter) # - adding formatter to the handler...

logger.addHandler(handler)

logger.debug("This is a debug message")
logger.info("This is not important info")
