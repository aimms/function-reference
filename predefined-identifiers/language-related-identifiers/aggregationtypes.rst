.. aimms:set:: AggregationTypes

.. _AggregationTypes:

AggregationTypes
================

The predefined set :aimms:set:`AggregationTypes` contains the collection of all
possible aggregation types supported by the :aimms:procedure:`Aggregate` and :aimms:procedure:`DisAggregate`
functions.

.. code-block:: aimms

        Set AggregationTypes {
            Index      :  IndexAggregationTypes;
            Definition :  {
                data { summation, average,
                       maximum, minimum,
                       interpolation }
                }
            }

Definition
----------

    The set :aimms:set:`AggregationTypes` contains the collection of all possible
    aggregation types supported by the :aimms:procedure:`Aggregate` and :aimms:procedure:`DisAggregate` functions.

Updatability
------------

    The contents of the set cannot be modified.

.. note::

    Element parameters into :aimms:set:`AggregationTypes` can be used as the *type*
    argument of the :aimms:procedure:`Aggregate` and :aimms:procedure:`DisAggregate` functions.

.. seealso::

    The functions :aimms:procedure:`Aggregate` and :aimms:procedure:`DisAggregate`. Time-dependent aggregation and
    disaggregation is discussed in full detail in :doc:`advanced-language-components/time-based-modeling/data-conversion-of-time-dependent-identifiers` of the
    `Language Reference <https://documentation.aimms.com/_downloads/AIMMS_ref.pdf>`__.
