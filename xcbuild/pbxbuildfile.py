import Cocoa
import Foundation
import os

class pbxbuildfile(object):
    self.reference = {};
    
    def __init__(self, dictionary, project):
        if 'fileRef' in dictionary.keys():
            self.reference = dictionary['fileRef'];