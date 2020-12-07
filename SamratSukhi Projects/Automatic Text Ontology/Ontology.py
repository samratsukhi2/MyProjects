import samrat as sam
import reex as r

pdffile='CF.pdf'
DataFilename='Data.txt'
freqn='Frequency.txt'
out='Fundamental_Of_Computer.owl'
core='Core.txt'

lin=0

'''1.  text Extraction on PDF content '''
# sam.textFromPDF(pdffile,DataFilename)
# print('text out')
# fr=sam.texttoFreq(sam.getText(DataFilename))
# fw=sam.mainwords(DataFilename)
# fw=fw.lower()
# fw=sam.removetoken(fw)
# sam.finfreq(fr,fw,core)

'''2.  Human inspection on Data'''

''' 3. Regular Expression Generation'''
r.apply(sam.getText(DataFilename),sam.getText(core),out)