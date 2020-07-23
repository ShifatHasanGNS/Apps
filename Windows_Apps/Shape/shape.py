import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import json, time, os

global a, b, c, d, area, trim_n, number_of_shapes, shapes, calculated_areas, deviations, accuracy_list, diagonals, report_dir

def line_len(x1, y1, x2, y2): return round(((x1-x2)**2 + (y1-y2)**2)**0.5, 10)

def area(shape): return 0.5*((shape[1][0] * shape[2][1]) + (shape[2][0] * shape[3][1]) - (shape[3][0] * shape[2][1]))

def calc_xd(xc, yc):
    n = xc*xc + yc*yc
    m = (n - c*c + d*d) / 2
    a1 = (2*m*xc) / n
    a2 = (m*m - yc*yc*d*d) / n
    D = a1*a1 - 4*a2
    if D >= 0: return (a1 - D**0.5)/2
    return None

def is_acceptable(calculated_area):
    dev = abs(area - calculated_area)
    if dev < 0.000001: return True
    return False

# ------------------------------------------------------------------------------------------ #

def report():
    count = 0
    shape_number = 0
    
    report = f'''
# Line Segments Of The Quadrilateral:

    AB = {a} feet
    BC = {b} feet
    CD = {c} feet
    DA = {d} feet

# Expected area : {area} square feet

# Number Of Possible Shapes : {number_of_shapes}

# Diagonals Of The Quadrilateral:'''

    for shape in shapes:
        shape_number += 1

        report = report + f'''
    

    Shape [{shape_number}] :

        A --> (0, 0)
        B --> (0, {a})
        C --> ({shape[2][0]}, {shape[2][1]})
        D --> ({shape[3][0]}, {shape[2][1]})
        
      # Calculated area ---> {calculated_areas[count]} square-feet
              Deviation ---> {deviations[count]} square-feet
               Accuracy ---> {accuracy_list[count]} %

      Diagonals:    AC = {diagonals[count][0]} feet
                    BD = {diagonals[count][1]} feet'''
        count += 1
    
    return report

# ------------------------------------------------------------------------------------------ #

def draw_shape(num):
    index = num - 1
    fig = plt.figure()
    ax = fig.add_subplot(111)

    x = [0, round(a, 5), round(shapes[index][2][0], 5), round(shapes[index][3][0], 5), 0]
    y = [0, 0, round(shapes[index][2][1], 5), round(shapes[index][3][1], 5), 0]

    r = (a+b+c+d)/4

    line = Line2D(x, y)
    ax.add_line(line)

    x1 = [0, x[2]]
    y1 = [0, y[2]]

    line = Line2D(x1, y1, color='chocolate', label=f'AC = {diagonals[index][0]}')
    ax.add_line(line)

    x2 = [a, x[3]]
    y2 = [0, y[3]]

    line = Line2D(x2, y2, color='yellowgreen', label=f'BD = {diagonals[index][1]}')
    ax.add_line(line)

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.set_xlim(min(x)-(0.5*r), max(x)+(1.25*r))
    ax.set_ylim(min(y)-(0.5*r), max(y)+(1.25*r))

    ax.set_title(f'Shape {num}', pad=25, fontdict={'fontsize':23, 'fontweight':'bold', 'fontname':'Segoe UI', 'color':'green', 'verticalalignment':'baseline'})

    plt.annotate(f'A ({x[0]}, {y[0]})', xy=(x[0], y[0]), xytext=(-25, -25),
            textcoords='offset points', ha='center', va='center',
            bbox=dict(boxstyle='round, pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '-|>', connectionstyle='arc3, rad=0'))

    plt.annotate(f'B ({x[1]}, {y[1]})', xy=(x[1], y[1]), xytext=(25, -25),
            textcoords='offset points', ha='center', va='center',
            bbox=dict(boxstyle='round, pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '-|>', connectionstyle='arc3, rad=0'))

    plt.annotate(f'C ({x[2]}, {y[2]})', xy=(x[2], y[2]), xytext=(25, 25),
            textcoords='offset points', ha='center', va='center',
            bbox=dict(boxstyle='round, pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '-|>', connectionstyle='arc3, rad=0'))

    plt.annotate(f'D ({x[3]}, {y[3]})', xy=(x[3], y[3]), xytext=(-25, 25),
            textcoords='offset points', ha='center', va='center',
            bbox=dict(boxstyle='round, pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '-|>', connectionstyle='arc3, rad=0'))

    plt.grid(True)
    plt.legend()
    plt.savefig(f'{report_dir}\\shape_{num}.png', transparent=True, bbox_inches='tight', dpi=2048)

# ------------------------------------------------------------------------------------------ #

if __name__ == "__main__":
    start_main = time.time()

    a, b, c, d = map(float, input('\n Enter The Line Segments (feet)\n >>> ').split())
    area = float(input('\n Enter The Expected area (square feet)\n >>> '))
    report_dir = input('\n Enter the Folder_Name/File_PATH, where you want to store the reports : (There should be no WhiteSpace in the PATH)\n >>> ')

    # initializing
    trim_n = 10
    shapes = list()
    calculated_areas = list()
    deviations = list()
    accuracy_list = list()
    diagonals = list()

    # Running Shape_Hunter
    start = time.time()
    print('\n Shape_Hunter is running...\n\n It may take some minutes to complete... So, keep patience... :)\n')
    xc = a - b + 0.000000000000000000001
    temp_shapes = dict()
    while xc < (a+b):
        yc = (b*b - (xc-a)**2)**0.5
        xd = calc_xd(xc, yc)
        if xd != None:
            yd = (d*d - xd*xd)**0.5
            ar = 0.5*((a * yc) + (xc * yd) - (xd * yc))
            if is_acceptable(ar):
                temp_shapes[ar] = [[0, 0], [round(a, trim_n), 0], [round(xc, trim_n), round(yc, trim_n)], [round(xd, trim_n), round(yd, trim_n)]]
        xc += 0.000001
    end = time.time()
    time_spent = (end - start) / 60
    print(f' Done... Shape_Hunter was running for {time_spent} minutes...\n')

    number_of_shapes = len(temp_shapes)
    print(f' {number_of_shapes} possible shapes found...\n\n Sorting out these acceptable shapes...\n')
    print(' Analysing and calculating some important data...\n')
    calculated_areas = sorted(temp_shapes)
    for calculated_area in calculated_areas:
        deviation = round(calculated_area-area, trim_n)
        deviations.append(deviation)
        accuracy = round((2 - (calculated_area/area))*100, 10)
        accuracy_list.append(accuracy)
        shapes.append(temp_shapes[calculated_area])

    for shape in shapes:
        ac = (shape[2][0]**2 + shape[2][1]**2)**0.5
        bd = ((shape[3][0]-a)**2 + shape[3][1]**2)**0.5
        diagonals.append((round(ac, 10), round(bd, 10)))
    print(' Done...\n')
    
    os.system(f'mkdir {report_dir}')

    json_data = {
        "segments" : [a, b, c, d],
        "expected_area" : area,
        "number_of_shapes" : number_of_shapes,
        "shapes" : shapes,
        "accuracy" : accuracy_list,
        "calculated_areas" : calculated_areas,
        "area_deviations" : deviations,
        "diagonals" : diagonals
    }

    with open(f'{report_dir}\\land_data.json', 'w') as file:
        json.dump(json_data, file, indent=4)

    with open(f'{report_dir}\\land_report.txt', 'w') as file:
        file.write(report())

    # Drawing Shapes
    print(' Shape_Artist has started drawing the shapes...\n')
    start = time.time()
    for num in range(1, number_of_shapes+1):
        print(f' Drawing the Shape {num}...')
        draw_shape(num)
        print(' Saving the shape...')
        print(' Done...\n')
    end = time.time()
    time_spent = end - start
    print(f' Shape_Artist was running for {time_spent} seconds...\n')

    end_main = time.time()
    time_spent_main = (end_main - start_main) / 60

    print(f' # This program was running for {time_spent_main} minutes...')
    print(f'\n\n Everything is ready for you...\n\n Now, you can see the reports in this location:\n ---> {report_dir}\\\n')
    print(' Wait... Opening the folder in File-Explorer...')

    os.system(f'start {report_dir}\\')
    print(' Now this program is terminating...')