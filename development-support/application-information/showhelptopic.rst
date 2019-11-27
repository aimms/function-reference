.. aimms:function:: ShowHelpTopic(topic[, helpfile])

.. _ShowHelpTopic:

ShowHelpTopic
=============

With the procedure :aimms:func:`ShowHelpTopic` you can jump to a specific help
topic in a help file.

.. code-block:: aimms

    ShowHelpTopic(
         topic,           ! (input) scalar string
         [helpfile]       ! (optional) scalar string
         )

Arguments
---------

    *topic*
        A string representing the help topic to jump to.

    *helpfile (optional)*
        A string representing the help file to open. If not specified, then
        AIMMS will use the help file that is specified in the project options.

.. note::

    AIMMS supports the following help file formats: WinHelp or WinHelp2000
    (``*.hlp``), compiled HTML Help (``*.chm``), and Acrobat Reader
    (``*.pdf``).
