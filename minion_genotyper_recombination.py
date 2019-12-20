import sys
import csv
from itertools import product

strain_codes = {"BE/38/2011": "QPYYRMCPHLTVH",
                "PRA1": "AAPPPCCQADFAQ",
                "PRA3": "ACSSSARHEKKZV",
                "PRA2": "AAPPPCCVTQEPC",
                "PRA5": "ACSSSARVHLYJH",
                "PRA4": "AANNNHAPWFKNV",
                "HAN19": "AAYYRMCPIPYSP",
                "NL/ROT3/NASAL/2012": "AAQQQHAQIPDZD",
                "BE/33/2010": "RVNNNRAVTQKQV",
                "BE/33/2011": "PACCCCVHADDZP",
                "HAN13": "ACVVVAACEKERN",
                "HAN12": "QPYYRMCPHLDZQ",
                "HAN11": "AQDAAAAQWDDXC",
                "BE/7/2011": "HRDAARAVTQLXP",
                "BE/7/2012": "HRDAARAVTQLXP",
                "HAN36": "QPHHHAQAHLDZH",
                "BE/26/2010": "HRDAARAVTQLXP",
                "JER3855": "ACFAARAVTQTJH",
                "BE/1/2012": "AHCCCCVVADEXV",
                "BE/1/2010": "AHDAAAAVEKKCR",
                "BE/1/2011": "AATTRCCVTQKAR",
                "HANSCTR11B": "QPDAARAHYRDHQ",
                "HANSCTR11A": "AACCCVCVOGLAH",
                "PRA7": "AAYYRMCPIPYSH",
                "JER4559": "AHYYRMCPWFKMV",
                "BE/23/2011": "PAYYRMCPWFFMP",
                "BE/23/2010": "AANNNHACAGTVF",
                "PRA6": "AQCCCCACTQDXH",
                "BE/3/2010": "AQYYRCCATQTZH",
                "BE/3/2011": "HRFAARACTQDNH",
                "BE/3/2012": "HRDAARAVTQDRN",
                "BE/13/2012": "AACCCCHVTQYZR",
                "UKNEQAS1": "AQNNNHPRIPWAN",
                "BE/13/2010": "ACCCCCPVTQLMC",
                "BE/13/2011": "AQSSSNVVADTZQ",
                "HAN16": "AACCCVCVTQKNR",
                "HAN3": "AATTRCCPOGDZP",
                "HAN2": "ACSSSARVHLYJH",
                "HAN1": "AAQQQHACEKDBP",
                "JER4035": "AAVVVAACEKEMP",
                "JER3230": "PACCCCCAADDXC",
                "BE/48/2011": "PAFAARAVADDXR",
                "BE/29/2011": "AQYYRCCVHLDRN",
                "HAN": "AQFAAHCPYRLAH",
                "UK/LON4/BILE/2011": "AATTRCCVADDAH",
                "HAN33": "AHNNNHAPOGLAQ",
                "JP": "AAYYRMCPIPYSH",
                "BE/6/2012": "QPPPPVQHIPEVP",
                "BE/2/2013": "AQQQQQCPHLDVR",
                "BE/15/2010": "AAVVVAACEKYXH",
                "BE/15/2011": "AHCCCCHVYREXR",
                "BE/15/2012": "HRDAARAVTQLXP",
                "2CEN30": "AAPPPCCVTQDAD",
                "JER1289": "PADAAQCHWFKSQ",
                "BE/37/2011": "QPCCCCAVTQKMV",
                "BE/27/2011": "PAYYRMCAWFFMP",
                "6397": "AHDAARAHTQTZR",
                "BE/35/2011": "PAFAAHAVWFEVQ",
                "UK/LON2/BLOOD/2013": "CQDAARAHADKXR",
                "BE/8/2011": "AANNNRAVYRYMP",
                "BE/14/2012": "QPTTRCCPWFKMP",
                "BE/14/2011": "AHCCCCAVIPFZF",
                "BE/31/2011": "HRFAARACADTZV",
                "BE/34/2011": "HRDAARAVYREMC",
                "JER4041": "AAQQQHAQHLEVR",
                "2CEN15": "PAVVVAACWFEXD",
                "BE/11/2010": "AQSSSNVAWFEVP",
                "MERLIN": "AANNNHACIPYHD",
                "U8": "HRDAARAVHLLZR",
                "BE/11/2011": "QPQQQHACTQDBP",
                "TOLEDO": "AAYYRHAAOGL--",
                "BE/11/2012": "HRDAARAVTQLXP",
                "3301": "AACCCCHVYREMC",
                "GERNA-5": "QPQQQHACTQDBP",
                "HANRTR4": "ACSSSARVHLYJH",
                "BE/25/2010": "AAQQQHAQHLEVR",
                "GERNA-1": "ACVVVAAHWFDHQ",
                "UK/LON9/URINE/2012": "CQDAAAACWFKMV",
                "HANRTR8": "QPCCCCHPIPTXH",
                "HANRTR9": "ACSSSARVOGYHR",
                "NAN4LA": "AHDAARAVEKDCF",
                "BE/39/2011": "PAFAARAVHLEVR",
                "UK/LON7/URINE/2011": "AQNNNAAAADTSP",
                "BE/41/2011": "CQTTRMCHTQLAQ",
                "BE/2/2012": "AQYYRCCVOGDVH",
                "PH": "CQNNNHAVEKEZP",
                "BE/2/2010": "AAYYRMCPYRYSP",
                "AF1": "AHHHHAQVHLDRN",
                "NL/ROT7/URINE/2012": "AANNNHAVTQDVH",
                "JER847": "AHDAARAVWFDVN",
                "DB": "CAYYRMCPIPEVP",
                "BE/40/2011": "HRTTRMCAADWHQ",
                "BE/43/2011": "QPNNNHAVTQKVP",
                "JER5695": "AAVVVAACEKYXH",
                "2CEN5": "AQYYRCCAWFKNR",
                "JER5268": "AQVVVAAVADLXP",
                "3157": "CQNNNHACIPEVC",
                "2CEN2": "ACSSSARVHLDAH",
                "DAVIS": "ACV--AACEKTPR",
                "PAT_A": "QPCCCCCVEKKXR",
                "NAN1LA": "QPPPPVQHIPEVP",
                "PAT_G": "AATTRCCVIPDHD",
                "BE/31/2010": "HRDAARAVIPLXP",
                "PAT_E": "CQDAARAPADKXR",
                "PAT_D": "AQYYRMCAEKKXR",
                "PAT_K": "AASSSNVCIPDVP",
                "BE/14/2010": "QPDAARAVOGTSP",
                "BE/17/2010": "AQYYRMCHIPLZR",
                "BE/17/2011": "RRCCCCCVWFEXV",
                "BE/30/2011": "HRDAARAVTQLXP",
                "BE/30/2010": "HRFAARAAWFDSR",
                "JER2002": "ACFAARAPWFDVH",
                "PAT_H": "AHDAARAAIPTQV",
                "BE/18/2011": "PAYYRMCAWFFMP",
                "BE/16/2012": "HRDAARAVTQLXP",
                "JER4053": "PAVVVAACEKTZH",
                "BE/18/2010": "AATTRCCVIPDHD",
                "CZ/3/2012": "AACCCCHPOGLAR",
                "HAN31": "HRSSSARVHLDJH",
                "NL/ROT6/NASAL/2012": "AHNNNPPPOGLAH",
                "BE/28/2011": "AANNNAAVIPFMR",
                "CZ/2/2013": "QPQQQHACTQDBP",
                "CZ/2/2012": "AAVVVCHVEKENQ",
                "JER1070": "PAYYRMCAWFFMP",
                "BE/45/2011": "AACCCCHPIQDNP",
                "PAV20": "AQCCCVQAADDJF",
                "BE/6/2011": "PAYYRMCAWFFMP",
                "BE/6/2010": "AQYYRCCAWFKZP",
                "PAT_C": "AADAARAPTQKMP",
                "HANSCTR9": "AAYYRMCPTQLZD",
                "HANSCTR8": "ACSSSARVTQLAQ",
                "NL/ROT1/URINE/2012": "CQNNNHAPIPEVC",
                "U11": "ACDAARAQADDHD",
                "HANSCTR2": "ACCCCCHVIPDHD",
                "HANSCTR4": "AHCCCCVVHLKMR",
                "PAV23": "AAYYRMCPWFKNR",
                "UK/LON8/URINE/2012": "AADAARCCIQLZH",
                "CINCY": "CQDAARAVWFEMH",
                "PAV25": "HRDAARAVYREMC",
                "TOWNE": "AHDAARAVYRTVP",
                "JER4755": "AHCCCVQPOQTSR",
                "PAT_F": "QPCCCAQCOGDAC",
                "HAN39": "RRCCCAACTQLZD",
                "HANCHILD4": "AANNNHACTQDVH",
                "HAN8": "AAVVVAACEKYXH",
                "NAN2LA": "PACCCCVHIPDZP",
                "HANCHILD1": "AQNNNAAVWFTZR",
                "BE/21/2011": "HRFAARACTQDNH",
                "BE/21/2010": "ACVVVAAHEKLPR",
                "HANCHILD2&3": "AQCCCVQCYRLXV",
                "HAN40": "AHNVVAAQADKHH",
                "BE/20/2010": "AQVVVAACIPTHD",
                "BE/20/2011": "CQDAAAAHWFKJC",
                "BE/42/2011": "AQYYRCCAWFLAF",
                "PAV21": "ACFAARAVADLAH",
                "HAN30": "AANNNHACIPDNH",
                "BE/36/2011": "QPTTRCCPWFKMP",
                "UKNEQAS2": "QPCCCCAVADFXD",
                "BE/32/2011": "HRDAARAVWFDMP",
                "HAN27": "PACCCCVPTQDAD",
                "BE/5/2012": "PAVVVAACWFEXD",
                "BE/5/2010": "QPCCCVQPWFEMC",
                "BE/5/2011": "AACCCCVHHLDVN",
                "PAV8": "AATTRCCATQEZC",
                "PAV1": "ACFAARAVADLAH",
                "PAV7": "CQDAARCPIPDXF",
                "PAV6": "PAYYRMCAWFLMP",
                "PAV5": "AACCCRAHTQDZP",
                "PAV4": "AQDAARAHTQFZQ",
                "BE/28/2010": "AQYYRCCAWFLZP",
                "BE/12/2010": "AQYYRCCATQTNN",
                "JHC": "CQMMMCCQWFLJH",
                "BE/12/2012": "AHNVVAAVTQDVN",
                "PAV26": "PAMMMARCIPDHD",
                "PAV24": "QPTTRMCAEKESV",
                "BE/2/2011": "HRDAARAVWFLXP",
                "BE/19/2010": "PAFAARACEKKAQ",
                "HAN38": "RVYYRARVEKTAQ",
                "JER893": "ACSSSNVHHLYCP",
                "HANSCTR13": "CQMMMAAQWDDMP",
                "HANSCTR12": "CQMMMAQVADDZP",
                "HANSCTR10": "QPQQQHACWFDVF",
                "BE/19/2011": "QPDAARAPHLTXH",
                "HAN32": "AATTRCCHWFDNQ",
                "BE/24/2011": "AHCCCCAVTQDNR",
                "TB40/E": "QPHHHAQAOGKNR",
                "BE/8/2010": "AATTRCCVTQKAR",
                "BE/8/2012": "AAVVVAACEKENV",
                "BE/46/2011": "HRDAARAVIPLXP",
                "BE/24/2010": "AATTRCCVHLDRN",
                "HANRTR1B": "AANNNHAVADFXV",
                "TR": "PAVVVAACWFLAH",
                "UK/LON5/BLOOD/2010": "AHCCCCAVTQTZR",
                "JER5409": "AAQQQHAQTQEVR",
                "BE/26/2011": "CQDAAAAHWFKQV",
                "BE/9/2012": "AATTRCCVTQKAR",
                "UK/LON6/URINE/2011": "PAVVVAACWFEXD",
                "BE/9/2010": "CQDAAAAVADKAQ",
                "BE/9/2011": "AHDAARAQYREXD",
                "NL/ROT4/NASAL/2012": "PAFAARAVADDXR",
                "BE/29/2010": "AATTRMVVTQDBP",
                "BE/22/2010": "CQDAARAHADDHQ",
                "BE/22/2011": "AHVVVAAQADKXD",
                "NANU": "ACVVVAAHADKBR",
                "BE/27/2010": "AQSSSNVVADDVP",
                "NL/ROT2/URINE/2012": "AHSSSHRQOQFZH",
                "BE/16/2010": "ACSSSARVHLYJH",
                "HAN22": "HRDAARAAYRDNP",
                "HANRTR6": "CQCCCNVAADDZP",
                "HAN20": "PAYYRCCAOGDZP",
                "HAN21": "HRFAARAVHLLAQ",
                "UK/LON1/BLOOD/2013": "RVVVVMCHWFWXP",
                "PAV18": "HRFAAAAHOGKZP",
                "PAV16": "AAYYRMCPIPYSH",
                "HAN28": "RRCCCAQVWFKVD",
                "BE/10/2010": "AAYYRMCPYREVR",
                "PAV12": "AACCCCHVADEAQ",
                "PAV11": "AADAARAHHLLJC",
                "AD169": "AAYYRMCPADKMV",
                "BE/49/2011": "AAYYRMCAWFDSH",
                "HANRTR5": "AACCCCVVTQDMH",
                "JER5550": "RRNVVAAVTQDHQ",
                "HANRTR10": "ACSSSARVHLYJH",
                "HANRTR2": "HRDAARAVWFTVN",
                "BE/4/2011": "AHCCCCCQTQLJH",
                "BE/4/2010": "AAYYRMCPIPYSH",
                "BE/4/2012": "AHTTRMCVEKEMQ",
                "JER851": "AAQQQHAQHLEVR",
                "JER2282": "Q-TTRMCPADDBP",
                "NL/ROT5/URINE/2012": "AATTRCCAOGTNN",
                "CZ/1/2012": "AHTTRCCVTQDVH",
                "CZ/1/2013": "AANNNHAVWFDVH",
                "CZ/1/2011": "ACYYRCCCTQDBP",
                "PRA8": "AACCCCHPOGLAR",
                "UK/LON3/PLASMA/2012": "AANNNHACIPDAH",
                "VR1814": "AADAARAAOGKXR",
                "BE/12/2011": "QPPPPVQHEKTZH",
                "BE/10/2012": "CQDAAAAHWFKQV",
                "BE/10/2011": "CQDAAAAAWFKMV",
                "HANRTR1A": "AHCCCCAVADFXV",
                "BE/32/2010": "AQNNNHACWFWHH",
                "HANSCTR1B": "AQYYRCCAWFLXR",
                "HANSCTR1A": "HRDAARAVOGFZP",
                "BE/44/2011": "AAYYRMCPWFDSV"}

print("minion_genotyper_recombination")

arguments = len(sys.argv)

if arguments == 1:
    for strain in strain_codes:
        print(strain + "\t" + strain_codes[strain])
        print("\nUsage: minion_genotyper_recombination.py read_code_file strain1 strain2")
        sys.exit(1)

if arguments != 4:
    print("Error - incorrect number of arguments - example usage:")
    print("minion_genotyper_recombination.py read_code_file strain1 strain2")
    sys.exit(1)

filename = sys.argv[1]
strain1_name = sys.argv[2].upper()
strain2_name = sys.argv[3].upper()

print("Genotype read code file = " + filename)

strain1 = ""
strain2 = ""

if strain1_name in strain_codes:
    strain1 = strain_codes[strain1_name]
else:
    found = False
    for code in strain_codes:
        if strain_codes[code] == strain1_name:
            strain1 = strain1_name
            strain1_name = code
            found = True

    if not found:
        print("Strain1 [" + strain1_name + "] not found in ref strain_codes")
        print("Exiting")
        sys.exit(1)

if strain2_name in strain_codes:
    strain2 = strain_codes[strain2_name]
else:
    found = False
    for code in strain_codes:
        if strain_codes[code] == strain2_name:
            strain2 = strain2_name
            strain2_name = code
            found = True

    if not found:
        print("Strain2 [" + strain2_name + "] not found in ref strain_codes")
        print("Exiting")
        sys.exit(1)

if len(strain1) != len(strain2):
    print("Error - strain1 and strain2 are different lengths")
    print("Exiting")
    sys.exit(1)

print("Strain1 name = " + strain1_name + ",  code = " + strain1)
print("Strain2 name = " + strain2_name + ", code = " + strain2)

print("Creating all possible genotype recombinations between the two strains")
geno_codes = []
for letter in range(len(strain1)):
    geno_codes.append([strain1[letter], strain2[letter], "-"])

geno_list = list(product(*geno_codes))
del geno_codes

genotypes = []
for geno in geno_list:
    genotypes.append(''.join(geno))

del geno_list

print("Total possible recombination codes (incl gaps) = " + str(len(genotypes)))

geno_counts = {}
geno_count = 0
geno_found = 0
not_counts = {}
not_found = 0
seqs = []

print("\nReading read code genotypes file")
with open(filename) as file_handler:
    reader = csv.reader(file_handler, delimiter='\t')

    for row in reader:
        geno_count += 1

        if geno_count % 1000 == 0:
            print("Processing line number: " + str(geno_count))

        # row[0] is the read_name and row[1] is the genotype code
        geno = row[1]
        seqs.append([geno, row[0]])

        if geno in genotypes:
            geno_found += 1

            if geno not in geno_counts:
                geno_counts[geno] = 1
            else:
                geno_counts[geno] += 1
        else:
            not_found += 1

            if geno not in not_counts:
                not_counts[geno] = 1
            else:
                not_counts[geno] += 1

print("\nTotal seqs = " + str(geno_count))
print("Found in strain1/strain2 genotypes = " + str(geno_found))
print("Not found in strain1/strain2 genotypes = " + str(not_found))

print("\nSorting genotypes based on observed counts")
geno_sort_list = []
for key, value in sorted(geno_counts.items(), key=lambda kv: kv[1], reverse=True):
    geno_sort_list.append([key, value])

not_sort_list = []
for key, value in sorted(not_counts.items(), key=lambda kv: kv[1], reverse=True):
    not_sort_list.append([key, value])

# original way - just print - don't store in a (ordered) list
# for key, value in sorted(geno_counts.items(), key=lambda kv: kv[1], reverse=True):
#     print(key + "\t" + str(value))

del geno_counts
del not_counts
del genotypes

print("Outputting genotype data")
print("N\tCode\tCount\tRecombination")

geno_recomb = []
recomb_count = 0
recomb_sum = 0
geno_count = 0
strain1_sum = 0
strain2_sum = 0
unsure_sum = 0

# geno_sort_list: [0] genotype_code [1] count
for geno in geno_sort_list:
    geno_count += 1
    s1 = 0
    s2 = 0

    for code in range(len(geno[0])):
        if strain1[code] != strain2[code] and geno[0][code] != '-':
            if geno[0][code] == strain1[code]:
                s1 += 1
            elif geno[0][code] == strain2[code]:
                s2 += 1

    if s1 > 0 and s2 > 0:
        recomb = "Recombinant"
        recomb_count += 1
        recomb_sum += geno[1]
        geno_recomb.append(geno[0])
    elif s1 > 0:
        recomb = "Strain1"
        strain1_sum += geno[1]
    elif s2 > 0:
        recomb = "Strain2"
        strain2_sum += geno[1]
    else:
        recomb = "Strain1-or-Strain2"
        unsure_sum += geno[1]

    # print Number [1-N], genotype code, count, and recombination state
    print(str(geno_count) + "\t" + geno[0] + "\t" + str(geno[1]) + "\t" + recomb)

print("\nNumber of recombinant genotype codes = " + str(recomb_count))
print("Total number of recombinant seqs = " + str(recomb_sum))
print("Strain 1 seqs = " + str(strain1_sum))
print("Strain 2 seqs  = " + str(strain2_sum))
print("Strain1-or-Strain2  seqs = " + str(unsure_sum))

print("\nOutputting genotypes that didn't match strain1 or strain2")
print("N\tCode\tCount")
geno_count = 0
for geno in not_sort_list:
    geno_count += 1
    print(str(geno_count) + "\t" + geno[0] + "\t" + str(geno[1]))

print("\nOutputting recombinant reads")
print("N\tGenoN\tCode\tSeqName")
geno_count = 0
seq_count = 0
for recomb in geno_recomb:
    geno_count += 1
    for seq in seqs:
        if seq[0] == recomb:
            seq_count += 1
            print(str(seq_count) + "\t" + str(geno_count) + "\t" + seq[0] + "\t" + seq[1])

# RL5A, 2488, 5819, -1
# RL6, 5958, 6473, -1
# RL12, 9849, 11094, 1
# RL13, 11188, 12070, 1
# UL1, 12173, 12830, 1
# UL9, 16946, 17648, 1
# UL11, 18641, 19460, 1
# UL20, 25639, 26656, 1
# UL73, 106936, 109088, 1
# UL74, 107429, 108848, -1
# UL120, 169365, 169971, -1
# UL146, 180929, 181292, -1
# UL139, 186461, 186878, -1
