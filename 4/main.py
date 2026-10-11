import pandas as pd

count = 5
mass = 0.2

df = pd.read_csv("table.csv")

df['t_floats'] = df['t'].apply(lambda x: [float(i) for i in x.split(';')])

df['t_mean'] = df['t_floats'].apply(lambda x: sum(x) / len(x))

df['radius'] = df['r'].apply(lambda x: float(x / 100))

df['oscillation'] = df['t_mean'].apply(lambda x: x / count)
df['osc_div'] = float('nan')

df.loc[1:, 'osc_div'] = pow(df.loc[1:, 'oscillation'] / df['oscillation'].get(0), 2) - 1

df['inertia'] = float('nan')
df.loc[1:, 'inertia'] = 2 * mass * (df.loc[1:, 'radius'] ** 2)
df['inertia_oscillation'] = float('nan')
df.loc[1:, 'inertia_oscillation'] = df['inertia'] / df['osc_div']

df.loc[0, 'inertia_oscillation'] = df.loc[1:, 'inertia_oscillation'].mean()
print(df['inertia_oscillation'])
