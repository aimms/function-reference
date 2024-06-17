.. aimms:function:: Unit(unit)

.. _Unit:

Unit
====

The function :aimms:func:`Unit` returns the unit value of a given unit constant.

.. code-block:: aimms

    Unit(
         unit          ! (input) scalar unit constant
         )

Arguments
---------

    *unit*
        A unit constant of which the associated unit value must be computed

Return Value
------------

    The function returns the unit value of a unit constant *unit*.



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

	_up_speed := Unit( km/hour );
	display _up_speed ; ! _up_speed := [km/hour] ;

illustrates how to assign a literal unit to a unit parameter.

.. note::

    The function :aimms:func:`Unit` simply returns its argument. It exists to allow
    the use of numeric constants in computed unit expressions.

.. seealso::

    Unit expressions discussed in full detail in :doc:`advanced-language-components/units-of-measurement/index` of the Language
    Reference.
