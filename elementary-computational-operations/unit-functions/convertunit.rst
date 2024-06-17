.. aimms:function:: ConvertUnit(unit, convention)

.. _ConvertUnit:

ConvertUnit
===========

With the function :aimms:func:`ConvertUnit` you can compute the associated unit
value of a unit expression with respect to a given convention.

.. code-block:: aimms

    ConvertUnit(
         unit,                ! (input) scalar unit expression
         convention           ! (input) element expression
         )

Arguments
---------

    *unit*
        A unit expression of which the associated unit value in the given
        convention must be computed

    *convention*
        An element expression in to :aimms:set:`AllConventions`, representing the convention with
        respect to which a unit value must be computed.

Return Value
------------

    The function returns the associated unit value of *unit* with respect to
    *convention*.


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
	Convention cnv_metric {
		PerQuantity: {
			SI_Length        : m,
			SI_Time_Duration : s,
			SI_Velocity      : m/s
		}
	}
	Convention cnv_imperial {
		PerQuantity: SI_Length : mile;
	}

The code:

.. code-block:: aimms

	_up_cnv := ConvertUnit( unit(km/hour), cnv_imperial );
	display _up_cnv ; ! _up_cnv := [mile/hour] ;

Returns the speed according to the imperial convention.


.. seealso::

    Unit expressions and conventions are discussed in full detail in :doc:`advanced-language-components/units-of-measurement/index`
    of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.
