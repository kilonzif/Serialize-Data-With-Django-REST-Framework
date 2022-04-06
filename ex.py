import collections

def getOD():
    x = collections.OrderedDict(
    [
        ('password', 'pass'), ('username', 'Steve'), ('first_name', 'c'), ('last_name', 'c'), ('email', 'c@user.com')]
    )
    
    print(x['username'])

getOD()