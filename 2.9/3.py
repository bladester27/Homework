import pickle

mag = {'alcohol': 20, 'vegetables': 100, 'Fruits': 70}
with open('magazine.json', 'wb') as f:
    pickle.dump(mag, f, protocol=3, fix_imports=True)

