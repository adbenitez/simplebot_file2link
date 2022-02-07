File2Link
=========

.. image:: https://img.shields.io/pypi/v/simplebot_file2link.svg
   :target: https://pypi.org/project/simplebot_file2link

.. image:: https://img.shields.io/pypi/pyversions/simplebot_file2link.svg
   :target: https://pypi.org/project/simplebot_file2link

.. image:: https://pepy.tech/badge/simplebot_file2link
   :target: https://pepy.tech/project/simplebot_file2link

.. image:: https://img.shields.io/pypi/l/simplebot_file2link.svg
   :target: https://pypi.org/project/simplebot_file2link

.. image:: https://github.com/adbenitez/simplebot_file2link/actions/workflows/python-ci.yml/badge.svg
   :target: https://github.com/adbenitez/simplebot_file2link/actions/workflows/python-ci.yml

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

A `SimpleBot`_ plugin that will upload to the cloud any file sent by the users in private.

You can set a list of URLs separated by space, that the bot can use to upload the file, the bot will pick
one randomly, you can change the default list with::

    simplebot -a bot@example.com db -s simplebot_file2link/server "https://example.com https://example2.org"

Install
-------

To install run::

  pip install simplebot-file2link


.. _SimpleBot: https://github.com/simplebot-org/simplebot
