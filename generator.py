import sqlite3
import logging
from threading import Thread

def INSERT_LINES(MIN_VALUE,MAX_VALUE):
    STR_MAX_SIZE = str(MAX_VALUE)
    for number in range(MIN_VALUE,MAX_VALUE):
        position = str(number+1).zfill(len(STR_MAX_SIZE))
        STR_INSERT = f"insert into meu_teste values(' Essa eh a mensagem de ID {position}',{position});"
        log.info(f" ({position}/{STR_MAX_SIZE}) - {STR_INSERT}")
        cursor.execute(STR_INSERT)

    log.info(f"( {MIN_VALUE} / {MAX_VALUE} ) Commitando: ")
    CONNECTION.commit()

CONNECTION = sqlite3.connect('test.db')
cursor = CONNECTION.cursor()

FORMAT = '%(asctime)s [%(levelname)s] - %(message)s'
logging.basicConfig(    format=FORMAT, level=logging.INFO   )
print(" >>> Inicializando processo")
log = logging.getLogger()

MAX_SIZE     = 1000 * 1000 * 1000

NUM_THREADS  = 300
LST_THREADS  = []
NUM_STEP     = MAX_SIZE//NUM_THREADS
log.info(f" Num NUM_STEP: {NUM_STEP}")

for number in range(0,NUM_THREADS):
    INITIAL = number  * NUM_STEP + 1
    END     = INITIAL + NUM_STEP
    log.info(f' ( {number + 1} / {NUM_THREADS} ) De: {INITIAL} | End: {END - 1}')
    INSERT_LINES(INITIAL,END)

log.info(" Encerrando ")
CONNECTION.close()
