# Cookie Cutter Assert
This project is intended to allow TDD testing for cookie cutter templates.

It is a Command Line Interface (cli) tool that will scan a `test` folder in a cookie cutter project to execute test cases and run assertions about generated files and their contents

The [Cookie Cutter](https://cookiecutter.readthedocs.io/) template merge tool is a great tool for templating projects

## Installing cookiecutterassert

### Pre-requisites
* pipx
  * `brew install pipx`
  * `pipx ensurepath`
* pipx windows install tbd...

### Install command
TBD

## Executing tests
go to the root of your cookiecutter project and run `cookiecutterassert`
If all tests pass, the return code is 0 and you will see `All tests passed`
If tests fail, the return code is 1 and you will see `There were failing tests`
The first failed assertion in each folder will print its failure results and the rest of the assertions are skipped.

As each test scenario executes, you will see `---Starting tests for {SCENARIO FOLDER NAME}`


## Setting up a cookiecutter assert project
Your cookie cutter project should have the following structure
```
templatefolder
|   build.sh
|   cookiecutter.json
|   defaultConfig.yaml
|   testConfig.yaml
└───{{ cookiecutter.project_name }}
|       templatefiles
|       ...
|
└───build
|       generatedoutputfiles
|       ...
└───test
    └───testCase0
    |   |   assertions.yaml
    |   |   config.yaml
    |
    └───testCase1
        |   assertions.yaml
        |   config.yaml
        ...
```
* `test` is where your cookiecutterassert tests go
* `{{ cookiecutter.project_name }}` is the directory with the project template files
* `build` is where the output from executing `run.sh` goes
* `cookiecutter.json` is a required file and should have variable names with empty values
* `defaultConfig.yaml` is default cookie cutter variables across all test cases.  Individual test cases can override the variables completely or partially
* `testConfig.yaml` is a way to set values to your cookiecutter vairables for local tests using build.sh
* `build.sh` is used for local testing.  It merges the templates using cookiecutter and the values in testConfig.yaml
    * If you want to run any scripts on the generated files, you would do it here

## `test` folder
Each folder name under test should define a scenario and expected outcome in the folder name

cookiecutterassert will recursively find every folder under test with both `config.yaml` and `assertions.yaml`

cookiecutterassert then generates the template using `config.yaml` folder to a `build` folder in that test.

Finally, cookiecutterassert runs the assertions in the assertions.yaml against the generated files

The merge of the root level `defaultConfig.yaml` and the test case's `config.yaml` file will hold the variable values used in that test.

The combination of `defaultConfig.yaml` and folder-specific `config.yaml` must define all variables from cookiecutter.json

The `assertions.yaml` file holds the rules that are executed on the generated files

Files are generated for each test in the build folder of that test

## `assertions.yaml` file
Here is a sample
```
assertions:
  - pathExists foo.txt
  - pathExists bin/scripts
  - pathNotExists missingFile
  - fileMatches build.gradle expectedBuild.gradle
  - runScript MyApp ./gradlew clean build
  - fileContainsLine MyApp/foo this line should exist
  - fileDoesNotContainLine MyApp/foo this line should not exist
  - fileHasMatchingLine MyApp/foo ^lo+king\sfor.*$
  - fileDoesNotHaveMatchingLine MyApp/foo ^lo+king\sfor.*$
  - fileContainsSnippet MyApp/foo goodSnippet.txt
  - fileDoesNotContainSnippet MyApp/foo badSnippet.txt
```

### Rules
* pathExists {generatedFileOrFolderPathRelativeToRoot}
  * Passes if the path exists in the `build` folder after generation
* pathNotExists {generatedFileOrFolderPathRelativeToRoot}
  * Passes if the path does not exist in the `build` folder after generation
* fileMatches {generatedFileOrFolderPathRelativeToRoot}  {expectedFilePathRelativeToTestFolder}
  * Passes if contents of file generated matches the contents of the expected file
* runScript {generatedFolderToRunScriptIn}  {script}
  * executes script in specified folder under `build`
  * Passes if script has a 0 return code
* fileContainsLine {generatedFile} {line}
  * Passes if generated file in `build` contains the expected line
* fileDoesNotContainLine {generatedFile} {line}
  * Passes if generated file in `build` does not contain the expected line
* fileHasMatchingLine {generatedFile} {regex}
  * Passes if generated file in `build` has a line matching the regular expression
* fileDoesNotHaveMatchingLine {generatedFile} {regex}
  * Passes if generated file in `build` does not contain a line matching the regular expression
* fileContainsSnippet {generatedFile} {snippetFile}
  * Passes if all of the lines in the snippet file occur in order in the generated file
* fileDoesNotContainSnippet {generatedFile} {snippetFile}
  * Passes if the generated file does not have all of the lines of the snippet file in order

### Developing cookiecutterassert
see [Development guide](Development.md)