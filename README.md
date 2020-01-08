Simple python script to detect recombination between two HCMV strains.

The script takes:

Argument 1: The readCodes.txt file from minion_genotyper, which is in the following format:

---
    Read	GenotypeCode  
    ed847705-0573-45d3-8156-f856c2fd07bf	--HHH-Q------
    c1ffed12-2c0a-4d6c-9c6f-9f3266139439	---HH--------
    e2b1b440-8b05-4ffa-af0a-8779f0486999	--------HL---
    etc
    etc
---
Argument 2: Strain1 [case insensitive]- either the name of the strain e.g. "merlin" or the strain code e.g. "AANNNHACIPYHD"

Argument 3:  Strain2 [case insensitive] - either the name of the strain e.g. "af1" or the strain code e.g. "AHHHHAQVHLDRN"

The script will then search through all the reads for any that show signatures of recombination between the two strain codes, and will output the following information to the screen and files:

---
    minion_genotyper_recombination
    Genotype read code file = RecAF1delMer_R1R2R3_readsCodes.txt
    Strain1 name = AF1,  code = AHHHHAQVHLDRN
    Strain2 name = MERLIN, code = AANNNHACIPYHD
    Creating all possible genotype recombinations between the two strains
    Total possible recombination codes (incl gaps) = 1062882
    Reading read code genotypes file
    Processing line number: 1000
    Processing line number: 2000
    Processing line number: 3000
    Processing line number: 4000
    Processing line number: 5000
    Processing line number: 6000
    Processing line number: 7000
    Processing line number: 8000
    Processing line number: 9000
    Processing line number: 10000
    Processing line number: 11000
    Processing line number: 12000
    Processing line number: 13000
    Processing line number: 14000
    Processing line number: 15000
    Processing line number: 16000
    Processing line number: 17000
    Processing line number: 18000
    Total seqs = 18466
    Found in strain1/strain2 genotypes = 16356
    Not found in strain1/strain2 genotypes = 2110
    Sorting genotypes based on observed counts
    Outputting genotype data to: RecAF1delMer_R1R2R3_readsCodes_genotypes.txt
    Number of recombinant genotype codes = 82
    Total number of recombinant seqs = 186
    Strain 1 [AF1] seqs = 14840
    Strain 2 [MERLIN] seqs  = 1306
    Strain1-or-Strain2  seqs = 24
    Outputting recombinant reads to: RecAF1delMer_R1R2R3_readsCodes_recomb_reads.txt
    Outputting genotypes that didn't match strain1 or strain2 to: RecAF1delMer_R1R2R3_readsCodes_genotypes_nomatch.txt
    Total genotypes that do not match the strains = 250, number of reads = 2110
---

The three output files are:

File 1: _genotypes.txt - a summary of each genotype observed and the number of times it is observed. The genotypes in this file only relate to strains 1 or 2, or any recombinations between the 2
File 2: _recomb_reads.txt - the read ID's that display signatures of recombination
File 3: _genotypes_no_match.txt - a summary of each genotype observed and the number of times it is observed. The genotypes in this file are those not related to strains 1 or 2 (so presumably errorenous)


