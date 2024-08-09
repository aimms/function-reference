.. aimms:function:: InvestmentSingleFutureValue(PresentValue, PeriodicRate)

.. _InvestmentSingleFutureValue:

InvestmentSingleFutureValue
===========================

The function :aimms:func:`InvestmentSingleFutureValue` returns the future value,
the cash balance, of a payment made at this moment, present value, with
periodic interest rates.

.. code-block:: aimms

    InvestmentSingleFutureValue(
        PresentValue,            ! (input) numerical expression
        PeriodicRate             ! (input) one-dimensional numerical expression
        )

Arguments
---------

    *PresentValue*
        Payment made at the start of the first period. *PresentValue* must be a
        real number. If *PresentValue* is a negative number it represents an
        outgoing amount and when it is a positive number it represents an
        incoming amount.

    *PeriodicRate*
        Interest rates which differ per period. *PeriodicRate* is a
        one-dimensional parameter, which should contain at least one nonzero
        number. The periods must be equally spaced in time and the interest
        rates must be ordered.

Return Value
------------

    The function :aimms:func:`InvestmentSingleFutureValue` returns the future value of
    the present value, using the periodic interest rates.

Equation
--------

    The future value :math:`v_f` is computed through the equation

    .. math:: v_f = v_p\prod_{i=1}^n(1+r_i)

    \ where :math:`v_p` is the present value, and :math:`r_i` the variable,
    periodic interest rates.

.. note::

    -  This function can be used in an objective function or constraint and
       the input parameters *PresentValue* and *PeriodicRate* can be used as
       a variable.

    -  The function :aimms:func:`InvestmentSingleFutureValue` is similar to the Excel
       function ``FVSCHEDULE``.


Example
-------

Given the local declarations:

.. code-block:: aimms

    Set _s_years {
        SubsetOf: Integers;
        Index: _i_year;
    }
    Parameter _p_value {
        IndexDomain: _i_year;
    }
    Parameter _p_npv;

Net present value can be computed as follows:

.. code-block:: aimms

    _s_years := ElementRange(2005,2008);
    _p_value(_i_year) := ord(_i_year) * 100 + 50 ;
    _p_npv := InvestmentVariablePresentValue( _p_value, 0.07 );
    block where single_column_display := 1, listing_number_precision := 6 ;
        display _p_npv ;
    endblock ;

With the following result in the listing file:

.. code-block:: aimms

    _p_npv := 987.553700 ;
      

References
-----------

    *   Day count basis :ref:`methods<ff.dcb>`.
