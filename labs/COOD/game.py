#! /usr/bin/env python3
# Author: EarlE
# Version: 1.0
# Description: This script will
"""
    Docstring:
"""
import sys
import tank

def main():
    thomas_tank = tank.Tank("german", "tiger")
    rick_tank = tank.Tank("american", "sherman")
    rajat_tank = tank.Tank("british", "churchill")

    thomas_tank.accel(39)
    rick_tank.accel(28)


    rajat_tank.rotate_left(289)
    rajat_tank.accel(31)
    rajat_tank.shoot()


    thomas_tank.take_damage(62)
    rick_tank.take_damage(22)


    # print(f"Thomas's tank has health of {thomas_tank._health}")

    # Example of operator OVERLOADING
    print(f"Status of Thomas's and Rick's tank {thomas_tank + rick_tank}")
    # thomas_tank._health = 100


    # print(f"New health of Thomas's tank is {thomas_tank._health}")
    thomas_tank.set_health(101)
    print(f"New health of Thomas's tank is {thomas_tank.get_health()}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)