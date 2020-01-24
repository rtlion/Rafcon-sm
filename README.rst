rtl_rafcon_sm
====
state machines for robocup@home (and other competitions) challenges/tasks/tests over the years

Dev (show) branch
====
Here are all state machine which are not released and still under development!

RAFCON
======

A little introduction to Rafcon (taken from the original rafcon github)

.. figure:: https://raw.githubusercontent.com/DLR-RM/RAFCON/master/documents/assets/Screenshot_Drill_Skill.png
   :figwidth: 100%
   :width: 800px
   :align: left
   :alt: Screenshot showing RAFCON with a big state machine
   :target: documents/assets/Screenshot_Drill_Skill.png?raw=true

* Documentation: Hosted on `Read the Docs <http://rafcon.readthedocs.io/en/latest/>`_
* Homepage: `DLR-RM.github.io/RAFCON/ <https://dlr-rm.github.io/RAFCON/>`_
* License: `EPL <https://github.com/DLR-RM/RAFCON/blob/master/LICENSE>`_

Develop your robotic tasks using an intuitive graphical user interface
----------------------------------------------------------------------

RAFCON uses hierarchical state machines, featuring concurrent state execution, to represent robot programs.
It ships with a graphical user interface supporting the creation of state machines and
contains IDE like debugging mechanisms. Alternatively, state machines can programmatically be generated
using RAFCON's API.

Universal application

  RAFCON is written in Python, can be extended with plugins and is hard- and middleware independent.

Visual programming

  The sophisticated graphical editor can be used for the creation, execution and debugging of state machines.

Collaborative working

  Share and reuse your state machines in form of libraries, stored as JSON strings in text files.

.. figure:: https://raw.githubusercontent.com/DLR-RM/RAFCON/master/documents/assets/RAFCON-sm-creation-preview.gif
   :figwidth: 100%
   :width: 570px
   :align: left
   :alt: Example on how to create a simple state machine

Rafcon/State Machine Preview Picutures
=====
To give an Idea how the state machine looks like the following picutures represents different state machines, which we developed using rafcon.

Receptionist
=====
An example of our current solution of Receptionist

.. figure:: https://github.com/rtlion/Rafcon-sm/blob/master/receptionist.png
   :figwidth: 100%
   :width: 800px
   :align: left
   :alt: Screenshot showing RAFCON with the receptionist challenge
   :target: receptionist.png?raw=true

Take out the Garbage
=====
An example of our current solution of Take out the garbage

.. figure:: https://github.com/rtlion/Rafcon-sm/blob/master/take_out_garbage.png
   :figwidth: 100%
   :width: 800px
   :align: left
   :alt: Screenshot showing RAFCON with the take out the garbage challenge
   :target: take_out_the_garbage.png?raw=true

Drop off thrash (from Take out the garbage)
=====
An example of our current solution of drop off thrash, which gets used as a library in take out the garbage)

.. figure:: https://github.com/rtlion/Rafcon-sm/blob/master/drop_off_thrash.png
   :figwidth: 100%
   :width: 800px
   :align: left
   :alt: Screenshot showing RAFCON with a drop off thrash library
   :target: drop_off_thrash.png?raw=true
