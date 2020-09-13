REM Copyright 2020 Ford Motor Company 

 

REM Licensed under the Apache License, Version 2.0 (the "License"); 

REM you may not use this file except in compliance with the License. 

REM You may obtain a copy of the License at 

 

REM     http://www.apache.org/licenses/LICENSE-2.0 

 

REM Unless required by applicable law or agreed to in writing, software 

REM distributed under the License is distributed on an "AS IS" BASIS, 

REM WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 

REM See the License for the specific language governing permissions and 

REM limitations under the License. 

set PYTHON_CMD=python
!command -v python3 && set PYTHON_CMD=python3
echo %PYTHON_CMD%
%PYTHON_CMD% --version
%PYTHON_CMD% -m venv venv
venv\Scripts\activate.bat