import yaml

from helpers.eta_formula import eta_formula

def line_spammer():
    with open('measurements/data.yml', 'r') as data_file:
        content = yaml.load(data_file, yaml.Loader)
        for img_data in content['images'].values():
            power = img_data['power']
            scale_factor = img_data['scale_factor']
            header = ''
            header += r'\begin{tabular}{|c|c|c|}' + '\n'
            header += r'\hline' + '\n'
            header += r'\multicolumn{3}{|c|}{' + f'Q = {power} Вт' + r'} \\' + '\n'
            header += r'\hline' + '\n'
            header += r'x, мм & y, мм & $ \eta $\\' + '\n'
            yield header

            sections = img_data['sections']
            for section in sections.values():
                points = section
                for point in points:
                    point_x = point['x'] / scale_factor
                    point_y = point['y'] / scale_factor
                    eta_value = eta_formula(point_x, point_y, power)
                    point_x, point_y = (point_x * 1_000, point_y * 1_000)
                    line_content = f'{point_x:.2f} & {point_y:.2f} & {eta_value:.4f}'
                    line_content += ' \\\\ \n'
                    yield line_content
            
            footer = ''
            footer += r'\hline'
            footer += r'\end{tabular}' + '\n' * 2
            yield footer

def main():
    output = ''
    for line in line_spammer():
        output += line

    with open('tables/points.latex-table', 'w') as output_file:
        output_file.write(output)


if __name__ == '__main__':
    main()
