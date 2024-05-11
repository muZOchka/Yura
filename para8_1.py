import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="para8_logfile.log",
                    filemode="w",
                    format="We have next logging message:%(asctime)s:%(levelname)s:%(message)s")

logging.debug("debug")
logging.info("Info")
logging.warning("warninng")
logging.error("Error")
logging.critical("Critical")


try:
    print(10/0)
except Exception:
    logging.exception("Exception")