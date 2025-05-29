import os 

def diskUsage(path):
    total = os.path.getsize(path)
    if(os.path.isdir(path)):
        for fileName in os.listdir(path):
            total += diskUsage(os.path.join(path, fileName))
    print('{0:<7}'.format(total), path)
    return total

if __name__ == '__main__':
    path = os.getcwd()
    diskUsage(path)