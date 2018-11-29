import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_entry(url=None, http_method=None, req_body=None, resp_body=None, response_code=None):
    if url and http_method is not None:
        logging.info("requesting: {} to {}".format(http_method, url))
    if req_body is not None:
        logging.info("request body: {}".format(req_body))
    if resp_body is not None:
        logging.info("response body: {}".format(resp_body))
    if response_code is not None:
        logging.info("response code: {}".format(response_code))
