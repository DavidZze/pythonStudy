
import os

class PathStudy2:

    def __init__(self):
        pass

    def path_test(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        src_dir = os.path.dirname(script_dir)
        # module_dir = os.path.dirname(src_dir)
        # lib_dir = module_dir + "/lib"
        print script_dir
        print src_dir