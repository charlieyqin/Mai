from __future__ import absolute_import
import Cocoa
import Foundation
import os

class PBXNativeTarget(object):
    contents = {};
    
    def __init__(self, dictionary, project):
        self.contents = dictionary;