.. aimms:set:: AllIdentifierTypes

.. _AllIdentifierTypes:

AllIdentifierTypes
==================

The predefined set :aimms:set:`AllIdentifierTypes` contains the names of all
possible identifier types.

.. code-block:: aimms

        Set AllIdentifierTypes {
            Index      :  IndexIdentifierTypes;
        }

Definition
----------

    The predefined set :aimms:set:`AllIdentifierTypes` contains the names of all
    possible identifier types.

Updatability
------------

    The contents of the set can not be modified; it has the following fixed
    contents: 

    .. code-block:: aimms

            AllIdentifierTypes := data 
            { set                       ,
              calendar                  ,
              horizon                   ,
              index                     ,
              parameter                 ,
              'element parameter'       ,
              'string parameter'        ,
              'unit parameter'          ,
              variable                  ,
              'element variable'        ,
              'complementarity variable',
              constraint                ,
              arc                       ,
              node                      ,
              'uncertainty variable'    ,
              'uncertainty constraint'  ,
              activity                  ,
              resource                  ,
              'mathematical program'    ,
              macro                     ,
              assertion                 ,
              'database table'          ,
              'database procedure'      ,
              file                      ,
              procedure                 ,
              function                  ,
              quantity                  ,
              convention                ,
              LibraryModule             ,
              module                    ,
              section                   ,
              declaration               } ;

.. seealso::

    -  The sets :aimms:set:`AllAttributeNames` and :aimms:set:`AllSuffixNames`.

    -  Model edit functions, see :doc:`advanced-language-components/model-structure-and-modules/runtime-libraries-and-the-model-edit-functions` of the `Language Reference <https://documentation.aimms.com/language-reference/index.html>`__.

    -  The functions :aimms:func:`me::ChangeType` and :aimms:func:`IdentifierType`.
