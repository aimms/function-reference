.. aimms:set:: CurrentErrorMessage

.. _CurrentErrorMessage:

CurrentErrorMessage
===================

The predefined string parameter :aimms:set:`CurrentErrorMessage` contains a
description of the last runtime error that occurred during the execution
of an AIMMS model.

.. code-block:: aimms

        StringParameter CurrentErrorMessage;

Definition
----------

    The string parameter :aimms:set:`CurrentErrorMessage` contains a description of
    the last runtime error that occurred during the execution of an AIMMS
    model. It also contains the error message associated with errors
    occurring in AIMMS interface functions.

Updatability
------------

    The value of :aimms:set:`CurrentErrorMessage` can be modified programmatically
    from within an AIMMS model. Its value cannot be modified from within the
    end-user interface.

.. note::

    -  AIMMS never clears the contents :aimms:set:`CurrentErrorMessage`, but only
       updates its value whenever an error occurs.

    -  When AIMMS is called through the AIMMS API, :aimms:set:`CurrentErrorMessage`
       is the only way to retrieve a description of the last AIMMS runtime
       error when an execution request failed.

.. seealso::

    Error handling in the AIMMS API is discussed in more detail in :doc:`advanced-language-components/the-aimms-programming-interface/passing-errors-and-messages`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__. Error messages from interface functions
    are discussed in Section 17.3 from the `User's Guide <https://documentation.aimms.com/_downloads/AIMMS_user.pdf>`__.
