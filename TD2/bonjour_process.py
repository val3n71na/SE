import time
import random
import logging
import sys, os
import multiprocessing
from multiprocessing import Process, Queue, current_process, freeze_support

#
# Function run by worker processes
#

def worker(input, output):
    for func, args in iter(input.get, 'STOP'):
        result = execute_function(func, args)
        output.put(result)

#
# Function used to calculate result
#

def execute_function(func, args):
    result = func(args)
    return '%s says that %s %s = %s' % \
        (current_process().name, func.__name__, args, result)

#
# Functions referenced by tasks
#

def dites_bonjour(personne):
    return "Bonjour " + personne + " !"
    
def utilisation():
    #Affichage mode d'utilisation
    print \
    """
          Le programme doit etre appelle avec minimum 1 argument:
          python bonjour_process.py Nom_de_fichier.txt
    """


def main(argv=None):
    working_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
    #Configurez le logging pour ecrire dans un fichier texte
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename=working_dir + 'process.log',
                        level=logging.INFO)
    logging.info("Main start")

    #multiprocessing.log_to_stderr(logging.INFO)

    #La boucle principale
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        utilisation()
        return 0
    
    else:

    NUMBER_OF_PROCESSES = 4
    TASKS1 = []
    TASKS2 = []

    # Create queues
    task_queue = Queue()
    done_queue = Queue()
    
    mlleThread = []
    mmeThread = []
    mThread = []

    with open(working_dir+argv[1], 'r') as f:
    #Dites bonjour a chaque personne de fichier
        for ligne in f:
           if ligne[0:2] == "M.":
               mThread.append((dites_bonjour, (ligne.strip(' \r\n'))))
           if ligne[0:4] == "Mme.":
               mmeThread.append((dites_bonjour, (ligne.strip(' \r\n'))))
           if ligne[0:5] == "Mlle.":
               mlleThread.append((dites_bonjour, (ligne.strip(' \r\n'))))
           #logging.info("Ligne: %s" % (ligne.strip(' \r\n')))

    # Submit tasks
    for mlle in mlleThread:
        logging.info(mlle)
        task_queue.put(mlle)

    # Start worker processes
    for i in range(NUMBER_OF_PROCESSES):
        Process(target=worker, args=(task_queue, done_queue)).start()

    # Get and print results
    for i in range(len(mlleThread)):
        print done_queue.get()

    # Add more tasks using `put()`
    for mme in mmeThread:
        logging.info(mme)
        task_queue.put(mme)

    # Get and print some more results
    for i in range(len(mme)):
        print done_queue.get()
        
    # Add more tasks using `put()`
    for m in mThread:
        logging.info(m)
        task_queue.put(m)

    # Get and print some more results
    for i in range(len(m)):
        print done_queue.get()

    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')
        
    logging.info("Main stop")
    return 0

if __name__ == '__main__':
    freeze_support()
    sys.exit(main())
