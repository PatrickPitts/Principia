import Kinematics as K
import Animation as A
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, ConnectionPatch
from matplotlib import animation


# This method implements several projectile arcs in one image;
def many_in_one(v0=None, angle=None, n_frames=100):
    if angle is None:
        angle = [np.pi / 4]
    if v0 is None:
        v0 = [10]
    if len(v0) != len(angle):
        raise ValueError("Mismatch number of initial velocities and initial launch angles")

    n_arcs = len(v0)

    projs = [K.ProjectileMotion2d(v=v0[n], theta=angle[n]) for n in range(n_arcs)]
    projectile_range = max([p.range()[0] for p in projs])
    print([p.range()[1] for p in projs])
    t_range = max([p.range()[1] for p in projs])
    max_height = max([p.max_height() for p in projs])

    x_pos = []
    y_pos = []
    v_angle = []
    for p in projs:
        a, b, c = p.vectorized_positions(tf=t_range, n_steps=n_frames + 1)
        x_pos.append(a)
        y_pos.append(b)
        v_angle.append(c)
    print([(n, y_pos[1][n]) for n in range(len(y_pos[1]))])
    fig = plt.figure()
    ax = plt.axes(xlim=(0, projectile_range * 1.1), ylim=(0, max_height * 1.1))
    ax.set_aspect('equal')
    arcs = []
    objs = [[A.basic_rocket_body(center=[x_pos[n][i], y_pos[n][i]], angle=v_angle[n][i]) for n in range(n_arcs)]
            for i in range(n_frames + 1)]
    for n in range(n_arcs):
        a, = plt.plot([], [], lw=2)
        arcs.append(a)

    def init():
        [arc.set_data([], []) for arc in arcs]
        [ax.add_patch(obj) for obj in objs[0]]
        return arcs + objs[0]

    def animate(i):
        [arcs[n].set_data(x_pos[n][:i + 1], y_pos[n][:i + 1]) for n in range(n_arcs)]
        ax.patches = []
        [ax.add_patch(obj) for obj in objs[i]]
        return arcs + objs[i]

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n_frames + 1,
                                   interval=20, blit=True, repeat=False)
    plt.show()


def single(v0=10, angle=np.pi / 4, n_frames=100):
    proj = K.ProjectileMotion2d(v=v0, theta=angle)
    projectile_range, t_range = proj.range()

    xpos, ypos, v_angle = proj.vectorized_positions(tf=t_range, n_steps=n_frames + 1)

    fixed_patches = []
    point = plt.Circle(proj.max_height(), radius=.1)
    vert_line = ConnectionPatch((proj.max_height()[0], 0), proj.max_height(), coordsA="data")
    horiz_line = ConnectionPatch((0, proj.max_height()[1]), proj.max_height(), coordsA="data")
    fig = plt.figure()
    ax = plt.axes(xlim=(0, projectile_range), ylim=(0, K.projectile_max_height(v=v0, theta=angle) * 1.1))
    ax.set_aspect('equal')
    arc, = plt.plot([], [], lw=2, color='blue')

    def init():
        obj = A.basic_rocket_body(center=[xpos[0], ypos[0]], angle=v_angle[0], scale=.5)
        arc.set_data([], [])
        ax.add_patch(obj)
        return arc, obj,

    def animate(i):
        obj = A.basic_rocket_body(center=[xpos[i], ypos[i]], angle=v_angle[i], scale=.5)
        ax.patches = []
        if abs(ypos[i] - proj.max_height()[1]) < 0.001:
            fixed_patches.append(point)
            fixed_patches.append(vert_line)
            fixed_patches.append(horiz_line)
        [ax.add_patch(n) for n in fixed_patches]
        ax.add_patch(obj)
        arc.set_data(xpos[:i], ypos[:i])

        return fixed_patches + [arc, obj]

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n_frames + 1,
                                   interval=20, blit=True, repeat=False)
    plt.show()


if __name__ == '__main__':
    # many_in_one([10, 10, 10], [np.pi/6, np.pi/3, np.pi/4])
    single()
