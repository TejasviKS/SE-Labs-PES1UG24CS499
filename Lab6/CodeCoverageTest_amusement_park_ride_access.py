import pytest
from amusement_park_ride_access import process_ride_admissions, inspect_safety_restraints

ADULT = {"height_cm": 150, "health_warning": False, "is_child": False}


def make_group(ride_type, patrons, has_fast_lane=False):
    return {
        "is_open": True,
        "ride_type": ride_type,
        "has_fast_lane": has_fast_lane,
        "patrons": patrons
    }


# Example test case:
def test_single_adult_family_ride():
    groups = [
        {
            "is_open": True,
            "ride_type": "family",
            "has_fast_lane": False,
            "patrons": [{"height_cm": 150, "health_warning": False, "is_child": False}]
        }
    ]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 10.0
    assert result["status"] == "COMPLETED"


# process_ride_admissions: input validation
def test_groups_not_a_list_raises_value_error():
    with pytest.raises(ValueError):
        process_ride_admissions("not a list", 5.0)


def test_negative_pass_fee_raises_value_error():
    with pytest.raises(ValueError):
        process_ride_admissions([], -1.0)


# process_ride_admissions: ride types
def test_closed_ride_is_skipped():
    groups = [{"is_open": False, "ride_type": "family", "patrons": [ADULT]}]
    result = process_ride_admissions(groups, 5.0)
    assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}


def test_roller_coaster_adult_ticket():
    result = process_ride_admissions([make_group("roller_coaster", [ADULT])], 5.0)
    assert result == {"total_revenue": 25.0, "status": "COMPLETED"}


def test_water_ride_adult_ticket():
    result = process_ride_admissions([make_group("water_ride", [ADULT])], 5.0)
    assert result == {"total_revenue": 18.0, "status": "COMPLETED"}


def test_unknown_ride_type_is_rejected():
    result = process_ride_admissions([make_group("haunted_house", [ADULT])], 5.0)
    assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}


# process_ride_admissions: patron rules
def test_invalid_height_patron_is_not_charged():
    patrons = [{"height_cm": 0}, ADULT]
    result = process_ride_admissions([make_group("family", patrons)], 5.0)
    assert result == {"total_revenue": 10.0, "status": "COMPLETED"}


def test_health_warning_on_roller_coaster_voids_whole_group():
    patrons = [ADULT, {"height_cm": 150, "health_warning": True}, ADULT]
    result = process_ride_admissions([make_group("roller_coaster", patrons)], 5.0)
    assert result == {"total_revenue": 0.0, "status": "ZERO_ADMISSIONS"}


def test_health_warning_on_family_ride_only_rejects_that_patron():
    patrons = [{"height_cm": 150, "health_warning": True}, ADULT]
    result = process_ride_admissions([make_group("family", patrons)], 5.0)
    assert result == {"total_revenue": 10.0, "status": "COMPLETED"}


def test_patron_under_height_limit_is_not_charged():
    patrons = [{"height_cm": 119}, ADULT]
    result = process_ride_admissions([make_group("family", patrons)], 5.0)
    assert result == {"total_revenue": 10.0, "status": "COMPLETED"}


def test_child_pays_sixty_percent():
    patrons = [{"height_cm": 130, "is_child": True}]
    result = process_ride_admissions([make_group("roller_coaster", patrons)], 5.0)
    assert result == {"total_revenue": 15.0, "status": "COMPLETED"}


def test_fast_lane_adds_express_pass_fee():
    groups = [make_group("family", [ADULT], has_fast_lane=True)]
    result = process_ride_admissions(groups, 5.0)
    assert result == {"total_revenue": 15.0, "status": "COMPLETED"}


def test_more_than_four_rejections_triggers_safety_audit():
    patrons = [{"height_cm": 100}] * 5 + [ADULT]
    result = process_ride_admissions([make_group("family", patrons)], 5.0)
    assert result == {"total_revenue": 10.0, "status": "SAFETY_AUDIT"}


# inspect_safety_restraints
def test_no_streams_returns_no_data():
    assert inspect_safety_restraints([]) == "NO_DATA"


def test_two_consecutive_unlatched_readings_lock_the_ride():
    assert inspect_safety_restraints([[1, 0, 0, 1]]) == "EMERGENCY_LOCK"


def test_non_consecutive_unlatched_readings_are_safe():
    assert inspect_safety_restraints([[0, 1, 0, 1], [1, 1]]) == "SAFE"
