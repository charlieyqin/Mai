from __future__ import absolute_import

class AnalyzeAction(object):
    # contents = {};
    # children = [];
    # buildConfiguration = '';
    
    def __init__(self, action_xml):
        self.contents = action_xml;
        if 'buildConfiguration' in self.contents.keys():
            self.buildConfiguration = self.contents.get('buildConfiguration');