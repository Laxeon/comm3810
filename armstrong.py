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
