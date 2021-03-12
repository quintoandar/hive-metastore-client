# Changelog
All notable changes to this project will be documented in this file.

Preferably use **Added**, **Changed**, **Removed** and **Fixed** topics in each release or unreleased log for a better organization.

## [1.0.7](https://github.com/quintoandar/hive-metastore-client/releases/tag/1.0.7)
### Added
* Added method `add_partitions_to_table` to add partitions receiving an exception if some partition already exists 
  ([#57](https://github.com/quintoandar/hive-metastore-client/pull/57))

### Fixed
* Handled the partitions adding inside a loop (adding each partition individually) to fix a silent bug (if some 
  partition already existed, none of the list were added) ([#57](https://github.com/quintoandar/hive-metastore-client/pull/57))

## [1.0.6](https://github.com/quintoandar/hive-metastore-client/releases/tag/1.0.6)
### Added
* Added `get_partition_keys` method to get partitions with name and type ([#53](https://github.com/quintoandar/hive-metastore-client/pull/53))

### Changed
* Handled exception when table has no partitions in method `get_partition_values_from_table` ([#55](https://github.com/quintoandar/hive-metastore-client/pull/55))

## [1.0.5](https://github.com/quintoandar/hive-metastore-client/releases/tag/1.0.5)
### Added
* Added bulk_drop_partitions method ([#49](https://github.com/quintoandar/hive-metastore-client/pull/49))
* Added get_partition_values_from_table method ([#50](https://github.com/quintoandar/hive-metastore-client/pull/50))

### Changed
* Changed max_parts parameter from get_partitions method to int32 ([#45](https://github.com/quintoandar/hive-metastore-client/pull/45))

## [1.0.4](https://github.com/quintoandar/hive-metastore-client/releases/tag/1.0.4)
### Added
* Added create_external_table method ([#42](https://github.com/quintoandar/hive-metastore-client/pull/42))
* Added get_partition_keys_objects and get_partition_keys_names methods ([#43](https://github.com/quintoandar/hive-metastore-client/pull/43))

### Fixed
* Enforced type as EXTERNAL when creating external tables ([#41](https://github.com/quintoandar/hive-metastore-client/issues/41))

## [1.0.3](https://github.com/quintoandar/hive-metastore-client/releases/tag/1.0.3)
### Changed
* Handled exception when adding duplicate partitions ([#37](https://github.com/quintoandar/hive-metastore-client/pull/37))
* Removed method return for create_database_if_not_exists ([#39](https://github.com/quintoandar/hive-metastore-client/pull/39))

## [1.0.2](https://github.com/quintoandar/hive-metastore-client/releases/tag/1.0.2)
### Added
* Added create_database_if_not_exists method ([#35](https://github.com/quintoandar/hive-metastore-client/pull/35))

## [1.0.1](https://github.com/quintoandar/hive-metastore-client/releases/tag/1.0.1)
### Added
* Added drop_columns_from_table method ([#30](https://github.com/quintoandar/hive-metastore-client/pull/30))

### Changed
* Updated imports in project ([#27](https://github.com/quintoandar/hive-metastore-client/pull/27))
* Shifted to quintoandar's docker image ([#28](https://github.com/quintoandar/hive-metastore-client/pull/28))

### Fixed
* Fixed typo in the client's filename ([#33](https://github.com/quintoandar/hive-metastore-client/pull/33))

## [1.0.0](https://github.com/quintoandar/hive-metastore-client/releases/tag/1.0.0)
First modules and entities of Hive Metastore Client package.

### Added
* Adding thrift files in project ([#4](https://github.com/quintoandar/hive-metastore-client/pull/4))
* Adding thrift python files ([#9](https://github.com/quintoandar/hive-metastore-client/pull/9))
* Create clients main class ([#16](https://github.com/quintoandar/hive-metastore-client/pull/16) and [#10](https://github.com/quintoandar/hive-metastore-client/pull/10))
* Adding DatabaseBuilder ([#13](https://github.com/quintoandar/hive-metastore-client/pull/13))
* Adding TableBuilder, ColumnBuilder, SerDeInfoBuilder and StorageDescriptorBuilder ([#15](https://github.com/quintoandar/hive-metastore-client/pull/15))
* Adding PartitionBuilder and method `add_partitions_to_table` ([#17](https://github.com/quintoandar/hive-metastore-client/pull/17))
* Adding method `add_columns_to_table` ([#18](https://github.com/quintoandar/hive-metastore-client/pull/18))