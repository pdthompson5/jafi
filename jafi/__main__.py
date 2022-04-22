
# What do I need this class to do:
# Open file, read contents, scanner -> parser -> interpreter 
# 
# 

import sys

class Jafi:

    def report_error(self, message: str):
        print("[Jafi Error] " + message, file=sys.stderr)

    def read_file(self, filename: str) -> str:
        try:
            jafi_file = open(filename)
            return jafi_file.read()
        except Exception as e:
            print("Could not find jafi file " + filename + ".")
            sys.exit(65)


    def run_file(self, filename: str):
        file_contents = self.read_file(filename)
        print(file_contents)
        
        
jafi = Jafi()
jafi.run_file("test.jaf")

