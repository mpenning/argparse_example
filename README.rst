Overview
========

A complex argparse example with command groups, file handles, required arguments, and mutually exclusive arguments...

Help for commands
-----------------

::
    $ python script_example.py -h
    usage: script_example.py [-h] {create,append,secure,upload} ...

    Manage a foo

    positional arguments:
      {create,append,secure,upload}
                            commands
        create              Create a foo
        append              Append a foo
        secure              Secure a foo
        upload              Upload a foo

    optional arguments:
      -h, --help            show this help message and exit


Help for create command
-----------------------

::
    $ python script_example.py create -h
    usage: script_example.py create [-h] -f FILE [-b | -z]

    optional arguments:
      -h, --help            show this help message and exit

    required:
      -f FILE, --file FILE  Foo file name

    optional:
      -b, --bar             bar a created foo
      -z, --baz             baz a created foo
 

Help for append command
-----------------------

::
    $ python script_example.py append -h
    usage: script_example.py append [-h] -f FILE

    optional arguments:
      -h, --help            show this help message and exit

    required arguments:
      -f FILE, --file FILE  Foo file name


Help for secure command
-----------------------

::
    $ python script_example.py secure -h
    usage: script_example.py secure [-h] -f FILE -l {public,private}

    optional arguments:
      -h, --help            show this help message and exit

    required arguments:
      -f FILE, --file FILE  Foo file name
      -l {public,private}, --level {public,private}
                            Foo file security level


Help for upload command
-----------------------

::
    $ python script_example.py upload -h
    usage: script_example.py upload [-h] -f FILE

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  foo file name

