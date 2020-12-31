# CRD operations on file-based-key-value-data-store

In this Python Program I build a file-based key-value data store that supports the basic CRD (create,read,delete) operations.

This data store is meant to be used as a local storage for one single process on one laptop.

The data store exposed as a library to clients that can instantiate a class and work with the data store.

this data store will support the following functinoal requirements.

it is initialized using an optional file path.
if one is not provided, it will create itself in a reasonable location on the laptop.
A new key-value pair can be added to the data store using the create operation.The key is always a string -capped at 32cgars. The value is always a json object which is also capped at 16kb.

if create is invoked for an existing key,an appropriate error must be returned.
A read on a key can be performed by providing the key,and receiving the value in response,as a json object.
A delete operation can be performed by providing the key.

Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.
