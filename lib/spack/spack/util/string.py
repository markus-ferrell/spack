##############################################################################
# Copyright (c) 2013, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Written by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://scalability-llnl.github.io/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License (as published by
# the Free Software Foundation) version 2.1 dated February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

def comma_list(sequence, article=''):
    if type(sequence) != list:
        sequence = list(sequence)

    if not sequence:
        return
    elif len(sequence) == 1:
        return sequence[0]
    else:
        out =  ', '.join(str(s) for s in sequence[:-1])
        out += ', '
        if article:
            out += article + ' '
        out += str(sequence[-1])
        return out

def comma_or(sequence):
    return comma_list(sequence, 'or')


def comma_and(sequence):
    return comma_list(sequence, 'and')
