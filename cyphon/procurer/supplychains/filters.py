# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
"""
Defines filters for SupplyChains.
"""

# third party
from django_filters.rest_framework import DjangoFilterBackend

# local
from .models import SupplyChain


class SupplyChainFilterBackend(DjangoFilterBackend):
    """
    Provides a filter backend to only show |SupplyChains| for which the
    current user has an available |Quartermaster|.
    """

    def filter_queryset(self, request, queryset, view):
        """Return a filtered queryset.

        Implements `custom filtering`_.

        Parameters
        ----------
        request : Request
             A |Request| for a resource.

        queryset : QuerySet
            A |QuerySet| to be filtered.

        view : ModelViewSet
            A |ModelViewSet|.

        Returns
        -------
        QuerySet
            A |QuerySet| filtered to only show |SupplyChains| for which
            the current user has an available |Quartermaster|.

        """
        user = request.user
        return SupplyChain.objects.filter_by_user(user).distinct()