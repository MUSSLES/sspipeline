.. _contributing:

*****************
Contributor Guide
*****************

This guide is intended to get new users and contributors started with SSPipeline.

Many potential contributors will be scientists with much expert knowledge but 
potentially little experience with open-source code development. This guide is 
primarily aimed at this audience, helping to reduce the barrier to contribution.

Start using SSPipeline
----------------------

The best way to start understanding how SSPipeline is to use it.

For developing the code the home of SSPipeline is on github and you'll see that
a lot of this guide boils down to using that platform well. so visit the
following link and poke around the code, issues, and pull requests: `SSPipeline
on Github <https://github.com/MUSSLES/sspipeline>`_.

It's probably also worth visiting the `Github <https://github.com/>`_ home page
and going through the "boot camp" to get a feel for the terminology.

In brief, to give you a hint on the terminology to search for, the contribution
pattern is:

    1. Setup git/github if you don't have it.
    2. Fork SSPipeline on github.
    3. Checkout your fork on your local machine.
    4. Create a new branch locally where you will make your changes.
    5. Push the local changes to your own github fork.
    6. Create a pull request (PR) to the official SSPipeline repository.

Note: You cannot mess up the main SSPipeline project unless you have been promoted
to write access and the dev-team. So when you're starting out be confident to
play, get it wrong, and if it all goes wrong you can always get a fresh install
of SSPipeline!!

PS: If you choose to develop in Windows/Mac you may find `Github Desktop
<https://desktop.github.com>`_ useful.


Got a problem? -- ask!
----------------------

Open source projects are all about community - we put in much effort to make
good tools available to all and most people are happy to help others start out.
Everyone had to start at some point and the philosophy of these projects
centres around the fact that we can do better by working together.

Much of the conversation happens in 'public' using the 'issues' pages on 
`Github <https://github.com/MUSSLES/sspipeline/issues>`_ -- doing things in public can
be scary but it ensures that issues are identified and logged until dealt with. 
This is also a good place to make a proposal for some new feature or tool that 
you want to work on.


Good coding practice
--------------------

The most important aspects of good coding practice are: (1) to work in managable
branches, (2) develop good code style, (3) write tests for new functions, and (4)
document what the code does. Tips on these points are provided below.

Use git to work in managable branches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Git is an open source "version control" system that enables you to can separate out
your modifications to the code into many versions (called branches) and switch between 
them easily. Later you can choose which version you want to have integrated into SSPipeline.

You can learn all about Git `here <http://www.git-scm.com/about>`_!

The most important thing to separate your contributions so that each branch is small
advancement on the "master" code or on another branch. 

Get the style right
^^^^^^^^^^^^^^^^^^^

TODO

Writing tests
^^^^^^^^^^^^^

TODO

Write documentation
^^^^^^^^^^^^^^^^^^^

Documentation comes in two parts docstrings and user-guide documentation.

Docstrings -- written at the start of a function and give essential information
about how it should be used, such as which arguments can be passed to it and what
the syntax should be. The docstrings need to follow the `numpy specification 
<https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>`_, 
as shown in `this example <https://github.com/numpy/numpy/blob/master/doc/example.py>`_.

User-guide Documentation -- A description of the functionality of the code and how
to use it with examples and links to the relevant code.

Build the documentation -- To check the output of what you wrote, you can build
the documentation. There are two commands you will have to run in order to build the documentation correctly::

        make clean
        make html


Learn more
----------

1. HyperSpy's `contribution guide <http://hyperspy.org/hyperspy-doc/current/dev_guide.html#developer-guide>`__: a lot of nice information on how to contribute to a scientific Python project.
2. The Python programming language, `for beginners <https://www.python.org/about/gettingstarted/>`__.
