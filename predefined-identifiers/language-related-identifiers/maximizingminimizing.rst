.. aimms:set:: MaximizingMinimizing

.. _MaximizingMinimizing:

MaximizingMinimizing
====================

The predefined set :aimms:set:`MaximizingMinimizing` defines the set of possible
optimization directions of mathematical programs.

.. code-block:: aimms

        Set MaximizingMinimizing {
            SubsetOf   :  AllValueKeywords;
            Index      :  IndexMaximizingMinimizing;
            Definition :  data { maximize, minimize };
        }

Definition
----------

    The predefined set :aimms:set:`MaximizingMinimizing` defines the set of possible
    optimization directions that can be entered in the ``Direction``
    attribute of mathematical programs.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Element parameters into the set :aimms:set:`MaximizingMinimizing` can be entered
    in the ``Direction`` attribute of mathematical programs to allow dynamic
    choices of the optimization direction.

.. seealso::

    The set :aimms:set:`AllValueKeywords`. Mathematical programs are discussed in more detail in
    Section 15.1 of the `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
