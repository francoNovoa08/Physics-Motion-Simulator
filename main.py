import math
import matplotlib.pyplot as plt


def main():
    print("--Physics Motion Simulation Tool--\n")
    print("Models:\n"
          "1 - Projectile motion\n"
          "2 - Two-dimensional motion\n"
          "3 - Exit program")
    while True:
        choice = get_user_choice()
        if 0 >= choice or choice > 3:
            continue
        match choice:
            case 1:
                simulate_projectile_motion()
            case 2:
                two_dimensional_motion()
            case 3:
                break


def get_user_choice():
    try:
        return int(input("Select a model: "))
    except ValueError:
        print("Invalid model")
        pass
    except Exception as e:
        print(f"An error has occurred, please try again\n {e}")
        pass


def simulate_projectile_motion():
    h, θ, u, g = get_projectile_motion_values()
    θ = math.radians(θ)
    #breaks the initial velocity into horizontal and vertical components
    u_x, u_y = velocity_breakdown(u, θ)

    total_time = (u_y + math.sqrt(u_y**2 + 2 * g * h)) / g

    #gathers times for plotting
    t_values = [t for t in float_range(0, total_time, 0.01)]

    x_values = []
    y_values = []

    for t in t_values:
        #adds the horizontal position of the projectile for every time t
        #assuming negligent air resistance, horizontal position is horizontal velocity * time
        x_values.append(u_x * t)

        #adds the vertical position of the projectile based on h + ut - 1/2(g)(t^2)
        vertical_position = h + u_y * t - 0.5 * g * t**2
        y_values.append(vertical_position)

        #exits loop once projectile hits the ground
        if vertical_position < 0:
            break

    plt.plot(x_values, y_values)
    plt.xlabel("Displacement (m)")
    plt.ylabel("Height (m)")
    plt.title("Projectile Motion Simulation")
    plt.show()


def get_projectile_motion_values():
    gravity_values = {"Earth":9.81, "Moon":1.62, "Mars":3.721, "Jupiter": 24.79}
    while True:
        try:
            height = float(input("Enter height (m): "))
            angle = float(input("Enter angle (°): "))
            initial_velocity = float(input("Enter initial velocity (m/s): "))
            planet = str(input("Enter body that exerts gravity\n "
                                 "(Earth, Moon, Mars, Jupiter): ")).lower().strip()
            gravity = gravity_values[planet]
        except ValueError:
            print("Invalid input")
            pass
        except Exception as e:
            print(f"An error has occured {e}")
        else:
            if height >= 0 and 0 < angle <= 90 and initial_velocity > 0:
                return height, angle, initial_velocity, gravity


def velocity_breakdown(velocity, angle):
    return velocity * math.cos(angle), velocity * math.sin(angle)


#modified range function to allow floats
def float_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment


def two_dimensional_motion():
    x, y, v_x, v_y, a_x, a_y, time = get_two_dimensional_motion_values()

    t_values = [t for t in float_range(0, time, 0.01)]

    x_values = [x]
    y_values = [y]

    for t in t_values:
        #adds positions based on ut + 1/2(a)(t^2)
        x_values.append(displacement(v_x, t, a_x) + x)
        y_values.append(displacement(v_y, t, a_y) + y)

    plt.plot(x_values, y_values)
    plt.title("Two-dimensional motion simulation")
    plt.show()


def get_two_dimensional_motion_values():
    while True:
        try:
            x_position = float(input("Enter x position: "))
            y_position = float(input("Enter y position: "))
            horizontal_velocity = float(input("Enter horizontal velocity (m/s): "))
            vertical_velocity = float(input("Enter vertical velocity (m/s): "))
            horizontal_acceleration = float(input("Enter horizontal acceleration (m/s^2): "))
            vertical_acceleration = float(input("Enter vertical acceleration (m/s^2): "))
            time = float(input("Enter time taken (s): "))
        except ValueError:
            print("Invalid input")
            pass
        except Exception as e:
            print(f"An error has occured {e}")
        else:
            return x_position, y_position, horizontal_velocity, vertical_velocity, horizontal_acceleration, vertical_acceleration, time


def displacement(u, t, a):
    return u * t + 0.5 * a * t**2


if __name__ == "__main__":
    main()
