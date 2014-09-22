"""
LICENCE
-------
Copyright 2013 by Kitware, Inc. All Rights Reserved. Please refer to
KITWARE_LICENSE.TXT for licensing information, or contact General Counsel,
Kitware, Inc., 28 Corporate Drive, Clifton Park, NY 12065.

"""

class DatabaseInfo (object):
    """
    Encapsulation of database connection information meant for MongoDB. This
    may or may not have collection information (None if it doesn't).
    """

    def __init__(self, host, port, name, collection=None):
        """
        Create a database info encapsulation object

        >>> dbi = DatabaseInfo('localhost', 12345, 'foobar')
        >>> dbi.host
        'localhost'
        >>> dbi.port
        12345
        >>> dbi.name
        'foobar'
        >>> print dbi.collection
        None

        :param host:
        :type host:
        :param port:
        :type port:
        :param name:
        :type name:
        :param collection:
        :type collection:
        :return:
        :rtype:
        """
        self.host = str(host)
        self.port = int(port)
        self.name = str(name)
        self.collection = collection if collection is None else str(collection)

    def copy(self):
        """
        Create an exact duplicate of this object. This is a deep copy.

        >>> dbi = DatabaseInfo('localhost', 12345, 'foobar', 'baz')
        >>> dbi2 = dbi.copy()
        >>> dbi.host == dbi2.host
        True
        >>> dbi.port == dbi2.port
        True
        >>> dbi.name == dbi2.name
        True
        >>> dbi.collection == dbi2.collection
        True

        :return: a completely new DatabaseInfo instance with the same data as
            this one.
        :rtype: DatabaseInfo

        """
        return DatabaseInfo(self.host, self.port, self.name, self.collection)

    def __repr__(self):
        """
        >>> dbi = DatabaseInfo('localhost', 12345, 'foobar')
        >>> print dbi
        DatabaseInfo{host: localhost, port: 12345, name: foobar, collection: None}

        """
        return "DatabaseInfo{host: %s, port: %d, name: %s, collection: %s}" \
               % (self.host, self.port, self.name, self.collection)
