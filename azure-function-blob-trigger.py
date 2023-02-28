import datetime
import logging
import random 

import azure.functions as func

def main(myblob: func.InputStream, outputblob: func.Out[str]):
    utc_timestamp = datetime.datetime.utcnow().replace(
    tzinfo=datetime.timezone.utc).isoformat()
    
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    
    myfile = myblob.read().decode('utf-8')
    output_string = myfile
    for x in range(10):
        output_string = output_string + f"{utc_timestamp},{random.random()},{random.random()},{random.random()},{random.random()}\n"
    outputblob.set(output_string)
