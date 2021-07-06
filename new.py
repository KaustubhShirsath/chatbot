import pickle
file = 'words.pkl'
fileobj = open(file,'rb')
x = pickle.load(fileobj)
print(x)