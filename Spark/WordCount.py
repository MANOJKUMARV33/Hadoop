def printfunc(x):
    print 'Word "%s" occurs %d times' % (x[0], x[1])

infile = sc.textFile('/hone/spark/<myTextFile.txt>', 4)
rdd1 = infile.flatMap(lambda x: x.split())  
rdd2 = rdd2.map(lambda x: (x, 1)).reduceByKey(lambda x: x + y) 
print rdd2.toDebugString()
rdd2.foreach(printfunc)
