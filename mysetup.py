from distutils.core import setup
import py2exe
options = {"py2exe":{"bundle_files": 1，
                     "zipfile": None
                     }}
setup(windows=["demo.py"])