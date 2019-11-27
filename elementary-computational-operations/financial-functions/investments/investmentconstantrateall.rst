.. aimms:function:: InvestmentConstantRateAll(PresentValue, FutureValue, Payment, NumberPeriods, Type, Mode, NumberSolutions, Solutions)

.. _InvestmentConstantRateAll:

InvestmentConstantRateAll
=========================

The procedure :aimms:func:`InvestmentConstantRateAll` returns the interest rate(s)
for an investment based on periodic, constant payments and a constant
interest rate.

.. code-block:: aimms

    InvestmentConstantRateAll(
        PresentValue,            ! (input) numerical expression
        FutureValue,             ! (input) numerical expression
        Payment,                 ! (input) numerical expression
        NumberPeriods,           ! (input) numerical expression
        Type,                    ! (input) numerical expression
        Mode,                    ! (input) numerical expression
        NumberSolutions,         ! (output) numerical expression
        Solutions                ! (output) one-dimensional parameter
        )

Arguments
---------

    *PresentValue*
        The total amount that a series of future payments is worth at this
        moment. *PresentValue* must be a real number.

    *FutureValue*
        The cash balance you want to attain after the last payment is made.
        *FutureValue* must be a real number.

    *Payment*
        The periodic payment for the investment. *Payment* must be a real
        number.

    *NumberPeriods*
        The total number of payment periods for the investment. *NumberPeriods*
        must be a positive integer.

    *Type*
        Indicates when payments are due. :math:`Type = 0`: Payments are due at
        the end of each period. :math:`Type = 1`: Payments are due at the
        beginning of each period.

    *Mode*
        Indicates whether all the solutions need to be found or just one.
        :math:`Mode = 0`: the search for solutions stops after one solution is
        found. :math:`Mode = 1`: the search for solutions continues till all
        solutions are found.

    *NumberSolutions*
        The number of solutions found. If :math:`Mode = 0` *NumberSolutions*
        will always be :math:`1`.

    *Solutions*
        There is not always a unique solution for *InterestRate*. Dependent on
        *Mode* one solution or all the solutions will be given. Solutions
        smaller than :math:`-1` are not supposed to be relevant, so the search
        for solutions is limited to the area greater than :math:`-1`.

.. note::

    -  When you want to use this procedure in an objective function or
       constraint you have to use ``InvestmentConstantRate``.

    -  The function :aimms:func:`InvestmentConstantRateAll` is similar to the Excel
       function ``RATE``.

.. seealso::

    General :ref:`equations<FF.inveq>` for investments with constant, periodic payments.
