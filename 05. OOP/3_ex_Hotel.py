""" Write a Python program that implements a Hotel Reservation System using OOP.
The program should:
  - Define a Room class with number, type, price per night, and availability
  - Define a Reservation class that stores client info and calculates total price
  - Define a Hotel class that manages multiple rooms
Allow:
  - adding rooms
  - viewing available rooms
  - reserving a room
  - releasing a room
Use a menu-based interface
Handle invalid input using try/except.  """


class Room:
    def __init__(self, number, room_type, price_per_night):
        if price_per_night <= 0:
            raise ValueError("Invalid price!")
        if room_type not in ["single", "double", "suite"]:
            raise ValueError("Invalid room type!")

        self.number = number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

    def reserve(self):
        if self.is_available:
            self.is_available = False
            print("Room successfully reserved!")
        else:
            print("Room is already reserved!")

    def release(self):
        if not self.is_available:
            self.is_available = True
            print("Room successfully released!")
        else:
            print("Room is already available!")

    def __str__(self):
        status = "Available" if self.is_available else "Reserved"
        return f"Room:{self.number} | Type:{self.room_type} | Price:{self.price_per_night} | Status:{status}"


class Reservation:
    def __init__(self, client, room, nights):
        self.client = client
        self.room = room
        self.nights = nights

    def total_price(self):
        return self.room.price_per_night * self.nights


class Hotel:
    def __init__(self):
        self.rooms = []

    def find_room(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    def add_room(self, room):
        if self.find_room(room.number):
            print("Room already exists!")
        else:
            self.rooms.append(room)
            print("Room added successfully!")

    def show_available_rooms(self):
        if not self.rooms:
            print("No rooms available")
            return

        print("\nAvailable rooms:")
        for room in self.rooms:
            if room.is_available:
                print(room)

    def reserve_room(self, number, client, nights):
        room = self.find_room(number)

        if room is None:
            print("Room not found!")
            return None

        if not room.is_available:
            print("Room is not available!")
            return None

        reservation = Reservation(client, room, nights)
        room.is_available = False
        return reservation


def main():
    hotel = Hotel()

    while True:
        try:
            print("\nHOTEL MANAGEMENT MENU")
            print("\n1. Add room")
            print("2. Show available rooms")
            print("3. Reserve room")
            print("4. Release room")
            print("5. Exit")

            option = int(input("\nChoose option: "))

            if option == 1:
                number = int(input("Room number: "))
                room_type = input("Room type: ")
                price = int(input("Price per night: "))
                room = Room(number, room_type, price)
                hotel.add_room(room)

            if option == 2:
                hotel.show_available_rooms()

            if option == 3:
                number = int(input("Room number: "))
                client = input("Client name: ")
                nights = int(input("Number of nights: "))

                reservation = hotel.reserve_room(number, client, nights)

                if reservation:
                    print("Room reserved successfully!")
                    print(f"Total price: {reservation.total_price()}")

            if option == 4:
                number = int(input("Room number: "))
                room = hotel.find_room(number)

                if room:
                    room.release()
                else:
                    print("Room not found!")

            if option == 5:
                print("Exit")
                break

        except ValueError:
            print("Invalid input!")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

