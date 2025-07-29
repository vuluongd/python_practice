import random 

pop_size = 6
chrom_length = 5
generations = 20
mutation_rate = 0.1

def decode(chrom):
    return int(chrom, 2)

def fitness(chrom):
    x = decode(chrom)
    return x**2

def init_population():
    return [''.join(random.choice('01')for _ in range(chrom_length) for _ in range(pop_size))]

def selection(pop):
    total_fit = sum(fitness(chrom) for chrom in pop)
    pick = random.uniform(0, total_fit)
    current = 0
    for chrom in pop:
        current += fitness(chrom)
        if current >= pick:
            return chrom
    return pop[-1]

def crossover(p1, p2):
    point = random.randint(1, chrom_length)
    return p1[:point] + p2[:point], p2[:point] + p1[:point]

def mutate(chrom):
    chrom_list = list(chrom)
    for i in range(chrom_length):
        if random.random() < mutation_rate:
            chrom_list[i] = '1' if chrom_list[i] == '0' else '0'

    return ''.join(chrom_list)

def genetic_algorithm():
    pop = init_population()
    for gen in range(generations):
        print(f"Thế hệ {gen + 1}")
        pop = sorted(pop, key=fitness, reverse=True)
        for chrom in pop:
            print(f" {chrom} (x={decode(chrom)}, fitness={fitness(chrom)})")
        next_gen = []
        while len(next_gen) < pop_size:
            p1 = selection(pop)
            p2 = selection(pop)
            c1, c2 = crossover(p1, p2)
            next_gen.extend([mutate(c1),mutate(c2)])
        pop = next_gen[:pop_size]

    best = max(pop, key=fitness)
    print(f"kết quả tốt nhất: {best} (x= {decode(best)}, fitness={fitness(best)})")


if __name__ == "__main__":
    genetic_algorithm()