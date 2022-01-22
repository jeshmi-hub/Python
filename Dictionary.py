data = {1:'Hershey', 2: 'Nutella', 4: 'Hairbo'} #in dictionary keys are used to fetch datas fetch values
print(data[4])

print(data.get(1))#get can also be used to fetch values in dictionary


print(data.get(3,'Not found'))
keys = ['gigi','Ruby','Tina']
values = ['Hadid','Rose','Aom']
datalist = dict(zip(keys,values))#using zip combines the key and values and dict converts them in dictionary
print(datalist)
print(datalist['gigi'])
datalist['gaylien'] = 'Alien'#adds more in the dictionary
print(datalist)


del datalist['gigi']
print(datalist)


prog = {'JS':['Atom','Sublime'],'CS': 'VS', 'Python':['Pycharm','Jupyter Notebook'],'Java':{'JSE':'Netbeans','JEE':'Intellij'}}
print(prog)

print(prog['Python'])
print(prog['Python'][1])
print(prog['Java'])
print(prog['Java']['JEE'])
