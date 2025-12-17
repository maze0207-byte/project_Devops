import pkgutil, sys, os
print('pkgutil module:', pkgutil)
print('file:', getattr(pkgutil, '__file__', None))
print('has get_loader:', hasattr(pkgutil,'get_loader'))
print('attrs:', [a for a in dir(pkgutil) if 'get' in a or 'loader' in a])
print('sys.path:', sys.path)
print('cwd:', os.getcwd())
