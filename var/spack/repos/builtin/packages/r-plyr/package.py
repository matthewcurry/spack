# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RPlyr(RPackage):
    """A set of tools that solves a common set of problems: you need to break a
    big problem down into manageable pieces, operate on each piece and then put
    all the pieces back together. For example, you might want to fit a model to
    each spatial location or time point in your study, summarise data by panels
    or collapse high-dimensional arrays to simpler summary statistics. The
    development of 'plyr' has been generously supported by 'Becton
    Dickinson'."""

    homepage = "http://had.co.nz/plyr"
    url      = "https://cloud.r-project.org/src/contrib/plyr_1.8.4.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/plyr"

    version('1.8.4', 'ef455cf7fc06e34837692156b7b2587b')

    depends_on('r@3.1.0:', type=('build', 'run'))
    depends_on('r-rcpp@0.11.0:', type=('build', 'run'))
