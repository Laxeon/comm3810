import itertools
class Armstrong:
    def __init__(self, inputF, inputDf, outputF, outputDf, FloMin, FloMax):
        self.inputF = inputF
        self.inputDf = inputDf
        self.outputF=outputF
        self.outputDf=outputDf
        self.FloMin=FloMin
        self.FloMax=FloMax
    def productOfMultiplexers(self):
        return (self.outputDf/float(self.inputDf))
    def primeFactors (self):
        n=self.productOfMultiplexers()
        I={2:0, 3:0, 5:0, 7:0, 11:0}
        for i in I.keys():
            while n%i==0:
                I[i]+=1
                n=n/i
        return (I)
    def MultiplierCombinaitons(self):
        I=self.primeFactors ()
        Ilist=[i for i in I.keys() for j in range(I[i])]
        stuff = Ilist
        productList=[]
        for L in range(0, len(stuff)+1):
            for subset in itertools.combinations(stuff, L):
                product=1
                for i in subset:
                    product=i*product
                    productList.append(product)
        return (sorted(set(productList)))
    def bestMatch(self):
        case1=case.outputF- case.productOfMultiplexers() * case.inputF 
        case2=-case.outputF +case.productOfMultiplexers() * case.inputF 
        case3=case.outputF +case.productOfMultiplexers() * case.inputF 
        for M2 in case.MultiplierCombinaitons():
            for c in [case1,case2,case3]:
                if c>0 and c/M2 < case.FloMax and c/M2>case.FloMin:
                    return(M2,c/M2)
                
        