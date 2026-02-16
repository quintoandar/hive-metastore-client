# Updating the Thrift Hive Metastore client

## Requirements

### The thrift service mapping 
Download the _hive_metastore.thrift_ (and its required thrift files if any, place them in the same directory).

These two files are the mapping for the Thrift Service that the Hive Metastore is built on: 
- [hive_metastore.thrift](https://github.com/apache/hive/blob/branch-3.0/standalone-metastore/src/main/thrift/hive_metastore.thrift)
- [fb303.thrift](https://github.com/apache/thrift/blob/master/contrib/fb303/if/fb303.thrift)

We are using the Hive Metastore version 3.0 ([branch-3.0](https://github.com/apache/hive/tree/branch-3.0/standalone-metastore))

### Thrift compiler (0.16.0)

This project uses **Thrift 0.16.0** for both the Python runtime and the code generator. You need the Thrift 0.16.0 **compiler** (CLI) installed to regenerate Python code from the `.thrift` files.

**Install options:**

- **macOS (Homebrew tap)** – older Thrift versions including 0.16 are available via a tap:
  ```shell
  brew tap cartman-kai/thrift
  brew install thrift@0.16
  ```
  After install, ensure `thrift` is on your PATH (the formula may install it as `thrift@0.16`; you can symlink or add the formula’s bin to PATH). Verify with:
  ```shell
  thrift --version
  ```
  You should see `Thrift version 0.16.0` (or 0.16.x).

- **Build from source** – See [Apache Thrift – Building from source](https://thrift.apache.org/docs/BuildingFromSource) and [OS X install](https://thrift.apache.org/docs/install/os_x.html). Download the [0.16.0 source](https://archive.apache.org/dist/thrift/0.16.0/thrift-0.16.0.tar.gz), then build and install with the documented dependencies (e.g. Boost, libevent, bison).

- **Docker** – Use the official image (requires Docker):
  ```shell
  docker run --rm -v "$(pwd)/thrift_files/source:/data" apache/thrift:0.16.0 thrift --gen py -o /data/gen-py /data/hive_metastore.thrift
  docker run --rm -v "$(pwd)/thrift_files/source:/data" apache/thrift:0.16.0 thrift --gen py -o /data/gen-py /data/fb303.thrift
  ```
  Generated code will appear under `thrift_files/source/gen-py/`. Then copy contents into `thrift_files/libraries/thrift_hive_metastore_client/` and `thrift_files/libraries/thrift_facebook_service/` and fix imports as in step 3 below.

**Verify:** Run `thrift --version` and confirm the output is 0.16.0 (or 0.16.x) before regenerating.

### Generating Python code

1 - With the Thrift 0.16.0 CLI installed and on your PATH, open the directory where the _hive_metastore.thrift_ (and others) is placed and run:
```shell
thrift --gen py hive_metastore.thrift
thrift --gen py fb303.thrift
```

2 - Now you have the new python code generated inside `gen-py`. Extract the classes and place them in the right directories (`thrift_files/libraries/thrift_hive_metastore_client/` from the hive_metastore output, `thrift_files/libraries/thrift_facebook_service/` from the fb303 output). Fix any imports so they use the `thrift_files.libraries.*` package names (see existing files for the pattern).

3 - The generated files are huge, therefore be sure that the generated files directory names are ignored in the make commands _style-check_ and _apply-lint_. So these files are not evaluated during the checks.

## Manual adjustments to Thrift source files

Some auto-generated code from Thrift communication with Hive Metastore can be changed to provide more features, thus allowing a more customized integration.

The following PRs change the Thrift base files and/or source files. Check whether they **need to be re-written** in case of re-generation by the previous steps:
- [#45](https://github.com/quintoandar/hive-metastore-client/pull/45) - Changing type, from I16 to I32, of `max_parts` parameter from `get_partitions` method.
