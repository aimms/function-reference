.. aimms:procedure:: WriteXML(XMLFile, MappingFile[, Merge])

.. _WriteXML:

WriteXML
========

With the procedure :aimms:func:`WriteXML` you write an XML data file according to
a given user-defined XML format.

.. code-block:: aimms

    WriteXML(
            XMLFile,         ! (input) scalar string expression
            MappingFile,     ! (input) scalar string expression
            Merge            ! (optional) 0 or 1
            )

Arguments
---------

    *XMLFile*
        The name of the file to which the XML data must be written

    *MappingFile*
        The name of the file containing the mapping between the user-defined XML
        format and the identifiers in your model.

    *Merge (optional)*
        Indicates whether or not the contents of the file can be merged within
        another XML file.

Return Value
------------

    The procedure returns 1 if successful, or 0 otherwise.

    .. note::

        Notice that the ``merge`` attribute does *not* mean that the generated
        XML will be appended to the specified XML file. The latter will *always*
        be overwritten. If the *merge* argument is non-zero, AIMMS will omit the
        XML header from the generated file, allowing you to merge its contents
        into another XML document.

.. seealso::

    - The procedures :aimms:func:`GenerateXML`, :aimms:func:`ReadGeneratedXML`, :aimms:func:`ReadXML`. 
    - Writing user-defined XML data is discussed in full detail in :doc:`data-communication-components/reading-and-writing-xml-data/reading-and-writing-user-defined-xml-data` of the Language Reference.
