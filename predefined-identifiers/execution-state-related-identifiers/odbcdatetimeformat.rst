.. aimms:stringparameter:: ODBCDateTimeFormat

.. _ODBCDateTimeFormat:

ODBCDateTimeFormat
==================

The predefined string parameter :aimms:stringparameter:`ODBCDateTimeFormat` defines, for each
identifier within an AIMMS model, the date-time conversion string.

.. code-block:: aimms

        StringParameter ODBCDateTimeFormat {
            IndexDomain  :  IndexIdentifiers;
        }

Definition
----------

    The string parameter :aimms:stringparameter:`ODBCDateTimeFormat` defines, for each identifier
    within an AIMMS model, the date-time format string, which AIMMS will use
    in converting AIMMS data to date-time columns in a database table and
    vice versa.

Updatability
------------

    The data of :aimms:stringparameter:`ODBCDateTimeFormat` can be modified both from within the
    model and the end-user interface.

.. note::

    The use of :aimms:stringparameter:`ODBCDateTimeFormat` to convert AIMMS data to date-time
    columns and vice versa, are not necessary for columns which are mapped
    onto AIMMS calendars. In that case, AIMMS is able to determine the
    conversion itself based on the timeslot format specified for the
    calendar.

.. seealso::

    The use of :aimms:stringparameter:`ODBCDateTimeFormat` is discussed in more detail in :doc:`data-communication-components/communicating-with-databases/dealing-with-date-time-values`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__. The format to which values of
    :aimms:stringparameter:`ODBCDateTimeFormat` should comply are discussed in :doc:`advanced-language-components/time-based-modeling/format-of-time-slots-and-periods`
