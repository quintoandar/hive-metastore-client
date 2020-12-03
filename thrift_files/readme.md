# Updating the Thrift Hive Metastore client

## Requirements

### The thrift service mapping 
Download the _hive_metastore.thrift_ (and its required thrift files if any, place them in the same directory).

These two files are the mapping for the Thrift Service that the Hive Metastore is built on: 
- [hive_metastore.thrift](https://github.com/apache/hive/blob/branch-3.0/standalone-metastore/src/main/thrift/hive_metastore.thrift)
- [fb303.thrift](https://github.com/apache/thrift/blob/master/contrib/fb303/if/fb303.thrift)

We are using the Hive Metastore version 3.0 ([branch-3.0](https://github.com/apache/hive/tree/branch-3.0/standalone-metastore))

### Thrift package
 
1 - First you need to install the thrift package so you can "compile" the thrift file into python code. 
You can refer to these tutorial for installing it: https://thrift-tutorial.readthedocs.io/en/latest/installation.html. We used the Thrift latest version (0.14.0)

2 - After installing thrift cli, you should open the directory where the _hive_metastore.thrift_ (and others) is placed and run:
```shell
thrift --gen py hive_metastore.thrift
thrift --gen py fb303.thrift
```

3 - Now you have the new python code generated inside `gen-py`. Extract the classes and place them in the right directories.

4 - The generated files are huge, therefore be sure that the generated files directory names are ignored in the make commands _style-check_ and _apply-lint_. So these files are not evaluated during the checks.