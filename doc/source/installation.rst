.. _installation:

************
Installation
************

----
PyPI
----

Since SSPipeline is still in development, PyPi won't be up to date with the latest changes, however, you can still install using ``pip``:

.. code-block:: bash

    pip install sspipeline

This installs SSPipeline, along with all the necessary dependencies such as NumPy and SciPy.

-------------------
Development Version
-------------------

The latest development version of SSPipeline can be installed directly from GitHub

.. code-block:: bash

    pip install git+https://github.com/mussles/sspipeline.git


or you can fork the `SSPipeline GitHub repository <https://github.com/mussles/sspipeline>`_ and install SSPipeline on your local machine via

.. code-block:: bash

    git clone https://github.com/<your-username>/sspipeline.git
    cd sspipeline
    pip install .


------------
Dependencies
------------

SSPipeline has the following dependencies:

- `Python <https://www.python.org/>`_ >= 3.6
- `Click <http://click.pocoo.org/>`_
- `tqdm <https://pypi.python.org/pypi/tqdm>`_
- `NumPy <http://www.numpy.org/>`_
- `pandas <http://pandas.pydata.org/pandas-docs/stable/>`_
- `SciPy <https://www.scipy.org/>`_
- `matplotlib <http://matplotlib.org/>`_

When you install SSPipeline, these requirements are installed automatically.