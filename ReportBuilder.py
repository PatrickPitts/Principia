import PIL
from matplotlib.patches import ConnectionPatch
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Image
from Kinematics import ProjectileMotion2d as pm
import Animation as A
import numpy as np
import matplotlib.pyplot as plt
import io, os


# A function that takes in a ProjectileMotion2d object, and returns io.BytesIO object containing
# the data to render the appropriate projectile motion figure image.
def single_proj_image(proj):
    # initializes local data from the ProjectileMotion2d object
    projectile_range, t_range = proj.range()
    xmax, ymax = proj.max_height()
    xpos, ypos, v_angle = proj.vectorized_positions(tf=t_range, n_steps=101)

    # initializing plot information
    fig = plt.figure()
    ax = plt.axes(xlim=(0, projectile_range * 1.3), ylim=(0, proj.max_height()[1] * 1.3))
    ax.set_aspect('equal')

    # creating guideline patches
    vert_line = ConnectionPatch((proj.max_height()[0], 0), proj.max_height(), coordsA="data")
    horiz_line = ConnectionPatch((0, proj.max_height()[1]), proj.max_height(), coordsA="data")
    range_pointer = ConnectionPatch((projectile_range, 0), (projectile_range * 1.1, ymax * 0.5), coordsA="data")

    # creating reference point patches
    max_height_point = plt.Circle(proj.max_height(), radius=.1)
    range_point = plt.Circle((projectile_range, 0), radius=.1, color="red")

    # initializing and adding guidelines, reference points, and rocket image patches
    [ax.add_patch(A.basic_rocket_body(center=[xpos[n], ypos[n]], angle=v_angle[n], scale=.5)) for n in [20, 40, 60, 80]]
    ax.add_patch(range_point)
    ax.add_patch(max_height_point)
    ax.add_patch(vert_line)
    ax.add_patch(horiz_line)
    ax.add_patch(range_pointer)

    # draws projectile motion arc
    arc, = plt.plot([], [], lw=2, color='blue')
    arc.set_data(xpos, ypos)

    # adds text annotations to the figure
    ax.annotate("Max height: {x:.3f}m".format(x=xmax), (xmax, ymax * 1.1))
    ax.annotate("Range:\n{r:.3}m".format(r=projectile_range), (projectile_range * 1.11, ymax * 0.55))

    # prepares io.BytesIO() data stream
    imgdata = io.BytesIO()
    fig.savefig(imgdata, format='png', pad_inches=0.0)
    imgdata.seek(0)
    return imgdata


# function that takes in a ProjectileMotion2d object, and creates a .pdf file reporting on the
# physical features of the system.
def build(proj):
    pdfpath="hello.pdf"
    doc = SimpleDocTemplate(pdfpath, pagesize=LETTER, rightMargin=inch, leftMargin=inch, topMargin=inch,
                            bottomMargin=inch)
    story = []
    with open("intro.txt", "r") as f:
        intro_text = ""
        for line in f.readlines():
            intro_text += line
    data_string = proj.__str__().replace('\n', '<br />\n')

    if intro_text:
        story.append(Paragraph(intro_text))

    im = Image(single_proj_image(proj))
    im._restrictSize(8*inch, 4*inch)
    story.append(im)
    story.append(Paragraph(data_string))
    doc.build(story)
    os.startfile(pdfpath)



if __name__ == "__main__":
    # single_proj_image(pm(v=10, theta=np.pi / 4))
    build(pm(v=15, theta=np.pi / 3))
