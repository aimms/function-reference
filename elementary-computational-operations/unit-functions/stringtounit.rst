.. aimms:function:: StringToUnit(str)

.. _StringToUnit:

StringToUnit
============

With the function :aimms:func:`StringToUnit` you can compute a unit value
corresponding to a given string expression.

.. code-block:: aimms

    StringToUnit(
         str          ! (input) scalar string expression
         )

Arguments
---------

    *str*
        A string expression of which the associated unit value must be computed

Return Value
------------

    The function returns the associated unit value of *str*, or fails if the
    given string does not correspond to a string constant.



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

The code:

.. code-block:: aimms

	_sp_speed := "km/hour" ;
	_up_speed := StringToUnit( _sp_speed );
	display _up_speed ; ! _up_speed := [km/hour] ;

Shows the coversion of string ``"km/hour"`` to unit ``[km/hour]``.


.. seealso::

    Unit expressions discussed in full detail in :doc:`advanced-language-components/units-of-measurement/index` of the Language
    Reference.
