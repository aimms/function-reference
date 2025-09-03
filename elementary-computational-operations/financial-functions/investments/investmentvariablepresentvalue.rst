.. aimms:function:: InvestmentVariablePresentValue(Value, InterestRate)

.. _InvestmentVariablePresentValue:

InvestmentVariablePresentValue
==============================

The function :aimms:func:`InvestmentVariablePresentValue` returns the net present
value for an investment based on a series of periodic cash flows at the
end of the periods and a constant interest rate.

.. code-block:: aimms

    InvestmentVariablePresentValue(
        Value,                   ! (input) one-dimensional numerical parameter
        InterestRate             ! (input) numerical expression
        )

Arguments
---------

    *Value*
        The periodic payments (positive or negative), which must be equally
        spaced in time and occur at the end of each period. The order of the
        payments in *Value* must be the same as the order in which the cash
        flows occur. *Value* is an one dimensional parameter of real numbers.
        *Value* should contain at least one nonzero number. *Value* given by
        positive numbers represent incoming amounts and *Value* given by
        negative numbers represent outgoing amounts.

    *InterestRate*
        The interest rate per period for the investment. *InterestRate* must be
        a numerical expression in the range :math:`(-1, 1)`.

Return Value
------------

    The function :aimms:func:`InvestmentVariablePresentValue` returns the net present
    value of an investment, which is the total value of all the future cash
    flows at the beginning of the first period.

Equation
--------

    The net present value :math:`v_p` is computed through the equation

    .. math:: v_p = \sum_{i=1}^n \frac{p_i}{(1+r)^i}

    \ where :math:`p_i` are the (variable) periodic payments, and :math:`r`
    is the (constant) interest rate.

.. note::

    -  When all payments are constant, the net present value computed here
       is equal to the negative value of the present value computed by the
       function :aimms:func:`InvestmentConstantPresentValue` with the future value set to 0.0.

    -  This function can be used in an objective function or constraint and
       the input parameters *Value* and *InterestRate* can be used as a
       variable.

    -  The function :aimms:func:`InvestmentVariablePresentValue` is similar to the
       Excel function ``NPV``.


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

with the following result in the listing file:

.. code-block:: aimms

    _p_npv := 987.553700 ;
      

.. seealso::

    *   The function :aimms:func:`InvestmentConstantPresentValue`.


