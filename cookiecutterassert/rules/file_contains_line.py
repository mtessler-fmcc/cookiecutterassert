# Copyright 2020 Ford Motor Company 

 

# Licensed under the Apache License, Version 2.0 (the "License"); 

# you may not use this file except in compliance with the License. 

# You may obtain a copy of the License at 

 

#     http://www.apache.org/licenses/LICENSE-2.0 

 

# Unless required by applicable law or agreed to in writing, software 

# distributed under the License is distributed on an "AS IS" BASIS, 

# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 

# See the License for the specific language governing permissions and 

# limitations under the License. 

import os.path
from cookiecutterassert.rules.rules_util import readLinesFromFile
from cookiecutterassert import messager


class FileContainsLineRule:

    def __init__(self, testFolder, fileName, line):
        self.line = line
        self.fileName = fileName
        self.testFolder = testFolder

    def execute(self, outputFolder):
        if (not os.path.exists(os.path.join(outputFolder, self.fileName))):
            messager.printError("assertion fileContainsLine {0} {1} failed. {0} does not exist in {2}.".format(
                self.fileName, self.line, outputFolder))
            return False

        fileLines = readLinesFromFile(self.fileName, folder=outputFolder)
        success = self.line in fileLines
        if not success:
            messager.printError("assertion fileContainsLine {0} {1} failed.  Matching line not found in {2}/{0}.".format(
                self.fileName, self.line, outputFolder))
        return success

    def __eq__(self, obj):
        return isinstance(obj, FileContainsLineRule) \
            and obj.line == self.line \
            and obj.fileName == self.fileName \
            and obj.testFolder == self.testFolder

    def __ne__(self, obj):
        return not self == obj

    def __str__(self):
        return "{0}: [testFolder={1}, fileName={2}, line={3}]".format(type(self).__name__, self.testFolder, self.fileName, self.line)

    def __repr__(self):
        return self.__str__()