import math;

def get_rec_fuel(m):
    x = math.floor(m/3) - 2;
    if x <= 0:
        return 0;
    return x + get_rec_fuel(x);

def calc_fuel(modules):
    total_fuel = 0;
    for m in modules:
        total_fuel = total_fuel + get_rec_fuel(m);
    return total_fuel;

if __name__ == '__main__':
    fin = open('input_day1.txt', 'r')
    modules = [];
    for line in fin:
        modules.append(int(line.strip('\n')));
    total_fuel = calc_fuel(modules)
    print("total fuel", total_fuel);
    