from __future__ import absolute_import

class BuildAction(object):
    contents = {};
    children = {};
    
    def __init__(self, action_xml):
        self.contents = action_xml;