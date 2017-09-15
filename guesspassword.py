import datetime
import genetic

#s
def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)


def display(genes, target, startTime):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    print("{0}\t{1}\t{2}".format(genes, fitness, str(timeDiff)))


def guess_password(target):
    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.1234567890@#$%^&*()-="
    start_time = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)

    def fnDisplay(genes):
        display(genes, target, start_time)

    optimal_fitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimal_fitness, gene_set, fnDisplay)


def hello_world():
    target = "Hello world!"
    guess_password(target)

def for_I_am_fearfully_and_wonderfully_made():
   target = "For I am fearfully and wonderfully made."
   guess_password(target)


if __name__ == '__main__':
    hello_world()
    for_I_am_fearfully_and_wonderfully_made()
