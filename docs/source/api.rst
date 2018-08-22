.. _api:

************
Pipeline API
************

Gelman & Rubin
-------------------

All the below functions are implemented according to Gelman & Rubin 1996 [#gr1996]_.

.. autofunction:: pipeline.gelman_rubin.GR_diag

.. autofunction:: pipeline.gelman_rubin.psrf

.. autofunction:: pipeline.gelman_rubin.GR_result

Distributions
-------------------

.. autofunction:: pipeline.distributions.normal_logpost

.. autofunction:: pipeline.distributions.gev_logpost

Utils
-------------------

.. autofunction:: pipeline.utils.check_params

.. autofunction:: pipeline.utils.read_and_clean

.. autofunction:: pipeline.utils.log

.. rubric:: Footnotes

.. [#gr1996] Gelman, Andrew; Rubin, Donald B. Inference from Iterative Simulation Using Multiple Sequences. Statist. Sci. 7 (1992), no. 4, 457--472. doi:10.1214/ss/1177011136. https://projecteuclid.org/euclid.ss/1177011136