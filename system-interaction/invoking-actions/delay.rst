.. aimms:function:: Delay(delaytime)

.. _Delay:

Delay
=====

With the procedure :aimms:func:`Delay` you can block the execution of your model
for the indicated delay time. You can use this procedure, for instance,
when you want to display intermediate results on a page using the
procedure ``PageRefreshAll``.

.. code-block:: aimms

    Delay(
         delaytime          ! (input) scalar expression
         )

Arguments
---------

    *delaytime*
        The number of seconds that the execution should be blocked.

.. seealso::

    The procedure :aimms:func:`PageRefreshAll`.
