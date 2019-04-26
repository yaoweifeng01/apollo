.. Copyright (c) 2016, Johan Mabille, Sylvain Corlay and Wolf Vollprecht


Installation
============


Download the source code
-----------------------

.. code::

    git clone https://github.com/ApolloAuto/apollo.git


Complier
-----------------------
.. code::

    cd /apollo
    bash docker/scripts/dev_start.sh
    bash docker/scripts/dev_into.sh
    bash apollo.sh build

Configuration Cyber RT environment
-----------------------
.. code::
    
    cd /apollo/cyber
    source setup.bash

Check and run
-----------------------
.. code::
    
    cd /apollo/cyber
    source setup.sh
    cyber_launch start modules/monitor/launch/monitor.launch
