from random import shuffle
from subprocess import run, PIPE

if __name__ != '__main__':
    exit()
countries_cmd = 'nordvpn countries'.split()
countries_output = run(countries_cmd, stdout=PIPE, stderr=PIPE, check=True, text=True,
                       universal_newlines=True)
countries = list(filter(lambda x: len(x) > 1, countries_output.stdout.split()))
shuffle(countries)
for country in countries:
    connect_cmd = f'nordvpn c {country}'.split()
    connect_output = run(connect_cmd, stdout=PIPE, stderr=PIPE, check=False, text=True,
                         universal_newlines=True)
    if connect_output.returncode == 0:
        print(f'connected to {country}')
        break
    a = "\n".join(list(filter(lambda x: len(x) > 2, connect_output.stdout.splitlines())))
    print(a)
