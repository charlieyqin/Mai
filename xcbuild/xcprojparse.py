import Cocoa
import Foundation
from .xcbpathobject import *
from .xcschemeparse import *
import os
import sys

class xcprojparse(object):
    path = {};
    contents = {};
    
    def __init__(self, xcproj_path):
        if xcproj_path.endswith('.xcodeproj') or xcproj_path.endswith('.pbproj'):
            self.path = xcbpathobject(xcproj_path, 'project.pbxproj');
        
            if os.path.exists(self.path.root_path) == True:
                # loading project file
                plistNSData, errorMessage = Foundation.NSData.dataWithContentsOfFile_options_error_(self.path.root_path, Foundation.NSUncachedRead, None);
                if errorMessage == None:
                    plistContents, plistFormat, errorMessage = Foundation.NSPropertyListSerialization.propertyListFromData_mutabilityOption_format_errorDescription_(plistNSData, Foundation.NSPropertyListMutableContainers, None, None);
                    if errorMessage == None:
                        self.contents = plistContents;
                    else:
                        print errorMessage;
                else:
                    print errorMessage;
            else:
                PrintUtils_debuglog([PrintUtils_Colour('red',True), PrintUtils_String('%s', 'Invalid xcodeproj file!'), PrintUtils_Colour('reset', True)]);
    
    def isValid(self):
        return self.contents != {};
    
    def objects(self):
        return self.contents['objects'];
    
    def rootObject(self):
        return self.objects()[self.contents['rootObject']];
    
    def targets(self):
        targets = [];
        target_ids = self.rootObject()['targets'];
        for target in target_ids:
            targets.append(self.objects()[target]);
        return targets;
    
    def schemes(self):
        schemes = [];
        # shared schemes
        shared_path = xcschemeparseGetSharedPath(self.path.obj_path);
        shared_schemes = xcschemeparseParseDirectoryForXCSchemes(shared_path);
        # user schemes
        user_path = xcschemeparseGetUserPath(self.path.obj_path);
        user_schemes = xcschemeparseParseDirectoryForXCSchemes(user_path);
        # merge schemes
        for scheme in shared_schemes + user_schemes:
            schemes.append(scheme);
        return schemes;