# go to parent path
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# go to ancestor path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "../../../")))
