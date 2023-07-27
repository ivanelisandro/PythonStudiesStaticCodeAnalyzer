from validators import ProjectValidator
import sys


start_path = sys.argv[1]

analyzer = ProjectValidator()
analyzer.run(start_path)
