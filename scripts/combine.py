'''
Combines blast results into single file. Final output is scaffold (or chromosome), start and end of subject.
In tab separated format.
'''

out_file = 'combined_blast_utricularia.txt'

expa1 = '/Users/nathanhepler/Desktop/ncbi-blast-2.8.1+/utricularia/expa1_out.txt'
expb1 = '/Users/nathanhepler/Desktop/ncbi-blast-2.8.1+/utricularia/expb1_out.txt'
exla1 = '/Users/nathanhepler/Desktop/ncbi-blast-2.8.1+/utricularia/exla1_out.txt'
exlb1 = '/Users/nathanhepler/Desktop/ncbi-blast-2.8.1+/utricularia/exlb1_out.txt'

queries = [expa1, expb1, exla1, exlb1]


combined = dict()
scaffold_n = list()
locations = list()


def createFile():
    with open(out_file, 'w'):
        pass


def scanner(input_file):
    with open(input_file, 'r') as file:
        for line in file.readlines():
            if '#' not in line:
               line = line.strip()
               line = line.split('\t')

               scaffold = line[1]
               start = line[8]
               end = line[9]

               scaffold_n.append(scaffold)
               locations.append((start,end))

            else:
                pass
        i=0
        for name in scaffold_n:
            combined[locations[i]] = name
            i+=1


def perform(qs):
    for query in qs:
        scanner(query)


def combined_out(in_dict):
    with open(out_file, 'w') as file:
        for val in in_dict:
            file.write(f'{combined[val]}\t{val[0]}\t{val[1]}\n')


createFile()
perform(queries)
combined_out(combined)