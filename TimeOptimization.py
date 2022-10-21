import catch as catch
from random import choices, randint, randrange, random, sample
from typing import List, Optional, Callable, Tuple
from collections import namedtuple
from functools import partial


Genome = List
Population = List[Genome]
PopulateFunc = Callable[[], Population]
FitnessFunc = Callable[[Genome], int]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]

class Graph:
    class Nodes:
        elements = []
        name = ""

        def __init__(self, x, name):
            self.elements = x
            self.name = name

        def getName(self):
            return self.name

        def getElements(self):
            return self.elements

        def __str__(self):
            return self.name

        def contains(self, alist):
            for i in self.elements:
                if i in alist:
                    return True;
            return False;

class product:
    name = ""
    getting_cost = 0;
    h = 0;

    def __init__(self, n, c, h=0):
        self.name = n
        self.getting_cost = c
        self.h = h

    def getCost(self):
        return self.getting_cost

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

things = {
    "Elma": [4],
    "Portakal": [4],
    "Muz": [4],
    "Lahana": [4],
    "Biber": [4],
    "Salatalık": [4],
    "Roka": [4],
    "Patates": [4],
    "Soğan": [4],
    "Balık": [1],
    "Balık Teslim": [10],
    "Süt": [1],
    "Peynir": [1],
    "Ekmek": [1],
    "Zeytin": [1],
    "Deterjan": [1],
    "Çikolata": [1],
    "Tavuk": [1],
    "Ayçiçek Yağı": [1],
    "Zeytin Yağı": [1],
    "Toz Şeker": [1],
    "Yumurta": [1],
    "İrmik": [1],
    "Tuz": [1],
    "Çubuk Kraker": [1],
    "Cipsi": [1],
    "Kurabiye": [10],
    "Lokum": [4],
    "Labne": [1],
    "Ketçap": [1],
    "Su": [1],
    "Kola": [1],
    "Pil": [1],
    "Şampuan": [1],
    "Duş Jeli": [1],
    "Deodorant": [1],
    "Diş Fırçası": [1],
    "Diş Macunu": [1],
    "Parfüm": [1],
    "Meyve Suyu": [1],
    "Pasta": [1],
    "Maden Suyu": [1],
    "Yüz Temizleme Jeli": [1],
    "Makyaj Malzemesi": [1],
    "Nemlendirici": [1],
    "Güneş Kremi": [1],
    "Tavuk": [1],
    "Tavuk Teslim": [5],
    "Sade Un": [1],
    "Mısır Unu": [1],
    "Makarna": [1],
    "Salça": [1],
    "Ton Balığı": [1],
    "Turşu": [1],
    "Pirinç": [1],
    "Bulgur": [1],
    "Fasulye": [1],
    "Mercimek": [1],
    "Nohut": [1],
    "Mısır": [1],
    "Türk Kahvesi": [1],
    "Filtre Kahve": [1],
    "Çekirdek Kahve": [1],
    "Soğuk Kahve": [1],
    "Sıcak Çikolata": [1],
    "Salep": [1],
    "Süt Tozu": [1],
    "Şalgam Suyu": [1],
    "Limonata": [1],
    "Kefir": [1],
    "Enerji İçeceği": [1],
    "Çay": [1],
    "Bitki Çayı": [1],
    "Puzzle": [1],
    "Oyuncak": [1],
    "Oyun Hamuru": [1],
    "Kitap": [1],
    "Dergi": [1],
    "Gazete": [1],
    "Defter": [1],
    "Kalem": [1],
    "Boya": [1],
    "Yapıştırıcı": [1],
    "Ofis Aksesuarı": [1],
    "Televizyon": [1],
    "Hoparlör": [1],
    "Kulaklık": [1],
    "Kağıt": [1],
    "Telefon": [1],
    "Buz Dolabı": [1],
    "Fırın": [1],
    "Lamba": [1],
    "Bilgisayar": [1],
    "Monitor": [1],
    "Bilgisayar Aksesuarı": [1],
    "Simit": [1],
    "Poğaça": [1],
    "Açma": [1],
    "Kek": [1],
    "YasPasta": [1],
    "Tatlı": [1],
    "Kakao": [1],
    "Maya": [1],
    "Vanilin": [1],
    "Kabartma Tozu": [1],
    "Krem Şanti": [1],
    "Nişasta": [1],
    "KAHVALTILIK": [1],
    "PET_SHOP": [1],
    "ATIŞTIRMALIK": [1],
    "KURUYEMİŞ": [5],
    "ALKOL": [1],
} #Ürünler
where = {
    "A": ["Ekmek",  "Simit", "Poğaça", "Açma"],
    "B": ["Muz", "Biber", "Lahana", "Portakal",
          "Elma", "Sogan", "Patates", "Roka", "Salatalik"],
    "C": ["Kurabiye", "Pasta","Kek","Tatlı","Kakao","Maya","Vanilin","Kabartma Tozu","Krem Şanti","Nişasta"],
    "D": ["Sade Un","Mısır Unu","Makarna","Salça",
          "Turşu","Ton Balığı","Pirinç","Bulgur","Buğday","Fasulye","Mercimek","Nohut","Mısır"],
    "E": ["Zeytin Yağı", "Ayçiçek Yağı","Yumurta","Toz Şeker","Tuz"],
    "F":["Meyve Suyu", "Kola", "Maden Suyu","Türk Kahvesi","Filtre Kahve",
         "Çekirdek Kahve","Soğuk Kahve","Sıcak Çikolata","Salep","Süt Tozu",
         "Şalgam Suyu","Limonata","Kefir","Enerji İçeceği","Çay","Bitki Çayı"],
    "D2":["Puzzle","Oyuncak","Oyun Hamuru","Kitap","Dergi",
          "Gazete","Defter","Kalem","Boya","Kağıt","Yapıştırıcı","Ofis Aksesuarı"],
    "J":["Deterjan", "Şampuan", "Duş Jeli", "Diş Macunu", "Diş Fırçası",
         "Yüz Temizleme Jeli", "Makyaj Malzemesi", "Nemlemdirici", "Güneş Kremi"],
    "K":["Balık", "KAHVALTILIK"],
    "N":["Tavuk","PET_SHOP"],
    "P":["ATIŞTIRMALIK"],
    "R":["KURUYEMİŞ"],
    "S":["Televizyon","Pil","Hoparlor","Kulaklık","Telefon","Buz Dolabı","Fırın",
         "Lamba","Bilgisayar","Monitor","Bilgisayar Aksesuarı"],
    "N3":["Et"]
} #Reyonlar

A = Graph.Nodes(["Ekmek",  "Simit", "Poğaça", "Açma"], "A")
B = Graph.Nodes(["Muz", "Biber", "Lahana", "Portakal",
                 "Elma", "Sogan", "Patates", "Roka", "Salatalik"], "B")
C = Graph.Nodes(["Kurabiye", "Pasta","Kek","Tatlı","Kakao","Maya",
                "Vanilin","Kabartma Tozu","Krem Şanti","Nişasta"], "C")
D = Graph.Nodes(["Sade Un","Mısır Unu","Makarna","Salça",
                 "Turşu","Ton Balığı","Pirinç","Bulgur","Buğday","Fasulye","Mercimek","Nohut","Mısır"], "D")  # buraya ekleme yap
E = Graph.Nodes(["Zeytin Yağı", "Ayçiçek Yağı","Yumurta","Toz Şeker","Tuz"], "E") #EKLE
F = Graph.Nodes(["Meyve Suyu", "Kola", "Maden Suyu","Türk Kahvesi","Filtre Kahve",
                 "Çekirdek Kahve","Soğuk Kahve","Sıcak Çikolata","Salep","Süt Tozu",
                 "Şalgam Suyu","Limonata","Kefir","Enerji İçeceği","Çay","Bitki Çayı"], "F")
G = Graph.Nodes([], "G")
H = Graph.Nodes([], "H")
D2 = Graph.Nodes(["Puzzle","Oyuncak","Oyun Hamuru","Kitap","Dergi",
                  "Gazete","Defter","Kalem","Boya","Kağıt","Yapıştırıcı","Ofis Aksesuarı"], "D2")
J = Graph.Nodes(
    ["Deterjan", "Şampuan", "Duş Jeli", "Diş Macunu", "Diş Fırçası",
     "Yüz Temizleme Jeli", "Makyaj Malzemesi", "Nemlemdirici", "Güneş Kremi"], "J")
K = Graph.Nodes(["Balık", "KAHVALTILIK",], "K")
L = Graph.Nodes([], "L")
M = Graph.Nodes([], "M")
N = Graph.Nodes(["Tavuk","PET_SHOP"], "N")
P = Graph.Nodes(["ATIŞTIRMALIK"], "P")
R = Graph.Nodes(["KURUYEMİŞ"], "R")
S = Graph.Nodes(["Televizyon","Pil","Hoparlor","Kulaklık","Telefon","Buz Dolabı","Fırın",
                 "Lamba","Bilgisayar","Monitor","Bilgisayar Aksesuarı"], "S")
T = Graph.Nodes([], "T")
N2 = Graph.Nodes(["Tavuk Teslim"],"N2")
K2 = Graph.Nodes(["Balık Teslim"], "K2")
N3 = Graph.Nodes(["Et"],"N3")
N4 = Graph.Nodes(["Et Teslim"],"N4")

adjac_lis = {
    A: [(B), (D)],
    B: [(A), (D), (C), (E)],
    C: [(B), (E), (F)],
    D: [(A), (B), (G), (D2)],
    E: [(C), (B), (G), (H), (J)],
    F: [(C), (H), (K)],
    G: [(D), (E), (H), (D2), (J)],
    H: [(E), (G), (F), (K), (J)],
    J: [(E), (G), (H), (L), (M), (P)],
    D2: [(D), (G), (L), (T)],
    T: [(D2), (L), (R)],
    K: [(F), (H), (M), (N), (K2)],
    M: [(J), (L), (P), (N), (K)],
    N: [(K), (S), (M), (N2),(N3),(N4)],
    S: [(P), (N), (R)],
    R: [(T), (P), (S)],
    P: [(J), (L), (R), (S), (M)],
    L: [(J), (D2), (T), (P), (M)],
    N2: [(N)],
    K2: [(K)],
    N3: [(N)],
    N4: [(N)]
}


def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]

    if start == goal:
        return [start]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    temp = []
                    for t in new_path:
                        temp.append(str(t))
                    return temp
            explored.append(node)
    return


def generate_genome(alist) -> Genome:
    t = targets(alist)
    return sample(t, k=len(t))

def generate_population(size: int,alist) -> Population:
    return [generate_genome(alist) for _ in range(size)]

def fitness(genome, product_list) -> int:
    if genome==[] or type(genome) != list:
        return genome,999
    if "Balık" in product_list:
        if genome.index(K) > genome.index(K2):
                return [],999
    if "Tavuk" in product_list:
        if genome.index(N) > genome.index(N2):
            return [],999
    if "Et" in product_list:
        if genome.index(N3) > genome.index(N4):
            return [],999
    path = []
    weight = 0
    for i in range(len(genome)):
        if genome[i] == K:                              #BALIK
            if i == 0:
                weight+=(len(BFS_SP(adjac_lis,A,K))-1)*0.5
                path = path + BFS_SP(adjac_lis,A,K) + ["\n"]
            else:
                weight+=(len(BFS_SP(adjac_lis,genome[i-1],K))-1)*0.5
                path = path + BFS_SP(adjac_lis,genome[i-1],K)[:]+ ["\n"]
            path.append("Balık siparişi verildi.\n")
            weight+=1
            temp_weight_K = weight
            continue
        elif genome[i] == K2:
            weight+=(len(BFS_SP(adjac_lis,genome[i-1],K))-1)*0.5
            path = path + BFS_SP(adjac_lis,genome[i-1],K)[:]+ ["\n"]
            if weight - temp_weight_K < 10:
                weight+=(10 -(weight - temp_weight_K))
            path.append("Balık alındı.\n")
            continue
        elif genome[i] == N:                              #TAVUK
            if i == 0:
                weight+=(len(BFS_SP(adjac_lis,A,N))-1)*0.5
                path = path + BFS_SP(adjac_lis,A,N)[:]+ ["\n"]
            else:
                weight+=(len(BFS_SP(adjac_lis,genome[i-1],N))-1)*0.5
                path = path + BFS_SP(adjac_lis,genome[i-1],N)[:]+ ["\n"]
            weight+=1
            path.append("Tavuk siparişi verildi.\n")
            temp_weight_N = weight
            continue
        elif genome[i] == N2:
            weight+=(len(BFS_SP(adjac_lis,genome[i-1],N))-1)*0.5
            path = path + BFS_SP(adjac_lis,genome[i-1],N)[:]+ ["\n"]
            if weight - temp_weight_N < 5:
                weight+=(5-(weight - temp_weight_N))
            path.append("Tavuk alındı.\n")
            continue
        elif genome[i] == N3:                              #TAVUK
            if i == 0:
                weight+=(len(BFS_SP(adjac_lis,A,N3))-1)*0.5-0.5
                path = path + BFS_SP(adjac_lis,A,N)[:]+ ["\n"]
            else:
                weight+=(len(BFS_SP(adjac_lis,genome[i-1],N3))-1)*0.5-0.5
                path = path + BFS_SP(adjac_lis,genome[i-1],N)[:]+ ["\n"]
            weight+=1
            path.append("Et siparişi verildi.\n")
            temp_weight_N3 = weight
            continue
        elif genome[i] == N4:
            weight+=(len(BFS_SP(adjac_lis,genome[i-1],N4))-1)*0.5-0.5
            path = path + BFS_SP(adjac_lis,genome[i-1],N)[:]+ ["\n"]
            if weight - temp_weight_N3 < 7:
                weight+=(7-(weight - temp_weight_N3))
            path.append("Et alındı.\n")
            continue

        if i == 0:
            weight+=(len(BFS_SP(adjac_lis,A,genome[i]))-1)*0.5
            path = path + BFS_SP(adjac_lis,A,genome[i])[:]+ ["\n"]
            for j in product_list:
                if j in where[str(genome[i])]:
                    path.append(j + " alındı.\n")
                    weight+=things[j][0]
        else:
            weight+=(len(BFS_SP(adjac_lis,genome[i-1],genome[i]))-1)*0.5
            path = path + BFS_SP(adjac_lis,genome[i-1],genome[i])[:]+ ["\n"]
            for j in product_list:
                if j in where[str(genome[i])]:
                    path.append(j + " alındı.\n")
                    weight+=things[j][0]
    weight+=(len(BFS_SP(adjac_lis,genome[-1],T))-1)*0.5
    path = path + BFS_SP(adjac_lis,genome[-1],T)
    path = remove_values_from_list(path,"N2")
    path = remove_values_from_list(path,"N3")
    path = remove_values_from_list(path,"N4")
    path = remove_values_from_list(path,"K2")
    return path,weight

def selection_pair(population,list) -> Population:
    i = randint(0,int(len(population)/2))
    j = randint(0,int(len(population)/2))
    return population[i],population[j]



def insertionSort(arr,genomes):
    for i in range(1, len(arr)):
        key = arr[i]
        key2 = genomes[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            genomes[j+1] = genomes[j]
            j -= 1
        arr[j + 1] = key
        genomes[j+1] = key2
    return genomes

def sort_population(population,list):
    ws = []
    gs = []
    for i in population:
        t,w = fitness(i,list)
        ws.append(w)
        gs.append(i)

    return insertionSort(ws,gs)


def crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if type(a)!=list or type(b)!=list:
        return [],[]
    if len(a) == 0 or len(b) == 0:
        return [],[]
    length = len(a)
    if length < 2:
        return a, b
    c1 = []
    c2 = []
    i = randint(0,length-1)
    j = randint(1,length-1)

    while(i<=j):
        i = randint(1,length-1)
        j = randint(1,length-1)


    c1mid = a[j:i]
    c2mid = b[j:i]
    if a!=b:
        for t in c1mid:
            b.remove(t)
        for t in c2mid:
            a.remove(t)
        for t in range(j):
            c1.append(b[0])
            b.pop(0)
            c2.append(a[0])
            a.pop(0)
        for t in range(i-j):
            c1.append(c1mid[t])
            c2.append(c2mid[t])
        for t in range(i,length):
            c1.append(b[0])
            b.pop(0)
            c2.append(a[0])
            a.pop(0)
    else:
        for t in c1mid:
            b.remove(t)
        for t in range(j):
            c1.append(b[0])
            b.pop(0)
        for t in range(i-j):
            c1.append(c1mid[t])
        for t in range(i,length):
            c1.append(b[0])
            b.pop(0)
    return c1,c2


def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    if genome==[] or type(genome)!=list:
        return []
    for _ in range(num):
        i = randrange(len(genome))
        j = randrange(len(genome))
        while(i==j):
            i = randrange(len(genome))
            j = randrange(len(genome))
        if random() > probability:
            return genome
        else:
            temp = genome[i]
            genome[i] = genome[j]
            genome[j] = temp
    return genome


def population_fitness(population: Population, fitness_func: FitnessFunc,list) -> int:
    return sum([fitness_func(genome,list) for genome in population])

def genome_to_string(genome: Genome) -> str:
    return "".join(map(str, genome))


def run_evolution(
        populate_func: PopulateFunc, fitness_func=fitness,
        selection_func: SelectionFunc = selection_pair,
        crossover_func: CrossoverFunc = crossover, mutation_func: MutationFunc = mutation,
        generation_limit: int = 100) -> Tuple[Population, int]:

    alist = input("Lütfen alışveriş listenizi giriniz : ") # Alış-Veriş listesi
    alist = alist.split(",")
    for i in range(len(alist)):
        if alist[i][0]==" ":
            alist[i] = alist[i][1:]
        alist[i] = alist[i][0].upper() + alist[i][1:]
    for i in alist:
        if i not in things:
            print(i,"ürünü marketimizde bulunmamaktadır!")
            alist.remove(i)
    if "Balık" in alist:
        alist.append("Balık Teslim")
    if "Tavuk" in alist:
        alist.append("Tavuk Teslim")
    if "Et" in alist:
        alist.append("Et Teslim")
    population = populate_func(20,alist)

    min_genome = None
    min_weight = 999
    for i in range(generation_limit):
        population = sort_population(population,alist)
        if fitness(population[0],alist)[1]<min_weight:
            min_genome,min_weight = fitness(population[0],alist)

        next_generation = population[0:2]
        for j in range(int(len(population) / 2)-1):
            parents = selection_func(population,alist)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]
            for i in next_generation:
                if i==[]:
                    next_generation.remove(i)
            next_generation+=generate_population(20-len(next_generation),alist)
        population = next_generation

    print(" ",*min_genome)
    """return min_genome,min_weight"""
def remove_values_from_list(the_list, val): #Yan Fonksiyon.
    return [value for value in the_list if value != val]

def targets_str(list):
    x = []
    for i in list:
        for j in adjac_lis.keys():
                if i in j.getElements():
                    x.append(j)
    for i in range(len(x)):
        if x[i] != 0:
            for j in range(i+1,len(x)):
                if(x[i]==x[j]):
                    x[j] = 0
    temp = []
    for t in remove_values_from_list(x,0):
        temp.append(str(t))
    return temp

def targets(list):
    x = []
    for i in list:
        for j in adjac_lis.keys():
            if i in j.getElements():
                x.append(j)
    for i in range(len(x)):
        if x[i] != 0:
            for j in range(i+1,len(x)):
                if(x[i]==x[j]):
                    x[j] = 0
    return remove_values_from_list(x,0)

run_evolution(generate_population,fitness,selection_pair,crossover,mutation,100)

