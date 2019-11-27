.. aimms:set:: AllAvailableCharacterEncodings

.. _AllAvailableCharacterEncodings:

AllAvailableCharacterEncodings
==============================

The predefined set :aimms:set:`AllAvailableCharacterEncodings` contains the names
of all character encodings available during the current AIMMS session.

.. code-block:: aimms

        Set AllAvailableCharacterEncodings {
            SubsetOf   :  AllCharacterEncodings;
            Index      :  IndexAvailableCharacterEncodings;
        }

Definition
----------

    The contents of the set :aimms:set:`AllAvailableCharacterEncodings` is the
    collection of all character encodings available during the current AIMMS
    session.

Updatability
------------

    The contents of the set can not be modified and is determined at AIMMS
    startup.

.. seealso::

    -  Paragraph Text files in the preliminaries of the language reference
       18.

    -  The encoding attribute of files, see 496.

    -  The set of all character encodings known to AIMMS: :aimms:set:`AllCharacterEncodings`.
