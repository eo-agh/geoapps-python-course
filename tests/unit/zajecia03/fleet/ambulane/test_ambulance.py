from geoapps.zajecia03.fleet.ambulance import Ambulance


class TestAmbulance:
    def test_ambulance_initialization(self):
        ambulance = Ambulance(
            id=1,
            vehicle_type="AZ124",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator", "stretcher"],
        )

        assert ambulance.id == 1
        assert ambulance.vehicle_type == "AZ124"
        assert ambulance.status == "available"
        assert ambulance.location == (50.095340, 19.920282)
        assert ambulance.medical_equipment == ["defibrillator", "stretcher"]

    def test_update_location(self):
        ambulance = Ambulance(
            id=1,
            vehicle_type="AZ124",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator"],
        )

        new_location = (50.095341, 19.920283)
        ambulance.update_location(new_location)
        assert ambulance.location == new_location

    def test_equality(self):
        ambulance1 = Ambulance(
            id=1,
            vehicle_type="AZ124",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator"],
        )

        ambulance2 = Ambulance(
            id=1,
            vehicle_type="AZ124",
            status="on_mission",  # different status
            location=(50.095341, 19.920283),  # different location
            medical_equipment=["stretcher"],  # different equipment
        )

        ambulance3 = Ambulance(
            id=2,  # different id
            vehicle_type="AZ124",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator"],
        )

        assert ambulance1 == ambulance2  # same id and vehicle_type
        assert ambulance1 != ambulance3  # different id

    def test_str_representation(self):
        ambulance = Ambulance(
            id=1,
            vehicle_type="AZ124",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator", "stretcher"],
        )

        expected_str = "Ambulance ID: 1, Type: AZ124, Status: available, Location: (50.09534, 19.920282), Equipment: defibrillator, stretcher"
        assert str(ambulance) == expected_str

    def test_validate_id(self):
        assert Ambulance.validate_id(123) is True
        assert Ambulance.validate_id(0) is False
        assert Ambulance.validate_id(-1) is False
        assert Ambulance.validate_id("123") is False
        assert Ambulance.validate_id(123.0) is False

    def test_instances_count(self):
        # Get initial count
        initial_count = int(Ambulance.get_instances_count().split(": ")[1])

        ambulance1 = Ambulance(
            id=1,
            vehicle_type="AZ124",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator"],
        )

        # Check if count increased by 1
        assert int(Ambulance.get_instances_count().split(": ")[1]) == initial_count + 1

        ambulance2 = Ambulance(
            id=2,
            vehicle_type="AZ2000",
            status="available",
            location=(50.095340, 19.920282),
            medical_equipment=["defibrillator"],
        )

        # Check if count increased by 1 again
        assert int(Ambulance.get_instances_count().split(": ")[1]) == initial_count + 2
