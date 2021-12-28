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

By default the bot will upload the files to https://0x0.st/, you can change the server with::

    simplebot -a bot@example.com db -s simplebot_file2link/server "https://example.com"

Install
-------

To install run::

  pip install simplebot-file2link


.. _SimpleBot: https://github.com/simplebot-org/simplebot
