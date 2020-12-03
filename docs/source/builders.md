# Builders

Willing to isolate its dependencies from users code, this library implements 
the [builder pattern](https://refactoring.guru/design-patterns/builder/python/example).

So instead of manually creating the Thrift objects for dealing with the
Hive Metastore server, you can use the [builders](https://github.com/quintoandar/hive-metastore-client/tree/main/hive_metastore_client/builders).

Each builder reflects the Thrift object's characteristics that it is building.
For more information about the object particularities you can 
try finding more information in the [hive_metastore.thrift](https://github.com/quintoandar/hive-metastore-client/blob/main/thrift_files/source/hive_metastore.thrift) mapping.

You should always call the `.build()` at the end to get the desired
object.

Some objects (like the Thrift `Table`) are more complex and requires other 
objects as parameters.

To learn more in practice use cases, see Hive Metastore Client's [examples](https://github.com/quintoandar/hive-metastore-client/tree/main/examples).