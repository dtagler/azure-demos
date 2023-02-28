import datetime
import logging
import random 

import azure.functions as func

def main(mytimer: func.TimerRequest, outputblob: func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    output_string = "timestamp,column_2,column_3,column_4,column_5\n"
    for _ in range(5):
        output_string = output_string + f"{utc_timestamp},{random.random()},{random.random()},{random.random()},{random.random()}\n"
    outputblob.set(output_string)
