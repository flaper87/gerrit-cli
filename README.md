gerrit-cli
==========

Gerrit CLI on top of python-gerrit


Usage
=====

    $ gerrit reviews list -l 3 --projects stackforge/marconi
    +-----------------------------------------------+--------------------+-----------------------+----------------+---------------------+-----------------------------------+------------------------------------+
    | Subject                                       | Project            | Topic                 | Owner          | Modified Time       | Reviews                           | URL                                |
    +-----------------------------------------------+--------------------+-----------------------+----------------+---------------------+-----------------------------------+------------------------------------+
    | fix(storage.mongodb): find_one() running slow | stackforge/marconi | bug/1218602           | Kurt Griffiths | 2013-09-06 23:57:11 | Name: Kurt Griffiths, Value: -2   | https://review.openstack.org/44560 |
    |                                               |                    |                       |                |                     | Name: Jenkins, Value: 1           |                                    |
    |                                               |                    |                       |                |                     | Name: Amit Gandhi, Value: 1       |                                    |
    | Move Unit tests under a unit package          | stackforge/marconi | refactor-system-tests | Flavio Percoco | 2013-09-06 22:40:15 | Name: Jenkins, Value: 1           | https://review.openstack.org/45046 |
    |                                               |                    |                       |                |                     | Name: Malini Kamalambal, Value: 1 |                                    |
    | Pull actual tests out of marconi/tests        | stackforge/marconi | refactor-system-tests | Flavio Percoco | 2013-09-06 22:37:58 | Name: Jenkins, Value: 1           | https://review.openstack.org/44475 |
    |                                               |                    |                       |                |                     | Name: Malini Kamalambal, Value: 1 |                                    |
    |                                               |                    |                       |                |                     | Name: Kurt Griffiths, Value: 2    |                                    |
    +-----------------------------------------------+--------------------+-----------------------+----------------+---------------------+-----------------------------------+------------------------------------+
