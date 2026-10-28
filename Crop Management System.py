"""
CROP MANAGEMENT SYSTEM
An Object-Oriented Programming (OOP) project in Python.

Features:
- Add and view crop records
- Search for a crop by ID
- Update crop details and growth status
- Record harvest quantities
- Delete crop records
- Save and load records from a JSON file

Run:
    python Crop_Management_System.py

The program stores data in crop_records.json in the same folder.
"""

import json
from pathlib import Path
from datetime import datetime


DATA_FILE = Path(__file__).with_name("crop_records.json")


class Crop:
    """Represents one crop record on a farm."""

    def __init__(
        self,
        crop_id,
        crop_name,
        variety,
        field_name,
        planting_date,
        expected_harvest_date,
        quantity_planted,
        status="Planted",
        harvest_quantity=0.0,
        notes=""
    ):
        self.crop_id = str(crop_id).strip()
        self.crop_name = str(crop_name).strip()
        self.variety = str(variety).strip()
        self.field_name = str(field_name).strip()
        self.planting_date = planting_date
        self.expected_harvest_date = expected_harvest_date
        self.quantity_planted = float(quantity_planted)
        self.status = status
        self.harvest_quantity = float(harvest_quantity)
        self.notes = str(notes).strip()

    def to_dict(self):
        """Convert a Crop object into a dictionary for JSON storage."""
        return {
            "crop_id": self.crop_id,
            "crop_name": self.crop_name,
            "variety": self.variety,
            "field_name": self.field_name,
            "planting_date": self.planting_date,
            "expected_harvest_date": self.expected_harvest_date,
            "quantity_planted": self.quantity_planted,
            "status": self.status,
            "harvest_quantity": self.harvest_quantity,
            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Crop object from a stored dictionary."""
        return cls(**data)

    def display(self):
        """Return a readable description of the crop."""
        return (
            f"Crop ID: {self.crop_id}\n"
            f"Crop name: {self.crop_name}\n"
            f"Variety: {self.variety or 'Not specified'}\n"
            f"Field: {self.field_name}\n"
            f"Planting date: {self.planting_date}\n"
            f"Expected harvest date: {self.expected_harvest_date}\n"
            f"Quantity planted: {self.quantity_planted:g} units\n"
            f"Status: {self.status}\n"
            f"Harvest quantity: {self.harvest_quantity:g} units\n"
            f"Notes: {self.notes or 'None'}"
        )


class CropManagementSystem:
    """Manages crop records and persistent storage."""

    VALID_STATUSES = ("Planned", "Planted", "Growing", "Ready for Harvest", "Harvested")

    def __init__(self, data_file=DATA_FILE):
        self.data_file = Path(data_file)
        self.crops = {}
        self.load_records()

    def load_records(self):
        """Load saved crop records; start with an empty list if no file exists."""
        if not self.data_file.exists():
            self.crops = {}
            return
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                records = json.load(file)
            self.crops = {
                str(item["crop_id"]): Crop.from_dict(item)
                for item in records
            }
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Warning: saved data could not be loaded ({error}). Starting with no records.")
            self.crops = {}

    def save_records(self):
        """Save all crop records to JSON."""
        records = [crop.to_dict() for crop in self.crops.values()]
        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

    def add_crop(self, crop):
        if crop.crop_id in self.crops:
            raise ValueError("A crop with that ID already exists.")
        self.crops[crop.crop_id] = crop
        self.save_records()

    def get_crop(self, crop_id):
        return self.crops.get(str(crop_id).strip())

    def list_crops(self):
        return list(self.crops.values())

    def update_status(self, crop_id, status):
        if status not in self.VALID_STATUSES:
            raise ValueError("Choose a valid crop status.")
        crop = self.get_crop(crop_id)
        if crop is None:
            raise KeyError("Crop ID was not found.")
        crop.status = status
        self.save_records()
        return crop

    def update_notes(self, crop_id, notes):
        crop = self.get_crop(crop_id)
        if crop is None:
            raise KeyError("Crop ID was not found.")
        crop.notes = notes.strip()
        self.save_records()
        return crop

    def record_harvest(self, crop_id, quantity):
        crop = self.get_crop(crop_id)
        if crop is None:
            raise KeyError("Crop ID was not found.")
        quantity = float(quantity)
        if quantity < 0:
            raise ValueError("Harvest quantity cannot be negative.")
        crop.harvest_quantity += quantity
        crop.status = "Harvested"
        self.save_records()
        return crop

    def delete_crop(self, crop_id):
        crop_id = str(crop_id).strip()
        if crop_id not in self.crops:
            raise KeyError("Crop ID was not found.")
        del self.crops[crop_id]
        self.save_records()

    def summary(self):
        total = len(self.crops)
        planted = sum(c.quantity_planted for c in self.crops.values())
        harvested = sum(c.harvest_quantity for c in self.crops.values())
        return total, planted, harvested


def prompt_nonempty(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def prompt_date(label):
    while True:
        value = input(label).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Enter the date in YYYY-MM-DD format, for example 2026-10-28.")


def prompt_number(label, allow_zero=True):
    while True:
        try:
            value = float(input(label).strip())
            if value < 0 or (not allow_zero and value == 0):
                raise ValueError
            return value
        except ValueError:
            print("Enter a valid non-negative number.")


def add_crop_menu(system):
    print("\n--- Add a Crop ---")
    crop_id = prompt_nonempty("Crop ID (e.g. C001): ")
    crop_name = prompt_nonempty("Crop name (e.g. Rice, Cassava, Maize, Cocoa): ")
    variety = input("Variety (optional): ").strip()
    field_name = prompt_nonempty("Farm/field name: ")
    planting_date = prompt_date("Planting date (YYYY-MM-DD): ")
    expected_date = prompt_date("Expected harvest date (YYYY-MM-DD): ")
    quantity = prompt_number("Quantity planted (bags, seedlings, or another unit): ")
    notes = input("Notes (optional): ").strip()
    crop = Crop(
        crop_id, crop_name, variety, field_name, planting_date,
        expected_date, quantity, notes=notes
    )
    try:
        system.add_crop(crop)
        print("Crop record added and saved successfully.")
    except ValueError as error:
        print(f"Could not add crop: {error}")


def view_crops_menu(system):
    print("\n--- Crop Records ---")
    crops = system.list_crops()
    if not crops:
        print("No crop records have been added yet.")
        return
    for crop in sorted(crops, key=lambda item: item.crop_id):
        print("-" * 40)
        print(crop.display())


def search_crop_menu(system):
    crop_id = input("Enter crop ID to search: ").strip()
    crop = system.get_crop(crop_id)
    if crop:
        print("\n" + crop.display())
    else:
        print("No crop record found with that ID.")


def update_status_menu(system):
    crop_id = input("Enter crop ID: ").strip()
    print("Available statuses:", ", ".join(system.VALID_STATUSES))
    status = input("Enter new status exactly as shown: ").strip()
    try:
        system.update_status(crop_id, status)
        print("Crop status updated.")
    except (KeyError, ValueError) as error:
        print(f"Could not update status: {error}")


def harvest_menu(system):
    crop_id = input("Enter crop ID to record harvest for: ").strip()
    quantity = prompt_number("Harvest quantity to add: ")
    try:
        crop = system.record_harvest(crop_id, quantity)
        print(f"Harvest recorded. Total recorded harvest: {crop.harvest_quantity:g} units.")
    except (KeyError, ValueError) as error:
        print(f"Could not record harvest: {error}")


def update_notes_menu(system):
    crop_id = input("Enter crop ID: ").strip()
    notes = input("Enter new notes: ")
    try:
        system.update_notes(crop_id, notes)
        print("Notes updated.")
    except KeyError as error:
        print(error)


def delete_crop_menu(system):
    crop_id = input("Enter crop ID to delete: ").strip()
    confirm = input(f"Delete crop {crop_id}? Type YES to confirm: ").strip()
    if confirm == "YES":
        try:
            system.delete_crop(crop_id)
            print("Crop record deleted.")
        except KeyError as error:
            print(error)
    else:
        print("Deletion cancelled.")


def show_summary(system):
    total, planted, harvested = system.summary()
    print("\n--- Farm Summary ---")
    print(f"Number of crop records: {total}")
    print(f"Total quantity planted: {planted:g} units")
    print(f"Total harvest recorded: {harvested:g} units")


def main():
    system = CropManagementSystem()
    print("=" * 44)
    print("       CROP MANAGEMENT SYSTEM")
    print("=" * 44)
    while True:
        print(
            "\nMAIN MENU\n"
            "1. Add a crop record\n"
            "2. View all crop records\n"
            "3. Search for a crop\n"
            "4. Update crop growth/status\n"
            "5. Record harvest quantity\n"
            "6. Update crop notes\n"
            "7. Delete a crop record\n"
            "8. View farm summary\n"
            "0. Exit"
        )
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_crop_menu(system)
        elif choice == "2":
            view_crops_menu(system)
        elif choice == "3":
            search_crop_menu(system)
        elif choice == "4":
            update_status_menu(system)
        elif choice == "5":
            harvest_menu(system)
        elif choice == "6":
            update_notes_menu(system)
        elif choice == "7":
            delete_crop_menu(system)
        elif choice == "8":
            show_summary(system)
        elif choice == "0":
            print("Thank you for using the Crop Management System.")
            break
        else:
            print("Invalid option. Please choose from the menu.")


if __name__ == "__main__":
    main()
