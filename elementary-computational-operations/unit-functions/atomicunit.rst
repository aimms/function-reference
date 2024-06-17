.. aimms:function:: AtomicUnit(unit)

.. _AtomicUnit:

AtomicUnit
==========

With the function :aimms:func:`AtomicUnit` you can retrieve the atomic unit
expression corresponding to the unit expression passed as the argument
to the function.

.. code-block:: aimms

    AtomicUnit(
         unit                ! (input) scalar unit expression
         )

Arguments
---------

    *unit*
        A unit expression of which the associated atomic unit expression must be
        computed

Return Value
------------

    The function returns the atomic unit expression corresponding to *unit*.

.. note::

    The atomic unit expression associated with a given unit is the unit
    expression solely in terms of atomic unit symbols by which the given
    unit differs a constant scale factor only.


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
		Conversions: km->m : #-># * 1000;
		Comment: "Expresses the value of a distance.";
	}
	UnitParameter _up_atomic;

The code:

.. code-block:: aimms

	_up_atomic := AtomicUnit( km/hour );
	display _up_atomic ; ! _up_atomic := [m/s] ;

Returns the atomic units for speed.


.. seealso::

    Unit expressions are discussed in full detail in :doc:`advanced-language-components/units-of-measurement/index` of the
     Language Reference.
