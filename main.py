import ReportBuilder as RB
from Kinematics import ProjectileMotion2d as pm
from Mathematics import deg_to_rad
def main():
    while True:
        print("Welcome to the Projectile Motion Report Builder.")
        print("Create a new Report, or press 'q' to quit")
        i = input(">>>")
        if i == "q":
            return
        vel = input("Input a launch velocity, a number greater than 0\n>>>")
        if not float(vel) or float(vel) <= 0.:
            print("Bad input: Must be a number greater than 0")
        deg = input("Input a launch angle, a number greater than 0 and less than 90\n>>>")
        if not float(deg) or float(deg) <= 0 or float(deg) >= 90:
            print("Bad input: Must be a number greater than 0 and less than 90")
        proj = pm(v=float(vel), theta=deg_to_rad(float(deg)))
        print(proj)
        print("Would you like a .pdf report of this model? [Y]es or No\nWarning: this will automatically generate and "
              "open a .pdf file.")
        confirm = input(">>>")
        if confirm.lower() == "y":
            RB.build(proj)


if __name__ == '__main__':
    main()
    # P.single()

