.. aimms:procedure:: ReadGeneratedXML(XMLFile[, merge])

.. _ReadGeneratedXML:

ReadGeneratedXML
================

The procedure :aimms:func:`ReadGeneratedXML` reads the contents of an
AIMMS-generated XML data file.

.. code-block:: aimms

    ReadGeneratedXML(
            XMLFile,      ! (input) scalar string expression
            merge         ! (optional) 0 or 1
            )

Arguments
---------

    *XMLFile*
        Name of the AIMMS-generated XML file to read.

    *merge (optional)*
        With this optional argument (default 0), you can choose whether you want
        to merge the data included in the XML file with the existing data, or
        overwrite any existing data (default)

Return Value
------------

    The procedure returns 1 if the XML file is read successfully, or 0
    otherwise.

.. seealso::

    The procedures :aimms:func:`GenerateXML`, :aimms:func:`ReadXML`, :aimms:func:`WriteXML`. Generating XML data is
    discussed in full detail in Section 30.3 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
