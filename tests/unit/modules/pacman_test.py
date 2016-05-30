# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Eric Vz <eric@base10.org>`
'''

# Import Python Libs
from __future__ import absolute_import

# Import Salt Testing Libs
from salttesting import TestCase, skipIf
from salttesting.mock import (
    MagicMock,
    patch,
    NO_MOCK,
    NO_MOCK_REASON
)

from salttesting.helpers import ensure_in_syspath

ensure_in_syspath('../../')

# Import Salt Libs
from salt.modules import pacman
from salt.exceptions import CommandExecutionError

@skipIf(NO_MOCK, NO_MOCK_REASON)
class PacmanTestCase(TestCase):
    '''
    Test cases for salt.modules.pacman
    '''

    def setUp(self):
        pacman.__salt__ = {}
        pacman.__context__ = {}


    def test_list_pkgs(self):
        '''
        Test if it list the packages currently installed in a dict
        '''
        cmdmock = MagicMock(return_value='A 1.0\nB 2.0')
        sortmock = MagicMock()
        stringifymock = MagicMock()
        with patch.dict(pacman.__salt__, {'cmd.run': cmdmock, 'pkg_resource.add_pkg': self._add_pkg, 'pkg_resource.sort_pkglist': sortmock, 'pkg_resource.stringify': stringifymock}):
            self.assertDictEqual(pacman.list_pkgs(), {'A': ['1.0'], 'B': ['2.0']})
        sortmock.assert_called_once()
        stringifymock.assert_called_once()


    def test_list_pkgs_as_list(self):
        '''
        Test if it list the packages currently installed in a dict
        '''
        cmdmock = MagicMock(return_value='A 1.0\nB 2.0')
        sortmock = MagicMock()
        stringifymock = MagicMock()
        with patch.dict(pacman.__salt__, {'cmd.run': cmdmock, 'pkg_resource.add_pkg': self._add_pkg, 'pkg_resource.sort_pkglist': sortmock, 'pkg_resource.stringify': stringifymock}):
            self.assertDictEqual(pacman.list_pkgs(True), {'A': ['1.0'], 'B': ['2.0']})
        sortmock.assert_called_once()
        stringifymock.assert_not_called()
        


    ''' 
    Helper methods for test cases
    '''
    def _add_pkg(self, pkgs, name, version):
        pkgs.setdefault(name, []).append(version)



if __name__ == '__main__':
    from integration import run_tests
    run_tests(PacmanTestCase, needs_daemon=False)
