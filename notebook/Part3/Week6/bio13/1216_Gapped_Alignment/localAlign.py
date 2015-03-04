#!/usr/bin/python -tt
#
# Local Alignment - Smith Waterman Algorithm  
# Copyleft (c) 2013. Ridlo W. Wibowo
#
import sys, math
 
def local_align():
    #### error message
    usage = """
    MANUAL
    Usage   : python localAlign.py [option] [input]
    Option  :   
        -i      input two sequence in command line argument
        -p      print Matrix, True = 1, default False
        -g      gap value, default 0
        -gp     gap penalty, default -1
        -m      match score, default +1
        -mm     mismatch score, default -1
        -f      input file [under construction]
                status: disable
                 
                Example: python localAlign.py -i ACACACTA AGCACACA -m 2
    END
    """
 
    #### default gap value
    gap = 0.
    match = 1.
    mismatch = -1.
    gapPenalty = -1.
    printM = 0
             
    #### input from command line argument
    if len(sys.argv) == 1:
        print usage
        sys.exit(1)
 
    while len(sys.argv) > 1:
        option = sys.argv[1]; del sys.argv[1]
        if option == '-i':
            seq1 = sys.argv[1]; del sys.argv[1]
            seq2 = sys.argv[1]; del sys.argv[1]
        elif option == '-g':
            gap = float(sys.argv[1]); del sys.argv[1]
        elif option == '-gp':
            gapPenalty = float(sys.argv[1]); del sys.argv[1]
        elif option == '-m':
            match = float(sys.argv[1]); del sys.argv[1]
        elif option == '-mm':
            mismatch = float(sys.argv[1]); del sys.argv[1]
        elif option == '-p':
            printM = int(sys.argv[1]); del sys.argv[1]
        else:
            print "\n", sys.argv[0], ': invalid option', option, usage
            sys.exit(1)
 
    #### print input
    print "Local Alignment - Smith Waterman Algorithm"
    print "SEQUENCE 1:", seq1; print "SEQUENCE 2:", seq2; 
    print "gap           : ", gap
    print "gap penalty   : ", gapPenalty
    print "match score   : ", match
    print "mismatch score: ", mismatch 
 
    #### initiate and calculate value
    lseq1 = len(seq1); lseq2 = len(seq2)
    row = lseq2+1; col = lseq1+1
 
    val = []
    for i in range(row):
        val.append([i*gap]) # gap value in first column
     
    for j in range(1,col):
        val[0].append(j*gap) # gap value in first row
     
    for i in range(1,row):
        for j in range(1,col):
            four = [0.]
            if (seq2[i-1] == seq1[j-1]): 
                four.append(val[i-1][j-1] + match)
            else: 
                four.append(val[i-1][j-1] + mismatch) # match or mismatch
            four.append(val[i-1][j] + gapPenalty)
            four.append(val[i][j-1] + gapPenalty)
            val[i].append(max(four))
 
    #### print value
    if (printM):
        for i in range(row):
            for j in range(col):
                print val[i][j], '\t',
            print ''
     
    #### search value and position of maxima
    maks = max([max(l) for l in val])
    print "Maximum Value : ", maks
     
    maxIdx = []
    for i in range(row):
        for j in range(col):
            if (val[i][j] == maks):
                maxIdx.append([i,j])
    print "Maximum Position :", maxIdx
     
    #### traceback
    for idx in maxIdx:
        sequ1 = ''; sequ2 = ''
        i = idx[0]; j = idx[1]
        while (val[i][j] > 0.):
            if (val[i][j] == val[i-1][j-1] + (match if seq2[i-1] == seq1[j-1] else mismatch)):
                sequ1 += seq1[j-1]
                sequ2 += seq2[i-1]
                i -= 1; j -= 1
            elif (val[i][j] == val[i-1][j] + gapPenalty):
                sequ1 += '_'
                sequ2 += seq2[i-1]
                i -= 1
            elif (val[i][j] == val[i][j-1] + gapPenalty):
                sequ1 += seq1[j-1]
                sequ2 += '_'
                j -= 1
         
        sequ1r = ' '.join([sequ1[j] for j in range(-1, -(len(sequ1) + 1), -1)])
        sequ2r = ' '.join([sequ2[j] for j in range(-1, -(len(sequ2) + 1), -1)])
         
        score = 0.
        for j in range(len(sequ1)):
            if (sequ1[j] == sequ2[j]):
                score += match
            else: 
                score += mismatch
         
        #### print result of local alignment
        print "Track "
        print "\tSequence 1 : ", sequ1r
        print "\tSequence 2 : ", sequ2r
        print "\tScore      : ", score
 
if __name__ == "__main__":
    local_align()