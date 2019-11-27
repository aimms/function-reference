.. aimms:set:: ASCIIUnicodeCharacterEncodings

.. _ASCIIUnicodeCharacterEncodings:

ASCIIUnicodeCharacterEncodings
==============================

The predefined set :aimms:set:`ASCIIUnicodeCharacterEncodings` is the union of
``ASCIICharacterEncodings`` and ``UnicodeCharacterEncodings``.

.. code-block:: aimms

        Set ASCIIUnicodeCharacterEncodings {
            SubsetOf   :  AllCharacterEncodings;
            Index      :  IndexAvailableCharacterEncodings;
        }

Definition
----------

    The contents of the set :aimms:set:`ASCIIUnicodeCharacterEncodings` is the union
    of ``ASCIICharacterEncodings`` and ``UnicodeCharacterEncodings``.

Updatability
------------

    The contents of the set can not be modified and is determined at AIMMS
    startup.

.. seealso::

    -  Paragraph Text files in the preliminaries of the language reference
       18.

    -  The encoding attribute of files, see 496.

    -  The set of all character encodings known to AIMMS: :aimms:set:`AllCharacterEncodings`.
