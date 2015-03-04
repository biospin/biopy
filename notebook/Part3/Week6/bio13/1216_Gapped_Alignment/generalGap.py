#!/usr/bin/python -tt
#
# General Gap Penalty, Needleman-Wunch Algorithm
# Copyleft (c) 2013. Ridlo W. Wibowo
#
import sys, math
 
def global_gap():
    #### error message
    usage = """
    MANUAL
    Usage   : python generalGap.py [option] [input]
    Option  :   
        -i      input two sequence in command line argument
        -g      gap value, default -1
        -gp     gap penalty, default -1
        -m      match score, default +1
        -mm     mismatch score, default -1
        -f      input file [under construction]
                status: disable
                 
                Example: python generalGap.py -i ATTGTC AGTGTAC -g -1
    END
    """
 
    #### default gap value
    gap = -1.
    match = 1.
    mismatch = -1.
    gapPenalty = -1.
             
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
        else:
            print "\n", sys.argv[0], ': invalid option', option, usage
            sys.exit(1)
 
    #### print input
    print "General Gap Penalty, Needleman-Wunch Algorithm"
    print "SEQUENCE 1:", seq1; print "SEQUENCE 2:", seq2
    print "gap           : ", gap
    print "gap penalty   : ", gapPenalty
    print "match score   : ", match
    print "mismacth score: ", mismatch
 
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
            three = []
            if (seq2[i-1] == seq1[j-1]): 
                three.append(val[i-1][j-1] + match)
            else: 
                three.append(val[i-1][j-1] + mismatch) # match or mismatch
            three.append(val[i-1][j] + gapPenalty) # Delete
            three.append(val[i][j-1] + gapPenalty) # Insert
            val[i].append(max(three))
 
    #### print value
    for i in range(row):
        for j in range(col):
            print val[i][j], '\t',
        print ''
     
    #### trace back
    sequ1 = ''
    sequ2 = ''
    i = lseq2
    j = lseq1
    while (i > 0 or j > 0):
        if (i>0 and j>0 and val[i][j] == val[i-1][j-1] + (match if seq2[i-1]==seq1[j-1] else mismatch)):
            sequ1 += seq1[j-1]
            sequ2 += seq2[i-1]
            i -= 1; j -= 1
        elif (i>0 and val[i][j] == val[i-1][j] + gapPenalty):
            sequ1 += '_'
            sequ2 += seq2[i-1]
            i -= 1
        elif (j>0 and val[i][j] == val[i][j-1] + gapPenalty):
            sequ1 += seq1[j-1]
            sequ2 += '_'
            j -= 1
     
    sequ1r = ' '.join([sequ1[j] for j in range(-1, -(len(sequ1)+1), -1)])
    sequ2r = ' '.join([sequ2[j] for j in range(-1, -(len(sequ2)+1), -1)])
     
    score = 0.
    for j in range(len(sequ1)):
        if (sequ1[j] == sequ2[j]):
            score += match
        else:
            score += mismatch
 
    print "Sequence 1: ", sequ1r
    print "Sequence 2: ", sequ2r
    print "Score     : ", score
 
if __name__ == "__main__":
    global_gap()
    