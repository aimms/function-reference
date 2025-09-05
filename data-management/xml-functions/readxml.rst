.. aimms:procedure:: ReadXML(XMLFile, MappingFile[, merge], SchemaFile)

.. _ReadXML:

ReadXML
=======

The procedure :aimms:func:`ReadXML` you can read an XML data file according to a
given user-defined XML format.

.. code-block:: aimms

    ReadXML(
            XMLFile,         ! (input) scalar string expression
            MappingFile,     ! (input) scalar string expression
            merge,           ! (optional) 0 or 1
            SchemaFile       ! (optional) scalar string expression
            )

Arguments
---------

    *XMLFile*
        The name of the file from which the XML data must be read

    *MappingFile*
        The name of the file containing the mapping between the user-defined XML
        format and the identifiers in your model.

    *merge (optional)*
        With this optional argument (default 0), you can choose whether you want
        to merge the data included in the XML file with the existing data, or
        overwrite any existing data (default)

    *SchemaFile*
        If you specify the name of a schema file through this argument, AIMMS
        will validate the contents of the XML data file against this schema
        prior to reading it into AIMMS.

Return Value
------------

    The procedure returns 1 if successful, or 0 otherwise.

    .. note::

        The namespace defined in the schema file (if specified) must match the
        namespace specified in the ``xmlns`` attribute of the root element in
        the XML data file.

.. seealso::

    - The procedures :aimms:func:`GenerateXML`, :aimms:func:`ReadGeneratedXML`, :aimms:func:`WriteXML`. 
    - Reading user-defined XML data is discussed in full detail in :doc:`data-communication-components/reading-and-writing-xml-data/reading-and-writing-user-defined-xml-data` of the Language Reference.
