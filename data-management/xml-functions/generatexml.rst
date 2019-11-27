.. aimms:procedure:: GenerateXML(XMLFile, IdentifierSet[, Merge, SchemaFile])

.. _GenerateXML:

GenerateXML
===========

The procedure :aimms:func:`GenerateXML` generates XML output data for a given set
of AIMMS identifiers.

.. code-block:: aimms

    GenerateXML(
            XMLFile,         ! (input) scalar string expression
            IdentifierSet,   ! (input) set expression
            Merge,           ! (optional) 0 or 1
            SchemaFile       ! (optional) scalar string expression
            )

Arguments
---------

    *XMLFile*
        Name of the file to which the generated XML must be written.

    *IdentifierSet*
        A subset of the predefined set :aimms:set:`AllIdentifiers`, containing the set of
        identifiers for which XML output must be generated.

    *Merge (optional)*
        Indicates whether or not the contents of the file can be merged within
        another XML file.

    *SchemaFile (optional)*
        If this argument is specified, a schema corresponding to the generated
        XML data will be written to the specified file name. A namespace will be
        generated for this schema file, and added to the ``xmlns`` attribute of
        the root element of the generated XML file.

Return Value
------------

    The procedure returns 1 on success. or 0 on failure.

.. note::

    Notice that the ``Merge`` attribute does *not* mean that the generated
    XML will be appended to the specified XML file. The latter will *always*
    be overwritten. If the *Merge* argument is non-zero, AIMMS will omit the
    XML header from the generated file, allowing you to merge its contents
    into another XML document.

.. seealso::

    The procedures :aimms:func:`ReadGeneratedXML`, :aimms:func:`ReadXML`, :aimms:func:`WriteXML`. Generating XML data is
    discussed in full detail in Section 30.3 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
