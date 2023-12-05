import sys, os

print(os.getcwd())

os.system('echo hi!')
os.system('python3 /workspaces/math_modeling/lec_5_listcomp.py')

print('Python version is:', sys.version)
print(sys.path)
print(sys.platform)
print(dir(sys))
print(dir(os))
print(dir(print))
print(dir(1))