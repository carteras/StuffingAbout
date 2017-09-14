import random


def _generate_parent(length, gene_set):
    genes = []
    while len(genes) < length:
        samplesize = min(length - len(genes), len(gene_set))
        genes.extend(random.sample(gene_set, samplesize))
    return ''.join(genes)


def _mutate(parent, geneset):
    index = random.randrange(0, len(parent))
    childgenes = list(parent)
    newgene, alternate = random.sample(geneset, 2)
    childgenes[index] = alternate if newgene == childgenes[index] else newgene
    return ''.join(childgenes)


def get_best(get_fitness, target_len, optimal_fitness, gene_set, display):
    random.seed()
    best_parent = _generate_parent(target_len, gene_set)
    best_fitness = get_fitness(best_parent)
    display(best_parent)

    if best_fitness >= optimal_fitness:
        return best_parent

    while True:
        child = _mutate(best_parent, gene_set)
        child_fitness = get_fitness(child)

        if best_fitness >= child_fitness:
            continue
        display(child)
        if child_fitness >= optimal_fitness:
            return child
        best_fitness = child_fitness
        best_parent = child
