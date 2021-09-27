.. aimms:set:: CurrentPageNumber

.. _CurrentPageNumber:

CurrentPageNumber
=================

The predefined parameter :aimms:set:`CurrentPageNumber` contains current page
number used by AIMMS when printing print pages.

.. code-block:: aimms

        Parameter CurrentPageNumber;

Definition
----------

    The predefined parameter :aimms:set:`CurrentPageNumber` contains current page
    number used by AIMMS when printing print pages.

Updatability
------------

    AIMMS will automatically reset the value :aimms:set:`CurrentPageNumber` to 1 at
    the following times:

    -  before printing a print page using the **File-Print** menu,

    -  before printing a print page using the :aimms:func:`PrintPage` function outside of
       a pair of calls to the functions :aimms:func:`PrintStartReport` and :aimms:func:`PrintEndReport`, and

    -  just after calling the function :aimms:func:`PrintStartReport`.

    The value of :aimms:set:`CurrentPageNumber` can be modified programmatically from
    within the AIMMS model.

.. note::

    According to the list of rules above, modifying the value of
    :aimms:set:`CurrentPageNumber` will only have an effect of the page numbers
    printed on print pages within a pair of calls to :aimms:func:`PrintStartReport` and
    :aimms:func:`PrintEndReport`.

.. seealso::

    The functions :aimms:func:`PrintPage`, :aimms:func:`PrintStartReport`, :aimms:func:`PrintEndReport`. Print pages are discussed
    in :doc:`miscellaneous/project-settings-and-options/print-configuration`
