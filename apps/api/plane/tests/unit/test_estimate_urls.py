# Copyright (c) 2023-present Plane Software, Inc. and contributors
# SPDX-License-Identifier: AGPL-3.0-only
# See the LICENSE file for details.

"""
The public API v1 estimate routes must be registered.

See: https://github.com/makeplane/plane/issues/9933
"""

import uuid

import pytest
from django.urls import resolve

from plane.api.views.estimate import (
    EstimatePointDetailAPIEndpoint,
    EstimatePointListCreateAPIEndpoint,
    ProjectEstimateAPIEndpoint,
)

PROJECT = f"/api/v1/workspaces/acme/projects/{uuid.uuid4()}/estimates/"
POINTS = f"{PROJECT}{uuid.uuid4()}/estimate-points/"


@pytest.mark.unit
@pytest.mark.parametrize(
    "url, view",
    [
        (PROJECT, ProjectEstimateAPIEndpoint),
        (POINTS, EstimatePointListCreateAPIEndpoint),
        (f"{POINTS}{uuid.uuid4()}/", EstimatePointDetailAPIEndpoint),
    ],
)
def test_estimate_routes_resolve(url, view):
    assert resolve(url).func.view_class is view
