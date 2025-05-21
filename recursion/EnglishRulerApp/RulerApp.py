def draw_line(tickLength, tickLabel=''):
    line = '-' * tickLength
    if tickLabel != '':
        line += ' ' + tickLabel
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)
    
def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for i in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(i))

if __name__ == '__main__':
    draw_ruler(2,3)
