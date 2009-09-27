# MolMod is a collection of molecular modelling tools for python.
# Copyright (C) 2007 - 2008 Toon Verstraelen <Toon.Verstraelen@UGent.be>
#
# This file is part of MolMod.
#
# MolMod is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# MolMod is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --


from molmod.io.sdf import SDFReader
from molmod.units import angstrom

import numpy, unittest


__all__ = ["SDFTestCase"]


class SDFTestCase(unittest.TestCase):
    def test_reader(self):
        sdf_reader = SDFReader("input/example.sdf")
        mol = sdf_reader.next()
        self.assertEqual(mol.title, "24978498")
        self.assertEqual(mol.size, 16)
        self.assertEqual(len(mol.graph.edges), 15)
        self.assert_(frozenset([1,14]) in mol.graph.edges)
        self.assertAlmostEqual(mol.coordinates[0,0]/angstrom,  2.8660)
        self.assertAlmostEqual(mol.coordinates[4,1]/angstrom, -1.9400)
        self.assertAlmostEqual(mol.coordinates[15,1]/angstrom, -2.5600)
        mol = sdf_reader.next()
        self.assertEqual(mol.title, "24978481")
        self.assertEqual(mol.size, 21)
        self.assertEqual(len(mol.graph.edges), 19)
        self.assert_(frozenset([3,9]) in mol.graph.edges)
        self.assertEqual(len(mol.graph.independent_nodes), 2)
        self.assertAlmostEqual(mol.coordinates[0,0]/angstrom, 2.2690)
        self.assertAlmostEqual(mol.coordinates[9,1]/angstrom, 2.5790)
        self.assertAlmostEqual(mol.coordinates[20,0]/angstrom, 1.7130)
        try:
            sdf_reader.next()
            self.fail("Expecting a StopIteration.")
        except StopIteration:
            pass

    def test_reader2(self):
        sdf_reader = SDFReader("input/CID_22898828.sdf")
        mol = sdf_reader.next()
        self.assertEqual(mol.title, "22898828")
        self.assertEqual(mol.size, 14)
        self.assertEqual(len(mol.graph.edges), 13)
        self.assert_(frozenset([4,6]) in mol.graph.edges)
        self.assertEqual(len(mol.graph.independent_nodes), 1)
        self.assertAlmostEqual(mol.coordinates[0,0]/angstrom, 6.8671)
        self.assertAlmostEqual(mol.coordinates[9,1]/angstrom, 0.2500)
        self.assertAlmostEqual(mol.coordinates[13,0]/angstrom, 12.6002)
        self.assert_((mol.formal_charges[:12]==-1).all())
        self.assert_((mol.formal_charges[12:]==0).all())

