import os

for base, dirs, files in os.walk('/home/parkhh/genres'):
    for f in files:
        name, ext = os.path.splitext(f)
        if ext == '.au':
            s = os.path.abspath(os.path.join(base,f))
            d = os.path.abspath(os.path.join(base, name+'.wav'))
            print d
            os.system('sox %s %s' % (s,d))
