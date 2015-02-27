Mai
=======

External Xcode scheme build tool
--------------------------------

Mai is a wrapper around `xcodebuild` that makes it easier to create specialized builds that depend on ordering of schemes. Doing this using Xcode alone is quite challenging, and displays evidence undefined behavior with dependency resolution. Mai solves this problem by parsing Xcode workspace and project files to find any schemes (both shared and user) and allows you to build them sequentially. In addition, Mai can also over-ride existing build settings for specific schemes, much like having an additional xcconfig file.


Configuration Files
-------------------



Install
-------

To install, run `python setup.py install` optionally add `--user` to install it to the user's python install rather than the system


How To Use
----------


	usage: mai [-h] [-l] [-c CONFIG] [-a ACTION] filename

	Resolve target dependencies

	positional arguments:
	  filename                      path to xcodeproj or xcworkspace

	optional arguments:
	  -h, --help                    show this help message and exit
	  -l, --list                    list schemes
	  -c CONFIG, --config CONFIG    path to the build config file
	  -a ACTION, --action ACTION    action to perform: "build", "test", "analyze", or "archive"