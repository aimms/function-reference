.. aimms:function:: EvaluateUnit(unit)

.. _EvaluateUnit:

EvaluateUnit
============

With the function :aimms:func:`EvaluateUnit` you can compute the numerical value
(with associated unit) of a given unit expression.

.. code-block:: aimms

    EvaluateUnit(
         unit                ! (input) scalar unit expression
         )

Arguments
---------

    *unit*
        A unit expression of which the numerical value (with associated unit)
        must be computed.

Return Value
------------

    The function returns the numerical value (with associated unit),
    corresponding to one unit of *unit*.



Example
-----------

Given the unit of measurement declarations:

.. code-block:: aimms


	Quantity SI_Time_Duration {
		BaseUnit: s;
		Conversions: {
			day->s : #-># * 86400,
			hour->s : #-># * 3600,
			minute->s : #-># * 60
		}
		Comment: "Expresses the value for the duration of periods.";
	}
	Quantity SI_Velocity {
		BaseUnit: m/s;
		Comment: "Expresses the value for the change in distance per time unit.";
	}
	Quantity SI_Length {
		BaseUnit: m;
		Conversions: {
			km->m : #-># * 1000,
			mile->m : #-># * 1609.344
		}
		Comment: "Expresses the value of a distance.";
	}
	Parameter _p_uv {
		Unit: m/s;
	}

The code

.. code-block:: aimms

	_p_uv := EvaluateUnit( unit(km/hour) );
	display _p_uv ; ! 0.278 ; ;

returns the conversion factor in ``[km/hour]``.



.. note::

    The function :aimms:func:`EvaluateUnit` is an extension of AIMMS' local unit
    override capabilities which allows computed unit expressions.

.. seealso::

    - Unit expressions are discussed in full detail in :doc:`advanced-language-components/units-of-measurement/index` of the Language Reference.
