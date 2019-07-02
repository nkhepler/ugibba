'''
Retrieves BLAST hits from genome file. Adds some bases on either end of hit to make sure entire gene is captured.
'''


from pyfaidx import Fasta

genome = Fasta('/Users/nathanhepler/Desktop/ncbi-blast-2.8.1+/db/Utricularia_gibba.faa.txt')

'''
Scf00173	38673	38365
print(genome['lcl|Scf00173'][38365:38673])
'''
inputFile = '/Users/nathanhepler/Desktop/ugibba/combined_blast_utricularia.txt'
out_file = '/Users/nathanhepler/Desktop/ugibba/retrieved_sequences.txt'

blastHits = list()
names = list()
seqs = list()
retrieved = dict()


def readFile(inputFile):
    with open(inputFile, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            line = line.split('\t')

            scaffold = line[0]
            start = line[1]
            end = line[2]

            blastHits.append((scaffold, start, end))

def retrievedSeqs(blastHits):
    for hit in blastHits:
        if int(hit[1]) < int(hit[2]):
            first = int(hit[1])
            second = int(hit[2])
        elif int(hit[1]) > int(hit[2]):
            first = int(hit[2])
            second = int(hit[1])

        first = first - 780
        second = second + 1500
        names.append(f'{hit[0]}:{first}-{second}')
        locus = f'lcl|{hit[0]}'

        seq = genome[locus][first:second]
        seqs.append(seq)


    i=0
    for n in names:
        retrieved[n] = seqs[i]
        i+=1


def createFile():
    with open(out_file, 'w'):
        pass


def combined_out(in_dict):
    with open(out_file, 'w') as file:
        for val in sorted(in_dict):
            file.write(f'>{val}\n{in_dict[val]}\n')


createFile()
readFile(inputFile)
retrievedSeqs(blastHits)
combined_out(retrieved)



