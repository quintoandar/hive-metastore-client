# Changelog
All notable changes to this project will be documented in this file.

Preferably use **Added**, **Changed**, **Removed** and **Fixed** topics in each release or unreleased log for a better organization.

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