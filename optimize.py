from subprocess import call
import os
import sys
import math
import os
import fnmatch 

cjpeg = '/home/fermin/workspace/mozjpeg/build/cjpeg'

def convertSize(size):
   if (size == 0):
	   return '0B'
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size,1024)))
   p = math.pow(1024,i)
   s = round(size/p,2)
   return '%s %s' % (s,size_name[i])

input = sys.argv[1]
output = sys.argv[2]

inpath = os.path.realpath(input) + '/'
outpath = os.path.realpath(output) + '/'

if not os.path.exists(outpath):
	os.makedirs(outpath)

totalsaved = 0

for root, dir, files in os.walk(inpath):
	dest = root.replace(inpath, '')
	destOut = os.path.join(outpath, dest)

	if not os.path.exists(destOut):
		os.makedirs(destOut)

	print dest
	print destOut
	print root + ' goes to ' + destOut

	for filename in files:
		if filename.lower().endswith(('.jpg', '.jpeg' )):
			infile = os.path.join(root, filename)
			outfile = os.path.join(destOut, filename)

			args = [cjpeg, '-quality', '60', '-progressive', '-optimize', '-outfile', outfile, infile]
			
			#print ' '.join(args)
			call(args)

			outSize = os.path.getsize(outfile)
			inSize = os.path.getsize(infile)

			totalsaved = totalsaved + (inSize - outSize)

			savedPercent = int( (1 - float(outSize) / inSize) * 100 )

			print filename + ' from ' + convertSize( inSize ) + ' to ' + convertSize( outSize ) + \
					'. Saved ' + str( savedPercent ) + '%. Total saved ' + convertSize( totalsaved )

	print ""

# call([cjpeg, '-quality', '70', '-progressive', '-optimize', '-outfile', output, input])

# outSize = os.path.getsize(output)
# inSize = os.path.getsize(input)

# print convertSize( inSize )
# print convertSize( outSize )
# print 'Saved ' + str( int( (1 - float(outSize) / inSize) * 100 ) ) + '%'